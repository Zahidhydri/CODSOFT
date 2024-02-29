from tkinter import *
# from tkinter.scrolledtext import *
import json

# Function to load contacts from a JSON file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

# Function to save contacts to a JSON file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=2)

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(new_contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")

# Function to search contacts by name or phone number
def search_contact(query):
    results = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    return results

# Function to update contact details
def update_contact():
    view_contacts()
    index = int(input("Enter the index of the contact to update: ")) - 1

    if 0 <= index < len(contacts):
        field = input("Enter the field to update (name, phone, email, address): ")
        new_value = input(f"Enter new {field}: ")

        contacts[index][field] = new_value
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Invalid index.")

# Function to delete a contact
def delete_contact():
    view_contacts()
    index = int(input("Enter the index of the contact to delete: ")) - 1

    if 0 <= index < len(contacts):
        del contacts[index]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Invalid index.")

contacts = load_contacts()

# Main
zahid=Tk()
zahid.title("Contact Manager")
zahid.configure(background='#91f',relief="ridge",bd=10)
zahid.resizable(0,0)
# zahid.attributes("-fullscreen",True)


# list_frame=Frame(zahid)
# list_frame.pack()

# t=Listbox(list_frame)
# for i in range(100):
#     Listbox.insert(END,i)

# t.pack(fill=Y)
# s=Scrollbar(list_frame)
# s.pack(side=RIGHT,fill=BOTH)


# t.config(yscrollcommand=Scrollbar.set)
# s.config(command=t.yview)



#======================================
# Add Contact

add_label = Label(zahid,font = ('arial',30,'bold'),fg="#eef",bg="#30f", text=" Add Contact ",relief="raised", bd=5)
add_label.grid(row=0, column=0,columnspan=3,pady=10,sticky="ew")

name_label = Label(zahid,font = ('arial',25,'bold'),bg="#91f", text=" Name:")
name_entry = Entry(zahid,font = ('arial',30,'bold'),bg="#97f")
name_label.grid(row=1, column=1,pady=5)
name_entry.grid(row=1, column=2,pady=5)

no_label = Label(zahid,font = ('arial',25,'bold'),bg="#91f", text=" Number:")
no_entry = Entry(zahid,font = ('arial',30,'bold'),bg="#97f")
no_label.grid(row=2, column=1,pady=5)
no_entry.grid(row=2, column=2,pady=5)

clear_entry = Button(zahid,font = ('bausaus',20,'bold'),text = "Clear",fg = "black",width = 8,height = 1,bg = "#f22",
                    cursor = "hand2",command = lambda: clear_input())
clear_entry.grid(row = 3, column = 1)
save_data= Button(zahid,font = ('bausaus',20,'bold'),text = "Save",fg = "black",width = 19,height = 1,bg = "#2e2",
                    cursor = "hand2",command = lambda: save_input())
save_data.grid(row = 3, column = 2,pady=10)

#=======================================
# Update Contact
update_label = Label(zahid,font = ('arial',30,'bold'),fg="#eef",bg="#30f", text=" Update Contact ",relief="raised", bd=5)
update_label.grid(row=4, column=0,columnspan=3,pady=10,sticky="ew")

name_label = Label(zahid,font = ('arial',25,'bold'),bg="#91f", text=" Name:")
name_entry = Entry(zahid,font = ('arial',30,'bold'),bg="#97f")
name_label.grid(row=5, column=1,pady=5)
name_entry.grid(row=5, column=2,pady=5)

no_label = Label(zahid,font = ('arial',25,'bold'),bg="#91f", text=" Number:")
no_entry = Entry(zahid,font = ('arial',30,'bold'),bg="#97f")
no_label.grid(row=6, column=1,pady=5)
no_entry.grid(row=6, column=2,pady=5)

clear_entry = Button(zahid,font = ('bausaus',20,'bold'),text = "Clear",fg = "black",width = 8,height = 1,bg = "#f22",
                    cursor = "hand2",command = lambda: clear_input())
clear_entry.grid(row = 7, column = 1)
update_data= Button(zahid,font = ('bausaus',20,'bold'),text = "Update",fg = "black",width = 19,height = 1,bg = "#9f0",
                    cursor = "hand2",command = lambda: save_input())
update_data.grid(row = 7, column = 2,pady=10)

#======================================
#Delete Contact
delete_label = Label(zahid,font = ('arial',30,'bold'),fg="#eef",bg="#30f", text=" Update Contact ",relief="raised", bd=5)
delete_label.grid(row=8, column=0,columnspan=3,pady=10,sticky="ew")

no_label = Label(zahid,font = ('arial',25,'bold'),bg="#91f", text=" Number:")
no_entry = Entry(zahid,font = ('arial',30,'bold'),bg="#97f")
no_label.grid(row=9, column=1,pady=5)
no_entry.grid(row=9, column=2,pady=5)

clear_entry = Button(zahid,font = ('bausaus',20,'bold'),text = "Clear",fg = "black",width = 8,height = 1,bg = "#f22",
                    cursor = "hand2",command = lambda: clear_input())
clear_entry.grid(row = 10, column = 1)
delete_data= Button(zahid,font = ('bausaus',20,'bold'),text = "Delete",fg = "black",width = 19,height = 1,bg = "#f90",
                    cursor = "hand2",command = lambda: save_input())
delete_data.grid(row = 10, column = 2,pady=10)


#=============================================
_space= Label(zahid,width=3,bg="#91f")
_space.grid(row=0,column=4,rowspan=10)

#============================================
search_label = Label(zahid,font = ('arial',30,'bold'),fg="#eef",bg="#30f", text=" Search Contact ",relief="raised", bd=5)
search_label.grid(row=0, column=5,columnspan=3,pady=10,sticky="ew")

s_entry = Entry(zahid,font = ('arial',30,'bold'),bg="#97f")
s_btn = Button(zahid,font = ('arial',20,'bold'),bg="#19f", text=" Search ")
s_entry.grid(row=1, column=5,pady=5)
s_btn.grid(row=1, column=6,pady=5)

#===========================================
# scroll_bar = Scrollbar(zahid)
# scroll_bar.pack(side = RIGHT,fill = BOTH)



t=Listbox(zahid,font = ("Courier",30,'bold'),bg="#99f",height=10,relief="sunken",bd=10) 
t.grid(row=2,column=5,rowspan=10,columnspan=2,sticky="EWNS",)

# s=Scrollbar(t).pack(side=RIGHT,fill=BOTH)
# scroll_bar.config(command=t.yview)

# list_frame=Frame(zahid)
# list_frame.grid(row=0,column=5)
# t.config(yscrollcommand=s.set)
# s.config(command=t.yview)
# t=Listbox(list_frame)
for i in range(100):
    t.insert(END,i)

# t.pack(fill=Y)
# s=Scrollbar(list_frame)
# s.pack(side=RIGHT,fill=BOTH)


# t.config(yscrollcommand=Scrollbar.set)
# s.config(command=t.yview)


zahid.mainloop()

