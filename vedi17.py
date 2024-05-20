# v = [1,2,3,4,5,6,7]
# jk = iter(v)

# print(next(jk))

# def hello():
#     yield 7
#     yield 7
#     yield 7
# value = hello()
# print(value.__next__())
# print(value.__next__())
# print(value.__next__())

# x = [1,2,3,4,5]
# hello = iter(x)

# print(next(hello))
# print(next(hello))
# print(next(hello))

# def vedi():
#     yield 3
# value = vedi()
# print(value.__next__())

# def vedi(h1,h2):
#     result = h1*h2
    
#     yield result
# v = vedi(4,5)

# print(v.__next__())

# def vedi():
#     for i in range(2,10):
#         yield 7
#         yield 7
# v = vedi()
# print(v.__next__())
# print(v.__next__())

# def vedi():
#     i = 2
#     while i<10:
#        yield i
#        i = i+2
# v = vedi()
# print(v.__next__())
# print(v.__next__())
# print(v.__next__())
# print(v.__next__())
# print(v.__next__())
# print(v.__next__())
# print(v.__next__())
# print(v.__next__())

# def vedi():
#     x = (f"my age is {17}")
#     yield x
# v = vedi()
# print(v.__next__())

class vedi:
    def __init__(hello,h1,h2):
        hello.h1 = h1
        hello.h2 = h2
        jk = hello.h2
        jk = hello.h1
        yield jk
data = vedi(50,60)
print(data.h1)
print(data.h2)
print(vedi.__next__())


