# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
import string
def generate_password (length=12):
#Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
#Generate a password by randomly selecting characters
    password= ''.join(random.choice(characters) for _ in range(length))

    return password
def main():
    try:
     password_length = int(input("Enter the desired password length: "))
     
     if password_length < 6:
         print("Password Length must be at least 6 character.")
     else: 
         generated_password = generate_password(password_length) 
         print("Generated password:", generated_password)
    except ValueError:
        print("Please enter a valid number for the password length.")
if __name__ == "__main__": main()