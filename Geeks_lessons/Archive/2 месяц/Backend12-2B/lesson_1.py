# class Geeks:
#     name = "Natasha"
#     def my_method(self):
#         print("Привет, это мой метод!!")
        
#     def hello_method(self):
#         print(f"Я {self.name}, я поняля что это твой метод")
# geeks = Geeks()
# geeks.my_method()
# geeks.hello_method()

# class User:
#     def __init__(self, name, surname, age, phone):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.phone = phone
        
#     def info_user(self):
#         print(f"Имя: {self.name}, Фамилия: {self.surname}, Возраст: {self.age}")
    
#     def contact(self):
#         print(f"Имя: {self.name}, Фамилия: {self.surname}, Телефонный номер: {self.phone}")
        
    
# user = User("Nurbolot", "Erk1nbaew", 17, "058495845748")
# user.info_user()
# user.contact()


class Car:
    def __init__(self, brand,model,year,type_fuel):
        self.brand = brand
        self.model = model
        self.year = year
        self.type_fuel = type_fuel
        
    def info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год: {self.year}, Топливо: {self.type_fuel}")
        
    def cars(self):
        print("Машина завелась")
        n = float(0)
        while True:
            n += 0.5
            if n ==20:
                print("Вы проехали 20 км.")
            elif n == 50:
                print("Вы проехали 50 км.")
            elif n ==80:
                print("Вы проехали 80 км.")
                print("У вас осталось мало топлива")
            elif n ==100:
                print("Вы проехали 100 км. ")
                print("Машина остановлена, не осталось тооплива ")
                break
                
car = Car("Tayota", "Camry 75", "2022", "Бензин")
car.info()
car.cars()