#Создайте список из 5 машин и попробуйте добавить в список новую машину под индексом 3 и затем выведите результат, далее вы должны удалить элемент под индексом 5.

# car = ["Lexus", "BMW", "Porter", "Bugati", "Nissan"]
# print(car)
# # car.append("TIKO")
# car.insert(3,"TIKO")
# print(car)
# car.pop(5)
# print(car)

# # Пользователь вводит свой текущий балл в тесте. Напишите программу и передайте условия , в результате у вас должно выйти следующим образом:
# # Если балл больше 90 выведите на экран (Отлично, вы получили 5)
# # Если балл больше 80 выведите на экран (Хорошо, вы получили 4)
# # Если балл больше 70 выведите на экран (Не очень, вы получили 3)
# # Если балл больше 60 выведите на экран (Плохо, вы получили 2)

# # user = int(input("Введите свой балл: "))

# # if  user >=90:
# #     print("Отлично, Вы получили 5 !!!")
# # elif user >=80 and user <90:
# #     print("Хорошо, Вы получили 4 !!!")
# # elif user >=70 and user <80:
# #     print("Не очень, Вы получили 3 !!!")
# # elif user >=60 and user <70:
# #     print("Плохо, Вы получили 2 !!!")
# # else:
# #     print("Ужисс !!!")

# #У вас есть список из рандомных чисел
# numbers = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8,909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3]

# # Ваша задача:
# # Отсортировать список numbers в порядке возрастания и вывести его.
# # Используйте подходящий метод списка для сортировки и выведите отсортированный список.
# print(numbers)
# numbers.sort()
# print(numbers)
# print(numbers[::-1])


# Tuple - кортеж (Неизменяемый тип данных)
# name = (1,"one",1.6, [1,2,3,4], True)
# print(name)
# # print(type(name))
# # name.append("23")
# # print(name)
# print(name[1:3])

# name_list = list(name)
# name_list.append(5)
# name = tuple(name_list)
# print(name)

# name = ("name",)
# print(name)
# print(type(name))

# numbers = ("1","2","3","4","5")
# print(numbers)
# name = ["Geeks", "Osh", "Bishkek", "Kyrgyzstan"]
# # print(name[0])
# # print(name[1])
# # print(name[2])
# # print(name[3])

# for element in name:
#     print(element)
    
# print(1)

# for num in range(1,101):
#     print(num)
# name = 34376482
# for char in name:
#     print(char)