from collections import UserDict


class AddressBook(UserDict):
    def search_by_name(self):
        pass

    def search_by_number(self):
        pass
    
    def show_all_contacts(self):
        pass


class Field:
    pass


class Name(Field):

    def __init__(self, value) -> None:
        self.value = value
        super().__init__()


class Phone(Field):
    
    phone = []
    email = []


class Record(AddressBook):

    name = ''
    phone = Phone.phone

    def __init__(self, name) -> None:
        self.name = name
        Record.name = self.name
            
    def add_new_contact(self):
        AddressBook().data[Record.name.value] = Record.phone
 
    def change_existing_number(self):
        pass

    def delete_contact(self):
        pass


ab = AddressBook()
contact_1 = Name('Mark')
record_1 = Record(contact_1)
phone_1 = Phone.phone.append(324)
phone_2 = Phone.phone.append(456)
record_1.add_new_contact()
print(Record.phone)

print(ab)
