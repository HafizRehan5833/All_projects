#. Write a function that takes a list of employee salaries and calculates the average salary.
def average_salary(salleries):
    if not salleries:
        return 0
    return sum(salleries)/len(salleries)
salleries_list=[]
#print("Your salleries list are -->", salleries_list)
user_input=input("\t\t\tDo you want to  addition or not: ")
if user_input == "add":
    num=int(input("\t\t\tEnter between 1 to 12..\n\t\t\t\tHow many employee in your company : "))
    if num == 1:
        add_salary1=int(input("Enter add salary: "))
        salleries_list.append(add_salary1)
        print("Your salleries list after addition -->", salleries_list)
        total_sum=sum(salleries_list)
        print("Your",len(salleries_list),"employee salleries, you want in one month-->",total_sum)
        result=average_salary(salleries_list)
        print(f"You need apyment in one month that pay you {len(salleries_list)} employees --> { result:.2f}")





    elif num == 2:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        salleries_list.extend([add_salary1,add_salary2])
        print("Your salleries list after addition -->", salleries_list)
        total_sum=sum(salleries_list)
        print("Your",len(salleries_list),"employee salleries, you want in one month-->",total_sum)
        result=average_salary(salleries_list)
        print(f"You need apyment in one month that pay you {len(salleries_list)} employees --> { result:.2f}")





    elif num == 3:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        salleries_list.extend([add_salary1,add_salary2,add_salary3])
        print("Your salleries list after addition -->", salleries_list)
        total_sum=sum(salleries_list)
        print("Your",len(salleries_list),"employee salleries, you want in one month-->",total_sum)
        result=average_salary(salleries_list)
        print(f"You need apyment in one month that pay you {len(salleries_list)} employees --> { result:.2f}")





    elif num == 4:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4])
        print("Your salleries list after addition -->", salleries_list)
        total_sum=sum(salleries_list)
        print("Your",len(salleries_list),"employee salleries, you want in one month-->",total_sum)
        result=average_salary(salleries_list)
        print(f"You need apyment in one month that pay you {len(salleries_list)} employees --> { result:.2f}")







    elif num == 5:
        #input the salaries
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        add_salary5=int(input("\tEnter add salary: "))

    #make a list
        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4,add_salary5])
    #show list
        print("Your salleries list after addition -->", salleries_list)
    #show sum 
        total_sum=sum(salleries_list)
        print("Your",len(salleries_list),"employee salleries, you need per year-->",total_sum)
    #show result
        result=average_salary(salleries_list)
        print(f"You need payment in one month that pay you {len(salleries_list)} employees --> { result:.2f}")






    elif num == 6:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        add_salary5=int(input("\tEnter add salary: "))
        add_salary6=int(input("\tEnter add salary: "))
        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6])
        print("Your salleries list after addition -->", salleries_list)
        total_sum=sum(salleries_list)
        print("Your",len(salleries_list),"employee salleries, you want in one month-->",total_sum)
        result=average_salary(salleries_list)
        print(f"You need apyment in one month that pay you {len(salleries_list)} employees --> { result:.2f}")






        

    elif num == 7:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        add_salary5=int(input("\tEnter add salary: "))
        add_salary6=int(input("\tEnter add salary: "))  
        add_salary7=int(input("\tEnter add salary: "))  
        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7])  
        print("Your salleries list after addition -->", salleries_list)
        total_sum=sum(salleries_list)
        print("Your",len(salleries_list),"employee salleries, you want in one month-->",total_sum)
        result=average_salary(salleries_list)
        print(f"You need apyment in one month that pay you {len(salleries_list)} employees --> { result:.2f}")






    elif num == 8:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        add_salary5=int(input("\tEnter add salary: "))
        add_salary6=int(input("\tEnter add salary: "))  
        add_salary7=int(input("\tEnter add salary: "))    
        add_salary8=int(input("\tEnter add salary: ")) 
        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7,add_salary8])
        print("Your salleries list after addition -->", salleries_list)
        total_sum=sum(salleries_list)
        print("Your",len(salleries_list),"employee salleries, you want in one month-->",total_sum)
        result=average_salary(salleries_list)
        print(f"You need apyment in one month that pay you {len(salleries_list)} employees --> { result:.2f}")






    elif num == 9:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        add_salary5=int(input("\tEnter add salary: "))
        add_salary6=int(input("\tEnter add salary: "))  
        add_salary7=int(input("\tEnter add salary: "))    
        add_salary8=int(input("\tEnter add salary: "))       
        add_salary9=int(input("\tEnter add salary: "))       
        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7,add_salary7,add_salary9])
        print("Your salleries list after addition -->", salleries_list)
        total_sum=sum(salleries_list)
        print("Your",len(salleries_list),"employee salleries, you want in one month-->",total_sum)
        result=average_salary(salleries_list)
        print(f"You need apyment in one month that pay you {len(salleries_list)} employees --> { result:.2f}")






    elif num == 10:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        add_salary5=int(input("\tEnter add salary: "))
        add_salary6=int(input("\tEnter add salary: "))  
        add_salary7=int(input("\tEnter add salary: "))    
        add_salary8=int(input("\tEnter add salary: "))       
        add_salary9=int(input("\tEnter add salary: ")) 
        add_salary10=int(input("\tEnter add salary: ")) 
        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7,add_salary8,add_salary9,add_salary10])          
        print("Your salleries list after addition -->", salleries_list)
        total_sum=sum(salleries_list)
        print("Your",len(salleries_list),"employee salleries, you want in one month-->",total_sum)
        result=average_salary(salleries_list)
        print(f"You need apyment in one month that pay you {len(salleries_list)} employees --> { result:.2f}")
        








    elif num == 11:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        add_salary5=int(input("\tEnter add salary: "))
        add_salary6=int(input("\tEnter add salary: "))  
        add_salary7=int(input("\tEnter add salary: "))    
        add_salary8=int(input("\tEnter add salary: "))       
        add_salary9=int(input("\tEnter add salary: ")) 
        add_salary10=int(input("\tEnter add salary: "))  
        add_salary11=int(input("\tEnter add salary: "))      
        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7,add_salary8,add_salary9,add_salary10,add_salary11])          
        print("Your salleries list after addition -->", salleries_list)


        total_sum=sum(salleries_list)
        print("Your",len(salleries_list),"employee salleries, you want in one month-->",total_sum)

        result=average_salary(salleries_list)

        print(f"You need apyment in one month that pay you {len(salleries_list)} employees --> { result:.2f}")
        
    elif num == 11:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        add_salary5=int(input("\tEnter add salary: "))
        add_salary6=int(input("\tEnter add salary: "))  
        add_salary7=int(input("\tEnter add salary: "))    
        add_salary8=int(input("\tEnter add salary: "))       
        add_salary9=int(input("\tEnter add salary: ")) 
        add_salary10=int(input("\tEnter add salary: "))  
        add_salary11=int(input("\tEnter add salary: "))
        add_salary12=int(input("\tEnter add salary: "))
        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7,add_salary8,add_salary9,add_salary10,add_salary11,add_salary12])          
        print("Your salleries list after addition -->", salleries_list)
        total_sum=sum(salleries_list)
        print("Your",len(salleries_list),"employee salleries, you want in one month-->",total_sum)
        result=average_salary(salleries_list)
        print(f"You need apyment in one month that pay you {len(salleries_list)} employees --> { result:.2f}")            





else:
     print("\t\tYou do not need to add salleries...")   



