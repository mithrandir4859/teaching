число = 691

простое = True
for i in range(2, число):
    if число % i == 0:
        простое = False
        break

print(f'Число простое: {простое}')


