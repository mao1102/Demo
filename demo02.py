#判断
# a=1
# b=2
# if a==1:
#     print("a等于1，通过")

# if a>b:
#     print("a比b大")
# else:
#     print("a比b小")

# age=int(input("请输入你的年龄"))
# if age==25:
#     print("热血青年")
# elif age>30:
#     print("中年人")
# elif age>40:
#     print("老年人")
# else:
#     print("未成年人")
 
 # 循环
# a = 1
# while a<10:
#     print("哈哈",a)
#     a=a+2


# 遍历
# a=["aaa","bbb","ccc"]
# for b in a:
#     print(b)

# b=list(range(0,100))
# print(b)  

# for i in range(5):
#     print(i) 

# aa={}
# bb={}
# a=["张三","李四","王五"]
# for i in a:
#     chengji=int(input("请输入你的成绩:"+i))
#     if chengji>=60:
#         aa[i]=chengji
#     else:
#         bb[i]=chengji

# print("及格",aa)
# print("不及格",bb)

# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#           print(i,"X",j,"=",i*j,end="|")
#     print()


name=input("请输入账号：")
mima=input("请输入密码：")
if len(name)>=5 and len(name)<=8:
    if name[0] in"qwertyuiopasdfghjklzxcvbnm":
        if len(mima)>=8 and len(mima)<=12:
            print("注册成功！你的账号为"+name,"密码为"+mima)
        else:
            print("密码长度必须是8-12位！")
    else:
            print("账号手写字母必须为小写！")
else:
    print("账号长度必须是5-8位！")

