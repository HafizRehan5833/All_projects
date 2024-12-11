import random


range =input("Your number:\t")




if range.isdigit():
    range=int(range)
    
    
    if range <=0:
                print("Please enter a larger than 0.")
                quit()
else:        
    print("Please type a number")
    quit()

score=0
random_number=random.randint(0,range)
        
#print(random_number)
a=0
b=int(input("Enter the number how much you want to guess the number: "))
while a<=b:
 

    guess=input("Make a guess-->\t")
    if guess.isdigit():
        guess=int(guess)
        
    else:        
           print("Please enter a number.")
           continue
        
        
    #if length==10:
     

        #print(random_number)
   


    if random_number== guess:
            random_number=random.randint(0,range)
            print("\t\t\tCongratulations!You got it.")
            score += 1        
        
                
    
    print("\t\t\tyou got ",score,"marks.")  

    a+=1
print("\n\t\tYOur term is over")
per=(score/a)*100
print("\n\t\t\tYou got ",(per),"% marks.")
if per <= 40:
    print("\n\t\t\t\tBad luck :) You Fail.")
else:
    print("\n\t\t\t\tCongrats :)(: You Pass.")

#print("\t\t\tBad Luck!! Your guess is incorrect.")   
            

