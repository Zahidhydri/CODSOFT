import json
import os

def file_check():
    global contacts
    file_path="contacts.json"
    if os.path.exists(file_path):
        try:
            with open("contacts.json", "r") as file:
                contacts = json.load(file)
        except FileNotFoundError:
            contacts = []
    else:
        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=2)
            contacts = []

         
    return contacts
         


#=========================================================
contacts = file_check()
#===================================================================

if "u" in contacts:
    print("yes")
else:
    print("no")

for i in contacts :
    for key in i:
        print(i[key])