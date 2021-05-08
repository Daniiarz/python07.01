import random

# d = 0
#
# while d < 10:
#     print(d)
#     d += 1
#
# num = random.randint(0, 10)
# inp = int(input())
#
# while inp != num:
#     print("Wrong Number, one more time!")
#     inp = int(input())


name = input()

while len(name) < 8:
    print("WRONG PASSWORD!")
    name = input()

print(name)
