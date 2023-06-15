def print_table(a,b):
    for i in range(2, 11):
        for j in range(a,b+1):
            print(f'{j} x {i:^2d} = {i * j:2d}', end = '   ')
        print()

print_table(2,5)
print()
print_table(6,9)





