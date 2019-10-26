import hashlib

def hash():

    
    password = input("Please enter a pwd: ")
    
    key = hashlib.sha256(str(password).encode()).hexdigest()
    key = key[:8]
    print(key)
                       
    hash()

hash()
