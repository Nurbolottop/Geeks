# numbers = [1,2,3,4,5]
# result = list(map(lambda num: num*2,numbers))
# print(result)


# numbers = [1,2,3,4,5]
# def result(numbers):
#     result_numbers = []
#     for num in numbers:
#         result_numbers.append(num *2)
#     return result_numbers
# print(result(numbers))

# def reverse(numbers):
#     print(numbers[::-1])

# numbers = [2,3,4,5,6,7,8,5,9,0,2]
# reverse(numbers)

# reversed = list(map(lambda x:x[::-1], [[1,2,3,4,5,6,7,8]]))
# print(reversed)


summ = lambda num1,num2: num1 *num2
print(summ(2,4))

# # def summ(num1,num2):
# #     print(num1+num2)

["Geeks", "Beksultan"]
 
# "Geeks"  5 букв

names = ["Mergul", "Beksultan", "Islam", "Vlad"]
# result = list(map(lambda num: f"{num} - {len(num)} букв", names ))
# print(f"Результат: {result}")
# for num in names:
#     print(num)
# name = "Kemran"
# print(len(name))
# M, B, I, V
# MERGUL, BEKSULTAN, ISLAM, VLAD  .upper()
# def result(names):
#     result_names = []
#     for num in names:
#         result_names.append(f"{num} - {len(num)} букв")
#     return(result_names)
# print(result(names))

# result = list(map(lambda x: x[0], names))
# print(result)

# result = list(map(lambda x: x.upper(), names))
# print(result)

# try except
# n = 0
# n2 = 2
# print(n2/n)


# try:
#     n = 0
#     n2 = 2
#     print(n2/n)
# except ZeroDivisionError:
#     print("На ноль делить нельзя, иди учи математику!!!")

# while True:
#     try:
#         try:
#             num1 = int(input("Введите первое число: "))
#             num2 = int(input("Введите второе число: "))
#             print(num1/num2 )
#         except:
#             print("На ноль делить нельзя, иди учи математику!!!")
#     except :
#         print("Не пиши буквы, иди учи русский ")

try:
    num1 = 6
    num2 = "6"
    print(f"Результат: {num1+num2}")
except TypeError:  
    result_num2 = int(num2)
    result_num1 = int(num2)
    print(f"Результат: {result_num1+result_num2}")