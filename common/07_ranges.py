ranges = [
    range(10),
    range(5, 10),
    range(5, 12),
    range(0, 10, 2),
    range(1, 10, 2),
    range(10, 0, -1),
    range(10, 0, -2),
    range(9, 0, -2),
    range(2, 11, 3),
    range(2, 11, -3),
    range(11112, 11),
]

for r in ranges:
    print(r, '->', list(r))
