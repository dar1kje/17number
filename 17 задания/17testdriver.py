from random import randint
with open('17test.txt', 'w') as f:
    for i in range(10):
        f.write(str(randint(10, 10_000))+'\n')
