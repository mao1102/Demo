"""
print("你好，阿毛酱")  # 字符串
print(2222)  #整数
print(2.3333) #小数
print(True) #布尔值
print(()) #元祖
print([]) #数组
print({})  #字典

print("哈哈",233,2.33)
print("哈哈哈"*10)
print("哈哈"+"嘻嘻")
print((52+2)*5)
print(2<3)
"""
# a=input("请输入内容:")
# b=input("请继续输入内容：")
# print("获取内容",a+b)

# a=str(input('请输入'))
# b=str(input('继续输入'))
# print('长度为',len(a+b))

# a=int(input("请输入"))
# b=int(input("请继续输入"))
# print("结果为",a+b)

#数据格式的转换
# print(type("哈哈"))   字符串/str
# print(type(123))      整数/int
# print(type(1.23))     小数/float
# print(type(True))     布尔值/bool
# print(type(()))       元组/tuple
# print(type([]))       数组/list
# print(type({}))       字典/dict  


# 元组，下标，从0开始
# a=(1,2,3,4,'哈哈','哈哈','嘻嘻',True,False)
# print(a[4])

# 切片
# print(a[4:7])
# print(a[:7]) #左闭右开
# print(a[7:])

#  print(a.count('哈哈'))
#  print(a.index('哈哈'))
#二维元组
# b=(a,"测试","呵呵")
# print(b[0][4])

#数组
# a=[1,2,3,4,'哈哈','哈哈','嘻嘻',True,False]
# a.remove(1)
# print(a)

# a.append('显示在最后面的数据')
# a.insert(0,"显示在最前面的数据")
# b=a.pop(0) #剪切a第一个数据
# c=a.pop(1) #剪切a第二个数据
# print(c)
# # a.clear()  清空a数据
# xx=['好好学习，天天向上']
# print(a+xx)


#字典
#1、字典中的值没有顺序 2、字典的结构必须是键值对的结构 key：value
# a={"name":"张三",0:"哈哈","age":"25"}
# #取值
# print(a["name"])
# #新增
# a["hight"]="155cm"
# #修改
# a["name"]="李四"
# print(a) 

name=input("请输入你的姓名:")
sex=input("请输入你的性别:")
age=input("请输入你的年龄:")
a={"你的姓名是":name,"性别是":sex,"年龄是":age}
# a.update(name=name,sex=sex,age=age)
print(a)




