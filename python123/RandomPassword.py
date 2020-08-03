#RandomPassword.py
#以整数17为随机数种子，获取用户输入整数N为长度，产生3个长度为N位的密码，\
# 密码的每位是一个数字。每个密码单独一行输出。
import random

def genpwd(length):
    a = 10**(length-1)
    b = 10**length - 1
    return "{}".format(random.randint(a, b))

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))