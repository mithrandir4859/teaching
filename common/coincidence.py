import random

count = 0
for experiment in range(10_000):
    days = [random.randint(1, 365) for i in range(20)]
    if len(set(days)) < len(days):
        print(sorted(days))
        count += 1

print(count / 10_000 * 100)
