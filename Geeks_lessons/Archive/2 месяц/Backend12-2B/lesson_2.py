# class User:
#     def __init__(self, name, email, phone):
#         print(name)
        
#     def info(self):
#         print(self.name)
        
        
# user = User("Нурболот", "email@gmail.com", "8943893")
# user.info()

# class User:
#     def __init__(self, name, email, phone):
#         self.name   = name 
#         self.email   = email
#         self.phone = phone
        
#     def info(self):
#         print(self.name)

# user = User("Нурболот", "email@gmail.com", "8943893")
# user.info()


# class Dad:
#     name = "Nurbolot"
#     def info_dad(self):
#         print("Я отец")
        
#     def info_dad(self):
#         print("Я отец")
        
#     def info_dad(self):
#         print("Я отец")
        
# class Son:
#     def info_son(self):
#         print("Я сын")
#         print(f"Привет {self.name}")
        
        
# son = Son()
# son.info_son()
# son.info_dad()


# Создайте Основной класс Dog  и так же создайте дочерный класс Cat который у нас будет наследоваться от основного класса.

# Внутри класса Dog:
    
#     Cоздайте метод speak_dog который будет выводить текст "ГАФ ГАФ"

# Внутри класса Cat:
    
#     Cоздайте метод spaek_cat который будет выводить текст "МИЯу МИЯу"
    
# И так же вызовите метод speak_dog с помощью класса Cat

# from mum import mother

# class Fatther:
#     def info_dad(self):
#         print("Я папа. Я родительский класс Father")
        
# class Son(Fatther, mother.Mother):
#     def info_son(self):
#         print("Я сын. Я дочерный класс Son, Я наследуюсь от класса Mother и Father")
        


# class SonSon(Son):
#     def info_sonson(self):
#         print("Я внук")
        
# sonson = SonSon()
# sonson.info_dad()
# sonson.info_mom()

# Создайте основной класс Phone и так же класс Camera. Затем создайте дочерный класс SmartPhone:

    # Внутри нашего основного класса Phone будет метод call, Который будет выводить текст  "Я звоню маме"
    
    # Внутири нашего основного класса Camera будет метод take_photo который будет выводить текст "Я фоткаю отца"
    
     #  Внутри нашего дочерного класса Smartphone будет метод alll который будет выводить текст " Я фоткаю и так же звоню"
     
# Вы должны создать эксемпляр класса для Smartphone и вызвать все три метода

class Dad:
    name = "Nurbolot"
    def car(self):
        print('Машина: BMW')
class Mom:
    name = "Aigul"
    def home(self):
        print('Дом')
class Son(Dad,Mom):
    def dont(self):
        print("Ничего нет")
        
        
son = Son()
son.car()
son.home()
print(son.name)