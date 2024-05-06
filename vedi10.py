#python in lambda function

# def myfun(x):
#     return x*5
# print(myfun(7))

# def blkpnk(j):
#     return j+10
# print(blkpnk(7))

# hello = lambda v:v-16
# print(hello(32))

# cat = lambda j:j/8
# print(cat(64))

# dog = lambda x,y:(x+y)*7
# print(dog(2,2))

# def myfun(v):
#     return lambda j:j*v
# blkpnk = myfun(7)
# print(blkpnk(3))

# def hello(x):
#     return lambda z:z+x
# myorder = hello(4)
# myorder7 = hello(6)

# print(myorder(8))
# print(myorder7(10))

#function to add perameter

def myfun(v1,v2):
    sum = v1+v2
    print("sum:",sum)
myfun(5,7)

#the return statement

def find(num,demo):
    result = num-demo
    return result
v = find(2,4)
print(v)

#perameter pass function 

def myfun(food):
    for v in food:
        print(v)

f = ["apple","mango"]
myfun(f)