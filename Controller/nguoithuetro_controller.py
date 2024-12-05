import tkinter as tk
from backend.models.db import create_database_connection
from backend.utils import Get_id_nguoithue_from_username, Get_id_phongtro_from_id_nguoithue, info_show_danh_sach_hoadon
from frontend.views.show_detail_hoadon import Show_detall_hoadon

class NguoithueController:
    def __init__(self, root, view, username):
        self.root = root
        self.view = view
        self.username = username
        self.id_nguoithue = Get_id_nguoithue_from_username(self.username)
        self.id_phongtro, self.id_chutro = Get_id_phongtro_from_id_nguoithue(self.id_nguoithue) or (None, None)
        #info_show_danh_sach_hoadon(id_nguoithue)

    def show_danh_sach_hoadon(self, tree):
        result = info_show_danh_sach_hoadon(self.id_nguoithue)
        print(f"ID Người thuê: {self.id_nguoithue}")
        #Hoadon.Ngayxuathoadon, HoaDon.BillID, CTHoadon.ghichu, Hoadon.Tongchiphi, TTPhongtro.TenPhong,TTphongtro.Address, Chutro.hoten, Chutro.Phone
        if result:
            tree.delete(*tree.get_children())
            for row in result:         # TenPhong,Address,hoten,Phone
                self.view.update_phongtro_info(row[4], row[5], row[6], row[7])
                                        #Ngayxuathoadon, BillID, ghichu, Tongchiphi
                tree.insert("", "end", values=(row[0], row[1], row[2], row[3]), tags=(row[1],))
        else:
            print("Chưa có hóa đơn")


    def on_row_double_click(self, tree, event):
        item = tree.selection()[0]  # Lấy dòng được chọn
        bill_id = tree.item(item, "values")[1]  # Lấy BillID từ cột thứ hai
        self.open_bill_detail(bill_id)

    def open_bill_detail(self, bill_id):
        Show_detall_hoadon(self.root, bill_id, self.id_chutro, self.id_phongtro)
