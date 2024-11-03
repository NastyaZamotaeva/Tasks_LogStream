#Создайте функцию, которая принимает аргументы «текст» 
#и «имя файла». Функция должна записать в файл 
#(если файла не существует, то создать его) 
#текст с новой строки. 
# Выведите информацию из четных строк файла.

def work_File(text, name_file):
    with open('text.txt',"a+", encoding="utf-8") as file:
        file.write(text + '\n')

    with  open('text.txt', 'r', encoding="utf-8") as file:
        lines = file.readlines()  
        for index, line in enumerate(lines):
         if index % 2 == 0:  
            print(line)  

text = input("Введите текст:")
name_file = "text.txt"
work_File(text,name_file)
    