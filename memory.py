from knowledge import knowledge
def save_convo(user):
    if user in knowledge:
     with open("convo.txt","a")as file:
        file.write(f"user asked--{user}\n bot replied--{knowledge[user]}\n")
    else:
        return True

def del_convo():
    with open ("convo.txt" ,"w") as file:
        pass
    print("history cleared")
def show_convo():
    with open ("convo.txt","r") as file:
        print(file.readlines())

         
    