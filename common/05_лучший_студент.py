студенты = [
    # номер, имя, финальный балл, пол
    [1, 'Маша', 81, 'ж'],
    [2, 'Петя', 55, 'м'],
    [3, 'Вася', 66, 'м'],
    [4, 'Катя', 91, 'ж'],
    [5, 'Витольд', 93, 'м'],
    [6, 'Катя', 92, 'ж'],
    [7, 'Петро', 91, 'м'],
    [8, 'Иван', 75, 'м'],
    [9, 'Аня', 77, 'ж'],
    [10, 'Влада', 59, 'ж'],
    [11, 'Леся', 84, 'ж'],
    [12, 'Артур', 93, 'м'],
    [13, 'Иван', 73, 'м'],
]

лучший = None
лучший_балл = None

for студент in студенты:
    if лучший is None:
        лучший = студент[1]
        лучший_балл = студент[2]
    elif лучший_балл < студент[2]:
        лучший = студент[1]
        лучший_балл = студент[2]


print(лучший, лучший_балл)
