# - variable declaration
# - Numbers
num1 = 42
num2 = 2.3
# - Boolean
boolean = True
# - Strings
string = 'Hello World'
# - Lists
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# - Tuples
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}
# - Dictionary
fruit = ('blueberry', 'strawberry', 'banana')

# - log statement
# - type check
print(type(fruit))
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])

# - conditional
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

# - length check
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# - for loop
for x in range(5):
    print(x)
for x in range(2, 5):
    print(x)
for x in range(2, 10, 3):
    print(x)
x = 0

# - while loop
while (x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

# - function


def print_hello_ten_times():
    for num in range(10):
        print('Hello')


print_hello_ten_times()

# - function


def print_hello_x_times(x):
    for num in range(x):
        print('Hello')


print_hello_x_times(4)

# - function


def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print('Hello')


print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


'''- comment
# - single line
- multiline'''

"""
Bonus section
"""


num3 = 72
print(num3)

fruit[0] = 'cranberry'
fruit.append('raspberry')
fruit.pop(1)
print(fruit)

print(person['favorite_team'])
print(pizza_toppings[7])
print(boolean)
