d = {'key': 'asldjfa;', 'c': 1231231}


def test(c, key):
    print(key)
    print(c)


test(*d)

l = ['Madaanbek', 'Nurbek', 'Samat']


def print_3_names(name1, name2, name3):
    return f"{name1} {name2} {name3}"


print(print_3_names(*l))
