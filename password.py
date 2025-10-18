welcome = ("welcom my Group")
print(welcome)


import string
import secrets
import getpass
import hashlib
import base64
from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    key = Fernet.generate_key()
    return key

# Encrypt password
def encrypt_password(password, key):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(password.encode())
    return cipher_text

# Decrypt password
def decrypt_password(cipher_text, key):
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text)
    return plain_text.decode()

# Generate a random password
def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

# Store password
def store_password(account, password, key):
    cipher_text = encrypt_password(password, key)
    with open("passwords.txt", "a") as f:
        f.write(f"{account}:{cipher_text.decode()}\n")

# Retrieve password
def retrieve_password(account, key):
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            acc, cipher_text = line.strip().split(":")
            if acc == account:
                return decrypt_password(cipher_text.encode(), key)
    return None

def main():
    key = generate_key()
    print("Your encryption key is:", key)

    while True:
        print("\n1. Generate password")
        print("2. Store password")
        print("3. Retrieve password")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            length = int(input("Enter password length: "))
            password = generate_password(length)
            print("Generated password:", password)
        elif choice == "2":
            account = input("Enter account name: ")
            password = input("Enter password: ")
            store_password(account, password, key)
            print("Password stored!")
        elif choice == "3":
            account = input("Enter account name: ")
            password = retrieve_password(account, key)
            if password:
                print("Password:", password)
            else:
                print("Account not found!")
        elif choice == "4":
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()