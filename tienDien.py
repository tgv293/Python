soKWh = int(input("Nhập số KWh tiêu thụ:"))
if soKWh >= 0 and soKWh <=50:
    tienDien = soKWh * 1500
if soKWh >50 and soKWh <=100:
    tienDien = 50 * 1500 + (soKWh - 50)*1750
if  soKWh > 100:
    tienDien = 50 * 1500 + 50 * 1750 + (soKWh - 100) * 2000
print("Tiền điện phải trả là: ", tienDien)

