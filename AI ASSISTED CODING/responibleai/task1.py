# Task 1: Privacy & Security in File HandlingIdentified Privacy Risks:
# Storing user data in plain text is a severe security vulnerability. If an AI tool generates a script that writes raw passwords to a .txt or .csv file without encryption, anyone with file access can read the credentials, leading to identity theft and data breaches.  Revised Version (Encrypted Password Storage):
# This script uses the hashlib library to hash the password before storing it, ensuring the plain text password is never saved. 
import hashlib
import json

def store_user_data(name, email, plain_password):
    # Hash the password using SHA-256 (in production, use bcrypt or Argon2 with a salt)
    hashed_password = hashlib.sha256(plain_password.encode()).hexdigest()
    
    user_record = {
        "name": name,
        "email": email,
        "password_hash": hashed_password
    }
    
    with open("users.json", "a") as file:
        file.write(json.dumps(user_record) + "\n")
    print("User securely stored.")

store_user_data("Alex", "alex@example.com", "SuperSecret123!")