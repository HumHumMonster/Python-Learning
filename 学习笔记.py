if __name__ == "__main__" :
一个python的文件有两种使用的方法，第一是直接作为脚本执行，第二是import到其他的python脚本中被调用（模块重用）执行。因此if __name__ == 'main': 的作用就是控制这两种情况执行代码的过程，在if __name__ == 'main': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，而import到其他脚本中是不会被执行的。

多组输入：
if __name__ == "__main__" :
    try :
        while True :
            pass
    except EOFError :
        pass


list列表[  ,   ,  ]
可以对列表的数据项进行修改或更新 list[2] = 2001
可以直接删除其中部分 del list[2]
求长度  len([1, 2, 3]) = 3
组合 [1, 2, 3] + [4, 5, 6] = [1, 2, 3, 4, 5, 6]
重复 ['Hi!'] * 4 = ['Hi!', 'Hi!', 'Hi!', 'Hi!']

max(list)
返回列表元素最大值

min(list)
返回列表元素最小值

list(seq)
将元组转换为列表
1	list.append(obj)
在列表末尾添加新的对象
2	list.count(obj)
统计某个元素在列表中出现的次数
3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素
9	list.sort( key=None, reverse=False)
对原列表进行排序
10	list.clear()
清空列表
11	list.copy()
复制列表


元组(   ,   ,   )
创建空元组
tup1 = ();
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合.
tup3 = tup1 + tup2;
元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
del tup;
实例元组被删除后，输出变量会有异常信息，
print (tup)
NameError: name 'tup' is not defined

len(tuple)
计算元组元素个数。

max(tuple)
返回元组中元素最大值。

min(tuple)
返回元组中元素最小值。

tuple(seq)
将列表转换为元组。


字典d = {key1 : value1, key2 : value2 }
键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

结果：
dict['Name']:  Runoob
dict['Age']:  7
如果用字典里没有的键访问数据，会输出错误KeyError:
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'} 
dict['Age'] = 8 # 更新 Age 
dict['School'] = "菜鸟教程" # 添加信息
del dict['Name'] # 删除键 'Name'
dict.clear() # 清空字典
del dict # 删除字典
如果键值可变，会出现TypeError
len(dict)
计算字典元素个数，即键的总数。
str(dict)
输出字典，以可打印的字符串表示。
type(variable)
返回输入的变量类型，如果变量是字典就返回字典类型。
1	radiansdict.clear()
删除字典内所有元素
2	radiansdict.copy()
返回一个字典的浅复制
3	radiansdict.fromkeys()
创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	radiansdict.get(key, default=None)
返回指定键的值，如果值不在字典中返回default值
5	key in dict
如果键在字典dict里返回true，否则返回false
6	radiansdict.items()
以列表返回可遍历的(键, 值) 元组数组
7	radiansdict.keys()
返回一个迭代器，可以使用 list() 来转换为列表
8	radiansdict.setdefault(key, default=None)
和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	radiansdict.update(dict2)
把字典dict2的键/值对更新到dict里
10	radiansdict.values()
返回一个迭代器，可以使用 list() 来转换为列表
11	pop(key[,default])
删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
12	popitem()
随机返回并删除字典中的最后一对键和值。

集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式：
parame = {value01,value02,...}
或者
set(value)
>>> # 下面展示两个集合间的运算. ... 
>>> a = set('abracadabra') 
>>> b = set('alacazam') 
>>> a {'a', 'r', 'b', 'c', 'd'} 
>>> a - b # 集合a中包含而集合b中不包含的元素 {'r', 'd', 'b'}
>>> a | b # 集合a或b中包含的所有元素 {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'} 
>>> a & b # 集合a和b中都包含了的元素 {'a', 'c'} 
>>> a ^ b # 不同时包含于a和b的元素 {'r', 'd', 'b', 'm', 'z', 'l'}


>>> thisset.add("Facebook")  #添加
>>> thisset.update({1,3}) #添加1 , 3
>>> thisset.update([1,4],[5,6]) #添加 1 , 4 , 5 , 6

>>>thisset.remove("Taobao") #删除
不存在会发生错误KeyError
此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。
s.discard( x )
我们也可以设置随机删除集合中的一个元素，语法格式如下：
s.pop() 
然而在交互模式，pop 是删除集合的第一个元素（排序后的集合的第一个元素）。
len(s)
计算集合 s 元素个数。
s.clear()
清空集合 s。
add()
为集合添加元素
clear()
移除集合中的所有元素
copy()
拷贝一个集合
difference()
返回多个集合的差集
difference_update()
移除集合中的元素，该元素在指定的集合也存在。
discard()
删除集合中指定的元素
intersection()
返回集合的交集
intersection_update()
返回集合的交集。
isdisjoint()
判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()
判断指定集合是否为该方法参数集合的子集。
issuperset()
判断该方法的参数集合是否为指定集合的子集
pop()
随机移除元素
remove()
移除指定元素
symmetric_difference()
返回两个集合中不重复的元素集合。
symmetric_difference_update()
移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()
返回两个集合的并集
update()
给集合添加元素


