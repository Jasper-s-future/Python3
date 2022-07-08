print('-------------------算术运算符-----------------------')
a = 10
b = 21
print('+ ', a + b)
print('- ',a - b,b - a)
print('* ',a * b)
print('/ ',a / b,b / a)
print('% ',a % b,b % a)
print('** ',a ** 2)
print('// ',a // b,b // a)

print('-------------------比较运算符-----------------------')
a = 10
b = 20
print('== ',a == b)
print('!= ',a != b)
print('> ',a > b)
print('< ',a < b)
print('<= ',a <= b)
print('>= ',a >=b)

print('-------------------赋值运算符-----------------------')
c = a + b
print('= ',c)

c += 1
print('+= ',c)

c -= 1
print('-= ',c)

c *= 2
print('*= ',c,type(c))

c /= 2
print('/= ',c,type(c))   #得出的是一个float

c **= 2
print('**= ',c,type(c))

c //= 2
print('//= ',c,type(c))
d = 30
d //= 2
print('//= ',d,type(d))

print('-------------------位运算符-----------------------')
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b  # 12 = 0000 1100
print("1 - c 的值为：", c)

c = a | b  # 61 = 0011 1101
print("2 - c 的值为：", c)

c = a ^ b  # 49 = 0011 0001
print("3 - c 的值为：", c)

c = ~a  # -61 = 1100 0011
print("4 - c 的值为：", c)

c = a << 2  # 240 = 1111 0000
print("5 - c 的值为：", c)

c = a >> 2  # 15 = 0000 1111
print("6 - c 的值为：", c)

print('-------------------逻辑运算符-----------------------')
a = 10
b = 20
print('and ',a > 0 & b < 30)
print('or ',a > 10 or b < 30)
print('not() ',not(a == 10 and b == 20))

print('-------------------成员运算符-----------------------')
list_num = [10,21,33,33,55,5,5,5,54,16,165,16,1,6516,516,5165,1]
print('in ',a in list_num)
print('not in ',b not in list_num)

print('-------------------身份运算符-----------------------')
# 判断两个标识符是不是引用自[一个对象]
print('is',a is b)
print('is',id(a) is id(b))
print(type(a) is type(b))
a = 10
b = 10
print(a == b)

c = 10
a = c
b = c
print(a is b)
'''
is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
'''