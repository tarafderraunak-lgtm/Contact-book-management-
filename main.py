def display_menu():
    print("\n" + "="*25)
    print("   CONTACT BOOK MENU")
    print("="*25)
    print("1. Add/Update Contact")
    print("2. View All Contacts")
    print("3. Search for a Contact")
    print("4. Delete a Contact")
    print("5. Exit")

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    
    if name in contacts:
        update = input(f"'{name}' exists with number {contacts[name]}. Update it? (y/n): ").lower()
        if update != 'y':
            return
            
    contacts[name] = phone
    print(f"Contact '{name}' saved successfully!")

def view_contacts(contacts):
    if not contacts:
        print("\n[!] Your contact book is empty.")
    else:
        print(f"\n{'NAME':<15} | {'PHONE':<15}")
        print("-" * 33)
        for name, phone in contacts.items():
            print(f"{name:<15} | {phone:<15}")

def search_contact(contacts):
    search_term = input("Enter name to search: ").strip()
    # Basic partial match search
    results = {n: p for n, p in contacts.items() if search_term.lower() in n.lower()}
    
    if results:
        for name, phone in results.items():
            print(f"Found: {name} -> {phone}")
    else:
        print(f"No contacts matching '{search_term}' found.")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        confirm = input(f"Permanently delete '{name}'? (yes/no): ").strip().lower()
        if confirm == 'yes':
            del contacts[name]
            print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    # In a real app, you might load this from a JSON file
    contacts = {} 
    print("Welcome to your Contact Book!")
    
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()
