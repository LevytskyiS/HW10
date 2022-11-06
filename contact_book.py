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
        self.phone = Phone(phone)
        self.list_of_obj_of_phone.append(self.phone)
        return f'The phone was added.'
        
    def change_phone(self, phone, new_phone):
        self.phone = phone
        self.new_phone = Phone(new_phone)
        for index, number in (enumerate(self.list_of_obj_of_phone)):
            if number.value == self.phone:
                self.list_of_obj_of_phone[index] = self.new_phone
                return f'The number was changed.'
            else:
                return f'The number {phone} doesn`t exist in your book.'

    def delete_phone(self, phone):
        self.phone = phone
        for number in self.list_of_obj_of_phone:
            if self.phone == number.value:
                self.list_of_obj_of_phone.remove(number)
                return f'The number was deleted successfully.'
            else:
                return f'The number {self.phone} cannot be deleted, cause it doesn`t exist.'
