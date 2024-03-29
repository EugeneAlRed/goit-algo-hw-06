from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        pattern = r'^\d{10}$'
        if not re.match(pattern, value):
            return "Invalid phone number format. The phone number must contain 10 digits"
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        self.phones = [num for num in self.phones if num.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for num in self.phones:
            if num.value == old_phone:
                num.value = new_phone

    def find_phone(self, phone):
        return [str(num) for num in self.phones if num.value == phone]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(num.value for num in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

# Після реалізації ваш код має виконуватися наступним чином:

# book = AddressBook()
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# book.add_record(john_record)
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)
# for name, record in book.data.items():
#     print(record)
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")
# print(john)
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")
# book.delete("Jane")