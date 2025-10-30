import json
jsonfile="mylinux.json"
from cryptography.fernet import Fernet

with open(jsonfile) as jf:
    my_dict = json.load(jf)

print("My username is: " + my_dict['username'])


mypass=my_dict['password']
message = mypass.encode("utf-8")

key=Fernet.generate_key()
f = Fernet(key)


#Encrypting Password
encrypted=f.encrypt(message)
decrypted=f.decrypt(encrypted)
my_new_pass=decrypted.decode("utf-8")
print(my_new_pass)