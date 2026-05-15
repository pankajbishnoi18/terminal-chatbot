import json
from brain import prompts ,commands
from memory import save_convo,old_convo,start_session,save_convo_of_commands,save_session_end
from ui import welcome_message,goodbye_message
# with open("convo.txt","a")as file:
#          file.write("___________________session started here____________________________\n"
#                     f"bot:{welcome_message}\n"
#                     " enter 5 for command log or you can ask about anything , just drop the word below\n")


           
start_session()

command_available=["1","2","3","4","5"]
while True:
    user=input("user:")
    if user=="4":
        old_data=old_convo()
        old_data=[]
    
    
    

    
    if user in command_available:
        command_response=commands(user)
        save_convo_of_commands(user,command_response)
        if user == "1":
          save_session_end()
          goodbye_message()
          break


        #  file.write(f"user commanded:{user}\n"
        #             f"bot responded:{command_response}")

        
        print("bot:",command_response)
       
        
        
    else:
        prompt_response=prompts(user)
        save_convo(user)
        print("bot:",prompt_response)
    

        

            
       
        
    
    



    
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

