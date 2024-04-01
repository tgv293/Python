# Cài đặt lớp Student mô tả các đối tượng sinh viên
class Student:
    # hàm thiết lập (constructor)
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade

    # hàm in thông tin
    def print_info(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Grade:", str(self.grade))


# Khởi tạo một đối tượng sinh viên
sv1 = Student(1, "Nguyễn Văn Khánh Hòa", 9.5)
sv1.print_info()
# In thông tin sinh viên
print("ID:", sv1.id)
print("Name:", sv1.name)
print("Grade:", sv1.grade)
