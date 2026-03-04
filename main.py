from langchain_ollama import ChatOllama

llm= ChatOllama(
    model="glm-5:cloud",
    temperature=0.7
)
response = llm.invoke("what is RAG")
print(response.content)