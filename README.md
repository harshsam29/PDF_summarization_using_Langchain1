# PDF_summarization_using_Langchain1
PDF Summarization Tool Using LangChain and Hugging Face
This project is a user-friendly PDF Summarization Tool that extracts text from PDF files and generates concise summaries using LangChain and Hugging Face API. Built with Streamlit, the tool provides a seamless interface for uploading PDFs and viewing their summarized content.

Features
PDF Text Extraction: Extracts text from uploaded PDF files using PyPDF2.
Text Summarization: Leverages pre-trained Hugging Face models (e.g., facebook/bart-large-cnn) for generating summaries.
Interactive Interface: Built with Streamlit for ease of use.
Error Handling: Handles corrupted or invalid PDFs gracefully.
API Integration: Uses Hugging Face API for LLM-based summarization.
Technologies Used
Python: Core programming language.
LangChain: For LLM integration and prompt management.
Hugging Face Hub: For accessing pre-trained models.
Streamlit: For building an interactive UI.
PyPDF2: For PDF text extraction.
Installation and Setup
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/your-username/pdf-summarization-tool.git
cd pdf-summarization-tool
Install Dependencies:
Install the required Python libraries using pip:

bash
Copy
Edit
pip install -r requirements.txt
Set Up Hugging Face API Key:
Create a file named .streamlit/secrets.toml and add your Hugging Face API key:

toml
Copy
Edit
HF_API_KEY = "your_huggingface_api_key"
Run the Application:
Start the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Upload PDF and Summarize:
Access the app at http://localhost:8501, upload a PDF file, and view the summary.

Usage
Upload a valid PDF document.
The tool extracts the text and displays it in the app.
Click on the "Summarize" button to generate a concise summary.
Project Structure
graphql
Copy
Edit
pdf-summarization-tool/
├── app.py               # Main Streamlit app script
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .streamlit/
    └── secrets.toml     # Hugging Face API key
Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

License
This project is licensed under the MIT License.

Acknowledgments
LangChain for providing a powerful framework for LLMs.
Hugging Face for their pre-trained models and APIs.
Streamlit for simplifying web app development.
Let me know if you need further modifications! 😊







You said:
give me requirement.txt for the same project 
ChatGPT said:
ChatGPT
Here is the requirements.txt file for the PDF Summarization Tool project:

makefile
Copy
Edit
langchain==0.0.154
streamlit==1.18.0
huggingface_hub==0.13.3
PyPDF2==3.0.0
requests==2.28.1
This file includes the required libraries to run the project:

langchain: For working with language models and integrating Hugging Face models.
streamlit: For creating the interactive web interface.
huggingface_hub: For interacting with Hugging Face models via the API.
PyPDF2: For extracting text from PDF files.
requests: A dependency that might be used indirectly by other libraries for HTTP requests.
To install the dependencies, simply run the following command:

bash
Copy
Edit
pip install -r requirements.txt
