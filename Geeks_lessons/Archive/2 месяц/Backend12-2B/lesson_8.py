# id, first_name, last_name, phone, devop, mounth, age
import sqlite3

connect = sqlite3.connect("students.db")
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students_data(
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone VARCHAR(255),
    devop VARCHAR(255),
    mounth INTEGER,
    age INTEGER
    )''')

class Data:
    def add_data(self):
        while True:
            first_name = input("Введите имя: ")
            last_name = input("Введите Фамилию: ")
            phone = input("Введите номер: ")
            devop = input("Введите направление: ")
            mounth = int(input("Введите месяц обучения: "))
            age = int(input("Введите возраст: "))
            cursor.execute(f''' INSERT INTO students_data(first_name,last_name,phone,devop, mounth,age) VALUES("{first_name}","{last_name}","{phone}","{devop}",{mounth}, {age})''')
            connect.commit()
            
data = Data()
data.add_data()