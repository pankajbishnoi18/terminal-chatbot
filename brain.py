from knowledge import knowledge
from memory import del_convo,show_convo
from ui import goodbye_message
from commands import command_log

def prompts(user):
    
    if user in knowledge:
        return knowledge[user]
    else :
        return f"sorry i dont have anything on {user}"

def commands(user):
    if user=="1":
        
        return  f"{goodbye_message()}\n" 

        
    elif user=="5":
        return f"{command_log}\n"
    elif user=="2":

        return ("saved successfully\n")
        
    elif user=="3":
        return f"{show_convo()}\n"
    elif user=="4":
        return del_convo()
    
        

    

    
