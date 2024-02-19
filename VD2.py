n = int(input("Nhập n:"))
n1 = n
sonut = 0
while n > 0:
    sonut += n % 10
    n = n // 10
print("Số nút = ", sonut)

maxdigit = 0
while n1 > 0:
    if n1 % 10 > maxdigit:
        maxdigit = n1 % 10
    n1 = n1 // 10
print("Chữ số lớn nhất là ", maxdigit)



