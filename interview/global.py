a = 10


def abc():
    global a
    a = 15


abc()
print(a)
