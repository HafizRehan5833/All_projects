import random
User_win=0
comp_win=0
Tie=0

options=["rock","paper","scissor"]
a=0
 
while True:
        user_input=input("Enter rock paper scissor and q for quit:")
        if user_input=="q":
            break

        elif user_input not in options:
            print("please enter rock paper scissor:")
            continue
    # 0=rock 1=paper 2=scissors
        random_number=random.randint(0,2)

        comp_pick=options[random_number]

        print("Computer picked-->",comp_pick,".")
        tie=user_input==comp_pick
        if tie:
            print("Tie")
            Tie += 1
            continue

        elif user_input =="rock" and comp_pick=="scissor":
            print("You win!!")
            User_win += 1
            continue
        
        elif user_input =="paper" and comp_pick=="rock":
            print("You win!!")
            User_win += 1
            continue
        
        elif user_input =="scissor" and comp_pick=="paper":
            print("You win!!")
            User_win += 1
            continue
        else:
            print("You loss!!")
            comp_win +=1
            continue  

print("\t\t\tYour score:",User_win,"\tComputer score:",comp_win,"\tTie-->",Tie,".")

if User_win>comp_win:
    print("Congratulation!You won")
elif comp_win>User_win:
    print("Bad Luck!You lost the game.")    
elif tie>User_win:
    print("Bad Luck!Your game is Tie.") 
#else :
 #   print("\n\t\t)

print("\t\tGood bye.Game is over")   





