'''
Python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。
Python 支持各种数据结构的推导式：
列表(list)推导式
字典(dict)推导式
集合(set)推导式
元组(tuple)推导式
'''
print('---------------List---------------------')
'''
[out_exp_res for out_exp in input_list]
[out_exp_res for out_exp in input_list if condition]
'''
names = ['aa','bbb','cccc','ddddd','xxxxxxxx']
names = [name for name in names if len(name)>3]
names1 = [name.upper() for name in names if len(name)>3]
print('list--',names,names1)

number_list1 = [0,1,2,3,4,5]
print('list--',[num**2 for num in number_list1])
print('list--',[num**2 for num in number_list1 if num>2])

print('---------------Dictionary---------------')
'''
{ key_expr: value_expr for value in collection }
{ key_expr: value_expr for value in collection if condition }
'''
dict_name = {'xiaoming','aHa','dingding','Weeeex','dingeeee'}
print('dict--',{name:'name' for name in dict_name})
'''生成的键值对，不要轻易key-value去取'''

print('---------------Set----------------------')
'''
{ expression for item in Sequence }
{ expression for item in Sequence if conditional }
'''
number_set = (1,2,3,4,5,6)
print('set--',{num+1 for num in number_set if num>3})

print('---------------Tuple--------------------')
'''
(expression for item in Sequence )
(expression for item in Sequence if conditional )
'''
print('tuple--',(x**2 for x in range(0,10))) #返回生成器对象 需要序列化
print('tuple--',tuple((x**2 for x in range(0,10))))