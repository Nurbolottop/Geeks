import sqlite3

connect = sqlite3.connect("users.db")
cursor  = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS clients(
    name VARCHAR(255),
    surname VARCHAR(255),
    age INTEGER,
    email VARCHAR(255),
    password VARCHAR(255)
    )''')
import random

class RegisterUsers:
    def game(self):
        n = 0
        limit = 5
        while True:
            randon = random.randint(1,5)
            user = int(input("Введите число: "))
            if limit !=0:
                if n !=5:
                    if user==randon:
                        n+=1
                        print(f"Вы угадали, Бот выбрал: {randon}. Выигрыш: {n}. Количество попыток: {limit}")
                    else: 
                        limit -= 1
                        print(f"Вы не угадали, Бот выбрал: {randon}. Выигрыш: {n}. Количество попыток: {limit}")
                else:
                    print(f"Вы выиграли, у вас 5 баллов!!! Выигрыш: {n}. Количество попыток: {limit}")
                    break
            else:
                print(f"Вы проиграли, у вас закончились попытки!!! Выигрыш: {n}. Количество попыток: {limit}")
                break
                
                
    def register(self, name,surname,age,email,pasword,pasword_confirm):
        if pasword == pasword_confirm:
            cursor.execute(f"""INSERT INTO clients(name,surname,age,email,password) VALUES('{name}','{surname}','{age}','{email}','{pasword}') """)
            connect.commit()
            print(f"Уважаемый {name} {surname}, вы успешно прошли регистрацию ")
            print("")
            self.game()
        else:
            print(f"Уважаемый {name} {surname}, вы не прошли регистрацию. Пароли не совподают")
    
    def  main(self):
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        age = int(input("Введите возраст: "))
        email = input("Введите почту: ")
        password = input("Введите пароль: ")
        password_confirm = input("Потвердите  пароль: ")
        if age <18:
            print("Регистрация не прошла, вам нет 18 лет!!!")
        else:
            self.register(name,surname,age,email, pasword=password, pasword_confirm=password_confirm)
registerusers = RegisterUsers()
registerusers.main()