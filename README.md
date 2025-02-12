# PDF Chatbot

## Overview

PDF Chatbot is a web application that allows users to upload a PDF containing medical symptoms and interact with a chatbot that references the document's content to provide accurate responses. This system integrates Natural Language Processing (NLP) and AI to process and analyze the uploaded medical information.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
    
- **Backend**: Python (Flask, Flask-CORS)
    
- **PDF Processing**: PyMuPDF (Fitz)
    
- **Chatbot Logic**: NLP using spaCy
    
- **AI Model**: Google Generative AI (Gemini)
    

## Features

- Upload a PDF containing medical symptoms.
    
- Extract and preprocess text from the PDF.
    
- Utilize NLP techniques to clean and analyze the text.
    
- Generate intelligent responses using Google Gemini AI.
    
- Provide accurate symptom-based answers using chatbot integration.

![image](https://github.com/user-attachments/assets/57e3a085-6704-404a-a70f-02bb3bacb7d0)

## Workflow

1. **PDF Upload**: User uploads a PDF document.
    
2. **Text Extraction**: Fitz (PyMuPDF) extracts text from the uploaded PDF.
    
3. **Text Preprocessing**: The extracted text undergoes tokenization, punctuation removal, lowercasing, whitespace cleanup, and lemmatization using spaCy.
    
4. **AI Processing**: The cleaned text is fed into Gemini AI with constraints to ensure responses are strictly based on the provided content.
    
5. **User Interaction**: The chatbot responds to user queries based on the medical symptoms mentioned in the uploaded document.
    
6. **Frontend Integration**: A user-friendly web interface enables seamless interaction with the chatbot.

   ### Steps to Run

1. Navigate to the project directory:
    
    ```
    cd PDF_Chatbot
    ```
    
2. Install dependencies:
    
    ```
    pip install -r requirements.txt
    ```
    
3. Run the Flask application:
    
    ```
    python app.py
    ```
    
4. After running `app.py`, the Flask development server will start, and you will see an output similar to:
    
    ```
    Running on http://127.0.0.1:5000/
    ```
    
5. Open a web browser and navigate to `http://127.0.0.1:5000/` to use the application.

   ## Contribution

Contributions are welcome! Feel free to fork the repository and submit pull requests.
