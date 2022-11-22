person1 = {"first_name": "Ada", "last_name": "Lovelace",
           "age": 42, "is_organ_donor": True}

# person2 = {"first_name": "Brendan", "last_name": "Cordova", "age": 27, "isProgrammer": "true"}
# can be written like this
person2 = {
    "first_name": "Brendan",
    "last_name": "Cordova",
    "age": 27, "isProgrammer":
    "true"
}

person1["first_name"] = "Alexa"
if "email" not in person1:
    person1["email"] = "alexalovelace@gmail.com"
else:
    print("Would you like to replace your existing email?")

if "email" not in person2:
    person2["email"] = "cordovalegacy19@gmail.com"
else:
    print("Would you like to update your existing email address?")


value_removed = person1.pop('is_organ_donor')
print(value_removed)


capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
capitals["usa"] = "Washington D.C."
capitals["aus"] = "Canberra"

print(person1)
print(person2)
print(capitals)
print(person1["age"])
print(person2["last_name"])

# PRINT OUT KEYS
for key in person2.keys():
    print(key)
# PRINT OUT VALUES
for value in person2.values():
    print(value)

for key, value in person1.items():
    print(key, "=", value)

my_dict = {"name": "Noelle", "language": "Python"}
for each_key in my_dict:
    print(each_key)
# output: name, language

my_dict = {"name": "Noelle", "language": "Python"}
for each_key in my_dict:
    print(my_dict[each_key])
# output: Noelle, Python

capitals = {
    "Washington": "Olympia",
    "California": "Sacramento",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Texas": "Austin",
    "Oklahoma": "Oklahoma City",
    "Virginia": "Richmond"
}
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc


people = [
    {
        "first_name": "Ada",
        "last_name": "Lovelace",
        "age": 42,
        "is_organ_donor": True
    },
    {
        "first_name": "Brendan",
        "last_name": "Cordova",
        "age": 27, "isProgrammer":
        "true"
    }
]

print(people[0]['last_name'], people[1]['last_name'])
print(people[0], people[1])
print(capitals["Idaho"][1])
print(people[1]["first_name"])
