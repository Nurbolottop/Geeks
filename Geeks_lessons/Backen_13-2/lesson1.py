# class Geeks:
#     name  =  "Geeks"
# geeks = Geeks()
# print(geeks.name)


# class User:
#     def hello_method(self):
#         return "Привет Наташа"
#         # print("Привет Наташа")
        
# user = User()     
# print(user.hello_method())
        
def info(name,surname):
    print(f"Привет {name} {surname}")
info("Geeks", "Osh")
        
# class Students:
#     def __init__(self,name,username,age):
#         self.name = name
#         self.username = username
#         self.age = age
#         print(f"Привет {self.name}")
        
#     def info(self):
#         print(f"Книга {self.title} Автор: {self.autor}")  
              
# students = Students("Geeks", "Osh", 18)
# students.info()

# Создайте класс Book. В классе Book должны быть 2 атрибута(атрибуты должны приниматся с помощью конструктора) 1) title, 2) autor
# Так же создайте метод info который будет выводить информацию про книгу
# Пример: "Книга: Гарри поттер, Автор: Джоан Роулинг"


# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
#     def info(self):
#         print(f"Книга: {self.title}, Автор: {self.author}")

# book = Book()
# book.main()

            
class Calculator:
    def add(self,num1,num2):
        print(f"Результат: {num1+num2}")
        
    def main(self):
        while True:
            num1 = int(input("Введите число: "))
            num2 = int(input("Введите число: "))
            a = input("Выберите - 1 Сложение, 2 Вычитание, 3 Умножение, 4 Деление: ")
            if a =="1":
                self.add(num1,num2)
            elif a =="2":
                self.subtract(num1,num2)
            elif a =="3":
                self.multiply(num1,num2)
            elif a =="4":
                self.divide(num1,num2)
            else:
                print("Такого выбора нет!!")
            