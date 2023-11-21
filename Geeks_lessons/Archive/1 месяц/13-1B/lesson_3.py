# listter = [1,2,3,4,5,6,7,8,9,10]
# print(type(listter))
# print(listter)

# users = ['Geeks', 5454, "Anton", "Nurbolot"]
# print(users[2])

# type_data = [5, "Пять", 5.5, True, [1,2,3,4,5]]
# print(type_data)

# users = ['Geeks', "Osh", "Anton", "Nurbolot"]
# user = ["Islam", "Anton"]
# print(users)
# users.append("Beksultan")    # Для добавления в конец списка
# print(users)
# users.insert(0, "Kyrgyzstan")   # Для добавления по индексу
# print(users)
# users.insert(3, "Islam")

# print(users)
# users.remove("Anton")      # Для удаления из списка 
# print(users)
# users.pop(1)        # Для удаления с индексом
# print(users)
# users.pop(2)        # Для удаления с индексом
# print(users)
# users.extend(user)   # Для объеденения двух списков
# print(users)
# # print(users.index("Nurbolot"))   # Что бы узнать индекс элемента
# # print(users.count("Nurbolot"))   # Что бы узнать количество элементов в списке
# users.pop(2)
# print(users)
# users.reverse()   # Что бы перевернуть список
# print(users)
# users.sort()     # Что бы сделать сортировку
# print(users)
# users.clear()   # Что бы очистить список
# print(users)


# name = input("Введите имя: ")
# age = int(input("Введите возраст: "))
# users = []
# if age >=18:
#     users.append(name)
#     print(users)
# else:
#     print("Доступ запрещен")


auto = ["Mersedes", "BMW", "TAYOTA", "Chevrale","Supra", "Nissan", "KIA", "Hyundai", "Tiko"]
name = input("Введите имя: ")
car = input("Введите название машины: ")
if car in auto:
    print(f"Уважаемый {name}, Ваш выбор у нас есть  в наличии. Ваш выбор: {car}")
else:
    print(f"Уважаемый {name}, Ваш выбор  у нас нет  в наличии. Ваш выбор: {car}")

