'''
元组是不可变的：元组所指向的内存中的内容不可变
'''

print('----------------函数-----------------')
tuplepppp = (1,2,3,4,5,6,7,8)
print(len(tuplepppp),max(tuplepppp),min(tuplepppp))

print(tuplepppp.index(2))

a = 1
b = 2
c = 3
d = 4
tup = (a,b,c)
print(id(tup),tup.index(b),id(tup.index(1)))
tup = (a,d,c)
print(id(tup),tup.index(d),id(tup.index(1)))
