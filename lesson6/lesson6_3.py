def int_input(text):
    num = int(input(text))
    return num


def ab():
    num1 = int(input())
    num2 = int(input())
    return num1 + num2

def a_mul_b():
    a = int(input())
    b = int(input())
    return a * b


def a_div_b(a, b):
    while b == 0:
        print("нельзя делить на 0")
        b = int(input())

    return a / b


a = a_div_b(ab(), int(input()))
print(a)
