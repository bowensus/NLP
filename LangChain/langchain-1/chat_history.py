from langchain_openai import OpenAI
from langchain_core.prompts import (
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
 
chat = OpenAI()
 
chat_history = ChatMessageHistory(memory_key="messages")
 
prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}"),
    ],
)
 
chain = prompt | chat
chain_with_memory = RunnableWithMessageHistory(
    chain,
    lambda session_id: chat_history,
    input_messages_key="content",
    history_messages_key="messages",
)
 
while True:
    content = input(">> ")
    result = chain_with_memory.invoke(
        {"content": content},
        {"configurable": {"session_id": "unused"}},
    )
    print(result)