"""
寻找水仙花数
"""

# for i in range(1000, 10000):
#     a = int(i/1000)
#     b = int(i%1000/100)
#     c = int(i%100/10)
#     d = int(i%10)
#     if pow(a, 4) + pow(b, 4) + pow(c, 4) + pow(d, 4) == i:
#         print(i, end=' ')

"""
完全数
"""

# def wanquanshu(x):
#     li = []
#     for i in range(2, x):
#         if x % i == 0:
#             li.append(i)
#     sum = 1    
#     for j in li:
#         sum += j
#     if sum == x:
#         print('该数是完全数%d' % x)
# for n in range(10000):  
#     wanquanshu(n)


"""
百钱百鸡
"""
# for i in range(20):
#     for j in range(34):
#         if 15*i + 9*j + (100-i-j) == 300:
#             print('公鸡有%d只， 母鸡有%d只， 雏鸡有%d' % (i, j, (100-i-j)))

# a1 = 1
# a2 = 1
# li = [1, 1]
# for n in range(3, 20):
#     a3 = a1 + a2
#     li.append(a3)
#     a1, a2 = a2, a3

# print(list(li))

"""
cpaps赌博游戏 

说明：
一个简单的赌博游戏，游戏规则如下：玩家掷两个骰子，点数为1到6，如果第一次点数和为7或11，则玩家胜，如果点数和为2、3
或12，则玩家输，如果和 为其它点数，则记录第一次的点数和，然后继续掷骰，直至点数和等于第一次掷出的点数和，则玩家胜，
如果在这之前掷出了点数和为7，则玩家输。

解法:
规则看来有些复杂，但是其实只要使用switch配合if条件判断来撰写即可，小心不要弄错胜负顺序即可。
--------------------- 
"""

# from random import randint


# while True:
#     i = randint(1, 7)
#     j = randint(1, 7)
#     if i + j == 7 or i + j ==11:
#         print('玩家胜')
#         break
#     elif i + j == 2 or i + j == 3 or i + j == 12:
#         print('玩家输')
#         break
    