# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a
def main():
#     str1 = 'hello, world!'
#     print(len(str1))  # 13
#     print(str1.capitalize()) #Hello, world!
#     print(str1.upper())  #HELLO, WORLD!
#     print(str1.find('or')) #8
#     print(str1.find('shit')) #-1
#     print(str1.startswith('He')) #False
#     print(str1.startswith('hel')) #True

#     print(str1.endswith('!'))
#     print(str1.center(20, '*')) #***hello, world!****
#     print(str1.rjust(20, ' '))  #       hello, world!
#     str2 = 'abc12345'
#     print(str2.isdigit())
#     print(str2.isalpha())
#     print(str2.isalnum())
#     str3 = '  jackfrued@126.com'
#     print(str3)
#     print(str3.strip())
#     print(str3.split('.'))
    

#     #字符切片就不多做学习了

#     # 添加元素
#     list1 = [ 1, 3, 5, 7, 100]
#     print(list1)
#     list2 = ['hello'] * 5
#     print(len(list1))
#     print(list1[0])
#     print(list1[4])
#     print(list1[-1])

#     list1.append(200)
#     list1.insert(1, 400)
#     list1 += [1000, 2000]
#     print(list1)

#     # 删除元素
#     list1.remove(3)
#     print(list1)

#     import sys

#     f = [x for x in range(1, 100)]
#     print(f)
#     f = [x + y for x in 'ABCDE' for y in '1234567']
#     print(sys.getsizeof(f))
#     print(f)

#     f = (x ** 2 for x in range(1, 1000))
#     print(sys.getsizeof(f))
#     print(f)
#     for val in fib(20):
#         print(val)

#     t = ('ailei', 25, True, '四川成都')
#     print(t)

#     print(t[0])
#     print(t[3])

#     for member in t:
#         print(member)

#     t = ('王大锤', 20, True, '云南昆明')
#     print(t)

#     person = list(t)
#     print(person)
#     person = tuple(person)
#     print(person)

#     set1 = {1, 2, 3, 3, 4, 2}
#     print(set1)
#     print('Length = ', len(set1))
#     set2 = set(range(1, 10))
#     print(set2)
#     set1.add(4)
#     set1.add(5)
#     set2.update([11, 12])
#     print(set1)
#     print(set2)
#     set2.discard(5)
#     if 4 in set2:
#         set2.remove(4)
#     print(set2)

#     for elem in set2:
#         print(elem ** 2, end=' ')
#     print()

#     set3 = set((1, 2, 3, 3, 2, 1))
#     print(set3.pop())
#     print(set3)
#     # 使用字典
#     scores = {'ailei': 95, 'chencheng': 78, 'direnjie': 83}
#     print(scores['ailei'])
#     print(scores['direnjie'])

#     for elem in scores:
#         print('%s\t--->\t%d' % (elem, scores[elem]))
        
#     scores.update(haha = 67, baiqi = 85)
#     print(scores)
#     print(scores.get('ailei'))

#     import os 
#     import time

#     content = '北京欢迎你为你开天辟地。。。'
#     while True:

#         os.system('cls')
#         print(content)

#         time.sleep(0.2)
#         content = content[1:] + content[0]

    """设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
    """
    # import random
    # def generate_code(code_len=4):
    #     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #     last_pos = len(all_chars) - 1
    #     code = ''
    #     for _ in range(code_len):
    #         index = random.randint(0, last_pos)
    #         code += all_chars[index]
    #     return code

    # """设计一个函数返回给定文件名的后缀名。"""
    # def get_suffix(filename, has_dot=False):
    #     """获取文件名的后缀名"""
    #     pos = filename.rfind('.')
    #     if 0 < pos < len(filename) - 1:
    #         index = pos if has_dot else pos + 1
    #         return filename[index:]
    #     else:
    #          return ''

    # def max(x):
    #     xm = sorted(x)
    #     m1 = xm[-1]
    #     m2 = xm[-2]
    #     return m1, m2

    # l = [1,2,5,7,9,5,3,2,8,0,3,4]
    # print(max(l))

    """计算指定的年月日是这一年的第几天"""
    # def is_leap_year(year):
    #     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    # def which_day(year, month, date):
    #     """计算传入的日期是这一年的第几天"""
    #     days_of_month = [
    #     [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    #     [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # ][is_leap_year(year)]

    # num = int(input("Number of rows: "))
    # yh = [[]] * num
    # for row in range(len(yh)):
    #     yh[row] = [None] * (row + 1)
    #     for col in range(len(yh[row])):
    #         if col == 0 or col == row:
    #             yh[row][col] = 1
    #         else:
    #             yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
    #         print(yh[row][col], end='\t')
    #     print()

    """双色球选号"""
    # from random import randrange, randint, sample

    # def display(balls):
    #     """
    #     输出列表中的双色球号码
    #     """
    #     for index, ball in enumerate(balls):
    #         if index == len(balls) - 1:  
    #             print('|', end=' ')
    #         print('%02d' % ball, end=' ')
    #     print()
    #     print(len(balls))
    #     print(list(enumerate(balls)))
    # def random_select():
    #     """随机选择一组号码"""
    #     red_balls = [x for x in range(1, 34)]
    #     selected_balls = []
    #     selected_balls = sample(red_balls, 6)
    #     selected_balls.sort()
    #     selected_balls.append(randint(1, 16))
    #     return selected_balls

    # n = int(input('机选几注：'))
    # for _ in range(n):
    #     display(random_select())
    
if __name__ == '__main__':
    main()