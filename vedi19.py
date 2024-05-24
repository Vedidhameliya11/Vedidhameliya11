# year = 2024

# if (year % 400 == 0) and (year % 100 == 0):
#     print("{0} is a leap year".format(year))
# elif (year % 4 == 0) and (year % 100 != 0):
#     print("{0} is a leap year".format(year))
# else:
#     print("{0} is not a leap year".format(year))

# class A:
#     def hello(self):
#         year = 2000
#         if (year % 400 == 0) and (year % 100 == 0):
#             print("{0} is a leap year".format(year))
#         elif (year % 4 == 0) and (year % 100 != 0):
#             print("{0} is a leap year".format(year))
#         else:
#             print("{0} is not a leap year".format(year))
    
# a1 = A()
# a1.hello()

# class B(A):
#     def hello2(self):
#         year = 1990
#         if (year % 400 == 0) and (year % 100 == 0):
#             print("{0} is a leap year".format(year))
#         elif (year % 4 == 0) and (year % 100 != 0):
#             print("{0} is a leap year".format(year))
#         else:
#             print("{0} is not a leap year".format(year))

# b1 = B()
# b1.hello2()

# class C(B,A):
#     def hello3(self):
#         year = 2016
#         if (year % 400 == 0) and (year % 100 == 0):
#             print("{0} is a leap year".format(year))
#         elif (year % 4 == 0) and (year % 100 != 0):
#             print("{0} is a leap year".format(year))
#         else:
#             print("{0} is not a leap year".format(year))

# c1 = C()
# c1.hello3()
# c1.hello()
# c1.hello2()

class V:
    def vedi(self):
        x = int(input("enter the answer:"))

        for i in range(2,x):
            if x % i == 0:
                print("prime number")
                break
            else:
                print("not a prime number")
                break
a1 = V()
a1.vedi()

class Z(V):
    def vedi1(self):
        x = int(input("enter the answer:"))
        for i in range(4,x):
            if x % i == 0:
                print("prime number")
                break
            else:
                print("not a prime number")
                break
b1 = Z()
b1.vedi1()


