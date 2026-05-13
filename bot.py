print("Good morning sir,how can i help you ")
print("these are the command onwhich i can act right now")
print("you can ask me anything\n"
        "1--to exit the chat\n"
        "2-- show full you ever had with me\n"
         "3--delete the previous convo")





while 1>0:
    file=open("logger.txt","a")
    user_asks=input()


    


    if user_asks=="hello ZOM":
        print( "At your command sir")

        file.write(f"user--{user_asks},bot--At your command sir \n" )

    elif user_asks=="tell me about earth":
        print("earth is a life supporting planet")

        file.write(f"user--{user_asks},bot--earth is a life supporting planet\n")
        user_asks_further=input()
        if user_asks_further=="tell me more":
            print("its the 3rd planet of the solar system ")

            file.write(f"user--{user_asks_further},bot--its the 3rd planet of the solar system \n ")
        



        else:
            print("sorry can you ask again")

            continue

    elif user_asks=="explain eye":
        print("eye is an vital organ in almost every animal , birds,reptiles etc almost in every form of life")

        file.write(f"user--{user_asks},bot--eye is an vital organ in almost every animal , birds,reptiles etc almost in every form of life\n")
        user_asks_further=input()
        if user_asks_further =="tell me more":
            print(" eye helps them to see ")

            file.write(f"user--{user_asks_further},bot--eye helps them to see \n")

        else :
            print("sorry can you ask again")

            continue

    elif user_asks=="1":
        print("Goodbye sir i am going down ")

        file.write(f"user--{user_asks},bot--Goodbye sir i am going down\n")

        file.write("_______________________________________________________________________________________________________________________________")

        file.close()

        break

    elif user_asks=="2":
        file=open("logger.txt","r")

        for line in file.readlines():
            print(line)
    elif user_asks=="3":
        file=open("logger.txt","w")
        print("deleted ")
        

    else:
        print("sorry sir i am unable to understand that ,you can ask again")

        
        
        

















