def head(x):
    return x[0]

def tail(x):
    return x[1:]

def concatena(x, y):
    if not x:
        return y
    else:
        return head(x)+concatena(tail(x), y)

print(concatena("abc", "def"))
