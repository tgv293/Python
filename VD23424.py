# Viết CT có các hàm sau:
# a) Hàm kiểm tra một số tự nhiên có phải số nguyên tố hay không
# b) Hàm in ra các số nguyên tố <=nguyên
# c) Hàm tìm số nguyên tố nhỏ nhất > n
def LaSNT(n):
    if n < 2:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True


def InSNT(n):
    for i in range(2, n+1):
        if LaSNT(i):
            print("%5d" % i, end=" ")


def TimSNT(n):
    for i in range(n+1, n*2):
        if i > n and LaSNT(i):
            print(i)
            break


if __name__ == '__main__':
    n = 37
    print(LaSNT(n))
    print("Các số nguyên tố <= {}:".format(n))
    InSNT(n)
    print("\nSố nguyên tố nhỏ nhất lớn hơn n: ")
    TimSNT(n)
