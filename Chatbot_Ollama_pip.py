"""
requirements:
    pip install ollama
    in the same terminal session enter python mode and pull the model
      import ollama
      ollama.pull('ModelName')
"""

from ollama import chat
def talk(In):
  
  stream = chat(
     model='llama3.2',
     messages=[{'role': 'user', 'content': In}],
      stream=True,
)
  print("AI: ",end="")
  for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
  

while True:
  print("\ntype end to exit chatbot.")
  UserIn = input("User: ")
  if UserIn=='end':
    break

  talk(UserIn)