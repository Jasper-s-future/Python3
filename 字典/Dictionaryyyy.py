'''
d = {key1 : value1, key2 : value2, key3 : value3 }
键 唯一
值 可以取任何数据类型，但键必须是不可变的，如字符串，数字。
'''
emptyDict = {}
#emptyDict = dict()
dictxxx = {1:'11',2:'22','3':'33'}

print(emptyDict,dictxxx)
print("Length:", len(emptyDict),len(dictxxx))
print(type(emptyDict),type(dictxxx))

print(dictxxx[1],dictxxx['3'])

dictxxx[2] = '222'
print('修改value',dictxxx)

del dictxxx['3']
print('删除指定key',dictxxx)

dictxxx.clear()
print('clear',dictxxx)

del dictxxx
#print('删除字典',dictxxx)  #del后，dictxx就变成 not define了

print('-------------------字典键的特性---------------------')
print('字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。')

tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print("tinydict['Name']: ", tinydict['Name'],'\n 相同的键值会被刷新掉')

print('键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行')
# tinydict = {['Name']: 'Runoob', 'Age': 7}
# print("tinydict['Name']: ", tinydict['Name'])

print('-------------------字典 函数---------------------')
dictxxxxx = {'1':2,'2':3}
dictxxxxx.clear()
print(dictxxxxx,id(dictxxxxx))

tinydict = dictxxxxx.copy()#浅copy
print(tinydict,'\n',id(dictxxxxx),'\n',id(tinydict))

print('dict.fromkeys(seq[,value]) seq 字典键值列表 value 可选参数 设置对应的值')
seq = ('name','age','sex')
tinydict = dict.fromkeys(seq)
print(tinydict)
tinydict = dict.fromkeys(seq,10)
print(tinydict)