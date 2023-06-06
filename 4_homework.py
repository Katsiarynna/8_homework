numbersList = list(range(0, 101))
summa = []

for number in numbersList:
    if number % 2 == 0:
        summa.append(number)
print(sum(summa))
