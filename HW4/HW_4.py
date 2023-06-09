# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений в
# порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого
# множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# n = int(input("Введите количество элементов первого множества: "))
# a = set()
# for i in range(n):
#     a.add(int(input("Введите элемент первого множества: ")))

# m = int(input("Введите количество элементов второго множества: "))
# b = set()
# for i in range(m):
#     b.add(int(input("Введите элемент второго множества: ")))

# inter = list(b.intersection(a))

# for j in range(len(inter) - 1):
#     for i in range(len(inter) - 1):
#         if inter[i] > inter[i + 1]:
#             temp = inter[i]
#             inter[i] = inter[i + 1]
#             inter[i + 1] = temp
# print(inter)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по
# окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени
# сбора на них выросло различное число ягод — на i-ом кусте
# выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического
# сбора черники. Эта система состоит из управляющего модуля и
# нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды
# с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь
# перед некоторым кустом заданной во входном файле грядки.

n = int(input("Введите количество кустов: "))
a = list(map(int, input("Введите урожайность кустов ").split()))

max_sum = 0
for i in range(1, n):
    if i == n-1:
        curr_sum = a[n-1] + a[0] + a[n-2]
    else:
        curr_sum = a[i-1] + a[i] + a[i+1]

    if curr_sum > max_sum:
        max_sum = curr_sum

print(max_sum)
