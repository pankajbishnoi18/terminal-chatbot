from knowledge import knowledge
def save_convo(user):
    
     with open("convo.txt","a")as file:
        file.write(
            f"user asked--{user}\n" 
            f"bot replied--{knowledge[user]}\n"
        )
    

def del_convo():
    with open ("convo.txt" ,"w") as file:
        file.write("history was cleared ,no idea when this session started\n")
    return ("history cleared\n")
def show_convo():
    with open ("convo.txt","r") as file:
        print("---------------convo history-------------")
        return file.read()