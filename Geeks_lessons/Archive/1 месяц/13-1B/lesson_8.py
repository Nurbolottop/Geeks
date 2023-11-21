# file_write = open('geeks.txt', "w")
# file_write.write("Всем привет, меня зовут Ивангай, это прохождение майнкрафта")
# file_write.close()

# test = open('test.txt','w')
# test.write("this is test work!!!")
# test.close()

# while True:
#     for i in range(1,25):
#         hacking = open(f"haha{i}.txt", "w")
#         hacking.write("Вас взломали")

#Запросите у пользователя его имя, возраст и телефонный и попробуйте их сохранить в файле users.txt 

# name = input("Введите имя: ")
# age = int(input("Введите возраст: "))
# phone = input("Введите телефонный: ")
# file_write = open("users.txt", "w")
# file_write.write(f"Имя: {name}, Возраст: {age}, Телефонный номер: {phone}")
# file_write.close()

# file_read = open('users.txt', "r")
# result = file_read.read()
# print(result)

# test = open('test.txt','w')
# test.write("this is test work!!!")
# test.close()

# 2 способ

# users = ['Beksultan',"Muha", "Islam", "Anton"]

# # with open('user_list.txt', "w") as write_list:
# #     write_list.write(f"Пользователи: {users}")
    
# with open("user.txt", 'w') as user_list:
#     for i in users:
#         user_list.write(f"Пользователь: {i}.\n")

# with open('calculator.py', "w") as calc:
#     calc.write('''num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# print(f"Результат после сложения: {num1 + num2}")
# print(f"Результат после вычитание: {num1 - num2}")
# print(f"Результат после умножение: {num1 * num2}")
# print(f"Результат после деление: {num1 / num2}")
# ''')


# with open("text.txt", "r") as read_file:
#     result = read_file.read()
#     print(result)