# Một máy ATM có các loại tiền 100, 20 và 5 USD
# Một người cần rút số tiền m
# a) Tìm phương án rút tốt nhất (có ít tờ tiền nhất)
# b) Liệt kê tất cả các cách rút được số tiền m. Có tất cả bao nhiêu cách

while True:
    m = int(input("Nhập số tiền rút: "))
    if m <= 0 or m % 5 != 0:
        print("Số tiền không thỏa mãn!")
    else:
        m1 = m
        break
# a)
# Cách làm: ưu tiên rút mệnh giá cao trước
soTo100 = m // 100
m = m % 100
soTo200 = m // 20
m = m % 20
soTo5 = m // 5
print("Phương án rút tiền tốt nhất: ")
print("{} tờ 100, {} tờ 20, {} tờ 5 USD".format(soTo100, soTo200, soTo5))
# b)
m = m1
soCach = 0
for soTo100 in range(m // 100 + 1):
    for soTo20 in range(m // 20 + 1):
        for soTo5 in range(m // 5 + 1):
            if (soTo100 * 100 + soTo20 * 20 + soTo5 * 5 == m):
                soCach += 1
                print("{} 100, {} 20, {} 5 USD".format(soTo100, soTo20, soTo5))
print("Có tất cả {} cách".format(soCach))
