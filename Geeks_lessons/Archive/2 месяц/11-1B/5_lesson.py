import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS users(
#     id  INTEGER PRIMARY KEY,ik
#     first_name TEXT,
#     last_name TEXT,
#     age INTEGER
#     )''')
# first_name = input("Введите имя")
# last_name = input("Введите фамилию: ")
# age = input("Введите Возраст")

# cursor.execute(f"INSERT INTO users(first_name, last_name, age) VALUES ('{first_name}','{last_name}', {age})")
    
# connect.commit()

# connect.close()



cursor.execute("""SELECT * FROM users""")

data = cursor.fetchall()

for result in data:
    print(f"ID: {result[0]}")
    print(f"First name: {result[1]}")
    print(f"Last name: {result[2]}")
    print(f"Age: {result[3]}")
    print(result)
    

cursor.close