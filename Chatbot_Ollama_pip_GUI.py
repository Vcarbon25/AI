"""
pip install ollama
    then enter in the terminal python mode
        import ollama
    and pull the desired model
        ollama.pull('ModelName')
        complete list https://ollama.com/search
"""

import tkinter as TK
import threading  #this will avoid the screen to freeze while waiting the model answer
from ollama import chat

root = TK.Tk() #def main window

modelo ="llama3.2" #must be the same model pulled during the module installation

LbStatus = TK.Label(root,text="Status:\nAvailable",border=3,bg="LightGreen")
LbStatus.grid(row=0,column=0)

ChatHist = TK.Text(root, width=100,height=25,wrap=TK.WORD,border=2)
UserI = TK.Entry(root, width=130,border=2)
Send = TK.Button(root, text="Send prompt") #will not use ENTER to send the message because the user can hit it accidentaly
#having to click the button will give time to verivy the input

ChatHist.grid(row=1,column=0,columnspan=2,padx=10)
UserI.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
Send.grid(row=2,column=2,padx=10)

def UpdateHist(text):
    ChatHist.insert(TK.END,text)
    ChatHist.see(TK.END) #this row scrolls the text field all the  way down

def Call_LM(Prompt):
    
    Complete_Prompt = "Conversation History:\n"+ChatHist.get("1.0","end")+"\n Last Update:\nUser: "+Prompt 
    #the chat history is followed by the user input so the conversation can run smootly
    
    stream = chat(model=modelo,
                  messages=[{'role':"user",'content':Complete_Prompt}])
    
   
    UpdateHist("\nIA:   "+stream['message']['content']) #render the answer on screen
    LbStatus.config(text="Status:\nAvailable",bg="LightGreen")

def Insert_UInput():
    LbStatus.config(text="Status:\nAguarde....",bg="Red") #must sinalize the system is busy
    UpdateHist("\n----------------------------") #just to keep a better formating
    UText ="\nUser: "
    UText += UserI.get()
    prompt = UserI.get()
    UserI.delete(0,TK.END) #clear the user input field
    UpdateHist(UText)
    
    threading.Thread(target=lambda: Call_LM(prompt)).start()
 
Send.config(command=Insert_UInput)

root.mainloop()