"""
用户身份验证
"""
# username = input("请输入用户名：")
# password = input("请输入口令：")

# if username == 'admin' and password == '123456':
#     print('身份验证成功')
# else:
#     print('身份验证失败！')

"""
分段函数求值
"""
# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print('f(%.2f) = %.2f' % (x, y))

"""
掷骰子决定做什么事情
"""

# from random import randint

# face = randint(1, 6)
# if face == 1:
#     result = '唱首歌'
# elif face == 2:
#     result = '跳支舞'
# elif face == 3:
#     result = '学狗叫'
# elif face == 4:
#     result = '绕口令'
# elif face == 5:
#     result = '做俯卧撑'
# else:
#     result = '讲冷笑话'
# print(face)
# print(result)

"""
输入一个正整数判断它是不是素数
"""
# from math import sqrt
# num = int(input('请输出一个整数：'))
# end = int(sqrt(num)) + 1
# is_prime = True
# for n in range(2, end):
#     if num % n == 0:
#         is_prime = False
#         break
# if is_prime == True and num != 1:
#     print('该数为质数：%d' % num)
# else:
#     print('该数为素数：%d' % num)

"""
输入两个正整数计算最大公约数和最小公倍数
"""
# x = int(input('x = '))
# y = int(input('y = '))

# if x > y:
#     x, y = y, x
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公倍数是%d' % (x, y, factor))
#         print('%d和%d的最小公约数是%d' % (x, y, x * y //factor))
#         break

