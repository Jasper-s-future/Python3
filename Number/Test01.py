'''
三种不同的数值类型：
整型(int)：  通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，
            所以 Python3 没有 Python2 的 Long 类型。布尔(bool)是整型的子类型。
浮点型(float)： 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
复数( (complex))： 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
'''
# 数据类型是不允许改变的,这就意味着如果改变数字数据类型的值，将重新分配内存空间。
import math
from math import ceil, exp, fabs, floor, log, log10, modf, sqrt
from random import choice, randrange, random, seed, shuffle, uniform

var1 = 1
var2 = 10
print(var1,var2)
del var1,var2 #del语句删除数字对象的引用
#print(var1,var2)   #这句会报错哦，已被del，相当于结束了作用域
print('----------------------------数学函数---------------------------------')
x = -3.14
x1 = 1
x2 = 3.2
x3 = -2.3
x4 = 9

print('abs(x)         ',abs(x))          #返回数字的绝对值，如abs(-10) 返回 10
print('ceil(x)        ',ceil(x))         #返回数字的上入整数，如math.ceil(4.1) 返回 5
#print('cmp(x, y)      ',cmp(x, y))      #如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃，使用 (x>y)-(x<y) 替换。
print('exp(x)         ',exp(x))          #返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
print('fabs(x)        ',fabs(x))         #返回数字的绝对值，如math.fabs(-10) 返回10.0
print('floor(x)       ',floor(x))        #返回数字的下舍整数，如math.floor(4.9)返回 4
print('log(x)         ',log(math.e))     #如math.log(math.e)返回1.0,math.log(100,10)返回2.0
print('log10(x)       ',log10(x2))        #返回以10为基数的x的对数，如math.log10(100)返回 2.0
print('max(x1, x2,...)',max(x1,x2,x3))   #返回给定参数的最大值，参数可以为序列。
print('min(x1, x2,...)',min(x1, x2))     #返回给定参数的最小值，参数可以为序列。
print('modf(x)        ',modf(x))         #返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
print('pow(x, y)      ',pow(x, x2))      #x**y 运算后的值。
print('round(x [,n])  ',round(x))        #返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。其实准确的说是保留值将保留到离上一位更近的一端。
print('sqrt(x)        ',sqrt(x4))        #返回数字x的平方根。

print('----------------------------随机数函数-------------------------------')
seq = range(10)
xxx = 1
eee = 4
list1 = [1,2,3,6,1,21,3,13,21,21,1,14,1,2]

print('choice(seq)  ',choice(seq))      #从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
print('randrange ([start,] stop [,step])'
      ,randrange(xxx,eee,2))            #从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
print('random()',random())              #随机生成下一个实数，它在[0,1)范围内。
#print('seed([x])',seed(10))              #改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
#print('shuffle(lst)',shuffle(list1))    #将序列的所有元素随机排序
print('uniform(x, y)',uniform(1, 3))    #随机生成下一个实数，它在[x,y]范围内。

print('----------------------------三角函数-------------------------------')
x = eval('90/360')
print('sin ',math.sin(x))
'''
```````````````````
'''