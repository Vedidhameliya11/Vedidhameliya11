# class sagar:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         print(x)
#         print(y)

#     def G(self):
#         print("HELLO DEMO")

# class Tg:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def G(self):
#         print("HELLO WORLD")

# class tgmec(sagar,Tg):
#     def __init__(self,c,d):
#         self.c = c
#         self.d = d

#     def G(self):
#         print("HELLO SAGAR")

# sagar1 = sagar("hello", "brother")
# tg1 = Tg("asdf","demo")
# tgmec1 = tgmec("tg", "123456")

# for n in (sagar1, tg1 , tgmec1):
#     n.G()      

# class vedi:
#     def __init__(self,j,v):
#         self.j = j
#         self.v = v
#         print(j,v)

#     def V(self):
#         print("EARTH INDIA")

# class rm:
#     def __init__(self,e,s):
#         self.e = e
#         self.s = s
#         print(e,s)

#     def V(self):
#         print("BLACKPINK")

# class jimin:
#     def __init__(self,a,z):
#         self.a = a
#         self.z = z
#         print(a,z)

#     def V(self):
#         print("BTS")

# jk = vedi("hello","world")
# suga = rm("lotus","rose")
# jin = jimin("light","hot")

# for n in (jk,suga,jin):
#    n.V()

# class vedi:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def V(self):
#         i = 1
#         while i<10:
#             print(i)
#             i = i+1
#             if i == 8:
#                 break

# class jk:
#     def __init__(self,c,d):
#         self.c = c
#         self.d = d

#     def V(self):
#         i = 2
#         while i<12:
#             i = i+1
#             if i == 9:
#                 continue
#             print(i)

# world = vedi("hello","world")
# self = jk("welcome","home")

# for n in (world,self):
#     n.V()

# class vedi:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def G(self):
#         a = [1,2,3,4,5,6,7,8,9]

#         for b in a:
#             print(b)
#             if b == 8:
#                 break

# class jk:
#     def __init__(self,c,d):
#         self.c = c
#         self.d = d

#     def G(self):
#         s = ["tiger","lion","blackpenther","fox","wolf"]

#         for j in s:
#             if j == "fox":
#                 continue
#             print(j)

# seven = vedi("hello","demo")
# one = jk("EARTH","world")

# for n in (seven,one):
#     n.G()

# class vedi:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def H(self):
#         x = int(input("enter the value:"))
#         for i in range(2,x):
#             if x%i == 0:
#                 print("prime number")
#                 break
#             else:
#                 print("not prime number")
#                 break

# class rm:
#     def __init__(self,c,d):
#         self.c = c
#         self.d = d

#     def H(self):
#         x = int(input("enter the value:"))
#         for i in range(6,x):
#             if x%i == 0:
#                 print("prime number")
#                 break
#             else:
#                 print("not prime number")
#                 break

# world = vedi("hello","sister")
# earth = rm("welcome","home")

# for n in (world,earth):
#     n.H()

class vedi:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def V(self):
        x = int(input("enter the value:"))
        for i in range(2,x):
            if x%i == 0:
                print("prime number")
                break
            else:
                print("not prime number")
                break
 

class jk:
    def __init__(self,c,d):
        self.c = c
        self.d = d

    def V(self):
        i = 2
        while i<13:
            print(i)
            i = i+2

class rm:
    def __init__(self,e,f):
        self.e = e
        self.f = f

    def V(self):
        i = 1
        while i<14:
            print(i)
            i = i+2
    
           

world = vedi("hello","sister")
earth = jk("welcome","home")
water = rm("lion","king")

for n in (world,earth,water):
    n.V()