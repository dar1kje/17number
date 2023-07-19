from random import randint
with open('17.txt', 'w') as f:
    for _ in range(10_000):
        f.write(str(randint(0, 10_000))+'\n')

