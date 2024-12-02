import random
import string

def generate_password(min_length, max_length, numbers= True, special_characters= True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    #print(letters, digits, special)

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        if len(pwd) >= max_length: # Ensure password doesnt exceed max_length
            break
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    
    # If the password exceeds the max_length after the loop, truncate it
    if len(pwd) > max_length:
        pwd = pwd[:max_length]

    return pwd

# User inputs
min_length = int(input("Enter the minimum length: "))
max_length = int(input("Enter the maximum length: "))
has_number = input("Do  you want to have numbers (y/n)? ").lower() == "y"
has_special = input("DO you want to have special characters (y/n)? ").lower() == "y"

# Generate and display the password 
pwd = generate_password(min_length, max_length, has_number, has_special)
print("The generated password is:", pwd)