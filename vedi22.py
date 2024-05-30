# scope

# def vedi():
#     j = 7
#     def jk():
#         print(j)
#     jk()
# vedi()

# def world():
#     v = 77
#     def earth():
#         print(v)
#     earth()
# world()

# global scope

# x = 10
# y = 20
# def hello():
#     print(x)
# hello()
# print(y)

# x = 5
# def hello():
#     y = 7
#     print(y)
# hello()
# print(x)

# global keyword

# def hello():
#     global x
#     x = 7
# hello()
# print(x)

# def vedi():
#     global v
#     v = 9
# vedi()
# print(v)

# nonlocal keyword

# def hello():
#     x = "vedi"
#     def jk():
#         nonlocal x
#         x = "jimin"
#     jk()
#     return x
# print(hello())

# def lisa():
#     x = "jisoo"
#     def jennie():
#         nonlocal x
#         x = "rose"
#     jennie()
#     return x
# print(lisa())

# python in math

# x = [1,2,3,4,5,6,7]
# y = ["lisa","jennie","jisoo","rose"]

# print(x)
# print(y)

# abs use in math

# x = abs(-7.777)
# print(x)

# pow using in math

# x = pow(7,2)
# print(x)

# y = pow(6,3)
# print(y)

# userdefine

import math

x = math.pi
print(x)