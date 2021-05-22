# def sum(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
#
#
# print(sum(2, 2, 3, 2, [2, 8120391, 12830918, ['asdfasdf', 'asdfas']]))


def ab(**kwargs):
    return kwargs


print(ab(a=2, c=2, d=2, e=2))


def print_name_surname(name, surname, *args, **kwargs):
    print(args)
    if 'otchestvo' in kwargs:
        return f"{name} {surname} {kwargs['otchestvo']}"
    return f"{name} {surname}"


name = "Nurtazim"
surname = "Жузумалиев"
othcestvo = input()
print(print_name_surname(name, surname, 20, 202020202, 2020, 22, otchestvo=othcestvo))


