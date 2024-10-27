#Напишите калькулятор, который будет осуществлять 6 операций: 
#сложение, вычитание, умножение, деление, 
#возведение в степень и выход из программы.
#Операции с числами выполните в функциях. 
#Обработайте ошибку деления на 0 и реализуйте проверку на входные данные.

def addition(x: float,y: float) -> float:
    return x+y

def subtraction(x: float,y: float) -> float:
    return x-y

def multiplication(x: float,y: float) -> float:
    return x*y

def division(x: float,y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Деление на ноль!")
    return x/y

def exponentiation(x:float,y:float)-> float:
    return x**y

def close(s: str)-> str:
    return "exit"

while True:
    try:
        inp_operation = int(input("Введите номер операции:\n1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление\n5 - возведение в степень\n6 - выход из калькулятора\n "))
        if (inp_operation == 6):
            print("exit")
            break
        x = float(input("Введите значение x "))
        y = float(input("Введите значение y "))

        if not isinstance(x,float) and not isinstance(y,float):
            raise ValueError("Wrong datatype") 

        if (inp_operation == 1):
            print(addition(x,y))
        elif (inp_operation == 2):
            print(subtraction(x,y))
        elif (inp_operation == 3):
            print(multiplication(x,y))
        elif (inp_operation == 4):
            print(division(x,y))
        elif (inp_operation == 5):
            print(exponentiation(x,y))
        else: 
            print("Не те операции")
    except ZeroDivisionError:
        print("Деление на ноль")
    except ValueError:
        print("Не тот тип данных")
          
    




