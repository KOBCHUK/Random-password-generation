
import random

# запрос параметров пароля
length = int(input("Введите длину пароля: "))
use_digits = input("Включать ли цифры? (да/нет): ").lower() == "да"
use_uppercase = input("Включать ли заглавные буквы? (да/нет): ").lower() == "да"
use_lowercase = input("Включать ли строчные буквы? (да/нет): ").lower() == "да"
use_symbols = input("Включать ли специальные символы? (да/нет): ").lower() == "да"

# создание списка возможных символов
symbols = ""
if use_digits:
    symbols += "0123456789"
if use_uppercase:
    symbols += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if use_lowercase:
    symbols += "abcdefghijklmnopqrstuvwxyz"
if use_symbols:
    symbols += "!#$%&()*+,-./:;<=>?@[\\]^_`{|}~"

# генерация пароля
password = "".join(random.choice(symbols) for i in range(length))

# вывод пароля на экран
print(password)