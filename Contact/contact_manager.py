# from tkinter import *
# import json
# import os


# def load_file():
#     global contacts
#     with open("contacts.json","r") as file:
#         contacts=json.load(file)
#         contacts=list(contacts)
#         print(contacts)
#     return contacts
# load_file()

# def add_file():
#     global contacts
#     new_contact={"name":"A","phone":8775677}
#     new_contact=contacts.append(new_contact)
#     with open("contacts.json","w") as file:
#         json.dump(new_contact,file,indent=2)

# add_file()

with open("mycontact.txt","a"   ) as file:
    file.write("a-85758")

with open("mycontact.txt","r") as file:
    n=file.read()
print(n)



