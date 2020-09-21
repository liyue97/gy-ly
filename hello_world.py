# #
# # a = [1,2,3,4] #可修改  有序
# #
# # print(a)
# # a[0] = 10
# # print(a)
# #
# # b = (1,2,3,4) #不可修改  有序
# #
# # print(b)
# #
# # c = {1,2,3,4}  #可修改  无序
# #
# # print(c)
# #
# # d = {"name":"王大锤","age":18}
# # print(d)
# # print(d["name"])
# # d["name"] = "asdasd"
# # print(d["name"])
# # # 类型转换
# #
# # a = 2
# # b = '20'
# # print(a + int(b))
# # print(str(a) + b)
# #
# # c = 5
# # d = '2.6'
# # print(c + float(d))
# #
# # l = [1,2,3,4,5]
# # print(tuple(l))
# # print(set(l))
# #
# # t = [1,2,3,4,5]
# # print(list(t))
# # print(set(t))
# #
# # s = [1,2,3,4,5]
# # print(list(s))
# # print(tuple(s))
# #
# # str = "132445"
# # print(list(str))
# # print(tuple(str))
# # print(set(str))
# #
# # #成员运算符 in   not in
# #
# # a = "asdafards"
# # l = ["a",1,"c"]
# # t = ("a",1,"c")
# # s = {"a",1,"c"}
# # d = {"name":"王大锤","age":18}
# #
# # print("a" in a)
# # print("a" in l)
# # print("a" in t)
# # print("a" in s)
# # print("name" in d) #字典只能判断key是否存在
#
# money = 10
# if(money >= 100 ):
#     print("叫滴滴")
# else:
#     print("坐地铁")
#
# money = 100
# if(money < 50):
#     print("做梦吧")
# elif(money < 100):
#     print("坐11路公交")
# elif(money < 1000):
#     print("坐公交")
# elif(money < 10000):
#     print("坐地铁")
# elif(money < 100000):
#     print("坐飞机")
# else:
#     print("坐火箭")
#
# for i in range(5):
# 	print("我是王冰华")

#for循环
# for i in  range(1,10,1):
#     print(i)

# #while循环
# i = 0
# while(i < 10):
#     print(i)
#     i+= 1

#跳过本次循环 pass  continue 的区别
# for i in range(1,11):
#     if(i == 7):
#         continue
#     print(i)
#
# for i in range(1,11):
#     if(i in [2,8]):
#         pass
#     else:
#         print(i)

#结束循环
# for i in range(1,11):
#     if(i == 7):
#         break
#     print(i)
#
# a = 132
# print(a//10%10)

#函数（方法）
#def + 方法名 a,b为参数   :表示下方包含一个代码块（方法体）
# def div(a,b):
#     if(b == 0):
#         print("被除数不能为0")
#     else:
#         print(a / b)
# div(20,5)
# div(6,2)

#return 表示一个方法结束，方法返回数据的关键字
# def select_data():
#     res = "查询结果"
#     return res

#result = select_data()  #使用变量接收方法返回值
# print(result)
#
# #位置参数
# def s(a,b):
#     return a + b
# print(s(1,6))

#关键字参数
#如果调用时没有传参则用默认值
#关键字，位置同时存在，位置参数在前边，关键字参数在后边
# def s(a=1,b=20):
#     return a+b
# print(s(1))

#调用传参
#按照位置传参
# print(s(1,2))

#按照关键字传参
# print(s(b=30))

#位置和关键字同时存在，位置在前，关键字在后
# print(s(5,b=60))

#动态参数定义
# def ar(a,*args,b=10,**kwargs):
#     print(args)
#     print(kwargs)
#     print(a)
#
#
# ar(1,2,3,4,5,6,7,8,9,0,c=6,b=2)

# def case1(a,b=2):
#     print(a)
#     print(b)
#     print("这是一个测试用例1")
#
# def case2(a,b,c=20):
#     print(a)
#     print(b)
#     print("这是一个测试用例2")
#
# def log(func,*args,**kwargs):
#     print("执行用例之前",args,kwargs)
#     r = func(*args,**kwargs)
#     print("用例执行之后", r)
#
#
# log(case1,10,20)
# log(case2,1,2)

# f = open("a.txt",'w')
# f.write("hello world")
# f.close()

