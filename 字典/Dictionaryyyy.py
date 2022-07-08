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



