from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def search_by_name(self):
        pass

    def search_by_number(self):
        pass
    
    def show_all_contacts(self):
        pass


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

        self.new_phone = Phone(new_phone)
        for index, number in enumerate(self.list_of_obj_of_phone):
            if number.value == self.phone.value:
                self.list_of_obj_of_phone[index] = self.new_phone
            else:
                print(f'The phone {self.phone.value} doesn`t exist')

    def delete_phone(self, phone):
        self.phone = phone  # Ця строка замість self.phone = Phone(phone). Якщо взагалі прибрати, то і пошук не проходить
        for number in self.list_of_obj_of_phone:
            if self.phone == number.value:
                self.list_of_obj_of_phone.remove(number)
            else:
                print(f'The number {self.phone.value} cannot be deleted, cause it doesn`t exist.')

ab = AddressBook()

user = Record('Mark')
user.add_new_phone(456)
user.change_phone(456, 222)
user.delete_phone(222)

ab.add_record(user)
for key, value in ab.data.items():
    print(key, value.phone) #Mark 222
