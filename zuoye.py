'''
1、编写一个返回随机手机号的方法
2、编写一个返回指定长度和内容的随机字符串方法
3、编写一个返回随机姓名的方法
'''
# import random
#
# def Test_1():
#     l = random.choices(("130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","166","171","172","173","175","176","177","178","181","182","183""184","185","186","187","188","189","198","199"),k=1)
#     a = random.choices("0123456789",k=8)
#     res = l+a
#     print("".join(res))
# Test_1()
#
# def Test_2(str,lenth):
#     res = random.choices(str,k=lenth)
#     return "".join(res)
# print(Test_2("SADAF12151",5))
#
# def Test_3():
#     a = random.choices(("张","李","胡","田","孙"),k=1)
#     b = random.choices(("三","四","天","花","水"), k=1)
#     res = a+b
#     print("".join(res))
#
# Test_3()

# try:
#     open("b.txt","r")
#     print(1/0)
# except FileNotFoundError as a:
#     print(a)
#     print("程序错误")
#     print("重新打开文件")
# except ZeroDivisionError as a:
#     print(a)
#     print("除数不能为0")
# else:
#     print("程序运git行没报错")
# finally:
#     print("不管程序有没有报错都会运行")
#
# print("文件已经打开")