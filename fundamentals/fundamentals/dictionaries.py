person1 = {"first_name": "Ada", "last_name": "Lovelace","age": 42, "is_organ_donor": True}

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
