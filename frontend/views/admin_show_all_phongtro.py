import tkinter as tk
from tkinter import ttk


from backend.models.phongtro import PhongTro


class Admin_show_all_phongtro:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.geometry("1400x800")


        tk.Label(self.root, text="Danh sách tất cả phòng trọ", font=("Arial", 14, "bold")).pack(pady=20)

        # Bảng nội dung hóa đơn
        self.tree_sho_phong_tro = ttk.Treeview(self.root,
        columns=("Tên phòng", "Địa chỉ", "Giá phòng", "Tên chủ trọ", "Tên người thuê"),show="headings", height=20)

        self.tree_sho_phong_tro.heading("Tên phòng", text="Tên phòng")
        self.tree_sho_phong_tro.heading("Địa chỉ", text="Địa chỉ")
        self.tree_sho_phong_tro.heading("Giá phòng", text="Giá phòng")
        self.tree_sho_phong_tro.heading("Tên chủ trọ", text="Tên chủ trọ")
        self.tree_sho_phong_tro.heading("Tên người thuê", text="Tên người thuê")

        self.tree_sho_phong_tro.column("Tên phòng", width=60)
        self.tree_sho_phong_tro.column("Địa chỉ", width=280)
        self.tree_sho_phong_tro.column("Giá phòng", width=60,anchor="center")
        self.tree_sho_phong_tro.column("Tên chủ trọ", width=120)
        self.tree_sho_phong_tro.column("Tên người thuê", width=120)

        self.load_du_lieu_phong_tro()
        self.tree_sho_phong_tro.pack(fill='x', padx=100, pady=5)

        # Nội dung cơ sở dữ liệu không
    def load_du_lieu_phong_tro(self):
        # Đãnh nghĩa dữ liệu
        rows = PhongTro.get_info_all_phongtro()
        self.tree_sho_phong_tro.delete(*self.tree_sho_phong_tro.get_children())
        for row in rows:
            self.tree_sho_phong_tro.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4]),tags=(row[5],))



if __name__ == '__main__':
    root = tk.Tk()
    app = Admin_show_all_phongtro(root)
    root.mainloop()
