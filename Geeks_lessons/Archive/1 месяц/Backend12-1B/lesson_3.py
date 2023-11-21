# name = "Kyrgyzstan"
#        #0123456789
# print(name[0:6])

name_list = ["Nurbolot","Nurai","Omonboi", "Erbol", "Yryskeldi"]
            # 0           1        2         3          4
# print(name_list)
# print(name_list[0])
# print(name_list[1:4])

# print(type(name_list))

# name_list.append("Geeks")
# print(name_list)

# name = ["Beksultan", "Ulan"]
# name_list.extend(name)
# print(name_list)

# name_list.insert(0,"Geeks")
# print(name_list)

# name_list.pop(6)
# print(name_list)

# print(name_list.index("Omonboi"))

# name_list.remove("Ulan")
# print(name_list)

# num1 = 20
# num2 = 100
# # if, elif,else

# if num1 > num2:
#     print(num1)
# else:
#     print(num2)

# num1  = int(input("Введи число: "))
# if num1 % 2 ==0:
#     print("Число четное")
# else:
#     print("Не четное")

age = int(input("Введите возраст: "))

if age <12:
    print("Ты ребенок!!!")
elif age >12 and age <18:
    print("Вы подросток")
elif age >=18 and age <30:
    print("Вы мужик/женщина")
else:
    print("Вы старый ")
    
