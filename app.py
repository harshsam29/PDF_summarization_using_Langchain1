import streamlit as st
from langchain.llms import HuggingFaceHub
import PyPDF2

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Initialize Hugging Face Model
def get_summarizer():
    hf_api_key = st.secrets["HF_API_KEY"]
    model = HuggingFaceHub(
        repo_id="facebook/bart-large-cnn",  # Use any suitable summarization model
        model_kwargs={"temperature": 0.7},
        huggingfacehub_api_token=hf_api_key
    )
    return model

# Function to summarize text
def summarize_text(summarizer, text):
    prompt = f"Summarize the following text: {text}"
    result = summarizer.predict(prompt)  # Use 'predict()' method
    return result

# Streamlit App Layout
st.title("PDF Summarization Tool")
st.write("Upload a PDF file, and this tool will summarize its content using an LLM!")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)
    st.write("### Extracted Text:")
    st.text_area("Extracted Text", pdf_text[:1000] + "..." if len(pdf_text) > 1000 else pdf_text, height=300)
    
    if st.button("Summarize"):
        with st.spinner("Summarizing text..."):
            summarizer = get_summarizer()
            summary = summarize_text(summarizer, pdf_text)
        st.write("### Summary:")
        st.write(summary)
