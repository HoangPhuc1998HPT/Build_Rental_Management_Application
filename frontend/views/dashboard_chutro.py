import tkinter as tk

from Controller.navigation import Go_to_xem_danh_sach_hoadon, Go_to_tao_phongtro
from Controller.navigation_until import go_to_show_danh_sach_nhatro


class DashboardChutro:
    def __init__(self,root,username):
        self.get_chutro_id = None
        self.root = root
        self.username = username
        self.root.title("Chủ trọ Dashboard")
        self.root.geometry("1000x600")
        #self.root.resizable(False, False)


        # Nội dung của Dashboard dành cho chủ trọ
        label = tk.Label(self.root, text="Chutro Dashboard", font=('Arial', 13))
        label.pack(pady=20)

        # Các chức năng dành cho chủ trọ...

    # tạo hiển thị các nút và chức năng của chủ trọ

    # tạo view hiển thị chức năng của phòng trọ

        # Nút tạo phòng trọ đã xong
        tk.Button(self.root, text="Tạo phòng trọ", command=lambda: Go_to_tao_phongtro(self.root, self.username)).pack(pady=20)

        # Nút xem danh sách phòng trọ
        tk.Button(self.root, text="Quản lý danh sách phòng trọ", command=lambda: go_to_show_danh_sach_nhatro(self.root, self.username)).pack(pady=20)

        # Nút xem danh sách hóa đơn
        tk.Button(self.root, text="Xem danh sách hóa đơn", command=lambda: Go_to_xem_danh_sach_hoadon(self.root,self.username)).pack(pady=20)

        # Button đăng xuất
        tk.Button(self.root, text="Đăng xuất", command=lambda: self.root.destroy()).pack(pady=20)


if __name__ == '__main__':
    root = tk.Tk()
    #app = DashboardChutro(root,'testchhutro5')
    root.mainloop()