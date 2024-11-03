#1)Создайте список квадратов первых 10 натуральных чисел, 
#используя list comprehensions.
#2)Создайте словарь, содержащий названия дней недели 
#и их порядковые номера, используя dict comprehension. 
#Для дней недели можно использовать список ["Понедельник", "Вторник" и т.д.]
#3)Создайте множество, содержащее теги библиотек в нижнем регистре,
#  используя list comprehension. Исходный список ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]

def list_comprehensions(num):
    list_comprehensions = []
    for i in range(num):
        list_comprehensions.append(i**2)
    return list_comprehensions

print(list_comprehensions(10))

def dict_comprehension():
    list_call_days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресение"]
    dict_comprehension = {}
    for i in range(len(list_call_days)):
        dict_comprehension[list_call_days[i]] = i+1
    return dict_comprehension

print(dict_comprehension())

def set_comprehension():
    list_comprehension = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
    set_comprehension = {i.lower() for i in list_comprehension}  
    return set_comprehension

print(set_comprehension())