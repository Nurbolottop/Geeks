# print(1 + 1.00 )

# int num = 2  Без пробела
#$num = 2 

# num = float(2)
# x = 11  
# y = 12  
# print(y + 12 + x)

# print(int(1.99999))

# Dict - Словарь

# student = {'name':'Geeks', 'age':2}
# # print(student)
# # print(student['age'])
# # print(f"Привет, меня зовут {student['name']}. Мне {student['age']} года.")
# student['surname'] = 'Osh'
# print(student)
# keys = student.keys()
# print(keys)
# items = student.items()
# print(items)
# values = student.values()
# print(values)

# while True:
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#     print(f"Результат после сложения: {num1+num2}")
#     print(f"Результат после вычитания: {num1-num2}")
#     print(f"Результат после умножения: {num1*num2}")
#     print(f"Результат после деления: {num1/num2}")
    

# n =0
# while True:
#     n +=100
#     print(n)


# 1) Сделайте игру Камень, Ножницы, Бумага .Добавьте туда цикл while, также у пользователя должно быть 5 попыток и каждый раз вы должны отнимать попытки по 1. Если попытки закончятся цикл должен остоновится и программа должна вывести  текст <<Игра окончена, у вас осталось 0 попыток>>

import random 

user_health = 5
bot_health =5 
while True:
    if user_health ==0 or bot_health ==0:
        break
    else:
        bot = random.choice(["Камень", "Ножницы", "Бумага"])
        user = input("Введите выбор:")
        if user =="Камень":
            if bot =="Камень":
                print(f"Ничья.У вас: {user_health}, у бота: {bot_health}")
            elif bot =="Ножницы":
                bot_health-=1
                print(f"Вы выиграли.У вас: {user_health}, у бота: {bot_health}")
            elif bot =="Бумага":
                user_health -=1
                print(f"Вы проиграли.У вас: {user_health}, у бота: {bot_health}")
        elif user =="Ножницы":
            if bot =="Камень":
                user_health -=1
                print(f"Вы проиграли.У вас: {user_health}, у бота: {bot_health}")
                
            elif bot =="Ножницы":
                print(f"Ничья.У вас: {user_health}, у бота: {bot_health}")
            elif bot =="Бумага":
                bot_health-=1
                print(f"Вы выиграли.У вас: {user_health}, у бота: {bot_health}")
                
                
        elif user =="Бумага":
            if bot =="Камень":
                bot_health-=1
                print(f"Вы выиграли.У вас: {user_health}, у бота: {bot_health}")
            elif bot =="Ножницы":
                user_health -=1
                print(f"Вы проиграли.У вас: {user_health}, у бота: {bot_health}")
            elif bot =="Бумага":
                print("Ничья")
        else:
            print("Неверный вариант")