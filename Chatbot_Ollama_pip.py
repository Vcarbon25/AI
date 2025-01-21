"""
requirements:
    pip install ollama
    in the same terminal session enter python mode and pull the model
      import ollama
      ollama.pull('ModelName')
"""
from ollama import chat

global ConvHist
ConvHist=[]

def talk(In):
  prompt ="ConversationHostory: \n"+str(ConvHist)+ In
  stream = chat(
     model='llama3.2',
     
     messages=[{'role': 'user', 'content': prompt}],
      stream=True
)
  AiAnswer="AI: "
  print("AI: ",end="")
  for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
    AiAnswer +=chunk['message']['content']+' '
  ConvHist.append(AiAnswer)
  
  

while True:
  print("\ntype 'Hist' to see past interactions or 'end' to exit chatbot.")
  UserIn = input("User: ")
  ConvHist.append("User: "+UserIn)
  if UserIn=='end':
    break
  elif UserIn=="Hist":
    print(ConvHist)
    continue

  talk(UserIn)