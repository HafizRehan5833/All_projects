import random
import string


def random_password(length):
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits=string.digits
    special_character=string.punctuation

    all_characters=lowercase+uppercase+digits+special_character

    if length<4:
        raise ValueError ("At least 4 character required to generate a password.But unfortunately you enter ",length)

    password=[
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_character)       
    ]

    password += random.choices( all_characters,k=length-4)


    random.shuffle(password)

    return ''.join(password)



user_input_for_length=int(input("Enter the length of password: "))

func=random_password(user_input_for_length)

print("Your password is generated according to your length:\n\t\t\t\t\t\t   ",func)


