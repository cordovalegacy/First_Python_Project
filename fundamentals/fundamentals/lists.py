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