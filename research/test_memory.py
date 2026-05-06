import os
from dotenv import load_dotenv
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from src.prompt import system_prompt, contextualize_q_system_prompt

load_dotenv()

# Initialize components
embeddings = download_hugging_face_embeddings()
index_name = "medical-chatbot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})
chatModel = ChatOpenAI(model="gpt-4o")

# Create History-Aware Retriever
contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", contextualize_q_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])
history_aware_retriever = create_history_aware_retriever(chatModel, retriever, contextualize_q_prompt)

# Create QA Chain
qa_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])
question_answer_chain = create_stuff_documents_chain(chatModel, qa_prompt)
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

# Test Conversation
chat_history = []

def chat(query):
    global chat_history
    print(f"User: {query}")
    response = rag_chain.invoke({"input": query, "chat_history": chat_history})
    print(f"Assistant: {response['answer']}\n")
    chat_history.extend([HumanMessage(content=query), AIMessage(content=response["answer"])])

if __name__ == "__main__":
    chat("What is Acne?")
    chat("What is the treatment for it?") # Follow-up question relying on memory
