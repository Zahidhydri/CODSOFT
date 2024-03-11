from tkinter import *
# from tkinter.scrolledtext import *
from tkinter import messagebox
import os
import pickle  

#==================================================
# Main
zahid=Tk()
zahid.title("Contact Manager")
zahid.configure(background='#91f',relief="ridge",bd=20)
# zahid.resizable(0,0)
zahid.attributes("-fullscreen",True)

#=============================================
#Exit
def exit_win():
    end = messagebox.askyesno("Exit","Are you sure you want to exit?")
    if end:
        zahid.destroy()


#============================================
#Function
#Clear
def clear_add():  # clear save entry column
        add_name_entry.delete(0,END)
        add_no_entry.delete(0,END)
def clear_update():  # clear save entry column
        up_name_entry.delete(0,END)
        up_no_entry.delete(0,END)
def clear_delete():  # clear save entry column
        del_entry.delete(0,END)
       
def clear_search():  # clear save entry column
        s_entry.delete(0,END)

#============================================  
# # Function to add a new contact
def add_contact():
    # global contacts
    check=False
    name = str(add_name_entry.get().strip())
    name=name.capitalize()
    phone = str(add_no_entry.get().strip())
    contacts = [name,phone]

    def add_data():
        with open("contacts.dat","ab") as file: 
                pickle.dump(contacts,file)
        #add_data()  # Use this to create file before reading

    with open("contacts.dat","rb") as file:
        while True:
            try:
                con_data=pickle.load(file)
                if name in con_data:
                        check=True
                else:
                        check=False
            except EOFError:
                    break

    if check:
        add_name_entry.delete(0,END)
        add_no_entry.delete(0,END)

        def change_text():
                conf_text="Prompt"
                prompt_label.config(text=conf_text)
        def change_text_up():
                conf_text=" Contact Exist !"
                prompt_label.config(text=conf_text)
                prompt_label.after(3000,change_text)
        change_text_up()
    else:
        add_data()
        add_name_entry.delete(0,END)
        add_no_entry.delete(0,END)
        def change_text():
                conf_text="Prompt"
                prompt_label.config(text=conf_text,fg="white")
        def change_text_save():
                load_data()
                conf_text=" Contact Saved !"
                prompt_label.config(text=conf_text)
                prompt_label.after(3000,change_text)
        change_text_save()

#==============================================================
def update_contact():
    check=False
    with open("contacts.dat","rb") as file:
        temp_data=[]
        up_name=str(up_name_entry.get())
        up_name=up_name.strip()
        up_name=up_name.capitalize()
        up_no=str(up_no_entry.get())
        up_no=up_no.strip()
        while True:
            try:
                my_data=pickle.load(file)
                temp_data.append(my_data)
            except EOFError:
                    break
    for i in temp_data:
        if i[0]==up_name:
            i[1]=up_no
            check=True
            break
        else:
            check=False
                
    with open("contacts.dat","wb") as file:
        for i in temp_data:
            pickle.dump(i,file)

    if check:
        up_name_entry.delete(0,END)
        up_no_entry.delete(0,END)
        def change_text():
            confirm_text="Prompt"
            prompt_label.config(text=confirm_text,fg="white")
        def change_text_up():
            load_data()
            confirm_text=" Contact Updated !"
            prompt_label.config(text=confirm_text)
            prompt_label.after(3000,change_text)
        change_text_up()
    else:
        up_name_entry.delete(0,END)
        up_no_entry.delete(0,END)

        def change_text():
            confirm_text="Prompt"
            prompt_label.config(text=confirm_text)
        def change_text_up():
            confirm_text=" Contact not Found !"
            prompt_label.config(text=confirm_text)
            prompt_label.after(3000,change_text)
        change_text_up()
            
