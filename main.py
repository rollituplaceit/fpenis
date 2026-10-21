def add(a, b):
    return a + b


def main():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: нужно ввести число.")
        return

    result = add(a, b)

    # Красивый вывод: 2.0 + 3.0 -> 5, а не 5.0
    if result.is_integer():
        result = int(result)

    print(f"Сумма: {result}")


if __name__ == "__main__":
    main()
