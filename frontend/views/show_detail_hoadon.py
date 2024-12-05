from tkinter import ttk
import tkinter as tk
import pyodbc

from backend.models.db import create_database_connection
from backend.utils import info_show_detail_hoadon



class Show_detall_hoadon():
    def __init__(self, root, id_hoadon, id_chutro, id_phong):
        # Gọi __init__ của lớp cha và truyền các đối số cần thiết
        self.new_window = tk.Toplevel(root)
        self.new_window.title("Xem chi tiết hóa đơn")
        self.id_hoadon = id_hoadon
        self.id_chutro = id_chutro
        self.id_phong = id_phong
        self.new_window.geometry("660x880")

        tk.Label(self.new_window, text="HÓA ĐƠN", font=("Arial", 18, "bold")).pack(pady=10)

        tk.Label(self.new_window, text=" Thông tin hóa đơn", font=("Arial", 14, "bold")).pack(pady=10)

        # Thông tin hoa don
        self.Label_Sohoadon = tk.Label(self.new_window, text="", font=("Arial", 12), anchor="w")
        self.Label_Sohoadon.pack(fill='x', padx=100, pady=5)

        self.Label_Ngayxuathoadon = tk.Label(self.new_window, text="", font=("Arial", 12), anchor="w")
        self.Label_Ngayxuathoadon.pack(fill='x', padx=100, pady=5)

        self.Label_Ghichu = tk.Label(self.new_window, text="", font=("Arial", 12), anchor="w")
        self.Label_Ghichu.pack(fill='x', padx=100, pady=5)



        # Nội dung cơ sở dữ liệu

        self.tree_info = ttk.Treeview(self.new_window, columns=("Họ tên", "Vai trò", "CCCD", "Số điện thoại"), show="headings",height = 3)

        self.tree_info.heading("Họ tên", text="Họ tên")
        self.tree_info.heading("Vai trò", text="Vai trò")
        self.tree_info.heading("CCCD", text="CCCD")
        self.tree_info.heading("Số điện thoại", text="Số điện thoại")

        self.tree_info.column("Họ tên", width=150)
        self.tree_info.column("Vai trò", width=80, anchor="center")
        self.tree_info.column("CCCD", width=100, anchor="center")
        self.tree_info.column("Số điện thoại", width=120, anchor="center")

        self.tree_info.pack(pady=10)

# Phần thân: Nội dung hóa đơn
        tk.Label(self.new_window, text="Nội dung hóa đơn", font=("Arial", 14, "bold")).pack(pady=20)

        # Bảng nội dung hóa đơn
        self.tree = ttk.Treeview(self.new_window, columns=("Nội dung", "Số lượng", "Đơn giá", "Thành tiền"), show="headings",height = 7)
        self.tree.heading("Nội dung", text="Nội dung")
        self.tree.heading("Số lượng", text="Số lượng")
        self.tree.heading("Đơn giá", text="Đơn giá")
        self.tree.heading("Thành tiền", text="Thành tiền")

        self.tree.column("Nội dung", width=150)
        self.tree.column("Số lượng", width=80, anchor="center")
        self.tree.column("Đơn giá", width=100, anchor="center")
        self.tree.column("Thành tiền", width=120, anchor="center")

        self.tree.pack(pady=10)

        # Tổng cộng
        self.total_label = tk.Label(self.new_window, text="Tổng cộng: 0 VNĐ", font=("Arial", 12, "bold"))
        self.total_label.pack(pady=5)
        self.load_thongtin_hoadon()

    def load_thongtin_hoadon(self):
        connection = create_database_connection()
        if connection:
            try:
                result, result1, result2, result3 = info_show_detail_hoadon(self.id_hoadon,connection)
                if result and result1 and result2 and result3:
                    #thong tin hóa đơn
                    self.Label_Sohoadon.config(text=f"Số hóa đơn: {result[0]}")
                    self.Label_Ngayxuathoadon.config(text=f"Ngày xuất hóa đơn: {result[8]}")

                    self.Label_Ghichu.config(text=f"Ghi chú: {result1[4]}")

                    # chủ trọ
                    self.tree_info.insert("", "end", values=(result2[1], "Chủ trọ", result2[2], result2[3]))
                    # người thuê
                    self.tree_info.insert("", "end", values=(result3[1], "Ngưởi thuê", result3[2], result3[3]))
                    # Nội dung hóa đơn
                    self.tree.insert("", "end", values=("Tiền thuê phòng", 1, result[1], result[1]))
                    self.tree.insert("", "end",
                                         values=("Tiền điện", result1[0], result1[2], result[2])) # cho truy xuat gia dien
                    self.tree.insert("", "end",
                                         values=("Tiền nước", result1[1], result1[3], result[3]))
                    self.tree.insert("", "end", values=("Tiền rác", 1, result[4], result[4]))
                    self.tree.insert("", "end", values=("Chi phí khác", 1, result[5], result[5]))
                    self.tree.insert("", "end", values=("Giảm giá", 1, result[6], result[6]))

                    # Tính tổng tiền
                    self.total_label.config(text=f"Tổng cộng: {format(result[7], ',.0f')} VNĐ")
                    return result
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
            finally:
                connection.close()

#if __name__ == '__main__':
    #root = tk.Tk()
    #app = Show_detall_hoadon(root, 4,5#)
    #root.mainloop()