# class Person(object):
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     # 访问器 - getter方法
#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age
    
#     @age.setter
#     def age(self, age):
#         self._age = age
#     def play(self):
#         if self._age <= 16:
#             print('%s正在玩飞行棋。' % self._name)
#         else:
#             print('%s正在玩斗地主。' % self._name)

# def main():
#     person = Person('王大锤', 12)
#     person.play()
#     person.age = 22
#     person.play()

# from math import sqrt

# class Triangle(object):
#     def __init__(self, a, b, c):
#         self._a = a 
#         self._b = b
#         self._c = c

#     @staticmethod
#     def is_valid(a, b, c):
#         return a + b > c and b + c > a and a + c > b
#     def perimeter(self):
#         return self._a + self._b + self._c
#     def area(self):
#         half = self.perimeter() / 2
#         return sqrt(half * (half - self._a) * )

# from time import time, localtime, sleep

# class Clock(object):
#     # 数字时钟
#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second
    
#     @classmethod
#     def now(cls):
#         ctime = localtime(time())
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

#     def run(self):
#         # 走字
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour +=  1
#                 if self._hour == 24:
#                     self._hour = 0
#     def show(self):
#         # 显示时间
#         return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

# def main():
#     clock = Clock.now()
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()

# class Person(object):
#     """人"""
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#     @property
#     def name(self):
#         return self._name
#     @property
#     def age(self):
#         return self._age
#     @age.setter
#     def age(self, age):
#         self._age = age
#     def play(self):
#         print('%s正在愉快的玩耍。' % self._name)
#     def watch_av(self):
#         if self.age >= 18:
#             print('%s正在观看爱情动作片。' % self._name)
#         else:
#             print('%s只能看《熊出没》。' % self._name)
# class Student(Person):
#     """学生"""
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self._grade = grade
#     @property
#     def grade(self):
#         return self._grade
#     @grade.setter
#     def grade(self, grade):
#         self._grade = grade
#     def study(self, course):
#         print('%s的%s正在学习%s.' % (self._grade, self._name, course))

# class Teacher(Person):
#     """老师"""
#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self._title = title
#     @property
#     def title(self, title):
#         return self._title
#     @title.setter
#     def title(self, title):
#         self._title = title
#     def teach(self, course):
#         print('%s%s正在讲%s.' % (self._name, self._title, course))
# def main():
#     stu = Student('王大锤', 15, '初三')
#     stu.study('数学')
#     stu.watch_av()
#     t = Teacher('ailei', 25, '老教授')
#     t.teach('Python程序设计')
#     t.watch_av()
from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
    """宠物"""
    def __init__(self, nickname):
        self._nickname = nickname
    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass
class Dog(Pet):
    """狗"""
    def make_voice(self):
        print('%s:汪汪汪...' % self._nickname)

class Cat(Pet):
    """猫"""
    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)

def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()
        

        


if __name__ == '__main__':
    main()