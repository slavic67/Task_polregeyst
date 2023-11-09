import matplotlib.pyplot as plt
import numpy as np



'''Задаем границы осей по X,Y для построения функции в трехмерном пространстве'''
X=np.arange(-10,10,0.1)
Y=np.array(X)

'''Далее записываем эти координаты в файл input.txt, затем вызываем plst_1.exe
После исполнения код с записью нужно закомментировать, а input.txt
input.txt переименовываем в input_1.txt для сохранения данных'''

# with open("input_1.txt","w") as file:
#     for i in range(len(X)):
#         for j in range(len(Y)):
#             file.write(f'{round(X[i],2)} {round(Y[j],2)}\n')

'''После запуска plst_1.exe у нас появляется файл plst_dstr.txt
Переименовываем его в plstr_dstr_1.txt для сохранения данных
Далее мы считываем сгенерированные данные в массив'''
polter=[]
with open("plst_dstr_1.txt", "r") as file:
    for i in range(len(X)):
        temp=[]
        for j in range(len(X)):
            line=file.readline()
            line=line.split()
            a=float(line[0])
            temp.append(a)
        polter.append(temp)

'''Делаем из получившегося массива numpy массив'''
polter=np.array(polter)
'''Выводим макисмальное значение функции плотности, пригодится в дальнейшем'''
print(polter.max())

'''Строим трехмерны график плотности вероятности'''
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Построение графика
X, Y = np.meshgrid(X, Y)
ax.plot_surface(X, Y, polter,cmap='viridis', edgecolor='none')    # метод для отрисовки графиков с параметрами по умолчанию
plt.show()