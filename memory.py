from knowledge import knowledge
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

def show_convo():
    with open ("convo.json","r") as file:
        data=json.load(file)
    return data
def del_convo():
    with open("convo.json","w")as file:
        json.dump([],file)
    return "history cleared"
    
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