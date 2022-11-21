# def multiply(num_list, num):
#     for x in num_list:
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# # output:
# # [2,4,10,16]


# def multiply(num_list, num):
#     a = [2,4,10,16]
#     b = multiply(a,5)
#     print(b)
# # output:
# # [2,4,10,16]

# def multiply(num_list, num):
#     print(num_list, num)
#     for x in num_list:
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# # output:
# # [2,4,10,16] 5
# # [2,4,10,16]

# def multiply(num_list,num):
#     print(num_list, num)
#     for x in num_list:
#         print(x)
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# # output:
# # [2, 4, 10, 16] 5
# # 2
# # 4
# # 10
# # 16
# # [2, 4, 10, 16]

def multiply(num_list, num):
    for i in range(len(num_list)):
        num_list[i] *= num
        print(i)
    return num_list
    print(i)
    print(num_list)
a = [2,4,10,16]
b = multiply(a,5)
print(b)