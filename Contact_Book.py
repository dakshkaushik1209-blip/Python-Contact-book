import string
import json
from pathlib import Path
database="database.json"
data={"Contact":[]}

if Path(database).exists():
    with open(database,"r") as f:
        content=f.read()
        if content:
            data=json.loads(content)

def save():
    with open (database,"w") as f:
        json.dump(data,f,indent=4)

def Add():
    while True:
        name=input("Enter name (or \"exit\" to exit):- ").upper()
        if name=="":
            print("Name can't be empty")
            continue
        if name=="EXIT":
            break

        phone=input("Enter phone number (or \"0\" to exit):- ")
        duplicate=False
        for i in data["Contact"]:
            if phone == i["Phone"]:
                duplicate=True
                break
        if duplicate:
            print("Phone number already exists")
            continue
        if phone=="0":
            break
        elif not phone.isdigit():
            print("This Phone is invalid and contains only numbers ")
            continue

        if len(phone)!=10:
            print("length of Phone must be 10 digits")
            continue

        try:
            email=input("Enter email address (or \"exit\" to exit):- ")
        except Exception as ex:
            print("Please give a valid email ")
        if "@gmail.com" not in email:
            print("This email is not allowed")
            continue
        else:
            print("Contact successfully added")    
        if email.upper()=="EXIT":
            break
        
        
        data["Contact"].append({
        "Name":name,
        "Phone":phone,
        "Email":email})
        save()
        

def View():
    Number=1
    for i in data["Contact"]:
        print(f"{Number}.")
        print("Name = "+ i["Name"])
        print("Phone = "+ i["Phone"])
        print("Email = "+ i["Email"]+"\n")
        Number+=1
    if len(data["Contact"])==0:
        print("No contacts available")

def Search():
    name=input("Enter name:- \n").upper()
    found=False
    for i in data["Contact"]:  
        if name.upper() == i["Name"]:
            found=True
            print("Name = "+i["Name"])
            print("Phone = "+i["Phone"])
            print("Email = "+i["Email"]+"\n")
    
    if len(data["Contact"])==0:
        print("No contact available")
    elif not found:
        print("Not found")    

def Update():
    print("What you want to update:- ")
    print("Press 1  To update Name")
    print("Press 2  To update Phone")
    print("Press 3  To update Email")
    try:
        update_choice=int(input("Enter your Choice:- "))
    except Exception as ex:
        print("Please choose only from 1,2 or 3\n")
        return
    if update_choice == 1:
        name=input("Enter old name:- ").upper()
        name_found=False
        for i in data["Contact"]:
            if name == i["Name"]:
                name_found=True 
                New_name=input("Enter new name:- ").upper()
                i["Name"]=New_name
                print("Name Updated succesfully")
        if name_found==False:
            print("Name not found")
        

    elif update_choice == 2:
        phone=input("Enter old phone number:- ")
        Phone_found=False
        for i in data["Contact"]:
            if phone == i["Phone"]:
                Phone_found=True
                New_Phone=input("Enter new Phone number:- ")
                for i in data["Contact"]:
                    if New_Phone == i["Phone"]:
                        print("Phone number already exists\n")
                        return
                if not New_Phone.isdigit():
                    print("This Phone is invalid and contains only digits")
                    continue
                if len(New_Phone)!=10:
                    print("length of Phone must be 10 digits")
                    continue
                i["Phone"]=New_Phone
                print("Phone Update successfully")
        if Phone_found==False:
            print("Phone not found")

    elif update_choice == 3:
        email=input("Enter old email:- ")
        email_found=False
        for i in data["Contact"]:
            if email == i["Email"]:
                email_found=True
                New_Email=input("Enter new email address:- ")
                for i in data["Contact"]:
                    if New_Email == i["Email"]:
                        print("Email address already exists\n")
                        return
                if "@gmail.com" not in New_Email:
                    print("This email is not allowed")
                    continue
                i["Email"]=New_Email
                print("Email update succesfully")
        if email_found==False:
            print("Email not found")

    else:
        print("Invalid choice")

def Delete():
    name=input("Enter name:- ").upper()
    name_found=False
    for i in data["Contact"]:
        if name==i["Name"]:
            name_found=True
            data["Contact"].remove(i)
            print("Contact deleted successfully")
    if name_found == False:
        print("Contact not found")
    if len(data["Contact"])==0:
        print("Not contact available")

        
def Statistics():
    print("Total contacts = ",end="")
    print(len(data["Contact"]))


while True:
    print("Welocme to Contact Book")
    print("Add Contacts     Click 1")
    print("View Contacts    Click 2")
    print("Search Contact   Click 3")
    print("Update Contact   Click 4")
    print("Delete Contact   Click 5")
    print("Statistics       Clcik 6")
    print("Exit             Click 7")
    try:
        choice = int(input("Enter your Choice:- "))
    except Exception as ex:
        print("Please select only from 1,2,3,4,5,6 or 7\n")
        continue
    if choice == 1:
        Add()
    elif choice ==2:
        View()
    elif choice ==3:
        Search()
    elif choice ==4:
        Update()
        save()
    elif choice ==5:
        Delete()
        save()
    elif choice == 6:
        Statistics()
    elif choice==7:
        break
    else:
        print("Invalid choice")
