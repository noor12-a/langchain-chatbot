from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
llm= ChatOllama(
    model="glm-5:cloud",
    temperature=0.7
)
messages=[
    SystemMessage(content="you are a helpful assistant that translates english messages to french"),
    HumanMessage(content="What is RAG?")
]
prompt = ChatPromptTemplate.from_messages([
    ("system", "you are an AI assistant"),
    ("human", "{question}")
])

chain=prompt | llm | StrOutputParser()

#response = chain.invoke({"question": "What is RAG?"})
#print(response)
for chunk in chain.stream({"question": "What is RAG?"}):
    print(chunk,end="", flush=True)