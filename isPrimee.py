while True :    #Создаю цикл
    try:        #Блок исключения
        num = int(input("Введите число: "))
        print(num)
        if num == 0:
            print("Начните с цифры 1")
        elif num % 2 == 0:
            print("Не простое число")
        elif num % 2 == 1:
            print("Простое число")
    except:
        print("Это не число")



