def SayHi(message):
    print("Hello " + message)
def LaSNT(n):
    if n<2:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

# Tạo hàm main
if __name__ == '__main__':
    SayHi()