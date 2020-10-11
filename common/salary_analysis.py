import csv


def load():
    with open('../data/2019_june_raw.csv') as f:
        reader = csv.reader(f)
        return list(reader)


данные = load()
заголовок = данные[0]
del данные[0]

print(заголовок)
print(len(данные))

salary = 0
count = 0
for row in данные:
    try:
        if float(row[3]) < 5:
            salary += float(row[5])
            count += 1
    except Exception:
        pass

print(28.2 * salary / count)
