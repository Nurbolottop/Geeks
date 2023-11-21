# name = input("Введите имя: ")
# last_name = input("Введите фамилию: ")
# age=  int(input("Введите ваш возраст: "))

# import sqlite3
# connect = sqlite3.connect("users.db")
# cursor = connect.cursor()

# # cursor.execute('''CREATE TABLE IF NOT EXISTS nurbolot(
# #     id INTEGER PRIMARY KEY,
# #     first_name TEXT,
# #     last_name TEXT,
# #     age INTEGER
# #     )''')

# # cursor.execute(f'''INSERT INTO nurbolot(first_name, last_name, age) VALUES('{name}', '{last_name}',  {age})''')
# # connect.commit()
# # connect.close()

# cursor.execute('''SELECT * FROM nurbolot''')
# data = cursor.fetchall()

# for result in data:
#     print(f"Id: {result[0]}")
#     print(f"Имя: {result[1]}")
#     print(f"Фамилия: {result[2]}")
#     print(f"Возраст: {result[3]}")
    
    
    
import sqlite3

connect = sqlite3.connect('cars.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS cars(
    id INTEGER PRIMARY KEY,
    brand TEXT,
    model TEXT,
    color TEXT,
    type TEXT,
    year INTEGER
    )''')


while True:
    data_vub = input("1 - Добавить новую машину, 2 - Посмотреть машины,3 - выйти: ")
    if data_vub == "1":
        brand = input("Введите бренд машины: ")
        model = input("Введите модель машины: ")
        color = input("Введите цвет машины: ")
        type_d =  input("Введите тип двигателя: ")
        year = input("Введите год выпуска: ")
        cursor.execute(f"""INSERT INTO cars(brand,model,color,type,year) VALUES('{brand}','{model}','{color}','{type_d}',{year})""")
        connect.commit()
        print(f"Ваши данные успешно добавлены!!!")
    elif data_vub =="2":
        cursor.execute("""SELECT * FROM cars""")
        data = cursor.fetchall()
        for result in data:
            print(f"Номер {result[0]}.")
            print(f"Бренд: {result[1]}")
            print(f"Модель: {result[2]}")
            print(f"Цвет машины: {result[3]}")
            print(f"Тип двигателя: {result[4]}")
            print(f"Год выпуска: {result[5]}")
    elif data_vub =="3":
        print("Программа остановлена!!!")
        break
    else:
        print("Такой команды нет!!!")
        