#====================================================
def delete_contact():
    check=False
    with open("contacts.dat","rb") as file:
        del_no=str(del_entry.get())
        del_no=del_no.strip()
        del_no=del_no.capitalize()
        temp_data=[]
        while True:
            try:
                con_data=pickle.load(file)
                temp_data.append(con_data)
            except EOFError:
                    break
    with open("contacts.dat","wb") as file:
        for i in temp_data:
            if i[0]==del_no or i[1]==del_no:
                check=True
                continue
            pickle.dump(i,file)
                    
    if check:
        del_entry.delete(0,END)

        def change_text():
                confirm_text="Prompt"
                prompt_label.config(text=confirm_text,fg="white")
        def change_text_up():
                load_data()
                confirm_text=" Contact Deleted !"
                prompt_label.config(text=confirm_text,fg="#f11")
                prompt_label.after(3000,change_text)
        change_text_up()
    else:
        del_entry.delete(0,END)

        def change_text():
                confirm_text="Prompt"
                prompt_label.config(text=confirm_text)
        def change_text_up():
                confirm_text=" Contact not Found !"
                prompt_label.config(text=confirm_text)
                prompt_label.after(3000,change_text)
        change_text_up()
    
                         
#========================================================
def load_data():
    mylist.delete(0,END)
    with open("contacts.dat","rb") as file:
        try:
            while True:
                my_data=pickle.load(file)
                data_1=str(my_data[0]) + " "*20
                data_1=data_1[0:15]
                data_2=str(my_data[1]) + " "*10
                data_2=data_2[0:10]
                phone_list=data_1 + " : " + data_2 
                list_len=Listbox.size(mylist) # count line 
                list_len=str(list_len+1) + ".    "
                list_len=list_len[0:4]

                mylist.insert(END," "+list_len + phone_list) 
                            
        except EOFError:
            file.close()

    # with open("contacts.dat","rb") as file:
    #     mydata=pickle.load(file)
    #     for i in mydata:
    #         mylist.insert(END,i)
#====================================================
def search_data():
    mylist.delete(0,END)
    search=s_entry.get().strip().lower()
    with open("contacts.dat","rb") as f:
        try:
            while True:
                data=pickle.load(f)

                list_len=Listbox.size(mylist) # count line 
                list_len=str(list_len+1) + ".    "
                list_len=list_len[0:4]

                for i in data:
                    if search in str(i).lower():
                        # if str(j).lower()==search or str(j).lower()==search:
                        mylist.insert(END," "+list_len+(str(data[0])+" "*20)[0:15]+ " : "+(str(data[1])+" "*10)[0:10] )       
                     
        except EOFError:
            f.close()


#=========================================
label=Label(zahid,font = ('arial',30,'bold'),fg="#eef",bg="#30f", text="Zahid .S. Hydri ",relief="raised", bd=5)
label.grid(row=0, column=0,columnspan=7,pady=5,sticky="ew")
exit = Button(zahid,font = ('bausaus',20,'bold'),text = "Exit",fg = "black",width = 8,height = 1,bg = "#f00",
                    cursor = "hand2",command = lambda: exit_win())
exit.grid(row = 0, column = 1)
#======================================
# Add Contact

add_label = Label(zahid,font = ('arial',30,'bold'),fg="#eef",bg="#30f", text=" Add Contact ",relief="raised", bd=5)
add_label.grid(row=1, column=0,columnspan=3,pady=5,sticky="ew")

name_label = Label(zahid,font = ('arial',25,'bold'),bg="#91f", text=" Name:")
add_name_entry = Entry(zahid,font = ('arial',30,'bold'),bg="#97f")
name_label.grid(row=2, column=1,pady=3)
add_name_entry.grid(row=2, column=2,pady=3)

no_label = Label(zahid,font = ('arial',25,'bold'),bg="#91f", text=" Number:")
add_no_entry = Entry(zahid,font = ('arial',30,'bold'),bg="#97f")
no_label.grid(row=3, column=1,pady=3)
add_no_entry.grid(row=3, column=2,pady=3)



clear_entry = Button(zahid,font = ('bausaus',20,'bold'),text = "Clear",fg = "black",width = 8,height = 1,bg = "#f55",
                    cursor = "hand2",command = lambda: clear_add())
clear_entry.grid(row = 4, column = 1)
save_data= Button(zahid,font = ('bausaus',20,'bold'),text = "Save",fg = "black",width = 19,height = 1,bg = "#2e2",
                    cursor = "hand2",command = lambda: add_contact())
save_data.grid(row = 4, column = 2,pady=3)

#=======================================
# Update Contact
update_label = Label(zahid,font = ('arial',30,'bold'),fg="#eef",bg="#30f", text=" Update Contact ",relief="raised", bd=5)
update_label.grid(row=5, column=0,columnspan=3,pady=5,sticky="ew")

