## Tạo Module tự định nghĩa và sử dụng
### B1: Tạo 1 thư mục đặt tên tùy ý, chẳng hạn 'my_lib'
#### Trong thư mục này phải tạo file có tên '__init__.py', file nầy không cần có mã nguồn
### B2: Trong thư mục 'my_lib tạo file mã nguồn, chẳng hạn 'functions.py' chứa các thành phần tự cài đặt

### B3: Sử dụng module tự định nghĩa
#### Tạo file mã nguồn python mới
#### Thêm dòng khai báo

## Nạp module tự định nghĩa
from my_lib.functions import *
SayHi("Nha Trang")

# B1: Input (có ràng buộc tương tự Lệnh do...while)
while True:
    n = int(input("Nhập số nguyên n (0<n<=1000): "))
    if 0<n<=1000:
        break
print(n, "là số nguyên")
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
        