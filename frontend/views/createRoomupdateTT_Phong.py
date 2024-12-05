import tkinter as tk

from Controller.navigation_until import go_back_to_create_show_rooms_view


# cập nhật thông tin phòng + thông tin hóa đơn phòng
# Phòng : số điện hiện tại, số nước hiện tại
class CreateRoomupdateTT_Phong:
    def __init__(self, root, id_chutro, id_phong):
        self.root = root
        self.root.title("Tạo phần trọ")
        self.id_chutro = id_chutro
        self.id_phong = id_phong
        self.root.geometry("400x400")

        # Các trường nhap thong tin phong
        # nhập số điện hiện tại
        tk.Label(self.root, text="Nhập Số điện hiện tại").pack(pady=10)
        self.sodienhientai_entry = tk.Entry(self.root, width=30)
        self.sodienhientai_entry.pack(pady=10)
        # nhập số nước hiện tại
        tk.Label(self.root, text="Nhập Số điện hiện tại").pack(pady=10)
        self.sonuochientai_entry = tk.Entry(self.root, width=30)
        self.sonuochientai_entry.pack(pady=10)

        # button cập nhật

        tk.Button(self.root, text="Cập nhật", command=lambda : self.go_to_verify_and_update()).pack(pady=10)
        tk.Button(self.root, text="Quay lại", command=lambda : go_back_to_create_show_rooms_view(self.root,self.id_chutro)).pack(pady=10)

    def go_to_verify_and_update(self):
        sodienhientai = self.sodienhientai_entry.get()
        sonuochientai = self.sonuochientai_entry.get()
        from backend.models.phongtro import PhongTro
        PhongTro.verify_and_update(self.root, self.id_chutro, self.id_phong, sodienhientai, sonuochientai)



if __name__ == '__main__':
    root = tk.Tk()
    CreateRoomupdateTT_Phong(root, 1, 1)
    root.mainloop()