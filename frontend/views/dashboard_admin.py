import tkinter as tk
from tkinter import ttk

from Controller.admin_controller import AdminController
from Controller.navigation import Xem_danh_sach_tat_ca_cac_chutro, Xem_danh_sach_tat_ca_cac_phongtro, \
    Xem_danh_sach_tat_ca_cac_nguoithuetro, Go_to_xem_danh_sach_tat_ca_cac_hoadon, Go_to_dangxuat
from backend.utils import clear_screen


class DashboardAdmin:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Admin Dashboard")
        self.root.geometry("1400x800")

        # Tạo AdminController
        self.controller = AdminController(self.root, self)

        # Nội dung của Dashboard dành cho admin
        label = tk.Label(self.root, text="Admin Dashboard", font=('Arial', 18))
        label.pack(pady=20)

        # Các chức năng dành cho admin...
        tk.Label(self.root, text="Danh sách User chưa active", font=("Arial", 14, "bold")).pack(pady=20)

        # Nội dung hóa đơn
        self.tree = ttk.Treeview(self.root, columns=("Tên User", "Chức danh", "Họ và tên", "CCCD", "Số điện thoại", "Active"),
                                 show="headings", height=7)

        self.tree.heading("Tên User", text="Tên User")
        self.tree.heading("Chức danh", text="Chức danh")
        self.tree.heading("Họ và tên", text="Họ và tên")
        self.tree.heading("CCCD", text="CCCD")
        self.tree.heading("Số điện thoại", text="Số điện thoại")
        self.tree.heading("Active", text="Active")

        self.tree.column("Tên User", width=100)
        self.tree.column("Chức danh", width=100, anchor="center")
        self.tree.column("Họ và tên", width=120, anchor="center")
        self.tree.column("CCCD", width=100, anchor="center")
        self.tree.column("Số điện thoại", width=100, anchor="center")
        self.tree.column("Active", width=120, anchor="center")

        self.tree.pack()

        # Sử dụng controller to load data
        self.controller.duyet_tao_user(self.tree)

        # Bind double-click to open user action window
        self.tree.bind("<Double-1>", lambda event: self.controller.on_double_click(event, self.tree))

        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")

        self.tree.configure(yscrollcommand=scrollbar.set)

        tk.Button(self.root, text="Xem danh sách tất cả chủ trọ", command=lambda: Xem_danh_sach_tat_ca_cac_chutro(self.root)).pack(pady=20)
        tk.Button(self.root, text="Xem danh sách tất cả các phòng trọ", command=lambda: Xem_danh_sach_tat_ca_cac_phongtro(self.root)).pack(pady=20)
        tk.Button(self.root, text="Xem danh sách tất cả các người thuê trọ", command=lambda: Xem_danh_sach_tat_ca_cac_nguoithuetro(self.root)).pack(pady=20)
        tk.Button(self.root, text="Xem danh sách tất cả các hóa đơn", command=lambda: Go_to_xem_danh_sach_tat_ca_cac_hoadon(self.root)).pack(pady=20)

        tk.Button(self.root, text="Reset", command=lambda: self.controller.reload_admin_dashboard(self.tree)).pack(pady=10)

        tk.Button(self.root, text="Đăng xuất", command=lambda: Go_to_dangxuat(self.root)).pack(pady=20)



if __name__ == '__main__':
    root = tk.Tk()
    app = DashboardAdmin(root, 'admin_1')
    root.mainloop()
