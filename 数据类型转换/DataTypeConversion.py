print('--------数据类型转换-------')
'''
int(x [,base])          将x转换为一个整数       [x -- 字符串或数字 ，base -- 进制数，默认十进制。] int('123',base=10)
float(x)                将x转换到一个浮点数
complex(real [,imag])   创建一个复数            [real -- int, long, float或字符串；imag -- int, long, float；]
str(x)                  将对象 x 转换为字符串
repr(x)                 将对象 x 转换为表达式字符串
eval(str)               用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)                将序列 s 转换为一个元组
list(s)                 将序列 s 转换为一个列表
set(s)                  转换为可变集合
dict(d)                 创建一个字典。d 必须是一个 (key, value)元组序列。
frozenset(s)            转换为不可变集合
chr(x)                  将一个整数转换为一个字符
ord(x)                  将一个字符转换为它的整数值
hex(x)                  将一个整数转换为一个十六进制字符串
oct(x)                  将一个整数转换为一个八进制字符串
'''
print('--------------隐式类型转换----------------')
num_int = 123
num_float = 0.123
num = num_int + num_float
print('num_int=',num_int,'num_int type is',type(num_int))
print('num_float=',num_float,'num_float type is',type(num_float))
print('num=',num,'num type is',type(num))

print('--------------显式类型转换----------------')
xxx_int = 123
xxx_float = 0.123
xxx_string = '123'
xxx_complex = 3+4j
xxx_dict = {'123','abc','/*-'}
xxx_tuple = [1,'2',xxx_dict]
xxx_set = (1,'2',xxx_tuple,xxx_dict)

print('int()--',int(xxx_float),int(xxx_string));
print('int(x,base=10)--',int(xxx_string,base=10))
print('float()--',float(num_int))
print('complex()--',complex(3,4))
print('str(x)--',str(num_float),str(num_int),'type',type(str(num_float)))
print('str(x)--',str(xxx_dict),'type--',type(str(dict)))
print('str(x)--',str(xxx_tuple),'type--',type(str(xxx_tuple)))
print('str(x)--',str(xxx_set),'type--',type(str(xxx_set)))
print('repr(x)--',repr(xxx_set),'type--',type(repr(xxx_set)))
xxx_eval_string = '3 * xxx_int'
print('eval()--',eval(xxx_eval_string))
print('chr()--',chr(0),chr(999))
print('ord()--',ord(chr(5)),ord(chr(2)))
print('hex()--',hex(153))
print('oct()--',oct(123))





