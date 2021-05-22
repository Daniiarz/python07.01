l = [1, 2, 3, 4, 5, 6, 7]
print(l)
# inp = input()
# l.append(inp)
l.append(9)
print(l)
l.pop(0)
print(l)
l.reverse()
l = l[::-1]
print(l)
l.extend([1, 2, 3, 34])
print(l)
print(l.count(34))
print(l.index(34))

t = (1, 2, 3, 2, 2)
print(t.count(2))
