
def kiri(i, n):
    a = ""
    for j in range(i, n):
        if i == 0:
            a += "x"
        elif j > i:
            a += " "
        else:
            a += "x"
    return a

def kanan(i, n):
    a = ""
    for j in range(i, n-1):
        if i == 0:
            a += "x"
        elif j < n-2:
            a += " "
        else:
            a += "x"
    return a

n = 10
for i in range (0, n):
    a = ""
    for j in range (0, i):
        a += " "

    a += kiri(i, n)
    a += kanan(i, n)
    
    # for j in range (i, j):
    #     if j > i:
    #         a += "o"
    #     else:
    #     a += "x"
    # for j in range (i, n-1j):
    #     if j < n-2:
    #         a += " "
    #     else:
    #         a += "x"
    print(a)