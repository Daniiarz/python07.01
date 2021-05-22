plane = [
    ["X", "X", "0"],  # 0
    ["0", "0", "*"],  # 1
    ["0", "X", "X"],  # 2
]


def check_winner(p):
    win = True
    for i in range(3):
        row = plane[i]
        start = ""
        for k in row:
            if k == "*":
                win = False
                break
            if not start:
                start = k
            else:
                if start == k:
                    start = k
                else:
                    win = False
                    break
        if win:
            return start

    l = []
    for i in range(3):
        for k in range(3):
            if p[k][i] == "*":
                break
            l.append(p[k][i])
        if l.count("0") == 3 or l.count("X") == 3:
            return l[0]

        l.clear()

    if p[0][0] == p[1][1] == p[2][2]:
        return p[0][0]
    if p[0][2] == p[1][1] == p[2][0]:
        return p[2][0]


def input_x_y():
    return int(input()) - 1, int(input()) - 1


def print_plane(plane):
    for i in range(3):
        row = plane[i]
        print(f"{row[0]} | {row[1]} | {row[2]}")
        if i != 2:
            print("-" * 9)


print(check_winner(plane))
