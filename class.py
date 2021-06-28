'''
date: 2021/06/28
author: Joe
'''

# 建立類別 <每個類別(class)都會有自己的屬性(attribute)與方法(method)>
class Person:
    # attribute 屬性
    name = 'Joe'
    age = 36
    # method 方法
    def greet(self):
        print('Hi, my name is ' + self.name)

# 建立物件 (Object)
p1 = Person()

# 調用方法
p1.greet()  # Hi, my name is Joe


# 修改 Object Properties
p1.name = "Allen"

p1.greet()  # Hi, my name is Allen

# ======================================================
class Person:
    def __init__(self):  # 初始化
        self.name = 'Joe'
    def greet(self):
        print(('Hi, my name is ' + self.name))

p1 = Person()
p1.greet() # Hi, my name is Joe

# ======================================================
class Person:
    def __init__(self, init_name):
        self.name = init_name
    def greet(self):
        print('Hi, my name is ' + self.name)

p1 = Person('Ken')
p1.greet() # Hi, my name is Ken

# ======================================================
# 繼承和多態
class Animal():
    def __init__(self, name):
        self.name = name
    def greet(self):
        print('Hello, I am an %s.' % self.name)

# class Dog():
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         print('WangWang.., I am %s.' % self.name)

# 繼承
class Dog(Animal):
    def greet(self):
        print('WangWang.., I am %s.' % self.name)

animal = Animal('Cat')
animal.greet() # Hello, I am an Cat.

dog = Dog('Dog')
dog.greet()  # WangWang.., I am Dog.

class Dog(Animal):
    def greet(self):
        print('WangWang.., I am %s.' % self.name)
    def run(self):
        print('I am running!')

dog = Dog('Dog')
dog.greet()  # WangWang.., I am Dog.
dog.run()  # I am running!

# =======================================================
# 多態 (Polymorphism)
class Animal():
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f'Hello, I am {self.name}.')

class Dog(Animal):
    def greet(self):
        print(f'WangWang.., I am {self.name}.')

class Cat(Animal):
    def greet(self):
        print(f'MiaoMiao.., I am {self.name}.')

def hello(animal):
    animal.greet()

dog = Dog('dog')
hello(dog) # WangWang.., I am dog.
cat = Cat('cat')
hello(cat) # MiaoMiao.., I am cat.

# ======================================================