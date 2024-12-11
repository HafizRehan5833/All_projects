n=1

while True:


    print("..................................................................................................................................................................................")
    print(f"\t\t\t\t\t{n}:Here is the function options.")
    print("1.Full-Dictionary\t\t2.Access the value\t\t\t3.Add a new entity\t\t4.Update the value\t\t5.Remove the key\n6.Print all keys\t\t7.Print all values\t\t\t8.print all key-value pairs in the format key: value\t\t9.Check if the key exists\n10.Count number of keys\t\t11.Merge the two dictionaries\t\t12.Create a dictionary from a list of tuples\t\t\t13:Sort the keys\n14.Create a nested dictionary\t15.Access the value from nested\t16.Add a key in nested dictionary\t17.Delete the key from the nested dictionary.\n18.The keys in the outermost level of the nested dictionary and print them.\t\t\t\t19.find the key with the maximum value\n20) 1 to 5 to their squares\t21.the value associated with the key.\t22.the keys are the first n positive integers, and the values are their cubes.\n23.Flatten the following nested dictionary into a single-level dictionary\t24.the values are odd or even")
    print("..................................................................................................................................................................................")

    user_input_for_options=input("\nEnter the option number which you want to use it: ")
    
                                                        #Basic operations

    # 1.	Create a dictionary student with keys: name, age, and grade. Assign them appropriate values.
    if user_input_for_options == "1":
        student_info={
                    "name":"Rehan",
                    "age":19,
                    "grade":"A"
                    
                    }
        print(student_info)

    #2.Access the value of the key grade in the student dictionary.
    elif user_input_for_options == "2":
        student_info={
                    "name":"Rehan",
                    "age":19,
                    "grade":"A"
                    
                    }
        print("\t\t\t	Access the key in dictionary  ")
        for key in student_info.keys():
            print(f"\t\t\t\t\t\t\t{key}")

        user_input=input("Enter the key Which value you want : ")
                
        print(f"\t\t\t\tThe value of {user_input} is {student_info[user_input]}")                     


    #3.	Add a new key city to the student dictionary and set its value to "New York"

    elif user_input_for_options=="3":


        student_info={
                    "name":"Rehan",
                    "age":19,
                    "grade":"A"
                    
                    }
        print("\t\t\t3.	Add a new key \n")
        print(f"\t\tThe dictionary before addition:{student_info}\n")

        user_input_for_key=input("Enter the key: ")
        user_input_for_value=input("Enter the value:")

        student_info[user_input_for_key]=user_input_for_value


        print("\t\t\tThe Dictionary after add a new key:",student_info)


    #4.	Update the value of the age key in the student dictionary to 20.


    elif user_input_for_options== "4":
        student_info={
                    "name":"Rehan",
                    "age":19,
                    "grade":"A"
                    }


        print(f"\tThe Dictionary before updation:{student_info}")
        print("\n\t\t\t4.After updation")

        user_input_For_update=input("Enter the key: ")
        user_input_For_update_value=input("Enter the value: ")

        (student_info[user_input_For_update])=user_input_For_update_value
        print(f"\t\t\tThe dictionary after updation: {student_info}")


    #5.Remove the key city from the student dictionary.

    elif user_input_for_options=="5":
        student_info={
                    "name":"Rehan",
                    "age":19,
                    "grade":"A"
                    
                    }

        print(f"\tThe Dictionary is:\n\t\t{student_info}")
        user_input_remove_key=input("\tEnter the key which you want to remove it")
        print(f"\n\t\t\t5.After removing ")
        del student_info[user_input_remove_key]

        print(f"The dictionary after remove the {user_input_remove_key}:\n\t\t\t{student_info}")

                                                        #Iterating through Dictionaries

    #6.	Iterate through the dictionary student and print all keys.
    elif user_input_for_options=="6":
        student_info={
                    "name":"Rehan",
                    "age":19,
                    "grade":"A"
                    
                    }


        print("\n\t\t\t\t6.print all keys")

        for keys,values in student_info.items():
            print(f"The key are:{keys}")
            print(f"\tThe values are:{values}")            


    #7.	Iterate through the dictionary student and print all values.
    elif user_input_for_options=="7":

            student_info={
                        "name":"Rehan",
                        "age":19,
                        "grade":"A"
                        
                        }



            print("\t\t\t7.This is only values.........")
            for value in student_info.values():
                print(f"The values:{value}")



    #8.	Iterate through the dictionary student and print all key-value pairs in the format key: value.


    elif user_input_for_options=="8":
        student_info={
                    "name":"Rehan",
                    "age":19,
                    "grade":"A"
                    
                    }


        print("\n\t\t\t\t8.print all keys in key:value sequence\n")

        for keys,values in student_info.items():
                    print("\t\t\t",keys,":",values)

    #9.	Check if the key grade exists in the student dictionary and print True or False

    elif user_input_for_options=="9":
        student_info={
                    "name":"Rehan",
                    "age":19,
                    "grade":"A",
                    "phone":+923019201234
        }
        #print(f"The Dictionary is:\n\t\t{student_info}")
                
        #print(f"\t9.Check if the key exists in the student dictionary ")
        user_input_for_exist_value=input("Enter the key which you want to exists: ")
                #for keys,values in student_info.items():
        if  user_input_for_exist_value in student_info:
                            print(f"\t\t\t\t{user_input_for_exist_value} is available..")
                        
                            
        else:
                            print(f"\t\t\t\t{user_input_for_exist_value} is not available..")   


    #10.	Count the total number of keys in the student dictionary.
    elif user_input_for_options=="10":

        student_info={
                    "name":"Rehan",
                    "age":19,
                    "grade":"A"
        }

        print("\t\t\t10..Count the total number of keys")
        length=len(student_info)

        print("The length of our dictionary is : ",length)

                                                        #Advanced Dictionary Usage

    #11.	Merge the following two dictionaries and print the result:
    #12.	dict1 = {'a': 1, 'b': 2}  
    #dict2 = {'c': 3, 'd': 4}  
    elif user_input_for_options=="11":
        dict1 = {'a': 1, 'b': 2}  
        dict2 = {'c': 3, 'd': 4}  

        dict1.update(dict2)
        print(f"After merging dictionary: {dict1}")


    #13.	Create a dictionary from a list of tuples: [('name', 'Alice'), ('age', 25), ('city', 'Paris')].
    elif user_input_for_options=="12":
        print("\n\t\t\tCreate a dictionary from a list of tuples\n")

        Tuple_list=[('name', 'Alice'), ('age', 25), ('city', 'Paris')]
        print(f"The Tuple list : {Tuple_list}")
                #dict functionis use to create 
        Tuple_list_from_dict=dict(Tuple_list)

        print(f"The list make a dictionary\n\t\t\t{Tuple_list_from_dict}")


    #14.	Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.
    elif user_input_for_options=="13":
        unsort_dict={'z': 1, 'a': 2, 'c': 3}
            # print(f"\t\tThe unsorting Dictionary: \t{unsort_dict}")

        sort_dict=dict (sorted(unsort_dict.items() )  )
        print(f"\n\tUnsorted Dictionary: {unsort_dict}")

        print(f"\n\t\t\tSorted dictionary{sort_dict}")



                                                        #Nested Dictionaries



    #16.	Create a nested dictionary to represent the following data:
    #17.	Person:  
    #18.	  Name: John  
    #19.	  Age: 30  
    #20.	  Address:  
    #21.	    Street: 123 Elm St  
    #22.	    City: Boston  

    elif user_input_for_options == "14":


        person={
            "Name" : "John" ,
            "Age": 30 ,
            "Address":{
                "Street": "123 Elm St ",
                "City": "Boston "
            }

        }

        print(person)



    #23.	Access the value of the City key in the nested dictionary from the previous question.
    elif user_input_for_options == "15":

        person={
            "name" : "Hafiz Muhammad Rehan" ,
            "age": 19,
            "address":{
                "street": "P-485 D block millat town",
                "city": "Faisalabad"
            }

        }
        for key in person.keys():
            print(f"\t\t\tThe keys are:{key}")

        user_input=input("Enter the key: ")
        if user_input in person:
            if user_input == "address":
                user_input_for_address=input("Enter the city or street:")
                address_dict=person["address"][user_input_for_address]
                print(address_dict)

            elif user_input != "address":
                calling_city=person[user_input]
                print(calling_city)
        

        else:
            print("Invalid")



    #24.	Add a new key Phone to the nested dictionary with the value "123-456-7890".
    elif user_input_for_options == "16":
        person={
            "name" : "Hafiz Muhammad Rehan" ,
            "age": 19,
            "address":{
                "street": "P-485 D block millat town",
                "city": "Faisalabad"
            }
        }
        user_input_for_permission=input("Do you want to add a number.Enter Yes/no:").lower()
        if user_input_for_permission == "yes":
            add_number=int(input("Enter a number in 123-456-7890 format: "))


            person["Phone-number"]=add_number
            print(person)
        else:
            print("\t\t\t\tYou do not add a key")
            print(f"\t\t\tYour dictionary without addition a key {person}")

    #print(f"Dictionry without add a key..{person}") 



    #25.	Delete the Address key from the nested dictionary.
    elif user_input_for_options == "17":

        person={
            "name" : "Hafiz Muhammad Rehan" ,
            "age": 19,
            "address":{
                "street": "P-485 D block millat town",
                "city": "Faisalabad"
            }
        }

        for key in person.keys():
            print("The key is: ",key)

        user_input=input("Enter the key which you want to delete: ")

        if user_input in person:

            if user_input == "address":
                #user_input_for_yes_no=input("Enter Yes or no: ").lower()
                # if user_input_for_yes_no == "yes":
                for key in person["address"].keys():
                            print(f"The address key :{key}")

                user_input_for_key=input("Enter the key which you want to delete: ").lower()
                del person["address"][user_input_for_key]
                print(f"\t\t\tThe Dictionary without {user_input_for_key}")
                #print(f"The dictionary is {person}")
                for key,value in person.items():
                    print(key,":",value)

                #else:
                #   print("No problem")
            else:

                print(f"\t\t\t\tThe dictionary without {user_input}")
                del person[user_input]
                for key,value in person.items():
                        print(key,":",value)
                #print(person)

        else:
            print(f"\t\t\t\tYou enter {user_input} is not key in dictionary..")        



    #26.	Iterate through all the keys in the outermost level of the nested dictionary and print them.
    elif user_input_for_options == "18":

        person={
            "name" : "Hafiz Muhammad Rehan" ,
            "age": 19,
            "address":{
                "street": "P-485 D block millat town",
                "city": "Faisalabad"
            }
        }


        for key in person.keys():
            if key == "address":
                for address_key in person["address"].keys():
                    print(f"The keys of address are ({address_key})")


                                                        #Applications of Dictionaries


    #27.	Write a Python program to find the key with the maximum value in the dictionary {'a': 10, 'b': 15, 'c': 7}.
    #dictionary={"a":10,"b":12,"c":14,"d":16}

    #.get is a built-in function that allows you to access the value of an item associated with the specified key.
    #print(f"The dictionary is {dictionary}")
    #max_num=max(dictionary,key=dictionary.get)

    #print(f"\n\t\t\tThe  value of {max_num} is maximum in your dictionary  ")

    elif user_input_for_options == "19":

        user_dict={}

        n=int(input("Enter a number how many items do you want to add: "))

        for i in range(n):
            key=input(f"Enter key {i+1}: " )
            value=input(f"Enter value for key {key}: ")
            user_dict[key]=value

        print(user_dict)

        if user_dict:
            max_key_user=max(user_dict,key=user_dict.get)
            print(f"The key with the maximum value in your dictionary is {max_key_user} with the value of {user_dict[max_key_user]}")

        else:
            print("The dictionary is empty ")        


    #28.	Create a dictionary to map numbers 1 to 5 to their squares (e.g., {1: 1, 2: 4, 3: 9, ...}).
    elif user_input_for_options == "20":
        user_input=int(input("Enter the number where loop ends: "))
        squares_dictionary={num:num**2 for num in range(1,user_input+1)}
        print(squares_dictionary)


    #29 Write a Python function that accepts a dictionary and a key, and returns the value associated with the key. If the key doesn’t exist, return "Key not found".

    elif user_input_for_options == "21":
        def accept_key(dictionary,key):
            return dictionary.get(key,"\n\t\t\t\tKEy not find")
        dictionary_user={'name': 'Rehan', 'age': 19, 'grade': 'A',"roll number":245289,"semester":"First Evening-B","phone":+923019201234,"university":"Government University of Faislabad"}
        while True:
            
            
            user_input=input("Enter the key which you want and q for quit : ").lower()
            if user_input == "q":
                quit()
            else:    
                func=accept_key(dictionary_user,user_input)
                print(func)
                
                                                                #Challenging Problems

    #30  Write a Python program to create a dictionary where the keys are the first n positive integers, and the values are their cubes. Take n as user input.
    elif user_input_for_options == "22":
        user_input=int(input("Enter the number: "))

        cude_root={num:num**3 for num in range(1,user_input+1)}

        print(cude_root)

                                                

    #31. Flatten the following nested dictionary into a single-level dictionary:
    elif user_input_for_options == "23":
        nested_list={"a":{
            "b":1,
            "c":2,
            "d":3
        },


        }
        print("Ourself")
        for key,sub_dict in nested_list.items():
            for sub_key,sub_value in sub_dict.items():
                print({f"{key}-{sub_key}:{sub_value}"})



        print("With the help of chat-gpt  ")
        flatten_dict={f"{key}-{sub_key}":sub_value for key,sub_dict in nested_list.items() for sub_key,sub_value in sub_dict.items() }

        print(flatten_dict)

    #32.Write a Python program to split a dictionary into two based on whether the values are odd or even
    elif user_input_for_options == "24":
        dictionary_num={"a":2,"b":3,"c":4,"d":6,"e":5,"f":7}
        new_dict={"g":8,"h":9,"i":10}

        dictionary_num.update(new_dict)

        reverse=dictionary_num.__reversed__()


        even_num={f"{k}:{v}" for k,v in dictionary_num.items() if v%2==0}
        odd_num={f"{k}:{v}" for k,v in dictionary_num.items() if v%2!=0}


        print("Even-numbers=",even_num)
        print("Odd-numbers= ",odd_num)

    elif user_input_for_options == "q":
        print("Thanks for using it")
        break


    n+=1





