import sqlite3

connect = sqlite3.connect('bank.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS clients(
    name VARCHAR(255),
    surname VARCHAR(255),
    age INTEGER,
    balance  INTEGER,
    wallet_id VARCHAR(12),
    email VARCHAR(255)
    )""")

class Bank:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None
        self.balance = 0
        self.wallet_id = None
        self.email = None
    
    def register(self,name,surname,age,email):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        cursor = connect.cursor()
        cursor.execute(f"""INSERT INTO clients(name,surname,age,balance,wallet_id,email) VALUES ('{name}',  '{surname}', {age}, 0, "hehehe8989", '{email}')""")
        connect.commit()
        print(f"Уважаемый {self.name} {surname}, Вы успешно создали счет в нашем Банке Nurbobo")
        
    def deposit(self, amount):
        cursor = connect.cursor()
        cursor.execute(f"UPDATE clients SET balance = balance + {amount} WHERE email = '{self.email}'")
        connect.commit()
        self.balance += amount
        print(f"Вы успешно пополнили баланс на сумму: {amount}. Ваш счет: {self.balance}")
    
    def money(self, amount):
        cursor = connect.cursor()
        cursor.execute(f"UPDATE clients SET balance = balance - {amount} WHERE email = '{self.email}'")
        connect.commit()
        self.balance -= amount
        print(f"Вы успешно Вывели деньги из баланса в сумме: {amount}. Ваш счет: {self.balance}")
        
    def main(self):
        while True:
            command = input("1 - регистрация, 2 - информация, 3 - пополнение баланса, 4 - вывод баланса,5 - выход из аккаунта: ")
            if command =="1":
                name = input("Введите имя: ")
                surname = input("Введите фамилию: ")
                age = int(input("Введите возраст: "))
                email = input("Введите почта: ")
                self.register(name,surname,age,email)
            elif command =="3":
                amount = int(input("Введите сумму"))
                self.deposit(amount)
            elif command =="4":
                amount = int(input("Введите сумму"))
                self.money(amount)
                
    
bank = Bank()
bank.main()