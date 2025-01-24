
# PDF Summarization Tool Using LangChain and Hugging Face

This project is a user-friendly PDF Summarization Tool that extracts text from PDF files and generates concise summaries using LangChain and Hugging Face API. Built with Streamlit, the tool provides a seamless interface for uploading PDFs and viewing their summarized content.




## Features

- PDF Text Extraction: Extracts text from uploaded PDF files using PyPDF2.
- Text Summarization: Leverages pre-trained Hugging Face models (e.g., facebook/bart-large-cnn) for generating summaries.
- Error Handling: Handles corrupted or invalid PDFs gracefully.
- API Integration: Uses Hugging Face API for LLM-based summarization.



# Usage

- Upload a valid PDF
- The tool extracts the text and displays it in the app.
- Click on the "Summarize" button to generate a concise summary.



## Installation and Setup

1: Clone the Repository:

```bash
  git clone https://github.com/your-username/pdf-summarization-tool.git
  cd pdf-summarization-tool

```

2: Install Dependencies:

   Install the required Python libraries using pip:

```bash
  pip install -r requirements.txt

```

3: Set Up Hugging Face API Key:

   Create a file named `.streamlit/secrets.toml `toml and add your Hugging Face API key:

```bash
  HF_API_KEY = "your_huggingface_api_key"


```

4: Run the Application:

   Start the Streamlit app:
```bash
  streamlit run app.py


```
5:  Upload PDF and Summarize:
Access the app at `http://localhost:8501 `, upload a PDF file, and view the summary.


# Project Structure

```bash
  pdf-summarization-tool/
├── app.py               # Main Streamlit app script
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .streamlit/
    └── secrets.toml     # Hugging Face API key

```






## Acknowledgements

 - [LangChain](https://awesomeopensource.com/project/elangosundar/awesome-README-templates) for providing a powerful framework for LLMs.
 - [Hugging Face](https://github.com/matiassingers/awesome-readme) for their pre-trained models and APIs.
 - [Streamlit ](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project) for simplifying web app development.

