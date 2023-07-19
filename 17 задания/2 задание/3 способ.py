f = open('../17.txt')  # открываем файл
a = [int(i) for i in f]  # создаем список из целочисленных элементов файла
s = [x for x in range(1003, 10_000, 10)]  # создаем список из элементов, подходящий под условие
maximum = 0
kol_vo = 0
for i in range(len(a) - 1):  # проходимся по всем числам
    if a[i] in s or a[i + 1] in s:  # проверяем, находится ли число в списке верных чисел
        maximum = max(maximum, a[i] + a[i + 1])  # ставим максимум
        kol_vo += 1  # счетчик
print(kol_vo, maximum)
