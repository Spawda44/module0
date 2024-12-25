i     = 0
count = int(input('Введите диапозон от 0 до >> \n'))

print(f'Четные числа в диапозоне от 0 до {count}:\n')

while i <= count:
    if i % 2 == 0 and i != 0:
        print(i, end='\t')
        if count > 200:
            if i % 20 == 0:
                print()
        else:
            if i % 10 == 0:
                print()
    i += 1
