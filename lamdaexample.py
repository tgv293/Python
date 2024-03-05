# Chương trình chính
if __name__ == '__main__':
    n = 5
    # Cách 1
    s = 0
    for i in range(n+1):
        s += i ** 2
    print("S = {}".format(s))
    # Cách 2
    s = 0
    for i in range(n+1):
        s += square_clustering(i)
    print("S = {}".format(s))
    # Cách 3
    s = 0
    for i in range(n+1):
        def x(i): return i*i
        s += x(i)
    print("S = {}".format(s))
