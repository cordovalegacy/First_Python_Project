fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']

fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

salad = 3 * vegetables
print(salad)

drawers = ['documents', 'envelopes', 'pens']

print(drawers[0])
print(drawers[1])
print(drawers[2])
print(drawers)

drawers[0] = 'socks'
drawers[1] = 'shirts'
drawers[2] = 'pants'
print(drawers)

drawers[1] = drawers[0]
print(drawers)

drawers.pop()
print(drawers)

drawers.append('ties')
print(drawers)

fruits.append(vegetables)
print('Updated grocery list: ', fruits)

fruits.extend(vegetables)
print(fruits)

words = ["start","going","till","the","end"]

print(words[:1])
print(words[1:])

print(words[1:1])
print(words[1:2])
print(words[4:])
print(words[4:1])
print(words[2:4])

# # Sub-ranges (portions) of the list
# print(words[1:]) # prints ['going', 'till', 'the', 'end']
# print(words[:4]) # prints ['start', 'going', 'till', 'the']
# print(words[2:4]) # prints ['till', 'the']
    
# # Making a copy of a list
# copy_of_words = words[:]
# copy_of_words.append("dojo") # only appends to the copy
# print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
# print(words) # prints ['start', 'going', 'till', 'the', 'end']

my_list = [1, 'zen', 'hi']
print(len(my_list))
my_list.pop()
my_list.pop()
my_list.append(9)
my_list.append(2)
print(my_list)
print(max(my_list))
print(min(my_list))
print(sorted(my_list))
my_list.reverse()
print(my_list)
my_list.sort()
print(my_list)