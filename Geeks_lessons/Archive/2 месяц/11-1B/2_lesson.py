# class Book:
#     def  __init__(self, title, author):
#         self.title = title
#         self.authoor = author
        
#     def __str__(self):
#         return f"Книага: {self.title} - Автор: {self.authoor}"

# book = Book("Geeks", "nurbolot")
# print(str(book))

# class Animals:
#     def info_animals(self):
#         print("Я - некое животное")
        
# class Cat(Animals):
#     def info_cat(self):
#         print("Мяу - Мяу")
        
# cat = Cat()

# cat.info_animals()
# cat.info_cat()\
    
    
# class Father:
#     def info_father(self):
#         print("Я отец")

# class Mother:
#     def info_mother(self):
#         print("Я мама")
        
# class Daugther(Father,Mother):
#     def info(self):
#         print("Я дочь")
        
# daugther = Daugther()
# daugther.info()
# daugther.info_mother()
# daugther.info_father()


# У вас должен быть основной класс под названием Work. Так же дочерный классы Работник_1 и Работник_2 которые наследуются от основного класс. Внутри основного класса должен быть метод info который будет выводить информацию о рабое (график работы и что делает эта работа) и внутри дочерных классов должен  быть метод который будет выводить информацию о сотруднике(Имя,Возраст,должность)


class Work:
    def __init__(self,schedule,descriptions):
        self.schedule = schedule
        self.descriptions = descriptions
    
    def info(self):
        print(f"График работы: {self.schedule}")
        print(f"Описание работы: {self.descriptions}")
    
class Worker_1(Work):
    def __init__(self,schedule,descriptions,name,age,job_title):
        super().__init__(schedule,descriptions)
        self.name = name
        self.age = age
        self.job_title = job_title
    
    def info(self):
        super().info()
        print(f"Имя сотрудника: {self.name}")
        print(f"Возраст сотрудника: {self.age}")
        print(f"Должность сотрудника: {self.job_title}")

class Worker_2(Work):
    def __init__(self,schedule,descriptions,name,age,job_title):
        super().__init__(schedule,descriptions)
        self.name = name
        self.age = age
        self.job_title = job_title
    
    def info(self,worker_1):
        super().info()
        print(f"Имя сотрудника: {self.name}")
        print(f"Возраст сотрудника: {self.age}")
        print(f"Должность сотрудника: {self.job_title}")
        worker_1.info()


worker_1 = Worker_1("Пн-Пт с 09:00 - 22:00","ЗНАНИЯ С ГАРАНТИЕЙИЗУЧАЙТЕ","Nurbolot","17", "Уборщик")
worker_2 = Worker_2("9","Hello", 'Geeks', '2', "Обучение")
worker_2.info(worker_1)



# График работы: 9
# Описание работы: Hello
# Имя сотрудника: Geeks
# Возраст сотрудника: 2
# Должность сотрудника: Обучение
# График работы: Пн-Пт с 09:00 - 22:00
# Описание работы: ЗНАНИЯ С ГАРАНТИЕЙИЗУЧАЙТЕ
# Имя сотрудника: Nurbolot
# Возраст сотрудника: 17
# Должность сотрудника: Уборщик
