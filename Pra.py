
# -*- coding: utf-8 -*-
#1,如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
#通过添加if语句保证列表生成式能正确地执行：
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L if isinstance(s,str)]


#2,斐波那契   

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)            #yield b  就是generator生成器
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(5) #执行不了



for n in fib(6):
    print(n)
#并不会用next（）


#3.杨辉三角  用到列表生成式   迭代器
def yangtri():
    L = [1]
    while True:
        yield(L) #for循环执行过程中，遇到yield就中断，下次又从该位置继续执行
        newL = [L[i]+L[i+1] for i in range(len(L)-1)] #列表生成器 上一章
        L = newL
        L.insert(0,1) #在第0位插入数据1
        L.append(1)


n = 0
for t in yangtri(): #使用for循环来迭代才能获取generator的下一个值，或者使用.next()
    print(t)
    n = n + 1
    if n==10:
        break
#在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。

#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
isinstance(iter([]), Iterator)
#True
#小结

    #凡是可作用于for循环的对象都是Iterable类型；

    #凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

    #集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

    #Python的for循环本质上就是通过不断调用next()函数实现的，


#函数式编程：
   #高阶函数 ：把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
#map
  #返回结果是Iterator  需要list()一下
#reduce
  #不需要list()


list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
['1', '2', '3', '4', '5', '6', '7', '8', '9']

from functools import reduce
def fn(x, y):
    return x * 10 + y

reduce(fn, [1, 3, 5, 7, 9])
13579
#map reduce混合将字符串转化为数字  先提取每个字符map（）  再*10求和（reduce）
from functools import reduce
def fn(x, y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

reduce(fn, map(char2num, '13579'))
#13579
#---->整合成一个函数
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

#还可以用lambda函数进一步简化成：

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
#+++++++++++++++++++++++++++++++++PRA
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    pass   #
#+++++++++++++++++++++++++++++++++PRA
#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    pass
#+++++++++++++++++++++++++++++++++PRA
#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    pass

filter() #惰性序列 需要list()一下
#把一个序列中的空字符串删掉，可以这么写：

def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']

#枚举
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

    
#输出情况
# Jan => Month.Jan , 1
#Feb => Month.Feb , 2


#把Student的gender属性改造为枚举类型，可以避免使用字符串：
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

    
#测试通过!
bart = Student('BBB',Gender.Male)
print(bart.gender)
Gender.Male
#Q:Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
