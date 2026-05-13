from knowledge import knowledge
def save_convo(user):
    if user in knowledge:
     with open("convo.txt","a")as file:
        file.write(
            f"user asked--{user}\n" 
            f"bot replied--{knowledge[user]}\n"
        )
    

def del_convo():
    with open ("convo.txt" ,"w") as file:
        pass
    print("history cleared")
def show_convo():
    with open ("convo.txt","r") as file:
        return file.read()

         
    