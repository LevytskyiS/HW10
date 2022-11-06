from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def search_by_name(self, record):
        return f'{self.data[record.name.value]}'
    
    def show_all_contacts(self):
        return '\n'.join(f'{k} - {v.phone.value}' for k, v in self.data.items())


class Field:
    def __init__(self, value) -> None:
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:

    def __init__(self, name) -> None:
        self.name = Name(name)
        self.list_of_obj_of_phone = []
            
    def add_new_phone(self, phone):
        self.phone = Phone(phone)
        self.list_of_obj_of_phone.append(self.phone)

    def change_phone(self, phone, new_phone):
        print(len(self.list_of_obj_of_phone))
        if phone in self.list_of_obj_of_phone:
            phone = Phone(new_phone)
            return f'The number was changed successfuly.'
        else:
            return f'This number {phone} doesn`t belong to this contact.'

    def delete_phone(self, phone):
        for number in self.list_of_obj_of_phone:
            if phone == number.value:
                self.list_of_obj_of_phone.remove(number)
                return f'The number was deleted successfully.'
            else:
                print(f'The number {self.phone.value} cannot be deleted, cause it doesn`t exist.')
