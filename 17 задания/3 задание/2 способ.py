def p(n):  # функция перевода из десятичной системы в пятеричную
    s = ''
    while n > 0:
        s += str(n % 5)
        n = n // 5
    return int(s[::-1])


f = open('../17.txt')  # открываем файл
a = [int(i) for i in f]  # создаем список из целочисленных элементов файла
s = [x for x in range(100, 1000) if p(x) % 10 == 1]  # создаем список из подходящих под условие чисел
maximum = 0
kol_vo = 0
for i in range(len(a) - 2):  # проходимся по всем числам списка
    if sum([a[i] in s, a[i + 1] in s, a[i + 2] in s]) == 1:  # проверяем, находится ли число в нужном списке
        maximum = max(maximum, a[i] + a[i + 1] + a[i + 2])  # ставим максимум
        kol_vo += 1  # счетчик
print(kol_vo, maximum)
