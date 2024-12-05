import tkinter as tk
from tkinter import ttk


from backend.models.nguoithuetro import NguoiThueTro


class Admin_show_all_nguoithuetro:

    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý người thuê nhà trọ")
        self.root.geometry("800x600")

        tk.Label(self.root, text="Danh sách người thuê nhà trọ", font=("Arial", 18, "bold")).pack(pady=10)

        self.tree_show_nguoi_thue = ttk.Treeview(self.root, columns=("Username", "Họ tên người thuê", "CCCD", "Số điện thoại", "Tên phòng trọ"),show="headings", height=25)
        self.tree_show_nguoi_thue.heading("Username", text="Username")
        self.tree_show_nguoi_thue.heading("Họ tên người thuê", text="Họ tên người thuê")
        self.tree_show_nguoi_thue.heading("CCCD", text="CCCD")
        self.tree_show_nguoi_thue.heading("Số điện thoại", text="Số điện thoại")
        self.tree_show_nguoi_thue.heading("Tên phòng trọ", text="Tên phòng trọ")

        self.tree_show_nguoi_thue.column("Username", width=100)
        self.tree_show_nguoi_thue.column("Họ tên người thuê", width=160, anchor="center")
        self.tree_show_nguoi_thue.column("CCCD", width=100, anchor="center")
        self.tree_show_nguoi_thue.column("Số điện thoại", width=100,anchor="center")
        self.tree_show_nguoi_thue.column("Tên phòng trọ", width=100, anchor="center")

        self.load_du_lieu_nguoi_thue()
        self.tree_show_nguoi_thue.pack(fill='x', padx=100, pady=5)

        # Nội dung cơ sở dữ liệu không

    def load_du_lieu_nguoi_thue(self):
        rows = NguoiThueTro.get_info_all_nguoithue()
        self.tree_show_nguoi_thue.delete(*self.tree_show_nguoi_thue.get_children())
        for row in rows:
            self.tree_show_nguoi_thue.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4]),tags=(row[0],))



if __name__ == '__main__':
    root = tk.Tk()
    app = Admin_show_all_nguoithuetro(root)
    root.mainloop()