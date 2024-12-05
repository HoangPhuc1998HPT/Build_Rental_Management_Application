
import tkinter as tk
from tkinter import ttk


from backend.models.hoadon import Hoadon


class Admin_show_all_hoadon():
    def __init__(self, root):
        self.root = root
        self.root.title("Danh sách hóa đơn")
        self.root.geometry("1400x800")

        tk.Label(self.root, text="Danh sách hoá đơn", font=('Arial', 14, "bold")).pack(pady=10)

        #quaylai_button = tk.Button(self.root, text="Quay lại", command=lambda: self.go_to_Dashboardchutro(), anchor="w",
        #                           width=10, height=2)
        #quaylai_button.place(x=10, y=10, width=80, height=30)
        # cần chỉnh sửa lại button

        self.tree_show_hoa_don = ttk.Treeview(self.root, columns=("Tên Phòng", "Họ tên chủ trọ", "Họ và tên người thuê", "Số điện thoại", "Tổng chi phí","Ngày xuất hóa đơn"), show="headings", height=25)


        self.tree_show_hoa_don.heading("Tên Phòng", text="Tên Phòng")  # ==> Id phòng --> TTPhong --> Tên phòng
        self.tree_show_hoa_don.heading("Họ tên chủ trọ", text="Họ tên chủ trọ")
        self.tree_show_hoa_don.heading("Họ và tên người thuê",text="Họ và tên người thuê")  # IDPhong -->TTPhong ==> Id người thuê ==>  NguoiThueTrọ
        self.tree_show_hoa_don.heading("Số điện thoại",text="Số điện thoại")  # IDPhong --> TTPhong ==> Id người thuê ==> NguoiThueTrọ
        self.tree_show_hoa_don.heading("Tổng chi phí", text="Tổng chi phí")  # Hóa đơn ==> bill
        self.tree_show_hoa_don.heading("Ngày xuất hóa đơn", text="Ngày xuất hóa đơn")  # Hóa đơn ==> bill
        # self.tree_show_hoa_don.heading("Xem chi tiết hóa đơn", text="Xem chi tiết hóa đơn") # tạo link liên kết mở Xuất hóa đơn

        self.tree_show_hoa_don.column("Tên Phòng", width=200)
        self.tree_show_hoa_don.column("Họ tên chủ trọ", width=200)
        self.tree_show_hoa_don.column("Họ và tên người thuê", width=200)
        self.tree_show_hoa_don.column("Số điện thoại", width=150)
        self.tree_show_hoa_don.column("Tổng chi phí", width=150)
        self.tree_show_hoa_don.column("Ngày xuất hóa đơn", width=150)

        self.tree_show_hoa_don.pack(pady=20)
        self.tree_show_hoa_don.bind("<Double-1>", self.on_row_click)
        self.Xem_danh_sach_tat_ca_cac_hoadon()

    def Xem_danh_sach_tat_ca_cac_hoadon(self):
        result = Hoadon.get_info_all_hoadon()
        self.tree_show_hoa_don.delete(*self.tree_show_hoa_don.get_children())
        for row in result:
            self.tree_show_hoa_don.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5]), tags=(row[6], row[7], row[8]))

    def on_row_click(self, event):
        # Kiểm tra xem có mục nào được chọn không
        selection = self.tree_show_hoa_don.selection()
        if selection:
            item = selection[0]
            print(f"Chọn dòng: {selection}")
            bill_id = self.tree_show_hoa_don.item(item, "tags")[0]  # BillID stored in tags
            id_phong = self.tree_show_hoa_don.item(item, "tags")[2]
            id_chutro=self.tree_show_hoa_don.item(item, "tags")[1]

            # Gọi hàm Xemchitiethoadon và truyền self.root
            self.Xemchitiethoadon(bill_id,id_chutro, id_phong)
        else:
            print("Không có mục nào được chọn.")


    def Xemchitiethoadon(self, bill_id, id_chutro, id_phong):
        from frontend.views.show_detail_hoadon import Show_detall_hoadon
        Show_detall_hoadon(self.root, bill_id, id_chutro, id_phong)


if __name__ == "__main__":
    root = tk.Tk()
    app = Admin_show_all_hoadon(root)
    root.mainloop()