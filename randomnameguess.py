import random

#tie=0

entry_names=["rehan","aleem","junaid","habib","sharjeel","ibrahim","hassan"]
user_names=["rehan","aleem","junaid","habib","sharjeel","ibrahim","hassan"]


permission=input("\t\tDo you want to play the guess the game\n\t\t\t\tEnter yes or no : ").lower()
User_win=0
comp_win=0
    
if permission == "yes":
    user_name=input("\n\tPlease enter Your name:").lower()  
    print(f"Here is the list of my Friends : {user_names}")     
                        
    while True:
        if  user_name in entry_names:

            user_input=input("\tPlease enter the friends name from list as a guess and Enter q for quit :").lower()
            if user_input == "q":
                print("\n\t\t\t\t--(Result of final total)--")
                print(f"\nYour final win score {User_win}\n\t\tYour final lost score {comp_win}.")
                print("\t\t\tThanks for using it .")
                quit()
            elif  user_input  not in user_names:
                    print(f"You enter {user_input},Please write from list ...")
                    continue    


            random_pick=random.randint(0,4) 
            comp_pick=user_names[random_pick]
            print(f"\nComputer pick :{comp_pick} ")
            Tie=comp_pick==user_input



            if user_input=="rehan" and comp_pick =="rehan":
                print(f"\n\tCongratulations,You win\n\t\tYou enter {user_input}\n\t\t\tYour guess is correct. ")
                User_win+=1
                print(f"\t\t\t\tYour score: {User_win}")
                print(f"\n\t\t\t\tHere is the list of my Friends : {user_names}")     


            elif user_input=="aleem" and comp_pick=="aleem":
                print(f"\n\tCongratulations,You win\n\t\tYou enter {user_input}\n\t\t\tYour guess is correct. ")
                User_win+=1
                print(f"\t\t\t\tYour score: {User_win}")
                print(f"\n\t\t\t\tHere is the list of my Friends : {user_names}")     



            elif user_input=="sharjeel" and comp_pick=="sharjeel":
                print(f"\n\tCongratulations,You win\n\t\tYou enter {user_input}\n\t\t\tYour guess is correct. ")
                User_win+=1
                print(f"\t\t\t\tYour score: {User_win}")
                print(f"\n\t\t\t\tHere is the list of my Friends : {user_names}")     


            elif user_input=="junaid" and comp_pick=="junaid":
                print(f"\n\tCongratulations,You win\n\t\tYou enter {user_input}\n\t\t\tYour guess is correct. ")
                User_win+=1
                print(f"\t\t\t\tYour score: {User_win}")
                print(f"\n\t\t\t\tHere is the list of my Friends : {user_names}")     


            elif user_input=="habib" and comp_pick=="habib":
                print(f"\n\tCongratulations,You win\n\t\tYou enter {user_input}\n\t\t\tYour guess is correct. ")
                        
                User_win+=1
                print(f"\t\t\t\tYour score: {User_win}")
                print(f"\n\t\t\t\tHere is the list of my Friends : {user_names}")     

            else:
                print("\tBad luck You loss the game.\n\t\tKindly restart the game.") 
                comp_win+=1
                print(f"\t\t\tYour lost score: {comp_win}")
                print(f"\n\t\t\t\tHere is the list of my Friends : {user_names}")     
                continue
        else:
            print(f"\t\t\t\tYou enter ({user_name}) name is not available in my list.Try again..")  
            quit()
else:
    print("\n\t\tOk,No problem for do not play.Good bye.")
    quit()