name_label = Label(zahid,font = ('arial',25,'bold'),bg="#91f", text=" Name:")
up_name_entry = Entry(zahid,font = ('arial',30,'bold'),bg="#97f")
name_label.grid(row=6, column=1,pady=3)
up_name_entry.grid(row=6, column=2,pady=3)

no_label = Label(zahid,font = ('arial',25,'bold'),bg="#91f", text=" Number:")
up_no_entry = Entry(zahid,font = ('arial',30,'bold'),bg="#97f")
no_label.grid(row=7, column=1,pady=3)
up_no_entry.grid(row=7, column=2,pady=3)

clear_entry = Button(zahid,font = ('bausaus',20,'bold'),text = "Clear",fg = "black",width = 8,height = 1,bg = "#f55",
                    cursor = "hand2",command = lambda: clear_update())
clear_entry.grid(row = 8, column = 1)
update_data= Button(zahid,font = ('bausaus',20,'bold'),text = "Update",fg = "black",width = 19,height = 1,bg = "#9f0",
                    cursor = "hand2",command = lambda: update_contact ())
update_data.grid(row = 8, column = 2,pady=5)

#======================================
#Delete Contact
delete_label = Label(zahid,font = ('arial',30,'bold'),fg="#eef",bg="#30f", text=" Delete Contact ",relief="raised", bd=5)
delete_label.grid(row=9, column=0,columnspan=3,pady=5,sticky="ew")

no_label = Label(zahid,font = ('arial',25,'bold'),bg="#91f", text=" Delete:")
del_entry = Entry(zahid,font = ('arial',30,'bold'),bg="#97f")
no_label.grid(row=10, column=1,pady=3)
del_entry.grid(row=10, column=2,pady=3)

clear_entry = Button(zahid,font = ('bausaus',20,'bold'),text = "Clear",fg = "black",width = 8,height = 1,bg = "#f55",
                    cursor = "hand2",command = lambda: clear_delete())
clear_entry.grid(row = 11, column = 1)
delete_data= Button(zahid,font = ('bausaus',20,'bold'),text = "Delete",fg = "black",width = 19,height = 1,bg = "#f90",
                    cursor = "hand2",command = lambda: delete_contact())
delete_data.grid(row = 11, column = 2,pady=5)

#======================================================
prompt_label = Label(zahid,font = ('arial',30,'bold'),fg="#eef",bg="#91f", text=" Prompt ")
prompt_label.grid(row=12, column=0,columnspan=3,pady=5,sticky="ew")

#=============================================
_space= Label(zahid,width=5,bg="#91f")
_space.grid(row=1,column=4,rowspan=10)

#============================================
search_label = Label(zahid,font = ('arial',30,'bold'),fg="#eef",bg="#30f", text=" Search Contact ",relief="raised", bd=5)
search_label.grid(row=1, column=5,columnspan=3,pady=5,sticky="ew")

s_entry = Entry(zahid,font = ('arial',30,'bold'),bg="#97f")
s_btn = Button(zahid,font = ('arial',20,'bold'),bg="#19f", text=" Search ",cursor = "hand2",command = lambda: search_data())
s_entry.grid(row=2, column=5,pady=3)
s_btn.grid(row=2, column=6,pady=3)

#===========================================
# scroll_bar = Scrollbar(zahid)
# scroll_bar.pack(side = RIGHT,fill = BOTH)



mylist=Listbox(zahid,font = ("Courier",30,'bold'),bg="#99f",relief="sunken",bd=10,width=35) 
mylist.grid(row=3,column=5,rowspan=9,columnspan=2,sticky="EWNS",)

load_data()

clear_s = Button(zahid,font = ('bausaus',20,'bold'),text = "Clear",fg = "black",width = 7,height = 1,bg = "#f22",
                    cursor = "hand2",command = lambda: clear_search())
clear_s.grid(row = 12, column = 6)
all_data= Button(zahid,font = ('bausaus',20,'bold'),text = "Reload",fg = "black",width = 19,height = 1,bg = "#0f0",
                    cursor = "hand2",command = lambda: load_data())
all_data.grid(row = 12, column = 5,pady=3)

#=========================================

zahid.mainloop()

