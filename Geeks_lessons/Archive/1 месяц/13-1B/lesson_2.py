# Конкантенация
# "My" "names" "Nurbolot"

# print("My" +" " + "names" + " " + "Nurbolot")

# Индексы

name = "Kyrgyzstan"
       #01234567890
# print(name[0])
# print(name[1])
# print(name[2])

# print(f"{name[0]}{name[1]}{name[2]}")

# print(name[3:6])

#string = str

# name = "Name"  

# print(type(name))

# number = 100
# print(type(number))
# number = str(number)
# print(type(number))

# integer - int - целые числа

# number = 3232
# print(number+8)

# number = "3232"
# print(int(number)+8)

# float  - не целые числа

# name = 85.90
# print(name - 5)

# print(6/5)

# bool = True, False

# print(type(6>5))

# if - если, elif - если, else - иначе 


# a = 10
# b = 600
# c = 100

# if a >b and  a >c:
#     print(f"{a} больше {b} так же {c}")
# elif c > b and c > a:
#     print(f"{c} больше {b} так же {a}")
# else:
#     print(f"{b} больше {a} так же {c}")

number = int(input("Введите число: "))
if number >0:
    print(f"{number} положительное число!!!")
if number == 0:
    print(f"{number} равно нулю")
else:
    print(f"{number} отрицательное число!!!")