#Написать такую функцию, которая примет два числа в качестве аргументов и посчитает наименьшее общее кратное
#написать нок двух чисел которые передаются в функцию в виде двух аргументов


def nok_numbers(x, y):
    c = []
    v = []
    g = 1
    while g < 10:
        c.append(x * g)
        v.append(y * g)
        print(c, v)
        g += 1
    a = set(c)
    b = set(v)
    q = a.intersection(b)
    l = sorted(list(q))
    print(l[0])

print(nok_numbers(x = 4, y = 6))


def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


x = int(input('a = '))
y = int(input('b = '))
print('НОК:', lcm(x, y))


