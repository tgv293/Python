#Bài tập: Nhập 1 số nguyên n thỏa 0<n<=1000 (Lặp lại việc nhập cho đến khi n thỏa mãn ràng buộc)
#a - Kiểm tra n có phải số nguyên tố hay không
#b - In ra các số nguyên tố nhỏ hơn n

# B1: Input (có ràng buộc tương tự Lệnh do...while)
while True:
    n = int(input("Nhập số nguyên n (0<n<=1000): "))
    if 0<n<=1000:
        break
print(n, "là số nguyên")

# Định nghĩa hàm kiểm tra 1 STN là số nguyên tố
def LaSNT(n):
    if n<2:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

# a - Kiểm tra n có phải số nguyên tố
if LaSNT(n):
    print("{} là số nguyên tố".format(n))
else:
    print("{} không phải là số nguyên tố".format(n))
    
# b - Các số nguyên tố nhỏ hơn n
print("Các số nguyên tố <= {}:".format(n))
for i in range(2, n+1):
    if LaSNT(i):
        print("%5d" % i, end=" ")