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

from math import sqrt

class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a 
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b
    def perimeter(self):
        return self._a + self._b + self._c
    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * )

if __name__ == '__main__':
    main()