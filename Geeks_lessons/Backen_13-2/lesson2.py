# class Car:
#     def __init__(self, model, mark, year, price):
#         self.model = model
#         self.mark = mark
#         self.year = year
#         self.price = price
                
#     def info(self):
#         print(f"Машина: {self.model}. Марка: {self.mark} Год выпуска: {self.year}. Цена: {self.price}")
    
#     def start(self):
#         print("Машина завелась")
    
#     def go(self):
#         print("Машина начала поездку")
#         n = 0
#         while True:
#             n +=1
#             if  n ==20:
#                 print("Машина едет со скоростью 20 km/h")
#             elif n ==40:
#                 print("Машина едет со скоростью 40km/h")
#             elif n ==60:
#                 print("Машина едет со скоростью 60km/h")
#             elif n ==80:
#                 print("Машина едет со скоростью 80km/h")
#             elif n ==100:
#                 print("Машина едет со скоростью 100km/h")
#             elif n >=100:
#                 n-100
#                 print("Машина снижает скорость")
#                 break
#     def stop(self):
#         print("Машина остановилась ")
        
# car = Car("Mersedes", "GT", 2022, "1млн  сомов")
# car.info()
# car.start()
# car.go()
# car.stop()


# 1 - способ
# class Father:
#     father = "Geeks"
#     def info_father(self):
#         print("Я родитель Отец")

# class Son(Father):
#     son = "Osh"
#     def info_son(self):
#         print("Я дочерный класс ")
        
# son = Son()
# son.info_father()
# son.info_son()
# print(son.father)
# print(son.son)
    
# 2 - способ
# class Father:
#     father = "Geeks"
#     def info_father(self):
#         print("Я родитель Отец")

# class Son:
#     son = "Osh"
#     def info_son(self):
#         print("Я дочерный класс ")
        
# son = Son()
# son.info_son()
# son.info_father()
# print(son.son)

# father = Father()
# father.info_father()
# print(father.father)



class Animal:
    def info_animals(self):
        print("Я некое животное")
    
    
class Cat(Animal):
    def info_cat(self):
        print("Я кошка, мяу мяу")


cat  = Cat()
cat.info_animals()
cat.info_cat()

# Создайте Родительский класс Car у которого будт метод info_car() который будет выводить информацию про машину

# Так же создайте Дочерный класс Start у которого будет метод start_car и он должен запускать вашу машину, и так же должен останавливать машину.

# Так же создайте эксемпляр для класса Start и через дочерный класс вызовите метод info_car
 