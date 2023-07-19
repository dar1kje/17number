f = open('../17.txt')  # открываем файл
a = [int(i) for i in f]  # создаем список из целочисленных элементов файла
maximum = 0
kol_vo = 0
for i in range(len(a)):  # проходимся по всем числам
    if 100 <= a[i] < 1000 and a[i] % 100 == 11:  # проверяем условие
        maximum = max(maximum, a[i])  # сверяем каждое число на максимальное
        kol_vo += 1  # счетчик
print(kol_vo, maximum)





