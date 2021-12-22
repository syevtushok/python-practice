from enum import Enum

name = "Flavio"
print(name)
age = 10
# this is comment
name = "string"  # String type
print(type(name))
num = 1  # int
fraction = 0.1  # float

print(True and False)
print(True or False)
print(not False)
print(4 ^ 2)

print(4 is 4)
print(4 is 5)


def is_adult(age):
    if age > 18:
        return True
    else:
        return False


def is_adult_ter(age):
    return age > 18


print("""
this 
is 
interesting""")

print("ss".isalpha())
print(len("sss"))
print("as" in "atas")
print(name[1])
print(name[0:3])

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])
print(read_any_book)
read_all_book = all([book_1_read, book_2_read])
print(read_all_book)

complexNumber = 2 + 3j
print(complexNumber.real)
print(5 // 2)
print(5 ** 2)


class Constants(Enum):
    WIDTH = 1024
    HEIGHT = 256
