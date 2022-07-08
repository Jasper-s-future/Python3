'''
列表都可以进行的操作包括索引，切片，加，乘，检查成员。
'''

list1 = [1, 2, 3, 4, 5]
list2 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print('不同索引的value',list1[0],list1[-1],list1[-len(list1)],list1[0:2],list1[1:2])
print('list +',list1+list2)
list1[1] = 666
print('修改后的list',list1)
list1.remove(3)#remove(x) x必须在list内
print('修改后的list',list1)
del list1[1]
print('修改后的list',list1)
list1.append(2)
print('修改后的list',list1)

print(list2)
if 'red' in list2:
    print('获取元素index', list2.index('red'))
    list2.remove('red')
print(list2)

print('-----------list嵌套-------------')
c = [1,2,3,[4,5,6,[7,8,9]]]
print(c)

print('-----------list函数-------------')
tuple_xx = (1,2,3,1,1,1,1,1)
list_xxx = [1,2,3,4,5,2,2,1,6,9,0]
print(len(list_xxx),max(list_xxx),min(list_xxx),list(tuple_xx))

list_xxx.append(999)
print(list_xxx,list_xxx.count(999),list_xxx.count(666))
list_xxx.extend(list(tuple_xx))
print(list_xxx)
list_xxx.extend(tuple_xx)
print(list_xxx)

print(list_xxx.index(999))
list_xxx.insert(1,888)
list_xxx.insert(len(list_xxx),0.22)
print(list_xxx)

print(list_xxx.pop(),list_xxx.pop(8))

list_xxx.reverse()
print(list_xxx)

list_xxx.remove(999)
print(list_xxx)

list_xxx.sort()
print(list_xxx)

list_xxxyyy = list_xxx.copy()
print(list_xxxyyy)

list_xxx.clear()
print(list_xxx,list_xxxyyy)
