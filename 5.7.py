def func(x, y):
    return ((x - y) * (x - y))


a = 1
b = 5
n = 10
alpha = 1.0
h = (b - a) / n
x = a
w = [0] * (n + 1)
w[0] = 1
for i in range(1, 4):
    k1 = h * func(x, w[i - 1])
    k2 = h * func(x + h / 2, w[i - 1] + k1 / 2)
    k3 = h * func(x + h / 2, w[i - 1] + k2 / 2)
    k4 = h * func(x + h, w[i - 1] + k3)
    w[i] = w[i - 1] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    x = a + i * h
    print(f'при x = {x} приближенное значение = {w[i]}')
for i in range(4, n + 1):
    k1 = 55 * func(x, w[i - 1]) - 59 * func(x - h, w[i - 2]) + 37 * func(x - h * 2, w[i - 3]) - 9 * func(x - h * 3,
                                                                                                         w[i - 4])
    w[i] = w[i - 1] + h / 24 * k1
    x = a + i * h
    print(f'при x = {x} приближенное значение = {w[i]}')
