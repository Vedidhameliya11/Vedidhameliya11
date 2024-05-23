# class A:
#     def vedi1(self):
#         print("rm")
#     def vedi2(self):
#         print("jin")
# a1 = A()
# a1.vedi1()
# a1.vedi2()

# class B(A):
#     def vedi3(self):
#         print("suga")
#     def vedi4(self):
#         print("jhope")
# b1 = B()
# b1.vedi1()
# b1.vedi2()
# b1.vedi3()
# b1.vedi4()

# class C:
#     def vedi5(self):
#         print("jimin")
#     def vedi6(self):
#         print("v")
#     def vedi7(self):
#         print("jungkook")
# c1 = C()

# c1.vedi5()
# c1.vedi6()
# c1.vedi7()

class A:
    def vedi(self):
        i = 1
        while i<9:
            print(i)
            i = i+1
    def v(self):
        i = 2
        while i<10:
            print(i)
            i = i+1
            if i == 8:
                break
a1 = A()
a1.vedi()
a1.v()

class B:
    def fun(self):
        i = 3
        while i<11:
            i = i+1
            if i == 10:
                continue
            print(i)
b1 = B()
# b1.vedi()
# b1.v()
b1.fun()

class C(A,B):
    def hello(self):
        i = 4
        while i<14:
            print(i)
            i = i+1
        else:
            print("hello")
c1 = C()
c1.vedi()
c1.v()
c1.fun()
c1.hello()
















  