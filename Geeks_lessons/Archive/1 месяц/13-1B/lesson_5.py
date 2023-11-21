# users = ("Nurbolot", "Islambek", "Anton", "Beksultan")
# print(type(users))
# users = list(users)
# users.append("Geeks")
# users.remove("Islambek")
# print(users)
# users = tuple(users)
# print(users)

student = {'name': "Beksultan", 'age': 20,'from':"Kyrgyzstan"}
# dop_info = {"hobby":"Играть"}
# print(f"Имя: {student['name']}")
# print(f"Возраст: {student['age']}")
# print(f"Место жительства: {student['from']}")   

# print(student)
# student['job'] = "Developer"
# print(student)

# student['name'] = "Nurbolot"
# print(student)

# del student['from']
# print(student)

# student.update(dop_info)
# print(student)


# print(student.keys())
# print(student.values())
# print(student.items())
# student.pop("from")
# print(student)

# set , frozenset 
#Cоздается с помощью фигурных скобок
# Не имеет структуры и определенного порядка
# Не можем использовать индексы  и срезы
# Не имеет дубликатов
# set()  -  Изменяемый тип данных
# frozenset()  -  Не изменяемый тип данных

# users = {"Nurbolot","Beksultan", "Beksultan", "Islambek","Geeks","Geeks","Geeks","Geeks","Geeks","Geeks","Geeks","Geeks", "Geeks"}
# print(users)
# users.add("Anton")
# print(users)
# # print(users[1])  Не работает индексы

users = frozenset(["Nurbolot", "Vlad", "Georgiy", "Ilya"])
users.add()