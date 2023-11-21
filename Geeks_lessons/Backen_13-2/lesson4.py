# class User:
#     name = "Geeks"
#     age = "Geeks"   #Публичный атрибут 
#     _phone = "0558999999"   #Защишенный атрибут
# user = User()
# print(user._phone)


# class Car:
#     def __init__(self,model,year):
#         self.__model = model
#         self.__year = year
        
#     def __info(self):
#         return f"Модель: {self.__model}, Год {self.__year}"
    
#     def set_year(self,new_model):
#         self.__model = new_model
        
#     def info_getter(self):
#         geeks = self.__info()
#         return geeks
        
# car = Car("BMW", 2022)
# # print(car.__model)
# # print(car.__info())
# car.set_year("Camry")
# print(car.info_getter())
# # print(car.__model)

# class Animals:
#     def make_sound(self):
#         pass 

# class Dog(Animals):
#     def make_sound(self):
#         return "Гаф гаф"

# class Cat(Animals):
#     def make_sound(self):
#         return "Мяу мяу"

# def animal_sound(geeks):
#     return geeks.make_sound()

# dog = Dog()
# cat = Cat()
# print(animal_sound(dog))


class Toys:
    def play(self):
        pass 
class Car(Toys):
    def play(self):
        return "Машина едет"
    
class Doll(Toys):
    def play(self):
        return "Кукла играет"
    
class Ball(Toys):
    def play(self):
        return "Мяч прыгает"
    
def play_toys(toy):
    return toy.play()

car = Car()
doll = Doll()
ball = Ball()
print(play_toys(doll))