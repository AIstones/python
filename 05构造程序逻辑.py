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


