import json
from brain import prompts ,commands
from memory import save_convo,old_convo
from ui import welcome_message,goodbye_message
# with open("convo.txt","a")as file:
#          file.write("___________________session started here____________________________\n"
#                     f"bot:{welcome_message}\n"
#                     " enter 5 for command log or you can ask about anything , just drop the word below\n")
old_data=old_convo()

with open ("convo.json","w")as file:
    welcome_data={"new session":"_____________________________________________________________________________________________________________________________________________",
           "bot":welcome_message(),
            }
    
    old_data.append(welcome_data)
    json.dump(old_data,file,indent=4)
           

print("bot:",welcome_message())
print("enter 5 for command log or you can ask about anything , just drop the word below")
command_available=["1","2","3","4","5"]
while True:
    user=input("user:")
    if user=="4":
        old_data=[]
    
    
    

    
    if user in command_available:
        command_response=commands(user)
        with open("convo.json","w") as file:
            command_data={
                "user commanded":user,
                "bot responded":command_response
            }
        
            old_data.append(command_data)
            json.dump(old_data,file,indent=4)



        #  file.write(f"user commanded:{user}\n"
        #             f"bot responded:{command_response}")

        
        print("bot:",command_response)
       
        
        
    else:
        prompt_response=prompts(user)
        save_convo(user)
        print("bot:",prompt_response)
    if user=="1":
        with open("convo.json","w")as file:
            good_bye={
                "session ended":"-------------------------------------------------------------------------------------"
            }

            
            old_data.append(good_bye)
            json.dump(old_data,file,indent=4)

            
       
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

