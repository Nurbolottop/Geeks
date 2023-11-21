names = ["Mergul", "Erbol", "Yryskeldi", "Beishen", "Omonboi", "Nurai", "Bakai"]
with open("names.txt", 'w') as file_write:
    for i in names: 
        file_write.write(f"Имя: {i}. ")

with open("names.txt", 'r') as file_read:
    result = file_read.read()
    print(result)