from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model=llama3)

def parse_with_llama3(dom_chunks,parse_description):
    
