"""
输入M和N计算C（M，N）
"""
# m = int(input('m = '))
# n = int(input('n = '))

# fm = 1
# for num in range(1, m+1):
#     fm *= num
# fn = 1
# for num in range(1, n+1):
#     fn *= num
# fmn = 1
# for num in range(1, m-n+1):
#     fmn *= num
# print(fm // fn // fmn)

# from random import randint

# def roll_dice(n = 2):
#     """
#     摇色子
#     """
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total

# def add(a = 0, b = 0, c = 0):
#     return a + b + c

# print(roll_dice())

# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))

# print(add(c =50, a = 100, b = 200))

# def add(*args):
#     total = 0
#     for val in args:
#         total += val
#     return total

def foo():
    global a
    a = 200
    print(a)

if __name__ == '__main__':
    a = 100
    foo()
    print(a)