import numpy as np
import random
import matplotlib.pyplot as plt


max_density=0.01466 #максимальное значение функции из предыдущего шага
num_samples=10000 #количество точек,которые мы будем генерировать

'''Генерируем n-ое количество точек для построения их потом на графике
После их записи комментируем фрагемнт программы'''
# with open("input_2.txt", "w") as file:
#     for _ in range(num_samples):
#         x = random.uniform(-10, 10)
#         y = random.uniform(-10, 10)
#         file.write(f'{round(x, 3)} {round(y, 3)}\n')
'''Далее вызываем .exe файл для формирования файла plst_dstr.txt
Затем переименовываем файл на plstr_dstr_2.txt
input.txt на input_2.txt'''
data=[]
with open("input_2.txt", "r") as file:
    for i in range(num_samples):
        string=file.readline()
        words=string.split()
        x,y=float(words[0]),float(words[1])
        data.append([x,y])

'''Считываем значение функции в сгенерированных нами точках'''
polter=[]
with open("plst_dstr_2.txt", "r") as file:
    for i in range(num_samples):
        line = file.readline()
        line = line.split()
        a = float(line[0])
        polter.append(a)


'''Далее создаем массивы для сгенерированных точек'''
generated_points=[]
x=[]
y=[]
z=[]
'''Используя метод Монте-Карло записываем в созданные раннее
массивы точки, соответствующие плотности вероятности функции полтергейста'''
for i in range(num_samples):
    if polter[i] >= random.uniform(0, max_density):
        generated_points.append([data[i][0],data[i][1],polter[i]])
        x.append(data[i][0])
        y.append(data[i][1])
        z.append(polter[i])

print(len(generated_points))
'''Строим график для визуализации сгенерированных точек'''
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
plt.show()