student_info={
            "name":"Rehan",
            "age":19,
            "grade":"A"
            
            }
print("\t\t\t\tThis is a dictionary Functional Software.")
while True:
    print("......................................................................................................................................................................................")
    print("\t\t\t\t\tHere is the function options.")
    print("1.Full-Dictionary\t\t\t\t\t2.User Grade\t\t\t\t3.Add a new city in dictionary\n4.Update the value\t\t\t\t\t5.Remove the key\t\t\t6.the dictionary student and print all keys\n7.the dictionary student and print all values\t\t8.print all key-value pairs in the format key: value\n9.Check if the key exists\t\t\t\t10.Count the total number of keys\t11.Merge the two dictionarie\n12.Create a dictionary from a list of tuples\t\t13:Sort the keys")
    print("......................................................................................................................................................................................")
    user_input_for_options=input("\n\t\tEnter the option number and q for quit : ").lower()

    if user_input_for_options == "q":
        print("\t\t\t\tThanks for using our software..")
        quit()
    #1.	Create a dictionary student with keys: name, age, and grade. Assign them appropriate values.
    
    
    elif user_input_for_options == "1":
        
            
            #{"name":"Aleem",
        # "age":20,
            #"grade":"B+"}
            
            
        print(f"\t\t\t\tDictionary is :{student_info}\n\n")
        

    #2.	Access the value of the key grade in the student dictionary
    elif user_input_for_options =="2":
        #user_input_for_acess_value=input("Enter what value you want: ")
        print("\t\t\t2.	Access the value of grade in dictionary ")

        
        print(f"\t\t\t\tThe grade of Rehan is:{student_info['grade']}")
            
    #3.	Add a new key city to the student dictionary and set its value to "New York".
    elif user_input_for_options == "3":
        print("\t\t\t3.	Add a new key city\n")

        print(f"\t\tThe dictionary before addition:{student_info}\n")

        (student_info["city"])="New York"
        print("\t\t\tThe Dictionary after add a new key:",student_info)


    #4.	Update the value of the age key in the student dictionary to 20.
    elif user_input_for_options =="4":

        print(f"\tThe Dictionary before updation:{student_info}")
        print("\n\t\t\t4.After updation")
        (student_info["age"])=20
        print(f"\t\t\tThe dictionary after updation: {student_info}")

    #5.	Remove the key city from the student dictionary.
    elif user_input_for_options =="5":
        print(f"\tThe Dictionary is:\n\t\t{student_info}")
        user_input_remove_key=input("\tEnter the key which you want to remove it")
        print(f"\n\t\t\t5.After removing ")
        del student_info[user_input_remove_key]

        print(f"The dictionary after remove the {user_input_remove_key}:\n\t\t\t{student_info}")

    #6.	Iterate through the dictionary student and print all keys.
    elif user_input_for_options == "6":
        print("\n\t\t\t\t6.print all keys")

        for keys,values in student_info.items():
                print(f"The key are:{keys}")
                print(f"\tThe values are:{values}")

    #7.	Iterate through the dictionary student and print all values.
    elif user_input_for_options =="7":
        print("\t\t\t7.This is only values.........")
        for value in student_info.values():
            print(f"The values:{value}")


    #8.	Iterate through the dictionary student and print all key-value pairs in the format key: value.    

    elif user_input_for_options == "8":
        print("\n\t\t\t\t8.print all keys in key: value\n")

        for keys,values in student_info.items():
            print("\t\t\t",keys,":",values)

    #9.	Check if the key grade exists in the student dictionary and print True or False.
    elif user_input_for_options == "9":
        
        
        print(f"The Dictionary is:\n\t\t{student_info}")
        

        print(f"\t9.Check if the key grade exists in the student dictionary ")

        #for keys,values in student_info.items():
        if  user_input_check_key in student_info:
                    print(f"\t\t\t\tGrade is available..")
                   
                    
        else:
                    print(f"\t\t\t\tGrade is not available..")   
              


    #10.	Count the total number of keys in the student dictionary.
    elif user_input_for_options ==" 10":
        print("\t\t\t10..Count the total number of keys")
        length=len(student_info)

        print("The length of our dictionary is : ",length)



    #11.	Merge the following two dictionaries and print the result:	dict1 = {'a': 1, 'b': 2}  , dict2 = {'c': 3, 'd': 4}  
    elif user_input_for_options=="11":
        print(f"\n\t\t\tMerging the dictionaries:\t{dict1} and {dict2}")
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        dict1.update(dict2)
        print(f"After merging dictionary: {dict1}")


    #12.	Create a dictionary from a list of tuples: [('name', 'Alice'), ('age', 25), ('city', 'Paris')].
    elif user_input_for_options=="12":
        print("\n\t\t\tCreate a dictionary from a list of tuples\n")

        Tuple_list=[('name', 'Alice'), ('age', 25), ('city', 'Paris')]
        print(f"The Tuple list : {Tuple_list}")
        #dict functionis use to create 
        Tuple_list_from_dict=dict(Tuple_list)

        print(f"The list make a dictionary\n\t\t\t{Tuple_list_from_dict}")



    #13.	Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.
    elif user_input_for_options =="13":

        unsort_dict={'z': 1, 'a': 2, 'c': 3}
       # print(f"\t\tThe unsorting Dictionary: \t{unsort_dict}")

        sort_dict=dict (sorted(unsort_dict.items() )  )
        print(f"\n\tUnsorted Dictionary: {unsort_dict}")

        print(f"\n\t\t\tSorted dictionary{sort_dict}")



#Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).

    #elif user_input_for_options == "14":
     
     #   empty_dict={}
      
      #  user_input=int(input("enter The length of dictionary:"))
        # for i in range(0,user_input+1):
         #   Enter_dictionary=input("Enter the name:")
          #  dict(empty_dict+Enter_dictionary)
        #print(empty_dict)



        

            



    else:
        print(f"\t\t\t\t\tYou enter {user_input_for_options} is not valid....")
        quit()