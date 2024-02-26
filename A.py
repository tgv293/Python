# Hàm không xác định số lượng tham số
# vd: Viết hàm tính tổng các số nguyên

def Sum(*n):
    s = 0
    for i in n:
        s += 1
    return s
