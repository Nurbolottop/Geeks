import sqlite3

connect = sqlite3.connect("bank.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS cliens(
    id INTEGER PRIMARY KEY,
    name  VARCHAR(255),
    surname VARCHAR(255),
    age INTEGER,
    balance INTEGER,
    wallet_id VARCHAR(20),
    emal VARCHAR(255)
    );
    """)

class Bank:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None 
        self.balance = 0
        self.wallet_id = None
        self.email = None
    
    def register(self, name,surname,age,email):
        self.name = name
        self.surname = surname
        self.age = age 
        self.email = email
        cursor.execute(f"INSERT INTO cliens (name,surname,age,balance,wallet_id,emal) VALUES ('{name}','{surname}',{age}, 0, 7583782, '{self.email}');")
        connect.commit()
        
    def deposit(self,amount):
        cursor.execute(f"UPDATE cliens SET balance = balance + {amount} WHERE emal = '{self.email}'")
        connect.commit()
        self.balance +=amount
        
    def minus(self, amount):
        cursor.execute(f"UPDATE cliens SET balance = balance - {amount} WHERE emal = '{self.email}'")
        connect.commit()
        self.balance -=amount
    def get_balance(self):
        print(f"Баланс на счете {self.name} {self.surname}: {self.balance} сом ")
        
    def main(self):
        while True:
            command = input("1 - регистрация, 2 - информация, 3 - пополнить, 4 - вывести, 5 - выйти: ")
            if command =="1":
                name = input("Введите имя: ")
                surname = input("Введите фамилию: ")
                age = int(input("Возраст: "))
                email = input("Почту: ")
                self.register(name,surname,age,email)
            elif command == "2":
                self.get_balance()
            elif command =="3":
                if self.email:
                    amount = int(input("Введите сумму: "))
                    self.deposit(amount)
                else: 
                    print("Пройдите регистрацию!")
            elif command =="4":
                if self.email:
                    amount = int(input("Введите сумму: "))
                    self.minus(amount)
                else: 
                    print("Пройдите регистрацию!")
            elif command == "5":
                break
bank =Bank()
bank.main()