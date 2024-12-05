import tkinter as tk

from backend.models.nguoithuetro import NguoiThueTro
from Controller.navigation_until import go_to_show_danh_sach_nhatro
from backend.utils import get_username_from_id_chutro


class CreateRoomThemnguoithue:
    def __init__(self, root, id_chutro,id_phong):
        self.root = root
        self.root.title("Tạo phần trọ")
        self.id_chutro = id_chutro
        self.id_phong = id_phong
        self.username = get_username_from_id_chutro(id_chutro)
        self.root.geometry("400x400")
        # thêm ngươi thuê vào phòng trọ
        # Các trường nhập thông tin người được thuê
        tk.Label(self.root, text="Nhập CCCD người thuê trọ:").pack(pady=10)
        self.cccd_entry = tk.Entry(self.root, width=30)
        self.cccd_entry.pack(pady=10)
        # nút tìm người thuê trọ

        tk.Button(self.root, text="Thêm người thuê", command=self.go_to_verify_and_update_view).pack(pady=10)

        tk.Button(self.root, text="Quay lại", command=lambda : go_to_show_danh_sach_nhatro(self.root, self.username)).pack(pady=10)
        # nút quay lại

    def go_to_verify_and_update_view(self):
        cccd = self.cccd_entry.get().strip()
        NguoiThueTro.verify_and_update(self.root,self.id_chutro,self.id_phong,cccd)





if __name__ == '__main__':
    root = tk.Tk()
    CreateRoomThemnguoithue(root,2,7)
    root.mainloop()