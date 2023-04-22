# Задача 26:  Посчитать факториал (произведение 1 до N) и 
# треугольное число (сумма чисел от 1 до N) для числа N

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def triangle_number(n):
    if n == 0:
        return 0
    else:
        return n + triangle_number(n-1)

n = int(input("Введите число: "))
print(f"Факториал числа {n}: {factorial(n)}")
print(f"Треугольное число для {n}: {triangle_number(n)}")

# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if b <= 0:
        return a + 0

    return sum(a + 1, b - 1)

a = int(input("Введите число: "))
b = int(input("Введите число: "))
print(f"Сумма равна: {sum(a, b)}")