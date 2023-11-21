# class Animal:
#     name = "Корова"

#     def make_sound(self, sound):
#         print(f"{self.name} издает звук {sound}")
        
# animal = Animal()
# animal.make_sound("Мууууу")


# class Calculator:
#     def add(self, num1,num2):
#         print(f"Результат: {num1+num2}")
#     def minus(self, num1, num2):
#         print(f"Результат: {num1 -num2}")
#     def multiply(self, num1,num2):
#         print(f"Результат: {num1*num2}")
#     def divide(self, num1,num2):
#         print(f"Результат: {num1/num2}")
    
# calculator = Calculator()

# calculator.add(5,6)
# calculator.divide(8,4)

# class Doll:
#     def __init__(self, color,size):
#         self.color = color
#         self.size = size
        
#     def info(self):
#         print(f"Кукла имеет цвет {self.color} и размер {self.size}.")
        
# doll = Doll("Черный", "Medium")
# doll.info()

# 1) Создайте класс Book.В классе Book должны быть 2 атрибута <<title>> и <<author>>. Эти атрибуты должны быть внутри конструктора.
# Создайте метод представиться, который будет выводить информацию о книге в формате "Книга [название], автор - [автор]."

# Создайте объект класса Книга с названием "Приключения Гарри Поттера" и автором "Джоан Роулинг".

# Вызовите метод представиться на созданном объекте и убедитесь, что выводится корректная информация о книге.

class Book:
    def __init__(self, title,author):
        self.title = title
        self.author = author
        
    def info(self):
        print(f"Книга: {self.title} автор: {self.author}")

book = Book("Приключения Гарри Поттера","Джоан Роулинг")
book.info()