import random
import subprocess
import time
import os

max_density=0.01466 #задаем максимальное значение функции плотности вероятности полтергейста
path=os.path.join(os.getcwd(),"plst_1.exe") #указываем путь к программе для plst_1.exe



def probability_density(x,y):
    '''Функция предназанчена для генерации
    занчения функции полтергейста'''

    '''Записываем значения x,y в файл input.txt'''
    with open('input.txt','w') as file:
        file.write(f'{x} {y}')

    '''Запускаем файл plst_1.exe,который вернет значение функции'''
    try:
        os.system(path)
    except FileNotFoundError:
        print(f"Файл '{path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при запуске файла: {e}")

    '''Считываем значение полученной функции'''
    with open('plst_dstr.txt','r') as file:
        z=float(file.readline())

    return z





result=[]
while result==[]:
    '''генерируем случайные величины x,y'''
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    '''Пользуясь правилом Монте-карло генерируем точку,соответствующую
    заданной плотности вероятности, как только точка сгенерируется цикл закончится'''
    if probability_density(x, y) >= random.uniform(0, max_density):
        result.append([x,y])

'''Выводим сгенерированную точку'''
print(result)
