
from brain import prompts ,commands
from memory import save_convo
from ui import welcome_message,goodbye_message
with open("convo.txt","a")as file:
         file.write("___________________session started here____________________________\n"
                    f"bot:{welcome_message}\n"
                    " enter 5 for command log or you can ask about anything , just drop the word below\n")

print("bot:",welcome_message())
print("enter 5 for command log or you can ask about anything , just drop the word below")
command_available=["1","2","3","4","5"]
while True:
    user=input("user:")
    
    
    

    
    if user in command_available:
        command_response=commands(user)
        with open("convo.txt","a") as file:
         file.write(f"user commanded:{user}\n"
                    f"bot responded:{command_response}")
        
        print("bot:",command_response)
        
    else:
        prompt_response=prompts(user)
        save_convo(user)
        print("bot:",prompt_response)
    if user=="1":
        with open("convo.txt","a")as file:
         file.write("___________________session ended here____________________________\n")
        break
    
    



    
#errors to fix
#it is printing 1 after the rep==1 run
#commands.py contains a lot of bullshit 

#what to fix
#errors obviously
#i will try to saperate prompt(text input) from command(integer input)
#organise this stuff

#upgrades
#we will store data as json
#try to add access any convo feature,add timestamps etc

