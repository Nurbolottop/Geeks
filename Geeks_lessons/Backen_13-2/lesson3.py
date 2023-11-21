# class  Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def __str__(self):
#             return (f"Фио: {self.name} Возраст: {self.age}  - Простой Магический")
        
#     def info_user(self):
#         print(f"Фио: {self.name} Возраст: {self.age}  - Простой метод")

# person = Person("Geeks",3)
# print(person)
# person.info_user()


# Множественное наследование

# class Mum:      #Родительский класс
#     home = "Дом" 
#     def add(sellf):
#         num1 = int(input("Введите первое число: "))
#         num2 = int(input("Введите второе число: "))
#         return f"Результат: {num1+num2}"
# class Dad:   #Родительский класс
#     car = "Машина"
    
# class Son(Mum,Dad):   # Дочерний класс
#     name = "Ничего" 

# son = Son()
# print(son.car)
# print(son.home)
# print(son.add())

# Создайте Основй класс Phone и так же класс Camera. Затем создайте дочерний класс SmartPhone:

    # Внутри вашего основного класса Phone будет метод call, Который будет выводить текст "Я звоню маме"

    # Внутри вашего основного класса Camera будет метод take_photo, Который будет выводить тектс "Я фоткаю отца"

    # Внутри вашего дочерного класса SmartPhone будет метод alll который будет выводить текст "Я фоткаю и так же звоню"

# Вы должны создать эксемпляр класса для SmartPhone и Вывовите все три метода

# class Home:
#     def info_home(self):
#         return "10-этажный  жилой комплекс "
    
# class Son_1(Home):
#     def info_son(self):
#         return "Привет Geeks"
    
# class Son_2(Home):
#     def info_son(self):
#         return "Привет Geeks"
    
    
# class Son_3(Home):
#     def info_son(self):
#         return "Привет Geeks"
    
# class Son_4(Home):
#     def info_son(self):
#         return "Привет Geeks"
# son_d = Son_4()
# print(son_d.info_home())
# son_3 = Son_3()
# print(son_3.info_home())

# class Grand:
#     def info_grand(self):
#         return "Я дедушка"
# class Dad(Grand):
#     def info_dad(self):
#             return "Я Отец"
# class Son(Dad):
#     def info_son(self):
#             return "Я Сын"

# son = Son()
# print(son.info_grand())

# dad = Dad()
# print(dad.info_grand())


class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass
        
class Dog(Animal):
    def __init__(self, name,color):
        super().__init__(name)
        self.color = color
        
    def  speak(self):
        return  f"{self.name} {self.color} издает звук Гаф гаф"
    
dog = Dog("Актош", "Серый")
print(dog.speak())