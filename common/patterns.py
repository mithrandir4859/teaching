m = 6

for i in range(m):
    for j in range(i):
        print(j, end=' ')
    print()

print()

for i in range(m - 1, 0, -1):
    for j in range(i):
        print(j, end=' ')
    print()

for i in range(m):
    print('  ' * (m - i - 1), end='')
    for j in range(i):
        print(j, end=' ')
    print()

print()

for i in range(m - 1, 0, -1):
    print('  ' * (m - i - 1), end='')
    for j in range(i):
        print(j, end=' ')
    print()
