from contact_book import AddressBook, Record

def decor(func):
    def wrapper(arg):
        try:
            return func(arg)
        except IndexError:
            return 'There is no phone number. Enter name and phone.' # If user didn`t put the number, only name.
        except ValueError: 
            return 'Number must contain only numbers.' # If number contains letters
        except KeyError:
            return 'Wrong command. Try again.' # This command is not in the dictionary with commands. 

    return wrapper

@decor 
def greeting(*_):
    return 'How can I help you? '

@decor
def exit_func(*_):
    return 'Good bye!'

@decor
def contact_book(*_):
    return address_book.show_all_contacts()

@decor
def new_contact(list_name_number : list):
    record = Record(list_name_number[0].capitalize())
    record.add_new_phone(int(list_name_number[1]))
    address_book.add_record(record)
    return 'Contact was added to the Address Book sucessfuly.'

@decor
def change_contact(list_available_name_and_new_number: list):

    record = Record(list_available_name_and_new_number[0].capitalize())
    print(list_available_name_and_new_number)
    if record.name.value in address_book.keys():
        return record.change_phone(int(list_available_name_and_new_number[1]), int(list_available_name_and_new_number[2]))
    else:
        return 'Name not found.'

@decor 
def phone_number(name_in_book: list):
    record = Record(name_in_book[0].capitalize())
    if record.name.value in address_book.keys():
        return address_book.search_by_name(record)
    else:
        return 'This name is not found in your contacts.'

@decor
def delete_number(number_to_delete: list): 
    record = Record(number_to_delete[0].capitalize())
    if record.name.value in address_book.keys():
        return record.delete_phone(int(number_to_delete[1]))
    else: 
        return 'The contact doesn`t exist at all.'    


FUNCTIONS = {
    'hello' : greeting, 
    'add' : new_contact,
    'change' : change_contact,
    'phone' : phone_number,
    'show all' : contact_book,
    'deletenum' : delete_number, # Name + number are needed
    'good bye' : exit_func,
    'exit' : exit_func,
    'close' : exit_func,
}

all_contact = {'Anna' : 321} # Dict was added for testing

address_book = AddressBook()

@decor
def handle(inp_by_user : str):

    inp_by_user = inp_by_user.lower().split()
    if ' '.join(inp_by_user[0:2]) == 'show all' or ' '.join(inp_by_user[0:2]) == 'good bye':
        func = ' '.join(inp_by_user[0:2])
    else:
        func = inp_by_user[0]
    args = inp_by_user[1:]
    
    if len(inp_by_user) == 1:
        return FUNCTIONS[func](args)

    elif func == 'show all' or func == 'good bye':
        return FUNCTIONS[func](args)

    elif len(inp_by_user) == 2 or len(inp_by_user) > 2:
        return FUNCTIONS[func](args)

while True:
    
    user_input = input('Enter the command: ')
    user_handler = handle(user_input)
    
    if user_handler == 'Good bye!':
        print(user_handler)
        exit()
    elif user_handler:
        print(user_handler)
