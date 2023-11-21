# # Функции

# # def sum(name):
# #     print(f"Привет {name}")
    
# # name_user = "nurbolot"
# # sum(name_user)

# # def hello():
# #     print("Hello world")

# # hello()

# def sum(num1,num2):
#     print(f"Результат: {num1+num2}")

# def subraction(num1,num2):
#     print(f"Результат: {num1-num2}")

# def divsion(num1,num2):
#     print(f"Результат: {num1/num2}")

# def multi(num1,num2):
#     print(f"Результат: {num1*num2}")


# def main():
#     while True:
#         num_1 = int(input("Введите первое число: "))
#         num_2 = int(input("Введите второе число: "))
#         a = input("1 - Сложение, 2 - Вычитание, 3 - Деление, 4 - Умножение: ")
#         # if a =="1":
#         #     sum(num_1,num_2)
#         # elif a=="2":
#         #     subraction(num_1,num_2)
#         # elif a =="3":
#         #     divsion(num_1,num_2)
#         # elif a =="4":
#         #     multi(num_1,num_2)

# main()

# a = input()

# float()
# int()

# def соунд():
#     print("Привет")
    
# соунд()


# def sound(title,animal_sound):
#     print(f"Я {title}. {animal_sound}")
    
# sound("Корова", "Муууу мумумуму")
# sound("Корова", "Муууу мумумуму")
# sound("Корова", "Муууу мумумуму")

# def users(*user):
#     for i in user:
#         print(f"Здравствуйте {i}")

# users("Nurbolot","Geeks","Aigerim", "Bishkek", "GO", "Cosmos")



# def users(**data):
#     for  key, value in data.items():
#         print(f"{key}: {value}")

# users(name = "Alina", age = "18", city = "Osh", language = "English")

# def math(*nums):
#     print(f"Среднее арифметическое число: {sum(nums) / len(nums)}")
    
# math(545,4325,4323,5532,45435,43,1,432,52,4,31,42,2,3222)

#Создайте функцию под названием summ и принимает 10 чисел с помощью args , функция выводит сумму чисел сделайте с помощью функции sum

#Создайте функцию под названием summ1 и принимает 10 чисел с помощью args , функция выводит сумму чисел сделайте с помощью цикла

#Создайте функцию под названием lend и принимает  числа с помощью args , функция выводит длину чисел 

#Создайте функцию под названием min и принимает 10 чисел с помощью args , функция выводит минимальное число и так же максимальное 

def numbers(*nums):
    n = 0
    for i in nums:
        n+=i
    print(f"Сумма: {n}")
numbers(545,434,324,3453,565,4654,3523,423,423,534)