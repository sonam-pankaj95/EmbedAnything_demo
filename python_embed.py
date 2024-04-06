# embed document
from langchain_openai import OpenAIEmbeddings




# importing required classes 
from pypdf import PdfReader 
import time

reader = PdfReader("test_paper.pdf") 
   
page = reader.pages[0]
  
text = page.extract_text()
start = time.time()

embed_model = OpenAIEmbeddings(model="text-embedding-ada-002",)

embeddings = embed_model.embed_documents(text)

print(embeddings[0])

end = time.time()
print(end - start)