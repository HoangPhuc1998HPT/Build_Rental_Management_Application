import tkinter as tk
from tkinter import ttk

from Controller.login_controller import go_back_to_login
from Controller.nguoithuetro_controller import NguoithueController


class DashboardNguoithuetro:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Người thuê trọ Dashboard")
        self.root.geometry("800x600")

        # Initialize the controller
        self.controller = NguoithueController(root, self, username)

        # Nội dung của Dashboard dành cho người thuê trọ
        label = tk.Label(self.root, text="Dashboard Người Thuê Trọ", font=('Arial', 18))
        label.pack(pady=20)

        # Phòng trọ information labels
        self.Label_Ten_Phong_tro = tk.Label(self.root, text="", font=("Arial", 12), anchor="w")
        self.Label_Ten_Phong_tro.pack(fill='x', padx=100, pady=5)

        self.Label_Dia_chi_Phong_tro = tk.Label(self.root, text="", font=("Arial", 12), anchor="w")
        self.Label_Dia_chi_Phong_tro.pack(fill='x', padx=100, pady=5)

        self.Label_Ten_chutro = tk.Label(self.root, text="", font=("Arial", 12), anchor="w")
        self.Label_Ten_chutro.pack(fill='x', padx=100, pady=5)

        self.Label_so_dien_thoai_chutro = tk.Label(self.root, text="", font=("Arial", 12), anchor="w")
        self.Label_so_dien_thoai_chutro.pack(fill='x', padx=100, pady=5)

        # Hóa đơn Treeview
        tk.Label(self.root, text="Danh sách hóa đơn", font=("Arial", 14, "bold")).pack(pady=20)
        self.tree = ttk.Treeview(self.root, columns=("Ngày hóa đơn", "Số hóa đơn", "Tên hóa đơn", "Thành tiền"),
                                 show="headings", height=7)
        self.tree.heading("Ngày hóa đơn", text="Ngày hóa đơn")
        self.tree.heading("Số hóa đơn", text="Số hóa đơn")
        self.tree.heading("Tên hóa đơn", text="Tên hóa đơn")
        self.tree.heading("Thành tiền", text="Thành tiền")

        self.tree.column("Ngày hóa đơn", width=150)
        self.tree.column("Số hóa đơn", width=80, anchor="center")
        self.tree.column("Tên hóa đơn", width=100, anchor="center")
        self.tree.column("Thành tiền", width=120, anchor="center")
        self.tree.pack(pady=20)

        # Bind double-click to controller
        self.tree.bind("<Double-1>", lambda event: self.controller.on_row_double_click(self.tree, event))

        # Load hóa đơn information
        self.controller.show_danh_sach_hoadon(self.tree)

        tk.Button(self.root, text="Đăng xuất", command=lambda: go_back_to_login(self.root)).pack(pady=20)

    def update_phongtro_info(self, ten_phongtro, dia_chi, ten_chutro, so_dien_thoai):
        self.Label_Ten_Phong_tro.config(text=f"Tên phòng: {ten_phongtro}")
        self.Label_Dia_chi_Phong_tro.config(text=f"Địa chỉ phòng: {dia_chi}")
        self.Label_Ten_chutro.config(text=f"Chủ trọ: {ten_chutro}")
        self.Label_so_dien_thoai_chutro.config(text=f"Số điện thoại: {so_dien_thoai}")


if __name__ == '__main__':
    root = tk.Tk()
    app = DashboardNguoithuetro(root, 'test30')
    root.mainloop()
