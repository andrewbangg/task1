num = input("Введите число: ")
while not num.isdigit():
    num = input("Ошибка. Введите число: ")
num = int();
c = 2
b = True
while b and c <= num // 2:
    b = num % c != 0
    c += 1
    print(c)
if b:
    print("Простое число")
else:
    print("Не простое число")


