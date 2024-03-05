ds = [1, 2, 3, 4, 5, 6]

nl = list(filter(lambda i: i % 2 == 0, ds))

print(nl)

# Viết hàm tính tổng không hạn chế các số nguyên


def TinhTong(*ds):
    s = 0
    for i in ds:
        s += 1
    return s


s = TinhTong(1, 2, 3, 4)
print(s)
