from memory import save_convo,del_convo,show_convo
from ui import welcome_message,goodbye_message
from brain import prompts
instuctions="just type the word(everything in lowercase) you want to learn about"
command_log={
    "1":"to shut down the chatbot\n",
    "2":"to save the conversation\n",
    "3":"to show the convo history\n",
    "4":"to delete all the history\n",
    "5":"to view the command log again\n"
}
def commands(user):
    if user=="1":
        goodbye_message()

        return False
    elif user=="5":
        return command_log
    elif user=="2":

        print("saved successfully")
        
    elif user=="3":
        return show_convo()
    elif user=="4":
        return del_convo()
    else :
        return prompts(user)


    
       
    