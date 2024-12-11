#6. Create a function that takes a string and counts the frequency of each character.
from collections import Counter
def frequency_of_lette(user_string):
    #return f"Your string is {user_input}"
    freq=Counter(user_string)
    return freq

user_input=input("Enter a string: ") 
print("Your string is: ",user_input)
#user_char=input("Enter character:")

func=frequency_of_lette(user_input)

print(func)

