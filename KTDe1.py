class SinhVien:
    muc_xet_hoc_bong = 7

    def __init__(self, ma_sv, ho_ten, diem_tb):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.diem_tb = diem_tb

    @property
    def ma_sv(self):
        return self._ma_sv

    @ma_sv.setter
    def ma_sv(self, value):
        if len(value) != 8:
            print("Mã sinh viên phải có độ dài 8 ký tự.")
        else:
            self._ma_sv = value

    @property
    def ho_ten(self):
        return self._ho_ten

    @ho_ten.setter
    def ho_ten(self, value):
        if len(value.split()) < 2:
            print("Họ và tên phải có ít nhất 2 từ.")
        else:
            self._ho_ten = value

    @property
    def diem_tb(self):
        return self._diem_tb

    @diem_tb.setter
    def diem_tb(self, value):
        if value < 0 or value > 10:
            print("Điểm trung bình phải nằm trong đoạn [0, 10].")
        else:
            self._diem_tb = value

    def nhap_thong_tin(self):
        self.ma_sv = input("Nhập mã sinh viên: ")
        self.ho_ten = input("Nhập họ và tên: ")
        self.diem_tb = float(input("Nhập điểm trung bình: "))

    def xuat_thong_tin(self):
        print(
            f"Mã sinh viên: {self.ma_sv} \t Họ và tên: {self.ho_ten} \t Điểm trung bình: {self.diem_tb:.1f}"
        )


if __name__ == "__main__":
    while True:
        n = int(input("Nhập số lượng sinh viên (0 < n < 100): "))
        if 0 < n < 100:
            break
        else:
            print("Sai số lượng. Vui lòng nhập lại!")

    danh_sach_sv = []

    for i in range(n):
        print(f"Nhập thông tin sinh viên thứ {i + 1}:")
        sv = SinhVien("", "", 0)  # Instantiate a new SinhVien object
        sv.nhap_thong_tin()
        danh_sach_sv.append(sv)

    print("\nDanh sách sinh viên vừa nhập:")
    for sv in danh_sach_sv:
        sv.xuat_thong_tin()

    diem_tb_thap_nhat = min(sv.diem_tb for sv in danh_sach_sv)
    print("\nThông tin sinh viên có điểm trung bình thấp nhất:")
    for sv in danh_sach_sv:
        if sv.diem_tb == diem_tb_thap_nhat:
            sv.xuat_thong_tin()

    count_hoc_bong = sum(
        1 for sv in danh_sach_sv if sv.diem_tb >= SinhVien.muc_xet_hoc_bong
    )
    print(f"\nSố lượng sinh viên được cấp học bổng: {count_hoc_bong}")

    danh_sach_sv = [sv for sv in danh_sach_sv if sv.diem_tb >= 5]
    print("\nDanh sách sinh viên sau khi xóa các sinh viên có điểm trung bình < 5:")
    for sv in danh_sach_sv:
        sv.xuat_thong_tin()

    print("\n--- Kết thúc ---")
