def sum_pairs(n):
    pairs = []
    for i in range(n + 1):   # от 0 до n включительно
        pairs.append([i, n - i])
    return pairs

# ввод от пользователя
n = int(input("Введите число, которое нужно разбить на пары: "))

# вывод результата
print("Пары чисел, сумма которых равна", n)
for pair in sum_pairs(n):
    print(pair)