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