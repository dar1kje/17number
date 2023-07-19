f = open('../17.txt')  # открываем файл
a = [int(i) for i in f]  # создаем список из целочисленных элементов файла
maximum = 0
kol_vo = 0
for i in range(len(a) - 1):  # проходимся по всем числам
    if 1_000 <= a[i] < 10_000 and a[i] % 10 == 3 or 1_000 <= a[i + 1] < 10_000 and a[i + 1] % 10 == 3:  # проверяем условие каждого числа пары
        maximum = max(maximum, a[i] + a[i + 1])  # ставим максимум
        kol_vo += 1  # счетчик
print(kol_vo, maximum)
