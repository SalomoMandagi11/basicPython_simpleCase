"""
    In this code, we will learn to implement some methods in case of string:
    1. len()
    This is actually a general purpose methods. It can be use to list also.
    This method is to count how much the characters on the string.
    2. upper()
    This method made a string to uppercase
    3. lower()
    This method made a string to lowercase
    4. title()
    This method is use to make each first alphabet on a word to upper.
    for example: This Method Is Use To Make Each
    4. find()
    This method is use to find a character or a sequence character who appear in the first place that have correspondent
    Return the index of the characters that appear in the first place.
    to a character.
    5. replace()
    This method is use to replace a string with another new string.

    How to use number 1 to 4 method?
    Simply write: variable_name.method()

    How to use number 5 method?
    Simply write: variable_name.method("string you want to replace", "the string")

    Case 1:
    Membuat sebuah login, dengan username dan password.
    Username dibatasi dengan 10 karakter.

    Case 2:
    Create a string and then find a correspondent character.

"""

# Case 1:

# for now, we don't use a function to make this code efficient
"""
username = input("Username: ")
msg = 'Username only accept 10 characters.'
password = input("Password: ")

if len(username) > 10:
    print(msg)
    print("Please input again.")
    username = input("Username: ")
    password = input("Password: ")
    if len(username) <= 10:
        print(f"Nice name {username.title()}, welcome to our social media! Make new friend(s), make happiness^-^")
else:
    print(f"Nice name {username.title()}, welcome to our social media! Make new friend(s), make happiness^-^")
"""

# Case 2:
"""
str_case2 = 'Stay motivated!'
upper_str = str_case2.upper()
# title_str = str_case2.title()
search = input("Search: ")

if upper_str.find(search) >= 0:  # if it is more than or equal to zero, then there is a character that we search
    print(f"Yeah, there is '{search}' on the string!")
    yes_or_no = input(f"Do you want to replace the word {search} with a new word?(yes/no) ")

    if yes_or_no == 'yes':
        new_word = input("Replace with: ")
        replace_str = upper_str.replace(search, new_word)
        print(f"Here is the new string: {replace_str}")
    elif yes_or_no == 'no':
        print("Okay, no problem with it, thank you!")
    else:
        print("You typed the wrong input!")
        
else:
    print(f"Seems like there is no '{search}' on the string.")
    print("Thank you for using this code!")
"""