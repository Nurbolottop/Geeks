# # print(1.500 + 1.500)

# print(1+1.0)
# print(20//3)

# print("Hello world")

# def candy():
#     print("Hello world")

# candy()


# def result(num1,num2):
#     print(num1/num2)
    
# result(6)

import random

def game(num):
    ran = random.randint(1,5)
    if ran ==num:
        print(f"Вы выиграли. Бот выбрал: {ran}")
    else:
        print(f"Вы проиграли. Бот выбрал: {ran}")
        
def menu():
    while True:
        print("1 - Играть, 2 - узнать информацию")
        num = input("Введите свой выбор: ")
        if num =="1":
            num1 = int(input("Введите число от 1 до 5: "))
            game(num1)

def register(name,age, phone):
    if age >=18:
        print("Добро пожаловать в наш мир!! ")
        print(f"Имя: {name}, телефонный номер: {phone}, возраст: {age}")
        menu()
    else:
        print("Вам нет 18 лет")

# register("Nurbolot", 18, "5498549583")


