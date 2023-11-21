import  sqlite3    

# name = input("Введите имя: ")
# last_name = input("Введите фамилию: ")
# age = int(input("Введите возраст: "))
# print(f"Имя: {name}, Фамилия: {last_name}, возраст: {age}")

connect = sqlite3.connect("info.db")
cursor = connect.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS info_users(
#     id INTEGER PRIMARY KEY,
#     name VARCHAR(255),
#     last_name VARCHAR(255),
#     age INTEGER
#     ) ''')

# cursor.execute(f'''INSERT INTO info_users(name,last_name,age) VALUES('{name}','{last_name}',{age}) ''')
# connect.commit()
# connect.close()

cursor.execute(f'''SELECT  * FROM info_users''')
data = cursor.fetchall()

for result in data:
    print(f'ID: {result[0]}, Имя: {result[1]}, Фамилия: {result[2]}, Возраст: {result[3]}')
    


# 1) brand 2)model 3) color 4)year