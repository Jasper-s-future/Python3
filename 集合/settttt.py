'''
合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式：
parame = {value01,value02,...}
或者
set(value)
'''
aaa = set()
bbb = {}
print(type(aaa),type(bbb))

ccc = {1,2,3}
print(ccc)
ccc.add(444)
print(ccc)
ccc.update('9','000')
print(ccc)
ccc.update({5,6,7})
print(ccc)

ccc.remove(5)
print(ccc)
# ccc.remove(999) #元素不存在会报错

ccc.discard(666)
print('discard 元素不存在也不会报错')

ccc.pop()#随机删除集合中的一个元素
print(ccc)

print('---------------------------------集合函数----------------------------------')
test1 = set()
test2 = {1,2,3,4,5,6}
test3 = {'1','2','3'}

test1.add(66666)
print('add ',test1)

test1.clear()
print('clear ',test1)

test4 = test2.copy()
print('copy ',test4,test2,id(test4),'\n',id(test2))

test0123 = test2.difference(test3)
print('diffrence ',test0123)

test5 = {1,2,3}
test2.difference_update(test5)
print('diffrence_update ',test2)

test3.discard('1')
print('discard()	',test3)

test666 = {1,2,3}
test777 = {2,3,4}
print('intersection() ',test666.intersection(test777))
test666.intersection_update(test777)
print('intersection_update',test666,test777)

test66 = {1,2,3}
test77 = {2,3,4}
print('isdisjoint 如果不包含相同元素返回True，else False',test66.isdisjoint(test77))

print('issubset ',{1,2,3}.issubset({1,2,3}))
print('issuperset ',{1,2,3}.issuperset({1,2,3}))

test66.pop()
print(test66)

test66.remove(2)
print(test66)

print('symmetric_diffrence ',{1,2,3}.symmetric_difference({2,3,4}))

print('symmetric_diffrence_update ',{1,2,3}.symmetric_difference({2,3,4}))

print('union ',{1,2,3}.union({2,3,4}))
test123 = {1,2,3}
test123.update('32')
print('update ',test123)