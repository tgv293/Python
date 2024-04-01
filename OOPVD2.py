# Viết CT HĐT Python: Giải quyết bài toán sau:
# Nhập 1 danh sách n điểm trong mặt phẳng. Mỗi điểm có tọa độ (x,y)
# a) In ra danh sách điểm và tọa độ
# b) Tìm điểm ở xa gốc tọa độ nhất
# c) Tìm cặp điểm gần nhau nhất
# d) Loại bỏ các điểm trùng nhau (nếu có), chỉ giữ lại 1 điểm

import math


class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Phương thức tính khoảng cách đến gốc tọa độ
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)

    # Phương thức tính khoảng cách giữa 2 điểm
    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def is_duplicate(point1, point2):
        return point1.x == point2.x and point1.y == point2.y

    # Phương thức in tọa độ điểm
    def print_info(self):
        print("({0}, {1})".format(self.x, self.y))


# Nhập số điểm trong mặt phẳng
n = int(input("Nhập số điểm trong mặt phẳng:"))
point_list = []

# Nhập tọa độ điểm
for i in range(n):
    print("Nhập điểm thứ {}: ".format(i + 1))
    x = int(input("x = "))
    y = int(input("y = "))
    point = Point2D(x, y)
    point_list.append(point)

# In ra danh sách điểm và tọa độ
for point in point_list:
    point.print_info()
# Tìm điểm ở xa gốc toạ độ nhất
max_distance = point_list[0].distance()
max_point = point_list[0]
for p in point_list[1:]:
    dist = p.distance()
    if dist > max_distance:
        max_distance = dist
        max_point = p
max_point.print_info()
# Tìm cặp điểm gần nhau nhất
closest_point1, closest_point2 = point_list[0], point_list[1]
min_distance = closest_point1.distance_to(closest_point2)
for p1 in point_list[:-1]:
    for p2 in point_list:
        if p1 != p2:
            if p1.distance_to(p2) < min_distance:
                min_distance = p1.distance_to(p2)
                closest_point1, closest_point2 = p1, p2
print("Cặp điểm gần nhau nhất:")
closest_point1.print_info()
closest_point2.print_info()
print("Cách nhau {}".format(min_distance))

# d) Loại bỏ các điểm trùng nhau (nếu có), chỉ giữ lại 1 điểm
# Sử dụng hàm filter để loại bỏ các điểm trùng nhau
unique_points = list(
    filter(
        lambda p: not any(Point2D.is_duplicate(p, q) for q in point_list), point_list
    )
)

# In ra danh sách điểm sau khi loại bỏ các điểm trùng nhau
print("Danh sách điểm sau khi loại bỏ trùng nhau:")
for point in point_list:
    point.print_info()
