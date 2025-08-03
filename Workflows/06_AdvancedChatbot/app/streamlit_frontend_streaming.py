# ChatGPT version
import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

# Configuration for LangGraph's checkpointer
CONFIG = {
    'configurable': {
        'thread_id': 'thread-1',          # REQUIRED
        'checkpoint_id': 'checkpoint-1'   # RECOMMENDED
    }
}

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

    # Generate and stream assistant's response
    with st.chat_message('assistant', avatar="🤖"):
        ai_response = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode='messages'
            )
        )

    # Save AI response to message history
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_response})



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
# #{'role': 'assistant', 'content': 'Hi=ello'}

# user_input = st.chat_input('Type here')

# if user_input:

#     # first add the message to message_history
#     st.session_state['message_history'].append({'role': 'user', 'content': user_input})
#     with st.chat_message('user'):
#         st.text(user_input)

#     # first add the message to message_history
#     with st.chat_message('assistant'):

#         ai_message = st.write_stream(
#             message_chunk.content for message_chunk, metadata in chatbot.stream(
#                 {'messages': [HumanMessage(content=user_input)]},
#                 config= {'configurable': {'thread_id': 'thread-1'}},
#                 stream_mode= 'messages'
#             )
#         )

#     st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})