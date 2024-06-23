

![LangChain notion](https://github.com/TH-Activities/saturday-hack-night-template/assets/117498997/af58a18d-932c-4ee7-870b-20820cfa3f3f)




# Langvisor
An interactive assistant which generates answers to any queries you raise based on the pdf file you upload
## Team members
1. Deva Nanda Nair(https://github.com/devananda6200)
2. Festin Biju(https://github.com/FestinBiju)
3. Irine Paul(https://github.com/irinepaul8I)
## Link to product walkthrough
[link to video](Link Here)
## How it Works ?
the working of project:
1. Upload PDF: Users upload a PDF file through the Streamlit interface.
2. Extract Text: The application extracts text from the PDF file.
3. Create Embeddings: The extracted text is split into chunks and embeddings are created for these chunks.
4. Store in Vector Store: The embeddings are stored in a FAISS vector store.
5. Query System: Users can ask questions about the content of the PDF. The system retrieves relevant chunks from the vector store and generates a response using the Together LLM.

## Libraries used
streamlit version 1.22.0
PyPDF2 version 3.0.1
langchain_community 
langchain_together 
faiss-cpu==1.7.3
## How to configure 
1. Clone the Repository https://github.com/devananda6200/Langvisor.git using the command:
   
   git clone https://github.com/your-username/your-repository.git
  
    cd your-repository
 
2. Create a Virtual Environment:

   python -m venv venv
   
   venv\Scripts\activate     # On Windows use
   
4. Set Together API Key
   
  
   

## How to Run
 Run the Streamlit App:
  
 streamlit run app.py
