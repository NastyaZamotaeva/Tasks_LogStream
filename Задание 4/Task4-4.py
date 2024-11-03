#Создайте для функции из задания №2 декоратор, 
#который будет выводить информацию о том, 
#что функция была вызвана с такими-то позиционными
#и именованными аргументами (*args, **kwargs), а также ее имя.

def decorator_Fibonacci(func):
    def Fibon(*args, **kwargs):
        print(f"Функция '{func.__name__}' вызвана с позиционными аргументами: {args} и именованными аргументами: {kwargs}")
        result = func(*args, **kwargs) 
        return result
    return Fibon

@decorator_Fibonacci
def Fibonacci(x):
    a = 1
    b = 1
    for i in range(x):
        yield a
        a_temp = a
        a = b
        b = a_temp + b

x = int(input("Введите кол-во чисел Фиббоначи: "))
digit = Fibonacci(x) 
print(list(digit))
