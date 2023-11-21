# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def info_user(self):
#         print(f"Привет, меня зовут {self.name}, мне {self.age} лет.")
# person = Person("Geeks", 2)


# person.info_user()


# class Toys:
#     def play(self):
#         pass

# class Car(Toys):
#     def play(self):
#         return "Машина едет"
# class Doll(Toys):
    # def play(self):
#         return "Я играю!!!"
# class Ball(Toys):
#     def play(self):
#         return f"Я прыгаю"
    
# def play_toys(toy):
#     return toy.play()

# car = Car()
# doll = Doll()
# ball = Ball()

# print(play_toys(ball))
# print(play_toys(car))
# print(play_toys(doll))

# Создайте класс Animals(род класс) у него будет метод speak но не будет выполнять действия. Так же создайте класс Cow у которого так же будет метод speak() который будет выводить текст "Я корова, Муууу мууу муу".Так же создайте класс Cat у которого так же будет метод speak() который будет выводить текст "Я кошка, мяу мяу мяу". Так же создайте класс Dog у которого так же будет метод speak() который будет выводить текст "Я Собака, Гав гав гав". Дале создайте метод animal_sound() который будет выпуолнять все действия когда вы будете его вызывать.

class Person:
    def __init__(self, name, age):
        self.__name = name      # Приватное поле (Доступно только внутри класса)
        self.__age = age
        
        #Геттеры для получение значений приватных полей
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age   
    
    # Сеттеры для изменения значений приватных полей    
    def set_name(self, name):
        self.__name = name
    
    def set_age(self,age):
        self.__age =age 
            
person = Person("Geek", 2)
print(f"Имя: {person.get_name()}")
print(f"Возраст: {person.get_age()}")

person.set_name("Жакшылык")
person.set_age("14")

print(f"Имя: {person.get_name()}")
print(f"Возраст: {person.get_age()}")