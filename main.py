x = {}
n = int(input())


def place(xpos, ypos):
    if ypos in x.values():
        return False
    j = 1
    while j < xpos:
        if abs(x[j] - ypos) == abs(j - xpos):
            return False
        j += 1
    return True


def clear_future_blocks(xpos):
    for i in range(xpos, n+1):
        x[i] = None


def queens(xpos):
    for ypos in range(1, n + 1):
        clear_future_blocks(xpos)
        if place(xpos, ypos):
            x[xpos] = ypos
            if xpos == n:
                for j in x:
                    print(x[j], end=' ')
                print('\n---------')
            else:
                queens(xpos + 1)


queens(1)
