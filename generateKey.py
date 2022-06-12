from cryptography.fernet import Fernet

print("Generating a random key...")
key = Fernet.generate_key().decode()
print("Key generated.")
print("Please input the entire following key into config.py: " + str(key))
