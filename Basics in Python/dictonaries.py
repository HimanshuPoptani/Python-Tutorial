# Dictionaries

# Giving a key value and calling
my_stuff = {'key1': "123", "key2": "Value of key2"}
print(my_stuff['key1'])
print(my_stuff['key2'])

# Something nexted
my_stuff2 = {'key1': "123", "key2": "Value of key2", 'key3': {'key4': [1, 3, 2]}}
print(my_stuff2['key3'])
print(my_stuff2['key3']['key4'])  # This will print the nexted dictionary in the mystuff_2

# Printing entire Dictionaries
print(my_stuff, '= Dictionary 1')
print(my_stuff2, '= Dictionary 2')  # Note in the output is not same in the dictionary as they are different from lists

#  SMALL EXERCISE
my_stuff3 = {'key1': "123", "key2": "Value of key2", 'key3': {'key4': [1, 3, 2, 'grab me']}}
print(my_stuff3['key3']['key4'][3])  # This is just an example for something complicated
print(my_stuff3['key3']['key4'][3].upper())  # Same result but in upper case
print(my_stuff3['key3']['key4'][3].capitalize())  # Same result but in capitalize form

# Redefining a the value

food = {'lunch': 'pizza', 'breakfast': 'eggs'}  # Main dictionary for down CODE

food['lunch'] = 'burger'
print(food['lunch'])  # re assaigned value for 'lunch'
print(food)  # Value is changed here

food['dinner'] = 'Pasta'
print(food)  # New value added here
