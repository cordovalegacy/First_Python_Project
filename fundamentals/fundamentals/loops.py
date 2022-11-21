# range(5, 10, 2) -- start, stop, iterator(step)
# output: 5, 7, 9 -- iterates by 2 inside the range of 5-10

# PRACTICE
# for i in range(10, 30, 3):
#     print(i)

# for i in range(10, 30, 3):
#     print(i*2)

# for i in range(0, 50, 5):
#     print(i-1)

# for i in range(25, 50, 1):
#     print(i+2)

# for i in range(50, 25, -10):
#     print(i)

# for i in range(5, -25, -5):
#     print(i)

# for i in range(5):
#     print(i)

# -------------------------------------
# LOOPING OVER LISTS & STRINGS

# STRINGS:
for i in 'Hello':
    print(i)

for i in 'Hello World my name is Brendan':
    print(i)
# LISTS:
my_list = ['abc', 123, 'xyz']
for i in range(0, len(my_list)):
    print(i, my_list[i])

for v in my_list:
    print(v)

# WHILE LOOPS

for count in range(0, 5):
    print("looping =", count)

    # IS THE SAME AS

count = 0
while count < 5:
    print('looping =', count)
    count += 1

    y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

    # BREAK

    for val in "string":
        if val == "i":
            break
        print(val)
# output: s, t, r

    # CONTINUE

for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i





# Loop Control
# We were introduced to control flow in the previous tabs with if and else statements. Loops, breaks, and continues are all a part of control flow as well. Control flow is the cornerstone of most programming languages.

# When you want finer control over your loops, use the following statements to do so.

# Break
# The break statement exits the current loop prematurely, resuming execution at the first post-loop statement. The break statement can be used in both while and for loops.

# The most common use for the break is when some external condition is triggered, requiring a hasty exit from a loop.

# When loops are nested, a break will only exit from the innermost loop.