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

