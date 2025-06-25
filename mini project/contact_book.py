# This mini project is based on the knowlegede till day 04

contacts = []
email_set = set()

while True:
    
    print("\nMenu:")
    print("1. Create contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
    
    option = input("Enter your choice: ").strip()
    
    if option == "1":
        name = input("Enter name: ").strip().title()
        email = input("Enter email: ").strip().lower()
        
        if email.find("@") == -1:
            print("Invalid email id !!!!")
            continue
        
        if email in email_set:
            print("Email already exists !!!")
            continue
        
        contact = (name, email)  
        contacts.append(contact)  
        email_set.add(email)  
        print(f"Contact added: {name} ({email})")
    
    elif option == "2":
        if not contacts:
            print("No contacts found.")
        else:
            print("\nAll Contacts:")
            for index, (name, email) in enumerate(contacts, 1):
                print(f"{index}. {name} - {email}")
    
    elif option == "3":
        s_name = input("Enter name to search: ").strip().title()
        found = False
        for name, email in contacts:
            if name == s_name:
                print(f"Found: {name} - {email}")
                found = True
                break
        if not found:
            print(f"No contact found with name: {s_name}")
    
    elif option == "4":
        d_name = input("Enter name to delete: ").strip().title()
        found = False
        for contact in contacts[:]:
            name, email = contact
            if name == d_name:
                contacts.remove(contact)
                email_set.remove(email)
                print(f"Deleted: {name} - {email}")
                found = True
                break
        if not found:
            print(f"No contact found with name: {d_name}")
    
    elif option == "5":
        break
    
    else:
        print("Invalid choice. Please enter (1-5).")