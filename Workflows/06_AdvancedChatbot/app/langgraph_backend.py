# Gemini
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
import google.generativeai as genai
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from langchain_core.messages import AIMessage
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Init
genai.configure(api_key=GEMINI_API_KEY)
llm = genai.GenerativeModel("models/gemini-2.5-flash")

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    # Extract just the text content from LangChain messages
    prompts = [msg.content for msg in messages]
    
    # Gemini expects plain strings (or Content objects), NOT LangChain types
    response = llm.generate_content(prompts)
    return {"messages": [AIMessage(content=response.text)]}


# Checkpointer
checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)




# OpenAI
# from langgraph.graph import StateGraph, START, END
# from typing import TypedDict, Annotated
# from langchain_core.messages import BaseMessage
# from langchain_openai import ChatOpenAI
# from langgraph.checkpoint.memory import InMemorySaver
# from langgraph.graph.message import add_messages
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatOpenAI()

# class ChatState(TypedDict):
#     messages: Annotated[list[BaseMessage], add_messages]

# def chat_node(state: ChatState):
#     messages = state['messages']
#     response = llm.invoke(messages)
#     return {"messages": [response]}

# # Checkpointer
# checkpointer = InMemorySaver()

# graph = StateGraph(ChatState)
# graph.add_node("chat_node", chat_node)
# graph.add_edge(START, "chat_node")
# graph.add_edge("chat_node", END)

# chatbot = graph.compile(checkpointer=checkpointer)