class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []
# Add the contact
    def add(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added.")
# View the contact
    def view(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name} - {contact.phone}")
# Search the contact
    def search(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not results:
            print("No contacts found.")
            return
        for contact in results:
            print(contact)
# update contact
    def update(self, name, new_contact):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.name = new_contact.name
                contact.phone = new_contact.phone
                contact.email = new_contact.email
                contact.address = new_contact.address
                print(f"Contact {name} updated.")
                return
        print(f"Contact {name} not found.")
#Delete the contact
    def delete(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {name} deleted.")
                return
        print(f"Contact {name} not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add(contact)
        
        elif choice == "2":
            contact_book.view()

        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_book.search(search_term)

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            new_contact = Contact(new_name, new_phone, new_email, new_address)
            contact_book.update(name, new_contact)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete(name)
# Terminte the CODE
        elif choice == "6":
            print("Exiting the Contact Book.")
            break

        else:
            print("Invalid nummber")
        lclose = input("Do you want to continue : (y/n):")
        if (lclose == 'n'):
            break

if __name__ == "__main__":
    main()