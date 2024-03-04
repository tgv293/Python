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

# # B1: Input (có ràng buộc tương tự Lệnh do...while)
# while True:
#     n = int(input("Nhập số nguyên n (0<n<=1000): "))
#     if 0<n<=1000:
#         break
# print(n, "là số nguyên")
# # a - Kiểm tra n có phải số nguyên tố
# if LaSNT(n):
#     print("{} là số nguyên tố".format(n))
# else:
#     print("{} không phải là số nguyên tố".format(n))
    
# # b - Các số nguyên tố nhỏ hơn n
# print("Các số nguyên tố <= {}:".format(n))
# for i in range(2, n+1):
#     if LaSNT(i):
#         print("%5d" % i, end=" ")
        
# Phạm vi của biến trong Python
# def MyFunc():
#     x = 100
    
# # Thử đọc giá trị biến x
# MyFunc()
# print('X = %d' % x)

# def MyFunc2():
#     global x2
#     x2 = 100
    
# # Thử đoc giá trị biến x2
# MyFunc2()
# print('X = %d' % x2)

# In ra các số chẵn <=100
i = 2
for i in range(1,101):
    if i % 2 != 0:
        continue
    print("{}".format(i))
    
# Lệnh lặp với kiểu từ điển
# Trường hợp 1: Lặp một biến chạy
numbers = {0: 'không', 1: 'một', 2: 'hai', 3: 'ba', 4: 'bốn', 5: 'năm'}
for i in numbers.items():
    print(i)
# Trường hợp 2: Lặp hai biến chạy
for k,v in numbers.items():
    print("Số {} đọc là {}".format(k,v))
    
# Trường hợp 3: Lặp for comprehensive
# Vd: Hãy tạo danh sách các số nguyên liên tiếp từ 1...100
myList = [i for i in range(1, 101)]
print(myList)
# Vd: Hãy tạo danh sách các số lẻ liên tiếp từ 1...100
myOddNumbers = [i for i in range(1,101) if i % 2 != 0]
print(myOddNumbers)

# Lệnh for với kiểu từ điển
personal_info = {
    'Name':'Hoàng',
    'Age':17,
    'Height':1.70,
    'Weight':68
}
# lặp 1 biến chạy
for i in personal_info.items():
    print(i)
# lặp 2 biến chạy
for k,v in personal_info.items():
    print(k,v)