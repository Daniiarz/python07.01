print("Hello, World!")
# print(input("Введите текст: "))


def ab():
    a = int(input())
    b = int(input())
    print(a + b)


def a_mul_b():
    a = int(input())
    b = int(input())
    print(a * b)


def a_div_b():
    a = int(input())
    b = int(input())
    while b == 0:
        print("нельзя делить на 0")
        b = int(input())

    print("Результат деления равен", a / b)


a_div_b()
a_div_b()
