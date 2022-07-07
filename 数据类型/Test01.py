counter = 100
miles = 1.002
xxx = "0.2"
print(counter,miles,xxx)
print(counter.__class__)
print(type(counter))
if xxx == miles:
    print("hhh")
else:
    print(1)

'''
标准数据类型
不可变    Number  String  Tuple
可变      List    Dictionary  Set
'''

'''
isinstance 和 type 的区别在于：
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''
a,b,c,d,e = 20,3.222,True,'4+ssss',3+4j
print(type(a),type(b),type(c),type(d),type(e))
if isinstance(a,int):
    print(True)

a = 3 + 56
b = 5 - 2
c = 3 * 7
d = 2 / 4
e = 2 // 4
f = 16 % 3
g = 2 ** 5

t = 5 // 2
print(a,b,c,d,e,f,g,t)

'String'

print('------字符串截取-----')
'变量[start:end]'

name = '我是一个字符串'
subName = name[2:5]
print('name=',name,'subName=',subName)

print('------字符串拼接-----')
print(name+' 截取 '+subName)

subName = subName[0:2]
print(subName)

print('------字符串反斜杠-----')
print('12345\6789')
print('12345\6789')

print('------字符串索引-----')
word = '123456789'
print(word[0], word[8])
print(word[-9], word[-1])

print('--------List-------')
list = ['abcd',123,2.22,3+4j]
tinylist = [123, 'runoob']
print('输出完整列表',list)
print('输出列表第一个元素',list[0])
print('从第二个开始输出到第三个元素',list[1:3])
print('输出从第三个元素开始的所有元素',list[2:])
print('输出两次列表',tinylist * 2)
print('连接列表',list + tinylist)

list = ['1','2','3','4','5','6']
print('列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：'
      ,list[1:4:2]
      ,list[-1::-1]
      ,list[-1:-5:-2]
      )

'''
注意：
1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的
'''

print('--------Tuple（元组）-------')
tuple = ('abcd',123,'qwer',1.005)
tinytuple = (123,'qwer')
print('输出完整元组',tuple)
print('输出元组第一个元素',tuple[0])
print('从第二个开始输出到第三个元素',tuple[1:3])
print('输出从第三个元素开始的所有元素',tuple[2:])
print('输出两次列表',tinytuple * 2)
print('连接列表',tuple + tinytuple)
'''
注意：
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。
'''
'''
元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取
可以把字符串看作一种特殊的元组
tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
'''
'''
string、list 和 tuple 都属于 sequence（序列）。
'''

print('--------Set（集合）-------')
'''
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
元素无序
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式：
parame = {value01,value02,...}
或者
set(value)
'''
sites = {'A','B','C','D','E','E'}
print(sites)
#成员测试
if 'A' in sites:
    print('A in sites')
else:
    print('A not in sites')

result = 'A not in sites'
if 'A' in sites:
    result = 'A in sites'
print(result)
#set
a = set('qwertyuiop-qwer-asdf')
b = set('asdfghjkl-jkl-uiop')
print(a,'&',b)
print('ab差集',a - b)
print('ab并集',a | b)
print('ab交集',a & b)
print('ab不同时存在的元素集合',a ^ b)

print('--------Dictionary（字典）-------')
'''
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
'''
dict1 = {}
dict1['one'] = "xxxx"
dict1[2] = "yyyy"
tinydict = {'name': '小A','age':10, 'favorate': 'xiaonaofu'}

print ('输出键为 \'one\' 的值',dict1['one'])
print ('输出键为 2 的值',dict1[2])
print ('输出完整的字典',tinydict)
print ('输出所有 键',tinydict.keys())
print ('输出所有 值',tinydict.values())

print('构造函数 dict() 可以直接从键值对序列中构建字典')
dictx = dict([('qwer', 1), ('qw', 2), ('we', 3)])
print(dictx)

dictx = {zzz:zzz**2 for zzz in (1,2,3)}
print(dictx)
'''
另外，字典类型也有一些内置的函数，例如 clear()、keys()、values() 等。
注意：
1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。
'''
print('--------数据类型转换-------')
'''
int(x [,base]) 将x转换为一个整数

float(x) 将x转换到一个浮点数

complex(real [,imag]) 创建一个复数

str(x) 将对象 x 转换为字符串

repr(x) 将对象 x 转换为表达式字符串

eval(str) 用来计算在字符串中的有效Python表达式,并返回一个对象

tuple(s) 将序列 s 转换为一个元组

list(s) 将序列 s 转换为一个列表

set(s) 转换为可变集合

dict(d) 创建一个字典。d 必须是一个 (key, value)元组序列。

frozenset(s) 转换为不可变集合

chr(x) 将一个整数转换为一个字符

ord(x) 将一个字符转换为它的整数值

hex(x) 将一个整数转换为一个十六进制字符串

oct(x) 将一个整数转换为一个八进制字符串
'''


