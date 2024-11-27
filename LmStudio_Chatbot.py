'''
Requirements:
For this code you will need to intall LmStudio and download the model,
every time you start LMstudio application verify if the model is properly selected, and start the local server
pip install aopenai ==0.28
'''
import openai

# Put your URI end point:port here for your local inference server (in LM Studio) 
openai.api_base='http://localhost:1234/v1'
# Put in an empty API Key
openai.api_key=''

# Adjust the following based on the model type
# Alpaca style prompt format:
prefix = "### Instruction:\n" 
suffix = "\n### Response:"

# 'Llama2 Chat' prompt format:
# prefix = "[INST]"
# suffix = "[/INST]"

# This is a simple wrapper function to allow you simplify your prompts
def get_completion(prompt, model="local model", temperature=0.0):
    formatted_prompt = f"{prefix}{prompt}{suffix}"
    messages = [{"role": "user", "content": formatted_prompt}]
    print(f'\nYour prompt: {prompt}\n')
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message["content"]

while True:
    prompt = input("\ntype 'exit' to quit chatbot \nUser: ")
    if prompt.lower()=='exit':
        break
    response = get_completion(prompt, temperature=0)
    print(f"AI Model:{response}")