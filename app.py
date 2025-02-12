from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import fitz  
import spacy
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)  

nlp = spacy.load("en_core_web_sm")

genai.configure(api_key="your_api_key")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

pdf_text = ""  

def extract_text_from_pdf(pdf_path):
    """Extracts text from the uploaded PDF."""
    doc = fitz.open(pdf_path)
    text = "\n".join(page.get_text("text") for page in doc)
    return text

def clean_text(text):
    """Cleans and processes text using NLP."""
    doc = nlp(text)
    cleaned_tokens = [
        token.lemma_.lower() for token in doc
        if not token.is_stop and not token.is_punct and not token.is_space and len(token.text.strip()) > 1
    ]
    return " ".join(cleaned_tokens)

@app.route("/")
def index():
    return render_template("task.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    """Handles PDF file upload and extracts text."""
    global pdf_text  
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    pdf_text = extract_text_from_pdf(file_path)  
    cleaned_text = clean_text(pdf_text)  
    return jsonify({"success": True, "text": cleaned_text})

@app.route("/ask", methods=["POST"])
def ask_question():
    global pdf_text  
    if not pdf_text:
        return jsonify({"error": "No PDF uploaded yet!"}), 400

    data = request.json
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"error": "Invalid question"}), 400

    try:
        model = genai.GenerativeModel("gemini-pro")
        prompt = f"You are an AI assistant that answers questions based on the given text.\nText: {pdf_text}\nQuestion: {question}\nAnswer:"
        response = model.generate_content(prompt)

        print("API Response:", response)  # Debugging line

        if not hasattr(response, "text") or not response.text.strip():
            return jsonify({"error": "No response from AI"}), 500

        return jsonify({"answer": response.text.strip()})

    except Exception as e:
        print(f"Error: {e}")  # Logs error in terminal
        return jsonify({"error": f"AI service error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
