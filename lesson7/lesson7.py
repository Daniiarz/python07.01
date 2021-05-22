# for i in range(10):
#     if i == 5:
#         continue
#     print(i)


# def a_div_b(a, b):
#     for i in range(33333333333333333333333333333333):
#         if i == 5:
#             print(i)
#             print("До break")
#             break
#
#     return a / b
#
#
# print(a_div_b(2, 2))
#
#
def take_students(num):
    l = []
    for i in range(num):
        student = input()
        if student == "Daniiar":
            return "Teacher can't be student"
        l.append(student)

    return l


print(take_students(3))


def take_students(num):
    l = []
    for i in range(num):
        student = input()
        if student == "Daniiar":
            raise ValueError("Teacher can't be student")
        l.append(student)

    return l


try:
    students = take_students(3)
except ValueError:
    students = []

for i in students:
    print(f"Student is {i}")
