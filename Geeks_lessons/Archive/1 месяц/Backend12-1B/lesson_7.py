# num1 = 9
# num2 = 0

# print(num1/num2)

# Исключения - try, except
# try:
#     num1 = 10
#     num2 = 0
#     print(num1/num2)
# except ZeroDivisionError:
#     print("На ноль делить нельзя, иди учись!!!")
# while True:
#     try:
#         num1 = int(input("Введите первое число: "))
#         num2 = int(input("Введите второе число: "))
#         print(f"Результат после сложения: {num1+num2}")
#         print(f"Результат после вычитания: {num1-num2}")
#         print(f"Результат после умнежение: {num1*num2}")
#         try:
#             print(f"Результат после деления: {num1/num2}")
#         except:
#             print("Ты чо, на ноль делить нельзяяя !!!")
#     except ValueError:
#         print("Введите только числа!!!")
# try:
#     print(fkdjfkdjk)
# except:
#     print("Не правильная команда")


# Множества set, fronzenset
#List = []
#tuple = ()
#dict = {}

# set = {}

# Создается с фигурными скобками 
# Не имеет структуры или определенного порядка
# Не можем использовать индекс и срезы
# Не имеет дубликатов имеет уникальные элементы(данные)
# Set изменяемый тип данных
# frosenset неизменяемый тип данных

# dicti = {"name": "Amina"}
# num = {"Amin", "Nurgeldi", "Nurbek", "Aibek", "Kyzbek"}
# # print(type(dicti))
# # print(type(num))
# print(num)
# print(num[1])

# users = {"Amin", "Nurgeldi", "Nurbek", "Aibek", "Kyzbek","Amin"}
# print(users)

# num = [23,432,443,54,5654,765,765,65,24,12,1,1,1,2,23,23,2,32,1,2,1,23,2,325,24342,3,4,5,435,344,13,124,45,4,556,45,434,633]
# print(num)
# duble_num = set(num)
# num = list(duble_num)
# print(num)

# try: 
#     users = {"Amin", "Nurgeldi", "Nurbek", "Aibek", "Kyzbek","Amin"}
#     print(users[1:5])
# except:
#     print("set() не может использовать индексы и срезы")

# users = {"Amin", 1 ,"Nurgeldi", "Nurbek", "Aibek", "Kyzbek","Amin"}
# print(users)
# users.add("Yryskeldi")
# print(users)
# users.add("Nurbek")
# print(users)
# users.add("1")
# print(users)

users_set = {"Amin", 1 ,"Nurgeldi", "Nurbek", "Aibek", "Kyzbek","Amin"}

users_frozenset = frozenset(["Amin", 1 ,"Nurgeldi", "Nurbek", "Aibek", "Kyzbek","Amin"])
print(users_set)
print(users_frozenset)
print(type(users_set))
print(type(users_frozenset))
