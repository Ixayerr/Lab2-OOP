import math


# Завдання 1: Визначення найближчої точки до A
def task_if20():

    # Визначає, яка з точок B або C знаходиться ближче до точки A.

    try:
        A = float(input("Введіть координату точки A: "))
        B = float(input("Введіть координату точки B: "))
        C = float(input("Введіть координату точки C: "))

        distance_B = abs(A - B)
        distance_C = abs(A - C)

        if distance_B < distance_C:
            print(f"Точка B ближча до точки A. Відстань: {distance_B}")
        elif distance_C < distance_B:
            print(f"Точка C ближча до точки A. Відстань: {distance_C}")
        else:
            print(f"Точки B і C однаково віддалені від точки A. Відстань: {distance_B}")
    except ValueError:
        print("введіть правильні числа.")


# Завдання 2: Визначення кількості точок в зеленій області (варіант 11)
def task_geometry11(points):

    #Підраховує кількість точок, що потрапляють в зелену область.
    #points - список точок (кожна точка має координати (x, y)).

    count = 0
    r = 1
    for x, y in points:
        # Умова для попадання точки в зелену область
        if (x - r) ** 2 + (y - r) ** 2 <= r ** 2:
            count += 1
    return count


# Завдання 3: Дослідження збіжності ряду
def task_series10(epsilon=1e-10, g=1e10):

    # epsilon - маленька величина для завершення циклу при збіжності.

    n = 1
    s = 0
    while True:
        term = (math.factorial(n) - 3 ** n) / n ** n
        s += term

        if abs(term) < epsilon:
            print(f"Ряд збігається. Сума: {s}")
            break
        elif abs(term) > g:
            print(f"Ряд розбігається. Сума: {s}")
            break

        n += 1
