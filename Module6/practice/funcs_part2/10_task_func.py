# Напишите функцию, находящую среднее арифметическое всех аргументов
# Функция должна вызываться с любым количеством аргументов

def average(*args):
    count_args = 0
    sum_args = 0
    for arg in args:
        count_args += 1
        sum_args = sum_args + arg
    return sum_args / count_args



print(average(3, 4, 8))
print(average(1, 4, 5, -3, 8, 4))
print(average(-10, 12, 6.3, -5.5, 7, 0.2))
