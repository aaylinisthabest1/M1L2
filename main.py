import random

# Символы
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# длина пароля
password_length = int(input("Введите длину пароля: "))

# Переменная пороля
generated_password = ""

# Выходит пароль
for _ in range(password_length):
    generated_password += random.choice(symbols)

# Вывод на консоль
print("Сгенерированный пароль:", generated_password)
