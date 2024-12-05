import tkinter as tk

from backend.models.db import connection, create_database_connection
from backend.utils import get_username_from_id_chutro


class CreateRoomView:
    def __init__(self, root,id_chutro):
        self.root = root
        self.root.title("Tạo phòng trọ mới")
        self.id_chutro = id_chutro
        self.root.geometry("400x480")
        self.username = get_username_from_id_chutro(self.id_chutro)

        # Các trường nhập thông tin phòng trọ
        tk.Label(self.root, text="Tên phòng").pack(pady=5)
        self.entry_room_name = tk.Entry(self.root)
        self.entry_room_name.pack(pady=5)



        tk.Label(self.root, text="Địa chỉ").pack(pady=5)
        self.entry_address = tk.Entry(self.root, width=50)
        self.entry_address.pack(pady=5)

        tk.Label(self.root, text="Giá điện (VNĐ)").pack(pady=5)
        self.entry_giadien = tk.Entry(self.root)
        self.entry_giadien.pack(pady=5)

        tk.Label(self.root, text="Giá nước (VNĐ)").pack(pady=5)
        self.entry_gianuoc = tk.Entry(self.root)
        self.entry_gianuoc.pack(pady=5)

        tk.Label(self.root, text="Giá phòng (VNĐ)").pack(pady=5)
        self.entry_giapong = tk.Entry(self.root)
        self.entry_giapong.pack(pady=5)

        # Nút lưu phòng trọ
        save_button = tk.Button(self.root, text="Lưu phòng trọ", command=self.go_to_save_room)
        save_button.pack(pady=20)
        from Controller.navigation import go_to_back_dashboard_chutro
        back_dashboard_chutro = tk.Button(self.root, text="Quay lại", command=lambda :go_to_back_dashboard_chutro(self.root, self.username))
        back_dashboard_chutro.pack(pady=20)


    def go_to_save_room(self):
        ten_phong = self.entry_room_name.get()
        address = self.entry_address.get()
        giadien = float(self.entry_giadien.get())
        gianuoc = float(self.entry_gianuoc.get())
        giaphong = float(self.entry_giapong.get())
        from backend.models.phongtro import PhongTro
        PhongTro.save_room(self.root, ten_phong, address, giadien, gianuoc, giaphong, self.id_chutro, self.username)


    # dashboard chủ trọ y/c username
    # get usename từ id_chủ trọ
    # laasys id chủ trọ get userID
    # lấy userID get username










