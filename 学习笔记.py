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



