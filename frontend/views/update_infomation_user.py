import tkinter as tk


from backend.models.admin import Admin
from backend.models.chutro import Chutro

from backend.models.nguoithuetro import NguoiThueTro


class UpdateInfomationView():
    def __init__(self, root, role,user_id):
        self.role = role
        self.user_id = user_id
        self.root = root
        self.root.title("Cập nhật thông tin")
        self.root.geometry("400x400")

        if role == "admin":
            # Các form input cho thông tin chi tiết
            tk.Label(self.root, text="Họ tên").pack(pady=5)
            self.entry_hoten = tk.Entry(self.root, width=30)
            self.entry_hoten.pack(pady=5)

            tk.Button(self.root, text="Hoàn tất", command=self.save_admin_info).pack(pady=20)

        elif self.role == "chutro":
            # Các form input cho thông tin chi tiết
            tk.Label(self.root, text="Họ tên").pack(pady=5)
            self.entry_hoten = tk.Entry(self.root, width=30)
            self.entry_hoten.pack(pady=5)

            tk.Label(self.root, text="CCCD").pack(pady=5)
            self.entry_cccd = tk.Entry(self.root, width=30)
            self.entry_cccd.pack(pady=5)

            tk.Label(self.root, text="Số điện thoại").pack(pady=5)
            self.entry_phone = tk.Entry(self.root, width=30)
            self.entry_phone.pack(pady=5)

            tk.Button(self.root, text="Hoàn tất", command=self.save_chutro_info).pack(pady=20)

        elif self.role == "nguoithuetro":
            # Họ tên
            tk.Label(self.root, text="Họ tên").pack(pady=5)
            self.entry_fullname = tk.Entry(self.root)
            self.entry_fullname.pack(pady=5)

            # CCCD
            tk.Label(self.root, text="CCCD").pack(pady=5)
            self.entry_cccd = tk.Entry(self.root)
            self.entry_cccd.pack(pady=5)

            # Số điện thoại
            tk.Label(self.root, text="Số điện thoại").pack(pady=5)
            self.entry_phone = tk.Entry(self.root)
            self.entry_phone.pack(pady=5)

            # Nút Hoàn tất
            tk.Button(self.root, text="Hoàn tất", command=self.save_nguoithue_info).pack(pady=20)

    def save_admin_info(self):
        hoten = self.entry_hoten.get().strip()
        Admin.save_info_admin(self.root, self.user_id, hoten)

    def save_chutro_info(self):
        hoten = self.entry_hoten.get().strip()
        cccd = self.entry_cccd.get().strip()
        phone = self.entry_phone.get().strip()
        Chutro.save_info_chutro(self.root, hoten, cccd, phone, self.user_id)

    def save_nguoithue_info(self):
        fullname = self.entry_fullname.get().strip()
        cccd = self.entry_cccd.get().strip()
        phone = self.entry_phone.get().strip()
        NguoiThueTro.save_info_nguoi_thue(self.root, self.user_id, fullname, cccd, phone)