# f = open("a.txt",'r')
# res = f.read()
# print(res)

#九九乘法表（循环嵌套）
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'X',i,'=',i*j,end='\t')
#     print()

# c = 10

# def aaa():
#     global c  #在局部作用域中声明全局作用域的变量
#     c = 20
#
# aaa()
# print(c)
#变量搜索规则 就近原则
#局部变量无法在外部使用
#global可以在局部作用域中声明变量为全局变量
#Python中变量赋值是对储存空间的引用，而不是对储存空间的拷贝

#字符串
a = "1234567890"
# b = "654"
#
# print(a+b) #拼接
# print(a*3) #复制
# print(a[0]) #通过下标获取
# print(a[2:6]) #获取3-6的字符
# print(a[:6]) #获取1-6的字符
# print(a[4:]) #获取5-0的字符
# print(a[-2:]) #倒着数
# print(a[1:-2])
# print(a[::-1]) #反序

# a = " sdgrafv "
# print(a)
# b = a.strip()
# print(b)
# print(a.strip())#去前后空格
# print(a.lstrip())#去左空格
# print(a.rstrip())#去右空格
# line = "用例名,账户名,充值金额,预期结果"
# line = line.replace("，",",")
# print(line)
# print(line.split(',')) #切片
# print(line.find("预期")) #查找，找到返回第一个字符的下标，找不到返回-1


# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{} X {} = {}".format(i,j,i*j),end='\t')
#     print()

#列表
#遍历列表
# l = [1,2,3,4,5,6,7,8,9]
# # for i in l:
# #     print(i)
#
# l[0] = 20 #根据下标修改列表元素的值
# l.append(9) #往列表末尾添加数据
# l.insert(2,30) #根据下标往列表中插入数据
# l.extend((1,2,3,4,5,)) #往列表末尾添加多个数据
# l.pop() #删除列表末尾最后一个元素
# l.pop(0) #根据下标删除数据
# l.remove(2) #根据内容删除列表中的数据，有重复只会删除第一个
# print(l.index(6)) #查询某个袁术的下标，多个值，只查询一个
# l.sort() #默认升序，会修改列表中的数据
# l.sort(reverse=True) #降序
#
# print(l)

#字典
# d = {"name":"王小锤","age":"10"}
#
# d["name"] = "吴邪" #修改
# d["sex"] = "女" #因为sex在原字典中不存在，所以是新增
# d.pop("sex") #删除字典中的数据
#
# d2 = {"sex":"女"}
# d.update(d2) #合并两个字典
# print(dict(d,addr="上海闵行",phone="465464")) #创建一个新的字典，并把数据放进去
#
# print(d)

#冒泡排序

# l = [69,45,89,63,74,30,60]
#
# for i in range(len(l)-1,0,-1): #i代表最后一个为排好序的数据下标
#     for j in range(0,i): #j代表每次循环时，当前位置的下标
#         if(l[j] > l[j+1]): #比较
#             l[j],l[j+1] = l[j+1],l[j] #交换两个数据的位置
#
# print(l)
#
# for i in range(10,0,-1):
#     print(i)

#类和对象
#创建一个类
# class str_demo():
#
#     s = None
#
#     def replace(self):
#         print("字符串替换")
#
#     def split(self):
#         print("字符串切割")
#
# sd = str_demo() #实例化 sd就是一个对象
# sd.s = "hello"
# sd.replace()
# sd.split()
# print(sd.s)
# class str_demo():
#
#     #不需要显示调用，程序自动调用的
#     def __init__(self):
#         print("魔法方法")
#
#     #实例方法
#     def replace(self):
#         print("实例方法")
#         pass
#
#     @classmethod #装饰器
#     def split(cls):
#         print("类方法")
#
#     @staticmethod
#     def static():
#         print("静态方法")

#类外部调用
# str_demo.split() #调用类方法
# str_demo().replace() #通过对象调用实例方法
# str_demo.static() #通过类名调用静态方法
# str_demo().static() #通过对象调用静态方法
# str_demo() #调用__init__魔法方法

#类的封装
# class Demo():
#
#     __a = "私有类变量"
#     b = "类变量"
#
#     def __say(self): #私有方法
#         print("hello")
#
#     def __see(self):
#         print("you see you")
#
# d = Demo()
# print(d.b)

#类的继承



