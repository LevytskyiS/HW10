from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record
        return f'New contact was added successfuly.'

    def search_by_name(self, record):
        if len(record.list_of_obj_of_phone) >= 1:
            return [num.value for num in record.list_of_obj_of_phone]
        else: 
            return f'This guy doesn`t have a number.'
    
    def show_all_contacts(self):
        res = []
        for key, value in self.data.items():
            res.append(key)
            res.append([num.value for num in value.list_of_obj_of_phone])
        return res

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
        self.list_of_obj_of_phone.append(Phone(phone))
        return f'The phone was added.'
        
    def change_phone(self, phone, new_phone):
        for values in self.list_of_obj_of_phone:
            if values.value == phone:
                values.value = new_phone
                return f'The number was changed.'
            else:
                return f'The number {phone} isn`t in your book.'

    def delete_phone(self, number):
        for values in self.list_of_obj_of_phone:
            if values.value == number:
                self.list_of_obj_of_phone.remove(values)
                return f'The number was deleted successfully.'
            else:
                return f'The number {number} isn`t in your book.'
