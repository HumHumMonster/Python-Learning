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

