"""
requirements:
    install ollama https://ollama.com/
        them test the installation typing (ollama) in cmd
        check the desired model in https://github.com/ollama/ollama
        install with (ollama pull NameModel)

        create a virtual env and install dependencies
        pip install langchain
        pip install langchain-ollama
        pip install ollama

"""
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question bellow.
Here is the conversation history: {context}
Question: {question}
Answer: 
"""

model = OllamaLLM(model="llama3.2:1b") #need to be the installed model name
prompt = ChatPromptTemplate.from_template(template=template)
chain = prompt | model

def CBot_engine():
    context = ""
    print("Talking to AI Chatbot - Open Source")
    print ("type 'exit' to quit")
    while True:
        UserInput = input("User: ")
        if UserInput.lower() =='exit':
            break
        result = chain.invoke({"context":context, "question":UserInput})
        print("Bot: ",result)
        context += f"\nUser: {UserInput}\nBot: {result}"


CBot_engine()