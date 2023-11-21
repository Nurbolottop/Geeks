# class Animals:
#     def __init__(self, name):
#         self.name = name
        
# class Dog(Animals):
#     def sound(self):
#         return "Гаф-Гаф-Гаф!!!"

# dog = Dog("Бульдок")
# dog.sound()
# # Бульдок: Гаф-Гаф
# print(f"{dog.name}: {dog.sound()}")

# Магический метод 

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def __str__(self):
#         return f"Круг с радиусом: {self.radius}"
    
# circle = Circle(8)
# print(str(circle))


# Инкапцуляция

# class User:
#     name = "Nurbolot"  # публичный атрибут
    
# user = User()
# print(user.name)

# Защищенный доступ  

# class Auto:
#     def __init__(self, mark, year):
#         self.mark = mark
#         self._year = year   # защищенный атрибут
        
# auto = Auto("Toyota", 2020)
# print(auto.mark)
# print(auto._year)

# Защищенный доступ  

# class Animals:
#     def __init__(self, name):
#         self.name = name
    
#     def _cat(self):
#         return f"Я кот, меня зовут: {self.name}"
    
# animals = Animals("Мурка")
# print(animals._cat())

# class MyClass:
#     def __init__(self):
#         self.__private_age = 20
        
# myclass = MyClass()
# print(myclass.__private_age)


class Car:
    def __init__(self, model, year):
        self.__model = model
        self.__year = year
        
    def __info(self):
        return f"Модель: {self.__model}, Год: {self.__year}"
    
    def set_year(self, new_year):
        self.__year =new_year
        
    def get_info(self):
        message = self.__info()
        return message
    
car = Car("BMW", 2023)
print(car.get_info())
car.set_year(2022)
print(car.get_info())
