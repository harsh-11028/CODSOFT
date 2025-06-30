#TASK - 3
#PASSWORD GENERATOR


import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length must be greater than 0.")
                continue
            password = generate_password(length)
            print("Generated password:", password)
            again = input("Generate another password? (y/n): ").lower()
            if again != 'y':
                print("Thank you for using the password generator. Goodbye!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
