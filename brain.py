from knowledge import knowledge
def prompts(user):
    
    if user in knowledge:
        return knowledge[user]
    else :
        return f"sorry i dont have anything on {user}"
        

    

    
