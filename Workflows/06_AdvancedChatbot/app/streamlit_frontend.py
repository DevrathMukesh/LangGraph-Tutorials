# Chat gpt version
import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

CONFIG = {'configurable': {'thread_id': 'thread-1'}}

st.set_page_config(page_title="LangGraph Chatbot", page_icon="🤖", layout="centered")

st.title("🧠 LangGraph Chatbot")

# Initialize message history
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Display chat history
for message in st.session_state['message_history']:
    with st.chat_message(message['role'], avatar="🙂" if message['role'] == 'user' else "🤖"):
        st.markdown(message['content'])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user's message
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user', avatar="🙂"):
        st.markdown(user_input)

    # Get AI response
    with st.spinner("Thinking..."):
        response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)

    ai_message = response['messages'][-1].content

    # Add AI message
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
    with st.chat_message('assistant', avatar="🤖"):
        st.markdown(ai_message)


# Easy One
# import streamlit as st
# from langgraph_backend import chatbot
# from langchain_core.messages import HumanMessage

# # st.session_state -> dict -> 
# CONFIG = {'configurable': {'thread_id': 'thread-1'}}

# if 'message_history' not in st.session_state:
#     st.session_state['message_history'] = []

# # loading the conversation history
# for message in st.session_state['message_history']:
#     with st.chat_message(message['role']):
#         st.text(message['content'])

# #{'role': 'user', 'content': 'Hi'}
# #{'role': 'assistant', 'content': 'Hello'}

# user_input = st.chat_input('Type here')

# if user_input:

#     # first add the message to message_history
#     st.session_state['message_history'].append({'role': 'user', 'content': user_input})
#     with st.chat_message('user'):
#         st.text(user_input)

#     response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)
    
#     ai_message = response['messages'][-1].content
#     # first add the message to message_history
#     st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
#     with st.chat_message('assistant'):
#         st.text(ai_message)