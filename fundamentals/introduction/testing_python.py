# import random

# print('Welcome to Python!')

# print('This is a loop printing 5 times')
# for x in range(1, 6):
#     print(f'x is: {x}')

# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# day = random.choice(weekdays)

# print(f'Today is: {day}')

# if day == 'Monday':
#     print('It will be a long week!')
# elif(day == 'Friday'):
#     print('Woohoo, time for the weekend!')
# else:
#     print('Not quite there yet.')
# -------------------------------------------
# INTEGERS FLOAT INT COMPLEX
age = 35 # storing an int
weight = 160.57 # storing a float

# -------------------------------------------
# COMPOSITE TYPES:

# TUPLES = MIXED DATA TYPES(IMMUTABLE)
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
# dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)

# LISTS = ARRAY
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

# DICTIONARIES = OBJECT
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        

# -------------------------------------------
# COMMON FUNCTIONS

# TYPE = IDENTIFIER OF DATATYPES
print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>

# LEN = .LENGTH
print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11 
