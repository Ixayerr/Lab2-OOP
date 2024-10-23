import math as mt


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
        print("Введіть правильні числа.")


# Завдання 2: Визначення кількості точок в зеленій області (варіант 11)
def task_geometry11(r, x, y):
    # Умова для нижнього зеленого півкола
    is_in_lower_circle = (x ** 2 + (y + r) ** 2) <= r ** 2 and y <= 0

    # Умова для верхнього зеленого сегмента
    angle = mt.atan2(y - r, x - r)
    is_in_upper_segment = (x - r) ** 2 + (y - r) ** 2 <= r ** 2 and (0 <= angle <= mt.pi / 2)

    # Перевірка потрапляння в зелені області
    if is_in_lower_circle or is_in_upper_segment:
        return "Точка в зеленій області!"
    else:
        return "Точка поза зеленою областю."


# Завдання 3: Дослідження збіжності ряду
def task_series10(epsilon=1e-10, max_iter=100):
    # Початкові параметри
    term = (mt.factorial(1) - 3 ** 1) / (1 ** 1)  # Перший член ряду
    print(f"Initial term: {term}")

    s = term  # Початкова сума
    n = 2  # Починаємо з другого члена
    e = epsilon  # Точність
    while abs(term) > e:  # Поки не досягнемо потрібної точності
        term = (mt.factorial(n) - 3 ** n) / (n ** n)
        print(f"Term at n={n}: {term}")
        s += term
        n += 1
        if n > max_iter:
            print("Error: Series did not converge within iteration limit.")
            return None

    print(f"Series converged to: {s}")
    return s
