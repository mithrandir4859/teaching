a = int(input())

divisors = list()
while a > 1:
    for i in range(2, a):
        if a % i == 0:
            divisors.append(i)
            a //= i
            break

print(divisors)
