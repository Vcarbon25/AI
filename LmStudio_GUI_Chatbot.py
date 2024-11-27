'''
Requirements:
For this code you will need to intall LmStudio and download the model,
every time you start LMstudio application verify if the model is properly selected, and start the local server
pip install aopenai ==0.28
'''
import tkinter as tk
import openai

root = tk.Tk()

ChatHist = tk.Text(root, width=40,height=20)
UserI = tk.Entry(root, width=30)
Send = tk.Button(root, text="Send prompt")
ChatHist.grid(row=0,column=0)
UserI.grid(row=1,column=0)
Send.grid(row=1,column=1)
#connection variables
openai.api_base='http://localhost:1234/v1'
# Put in an empty API Key
openai.api_key=''

def UpdateHist(text):
    ChatHist.insert(tk.END,text)

#prepare alpaca prompt formating
prefix = "### Instruction:\n"
suffix="\n### Response:"

def Call_LM(Prompt, model='local model'):
    Formated_prompt = f"{prefix}{Prompt}{suffix}"
    message = [{"role":"user","content":Formated_prompt}]
    temp=0    
    ModelAnswer = openai.ChatCompletion.create(
        model = model,
        messages=message, temperature=temp
    )
    IaAnswer="\nIA: "
    IaAnswer += ModelAnswer.choices[0].message['content']
    UpdateHist(IaAnswer)


def Insert_UInput():
    UText ="\nUser: "
    UText += UserI.get()
    prompt = UserI.get()
    UserI.delete(0,tk.END)
    UpdateHist(UText)
    Call_LM(prompt)

Send.config(command=Insert_UInput)


root.mainloop()