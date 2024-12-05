import tkinter as tk

from tkinter import ttk, messagebox

from Controller.hoadonController import HoadonController
from Controller.navigation_until import go_to_show_danh_sach_nhatro
from backend.utils import get_username_from_id_chutro


class CreateHoadon_XuatHoaDon:
    def __init__(self, root, id_chutro, id_phong):
        self.root = root
        self.root.title("Xuất hóa đơn")
        self.root.geometry("1000x800")
        self.controller = HoadonController(self, id_chutro, id_phong)
        self.username = get_username_from_id_chutro(id_chutro)
        # Initialize UI elements here...
        self.thiet_lap_table()

        # Load initial data
        self.controller.load_thongtin_hoadon()

    def thiet_lap_table(self):
        tk.Label(self.root, text="HÓA ĐƠN", font=("Arial", 18, "bold")).pack(pady=10)
        tk.Label(self.root, text="Thông tin hóa đơn", font=("Arial", 14, "bold")).pack(pady=10)

        self.Label_Sohoadon = tk.Label(self.root, text="", font=("Arial", 12), anchor="w")
        self.Label_Sohoadon.pack(fill='x', padx=100, pady=5)

        self.tree = ttk.Treeview(self.root, columns=("Nội dung", "Số lượng", "Đơn giá", "Thành tiền"), show="headings", height=7)
        self.tree.heading("Nội dung", text="Nội dung")
        self.tree.heading("Số lượng", text="Số lượng")
        self.tree.heading("Đơn giá", text="Đơn giá")
        self.tree.heading("Thành tiền", text="Thành tiền")
        self.tree.pack(pady=10)

        self.total_label = tk.Label(self.root, text="Tổng cộng: 0 VNĐ", font=("Arial", 12, "bold"))
        self.total_label.pack(pady=5)

        self.btn_xuathoadon = tk.Button(self.root, text="Xuất hóa đơn", command= lambda: self.controller.go_to_nhaphoadon())
        self.btn_xuathoadon.pack(pady=10)

        self.btn_quaylai = tk.Button(self.root, text="Quay lai", command=lambda: go_to_show_danh_sach_nhatro(self.root, self.username))
        self.btn_quaylai.pack(pady=10)

    def update_view(self, result, giadien, gianuoc, tongchiphi):
        self.Label_Sohoadon.config(text=f"Số hóa đơn: {result[0]}")
        self.tree.insert("", "end", values=("Tiền nhà", 1, result[4], result[4]))
        self.tree.insert("", "end", values=("Tiền điện", result[1], giadien, result[1] * giadien))
        self.tree.insert("", "end", values=("Tiền nước", result[2], gianuoc, result[2] * gianuoc))
        self.tree.insert("", "end", values=("Tiền rác", 1, result[6], result[6]))
        self.tree.insert("", "end", values=("Chi phí khác", 1, result[5], result[5]))
        self.tree.insert("", "end", values=("Giảm giá", 1, result[7], result[7]))
        self.total_label.config(text=f"Tổng cộng: {tongchiphi:,} VNĐ")

    def get_hoadon_data(self):
        # Gather necessary data to create a new invoice
        data_hoadon = self.controller.load_thongtin_hoadon()

        return data_hoadon

    def show_success_message(self, message):
        messagebox.showinfo("Thành công", message)




if __name__ == '__main__':
    root = tk.Tk()
    CreateHoadon_XuatHoaDon(root, 4, 2)
    root.mainloop()