from knowledge import knowledge
from ui import welcome_message,goodbye_message
import json
def old_convo():
    with open ("convo.json","r") as file:
        data=json.load(file)
    return data
def new_convo(user):
    if user in knowledge:
     new_data={
              "user asked":f"{user}",
              "bot replied" : f"{knowledge [user]}"
    }
    else: 
        new_data={
              "user asked":f"{user}",
              "bot replied" : f"sorry sir i dont have anything on {user}"
        }

    return new_data


def save_convo(user):
    
    data=old_convo()
    
    new_data=new_convo(user)
    data.append(new_data)
    with open("convo.json","w")as file:
        json.dump(data,file,indent=4)
    return data
def save_convo_of_commands(user,command_response):
    old_data=old_convo()
    with open("convo.json","w") as file:
            command_data={
                "user commanded":user,
                "bot responded":command_response
            }
        
            old_data.append(command_data)
            json.dump(old_data,file,indent=4)
    return old_data
    


def show_convo():
    with open ("convo.json","r") as file:
        data=json.load(file)
    return data
def del_convo():
    with open("convo.json","w")as file:
        json.dump([],file)
    return "history cleared"

def start_session():
    old_data=old_convo()
    with open ("convo.json","w")as file:
        welcome_data={"new session":"_____________________________________________________________________________________________________________________________________________",
           "bot":welcome_message(),
            }
    
        old_data.append(welcome_data)
        json.dump(old_data,file,indent=4)
    return print(f"bot:{welcome_message()}enter 5 for command log or you can ask about anything , just drop the word below")
def save_session_end():

    old_data = old_convo()

    with open("convo.json", "w") as file:

        good_bye = {
            "session ended": "-------------------------------------------------------------------------------------"
        }

        old_data.append(good_bye)

        json.dump(old_data, file, indent=4)
   
def end_session():
    return goodbye_message()
    
# def save_convo(user):
    
#      with open("convo.txt","a")as file:
#         file.write(
#             f"user asked--{user}\n" 
#             f"bot replied--{knowledge[user]}\n"
#         )
    

# def del_convo():
#     with open ("convo.txt" ,"w") as file:
#         file.write("history was cleared ,no idea when this session started\n")
#     return ("history cleared\n")
# def show_convo():
#     with open ("convo.txt","r") as file:
#         print("---------------convo history-------------")
#         return file.read()