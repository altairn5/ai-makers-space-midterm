#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# ### Task 1: Dealing with the Data
# You identify the following important documents that, if used for context, you believe will help people understand what’s happening now:
# Your boss, the SVP of Technology, green-lighted this project to drive the adoption of AI throughout the enterprise.  It will be a nice showpiece for the upcoming conference and the big AI initiative announcement the CEO is planning.
# 
# https://www.whitehouse.gov/wp-content/uploads/2022/10/Blueprint-for-an-AI-Bill-of-Rights.pdf
# 
# https://www.whitehouse.gov/wp-content/uploads/2022/10/Blueprint-for-an-AI-Bill-of-Rights.pdf
# 
# 
# Your boss, the SVP of Technology, green-lighted this project to drive the adoption of AI throughout the enterprise.  It will be a nice showpiece for the upcoming conference and the big AI initiative announcement the CEO is planning.

# In[14]:


get_ipython().system('pip install -qU langgraph langchain langchain_openai langchain_experimental langchain_community')


# In[4]:


get_ipython().system('pip install -qU --disable-pip-version-check qdrant-client pymupdf tiktoken')


# 

# In[5]:


import os
import getpass
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# In[9]:


from langchain.document_loaders import PyMuPDFLoader

docB = PyMuPDFLoader("https://www.whitehouse.gov/wp-content/uploads/2022/10/Blueprint-for-an-AI-Bill-of-Rights.pdf").load()
docN = PyMuPDFLoader("https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf").load()

documents = docB + docN
print(f"Loaded {len(documents)} documents")
print(f"Loaded {documents[:1]} documents")


# In[11]:


import tiktoken
from langchain.text_splitter import RecursiveCharacterTextSplitter

def tiktoken_len(text):
    tokens = tiktoken.encoding_for_model("gpt-4o-mini").encode(
        text,
    )
    return len(tokens)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 0,
    length_function = tiktoken_len,
)

split_chunks = text_splitter.split_documents(documents)

print(f"Split {len(split_chunks)} chunks")


# In[12]:


from langchain_openai import OpenAIEmbeddings
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")


# In[19]:


from langchain_community.vectorstores import Qdrant

qdrant_vectorstore = Qdrant.from_documents(
    split_chunks,
    embedding_model,
    location=":memory:",
    collection_name="extending_context_window_llama_3",
)



# In[23]:


qdrant_retriever = qdrant_vectorstore.as_retriever()


# In[31]:


from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = """
CONTEXT:
{context}

QUERY:
{question}

You are a helpful assistant. Use the available context to answer the question only. If the question is not in the context then, say 'I don't know brah!'.
"""

rag_prompt = ChatPromptTemplate.from_template(RAG_PROMPT)


# In[27]:


from langchain_openai import ChatOpenAI

openai_chat_model = ChatOpenAI(model="gpt-4o-mini")


# In[33]:


from operator import itemgetter
from langchain.schema.output_parser import StrOutputParser

rag_chain = (
    {"context": itemgetter("question") | qdrant_retriever, "question": itemgetter("question")}
    | rag_prompt | openai_chat_model | StrOutputParser()
)


# In[37]:


rag_chain.invoke({"question" : "tell about CBRN Information or Capabilities?"})


# In[ ]:




