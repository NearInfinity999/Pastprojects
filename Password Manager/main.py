from cryptography.fernet import Fernet
import os

# Generate a key(tijori ki chabi) if it doesn't exist
def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

# Load the key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a password
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Decrypt a password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Save password to a file
def save_password(website, username, encrypted_password):
    with open("passwords.txt", "a") as f:
        f.write(f"{website},{username},{encrypted_password.decode()}\n")

# View stored passwords
def view_passwords(key):
    if os.path.exists("passwords.txt"):
        with open("passwords.txt", "r") as f:
            for line in f.readlines():
                website, username, encrypted_password = line.strip().split(",")
                decrypted_password = decrypt_password(encrypted_password.encode(), key)
                print(f"Website: {website}, Username: {username}, Password: {decrypted_password}")
    else:
        print("No passwords stored yet!")

# Main function to interact with the password manager
def main():
    generate_key()
    key = load_key()

    while True:
        print("\nPassword Manager")
        print("1. Add a new password")
        print("2. View stored passwords")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter the website name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            encrypted_password = encrypt_password(password, key)
            save_password(website, username, encrypted_password)
            print("Password saved successfully!")
        
        elif choice == "2":
            view_passwords(key)
        
        elif choice == "3":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
