import sys
from lab_2_oop import task_if20, task_geometry11, task_series10


# Завдання 4: Меню для вибору завдань
def menu():
    while True:
        print("\nВиберіть завдання:")
        print("1. Визначити, яка точка ближче до A.")
        print("2. Порахувати кількість точок в зеленій області.")
        print("3. Дослідити збіжність ряду.")
        print("0. Вихід")

        try:
            choice = int(input("Ваш вибір (0-3): "))

            if choice == 1:
                task_if20()
            elif choice == 2:
                points = [(float(input("x: ")), float(input("y: "))) for _ in range(int(input("Кількість точок: ")))]
                print(f"Кількість точок у зеленій області: {task_geometry11(points)}")
            elif choice == 3:
                task_series10()
            elif choice == 0:
                sys.exit(0)
            else:
                print("Невірний вибір.")
        except ValueError:
            print("Помилка введення.")


# Викликати головне меню:
if __name__ == "__main__":
    menu()
