from knowledge import knowledge
from brain import prompts
from memory import save_convo
from ui import welcome_message,goodbye_message
from commands import commands
welcome_message()
print("enter 5 for command log")

while True:
    user=input()
    resp=commands(user)
    print( resp)
    save_convo(user)


    if resp==1:
        with open("convo.txt","a")as file:
         file.write("___________________session ended here____________________________\n")
        break
    


