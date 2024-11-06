import os
import shutil
import openai 
from dotenv import load_dotenv

from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY'] 


CHROMA_PATH = "chroma"  # Vector Database Storage Path
DATA_PATH = "data/books"  # Source Document Directory


def generate_data_store():
    documents = load_documents()  
    chunks = split_text(documents)  
    save_to_chroma(chunks)


# Load Documents from Directory (supports *.md files)
def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load() 
    return documents


def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300, 
        chunk_overlap=100, 
        length_function=len, 
        add_start_index=True,  
    )

    # Split documents into chunks
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    # Debug: Inspect a chunk's content and metadata
    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks


def save_to_chroma(chunks: list[Document]):

    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Initialize Chroma DB with chunks, OpenAI embeddings, and storage path
    db = Chroma.from_documents(
        chunks, 
        OpenAIEmbeddings(), 
        persist_directory=CHROMA_PATH  
    )
    db.persist()  # Save the database to disk
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")


def main():
    generate_data_store()


if __name__ == "__main__":
    main()
