from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter\
from langchain.vectorstores import FAISS    
from langchain_community.embeddings import BedrockEmbedding
from langchain.llms.bedrock import Bedrock

import json
import os
import sys
import boto3

### BED ROCK CLIENT

Bedrock=boto3.client(service_name="bedrock-runtime")
bedrock_embeddings=BedrockEmbedding(model_id="amazon.titan-embed-text-v1",client=bedrock)


def data_ingestion():
    loader = PyPDFDirectoryLoader("data")
    documents = loader.load("./data")
    

    text_splitter = RecursiveCharacterTextSplitter(chunk_Szie=1000,chunk_overlap=1000)
    text_splitter.split_documents(documents)
    
    docs = text_splitter.split_documents(documents)
    
    return docs


def get_vector_store(docs):
        vector_store_faiss = FAISS.from_document(docs,bedrock_embeddings)
        vector_store_faiss.save_local(:faiss index)
        
            
if __name__ == '__main__':
    docs = data_ingestion()
    get_vector_store(docs)
    