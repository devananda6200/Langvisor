import streamlit as st
import os
from PyPDF2 import PdfReader
import io
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAI
from langchain.chains import RetrievalQA
from langchain_together.embeddings import TogetherEmbeddings
from langchain_together import Together

# Set up OpenAI API key
#openai_api_key = os.environ.get("OPENAI_API_KEY")
#if not openai_api_key:
    #raise ValueError("OPENAI_API_KEY environment variable is not set")

chat = Together(
    together_api_key="0e28e966f09ae8077a96a2dbf31ad34cfd56f6cda4a3c450697d3ba187a43c8e",
    model= "meta-llama/Llama-3-70b-chat-hf",
    
)


def process_pdf(uploaded_file):
    pdf_reader = PdfReader(io.BytesIO(uploaded_file.read()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def setup_qa_system(text):
    # Split the text into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # Create embeddings and store in vectorstore
    embeddings = TogetherEmbeddings(model="togethercomputer/m2-bert-80M-2k-retrieval",     together_api_key="0e28e966f09ae8077a96a2dbf31ad34cfd56f6cda4a3c450697d3ba187a43c8e",
)
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)

    # Create a retrieval-based QA system
    qa = RetrievalQA.from_chain_type(
        llm=chat,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    return qa
st.set_page_config(page_title="PDF Chat App", page_icon="📚")

st.title("PDF Chat App")
st.write("Upload a PDF file to start chatting with its content.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner("Processing PDF..."):
        pdf_text = process_pdf(uploaded_file)
        qa_system = setup_qa_system(pdf_text)
    
    st.success("PDF processed successfully. You can now ask questions about its content.")
    
    query = st.text_input("Ask a question about the PDF content:")
    
    if query:
        with st.spinner("Generating response..."):
            response = qa_system.run(query)
        st.write("Response:", response)

# Add a footer
st.markdown("---")
st.markdown("Built with Streamlit and LangChain")