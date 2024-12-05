import tkinter as tk
from tkinter import ttk
from Controller.navigation_until import go_to_Dashboardchutro
from backend.models.hoadon import Hoadon


class CreateHoadon_showDSHoaDon:


    def __init__(self, root, id_chutro):
        self.root = root
        self.root.title("Xem danh sách hoàn đơn")
        self.id_chutro = id_chutro
        self.root.geometry("1200x600")

        # Nội dung cơ sở dữ liệu
        #self.tree_info = ttk.Treeview(self.root, columns=("Họ tên", "Vai trò", "CCCD", "Số điện thoại"), show="headings",height = 3)
        tk.Label(self.root, text="Danh sách hoá đơn", font=('Arial', 14, "bold")).pack(pady=10)

        quaylai_button = tk.Button(self.root, text="Quay lại", command=lambda: go_to_Dashboardchutro(self.root,self.id_chutro), anchor="w", width=10, height=2)
        quaylai_button.place(x=10, y=10, width=80, height=30)
        # cần chỉnh sửa lại button

        self.tree_show_hoa_don = ttk.Treeview(self.root, columns=("Tên Phòng","Họ và tên người thuê","Số điện thoại","Tổng chi phí","Ngày xuất hoàn đơn"), show="headings", height = 10)
        self.tree_show_hoa_don.heading("Tên Phòng", text="Tên Phòng") # ==> Id phòng --> TTPhong --> Tên phòng
        self.tree_show_hoa_don.heading("Họ và tên người thuê", text="Họ và tên người thuê") # IDPhong -->TTPhong ==> Id người thuê ==>  NguoiThueTrọ
        self.tree_show_hoa_don.heading("Số điện thoại", text="Số điện thoại") # IDPhong --> TTPhong ==> Id người thuê ==> NguoiThueTrọ
        self.tree_show_hoa_don.heading("Tổng chi phí", text="Tổng chi phí") # Hóa đơn ==> bill
        self.tree_show_hoa_don.heading("Ngày xuất hoàn đơn", text="Ngày xuất hoàn đơn")# Hóa đơn ==> bill
        #self.tree_show_hoa_don.heading("Xem chi tiết hóa đơn", text="Xem chi tiết hóa đơn") # tạo link liên kết mở Xuất hóa đơn
        self.tree_show_hoa_don.pack(pady=20)
        self.tree_show_hoa_don.bind("<Double-1>", self.on_row_click)
        self.load_data_hoadon()

        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree_show_hoa_don.yview)
        scrollbar.pack(side="right", fill="y")

        self.tree_show_hoa_don.configure(yscrollcommand=scrollbar.set)

    def load_data_hoadon(self):
        result = Hoadon.get_hoadon_by_chutro(self.id_chutro)
        for row in result:
            self.tree_show_hoa_don.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4],),tags=(row[5],row[6]),)

    def on_row_click(self, event):
        # Kiểm tra xem có mục nào được chọn không
        selection = self.tree_show_hoa_don.selection()
        if selection:
            item = selection[0]
            print(f"Selected item: {selection}")
            bill_id = self.tree_show_hoa_don.item(item, "tags")[0]  # BillID stored in tags
            id_phong = self.tree_show_hoa_don.item(item, "tags")[1]
            # Gọi hàm Xemchitiethoadon và truyền self.root
            self.Xemchitiethoadon(bill_id, self.id_chutro, id_phong)
        else:
            print("Không có mục nào được chọn.")

    def Xemchitiethoadon(self, bill_id, id_chutro, id_phong):
        from frontend.views.show_detail_hoadon import Show_detall_hoadon
        Show_detall_hoadon(self.root, bill_id, id_chutro, id_phong)


if __name__ == '__main__':
    root = tk.Tk()
    app = CreateHoadon_showDSHoaDon(root,4)
    root.mainloop()