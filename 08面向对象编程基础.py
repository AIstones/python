# class Student(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def study(self, course_name):
#         print('%s正在学习%s' % (self.name, course_name))
    
#     def watch_movies(self):
#         if self.age < 18:
#             print('%s只能观看《熊出没》。' % self.name)
#         else:
#             print('%s正在观看岛国爱情大电影。' % self.name)
# def main():
#     stu1 = Student('ailei', 25)
#     stu1.study('python程序设计')
#     stu1.watch_movies()
#     stu2 = Student('wangdachui', 15)
#     stu2.study('思想品德')
#     stu2.watch_movies()

# class Test:
#     def __init__(self, foo):
#         self.__foo = foo
#     def __bar(self):
#         print(self.__foo) # 私有属性，无法ch
#         print('__bar')
    
# def main():
#     test = Test('hello') # AttributeError: 'Test' object has no attribute '__bar'
#     test.__bar()  # AttributeError: 'Test' object has no attribute '__foo'
#     print(test.__foo)

# from time import sleep

# class Clock(object):
#     """数字时钟"""
#     def __init__(self, hour=0, minute=0, second=0):
#         """初始化方法"""
#         self._hour = hour
#         self._minute = minute
#         self._second = second
    
#     def run(self):
#         """走字"""
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0

#     def show(self):
#         """显示时间"""
#         return '%02d:%02d：%02d' % (self._hour, self._minute, self._hour)

# def main():
#     clock = Clock(23, 59, 58)
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()

# from math import sqrt

# class Point(object):
#     def __init__(self, x=0, y=0):

#         self.x = x
#         self.y = y
#     def move_to(self, x, y):
#         self.x += x
#         self.y += y
#     def move_by(self, dx, dy):
#         self.x += dx
#         self.y += dy
#     def distance_to(self, other):
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return sqrt(dx ** 2 + dy ** 2)
#     def __str__(self):
#         return '(%s, %s)' % (str(self.x), str(self.y))

# def main():
#     p1 = Point(3, 5)
#     p2 = Point()
#     print(p1)
#     print(p2)
#     p2.move_by(-1, 2)
#     print(p2)
#     print(p1.distance_to(p2))

        

# if __name__ == '__main__':
#      main()