def p(n):  # функция перевода из десятичной системы в пятеричную
    s = ''
    while n > 0:
        s += str(n % 5)
        n = n // 5
    return int(s[::-1])


f = open('../17.txt')  # открываем файл
a = [int(i) for i in f]  # создаем список из целочисленных элементов файла
maximum = 0
kol_vo = 0
for i in range(len(a) - 2):  # проходимся по всем числам списка
    if sum([100 <= a[i] < 1000 and p(a[i]) % 10 == 1, 100 <= a[i + 1] < 1000 and p(a[i + 1]) % 10 == 1,
            100 <= a[i + 2] < 1000 and p(a[i + 2]) % 10 == 1]) == 1:  # проверяем условие
        kol_vo += 1  # счетчик
        maximum = max(maximum, a[i] + a[i + 1] + a[i + 2])  # ставим максимум
print(kol_vo, maximum)


