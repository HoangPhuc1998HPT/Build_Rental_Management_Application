import tkinter as tk
from datetime import datetime
from tkinter import messagebox

from Controller.hoadonController import HoadonController
from backend.models.cthd import CTHD
from backend.models.nguoithuetro import NguoiThueTro
from backend.utils import get_id_nguoithue_from_id_phong,get_id_chutro_from_id_phong


class CreateHoadon_update:

# class này dùng đẻ update dữ liệu cho chi tiết hóa đơn ==> phục vụ cho xuất hóa đơn
# được chuyển hướng từ createShowRoomsView nên sẽ có id_phòng

    def __init__(self, root, id_phong):
        self.root = root
        self.id_phong = id_phong
        self.root.title("Tạo hóa đơn")
        self.root.geometry("600x1000")
        self.id_chutro = get_id_chutro_from_id_phong(id_phong)

        # Các trường nhap thong tin
        tk.Label(self.root, text="Hóa đơn phòng {}".format(self.id_phong)).pack(pady=5)

        tk.Label(self.root, text="Tên hóa đơn").pack(pady=5)
        self.entry_tenhoadon = tk.Entry(self.root, width=30)
        self.entry_tenhoadon.pack(pady=5)

        # ==> Tên hóa đơn sẽ được lưu vào bảng CTHD với tên ghichu

        tk.Label(self.root, text="Nhập ngày dự kiến thu tiền trọ").pack(pady=5)
        self.entry_ngaydukienthutien = tk.Entry(self.root, width=30)
        self.entry_ngaydukienthutien.pack(pady=5)
        # Nút "Tính toán" sẽ tính toán sau khi nhập ngày dự kiến thu tiền trọ

        tk.Button(self.root, text="Tính toán", command= lambda :self.hien_thi_ket_qua()).pack(pady=5)
        # Hiển thị số ngày ở trong tháng tính đến thời điểm dự kiến thu tiền trọ

        # Hiển thị chi phí phát sinh 1
        tk.Label(self.root, text = " Chi phí phát sinh 1 ").pack(pady=5)
        self.entry_chiphiphatsinh1 = tk.Entry(self.root, width=30)
        self.entry_chiphiphatsinh1.pack(pady=5)

        # Hiển thị chí phí phát sinh 2
        tk.Label(self.root, text = " Chi phí phát sinh 2 ").pack(pady=5)
        self.entry_chiphiphatsinh2 = tk.Entry(self.root, width=30)
        self.entry_chiphiphatsinh2.pack(pady=5)

        # chi phí phát sinh = chi phí phát sinh 1  + chi phí phát sinh 2


        # Hển thị chi phí tiền rác
        tk.Label(self.root, text = " Chi phí tiền rác ").pack(pady=5)
        self.entry_chiphirac = tk.Entry(self.root, width=30)
        self.entry_chiphirac.pack(pady=5)


        # Hiển thị giảm giá
        tk.Label(self.root, text = " Giảm giá ").pack(pady=5)
        self.entry_giamgia = tk.Entry(self.root, width=30)
        self.entry_giamgia.pack(pady=5)

        # Các trường hiển thị kết quả
        self.label_sodienthangtruoc = tk.Label(self.root, text="")
        self.label_sodienthangtruoc.pack(pady=5)

        self.label_sonuocthangtruoc = tk.Label(self.root, text="")
        self.label_sonuocthangtruoc.pack(pady=5)

        self.label_sodiendasudung = tk.Label(self.root, text="")
        self.label_sodiendasudung.pack(pady=5)

        self.label_sonuocdasudung = tk.Label(self.root, text="")
        self.label_sonuocdasudung.pack(pady=5)

        self.label_tiennha = tk.Label(self.root, text="")
        self.label_tiennha.pack(pady=5)

        tk.Button(self.root, text="Nhập dữ liệu", command=lambda: self.tao_CTHD(self.id_phong)).pack(pady=5)
        from Controller.navigation_until import go_back_to_create_show_rooms_view
        tk.Button(self.root, text="Quay lại", command=lambda: go_back_to_create_show_rooms_view(self.root,self.id_chutro)).pack(pady=5)

        # Nhập ngày dự kiến thu tiền trọ - sẽ là ngày xuất hóa đơn

        # insert vào hoadon Ngayxuathoadon with idCTHD

        # Nhập số ngày ở trong tháng

            # xử lý nếu ngày ở tính từ ngày được cập nhật nhận phòng đủ 30 ngày trở lên tính tròn tháng
            # Với tháng 2 đủ 28 ngày trở lên tính tròn tháng
            # Xuất ngày nhận phòng ở NguoiThueTro.Ngaybatdauthue
            # số ngày ở  = ngày dự kiến thu tiền trọ - NguoiThueTro.Ngaybatdauthue

        # Hiển thị tiền nhà thêm nút cho phép cập nhật

    # xử lý tính toán số điện đã sử dụng và số khối nước đã sử dụng cho hiển thị lên

    # xử lý tiền nhà
    def tao_CTHD(self,id_phong):

        entry_data = self.get_all_entries()
        chiphirac = entry_data["chi_phi_rac"]
        giamgia = entry_data["giamgia"]
        ghichu = entry_data["ghichu"]
        chiphiphatsinh = entry_data["chi_phi_phat_sinh"]
        thang, nam = self.get_entry_ngay_thang_nam()

        ngaydutinhthutien = self.entry_ngaydukienthutien.get()
        sodien_use = int(CTHD.get_sodien_dasudung(thang, nam,self.id_phong)) if CTHD.get_sodien_dasudung else 0
            #print("số diện sử dụng: ", sodien_use) #OK
        sonuoc_use = int(CTHD.get_sonuocdasudung(thang, nam,self.id_phong)) if CTHD.get_sonuocdasudung else 0
            #print("số nước sử dụng: ", sonuoc_use) #Ok
        so_ngay_o_trong_thang = NguoiThueTro.Xu_Ly_So_ngay_o_trong_thang(get_id_nguoithue_from_id_phong(self.id_phong),ngaydutinhthutien)
            #print("so ngày o trong tháng: ", so_ngay_o_trong_thang) #OK
        tien_nha =float( CTHD.get_tien_nha_from_TTPhong(id_phong))
            #print("tiền nha: ", tien_nha) #OK
            #print("tiền chi phi phat sinh: ", chiphiphatsinh) #OK
        sodienthangtruoc = int(CTHD.get_sodien_thangtruoc(thang, nam, self.id_phong))
            # print(so dienthangtruoc: ", sodienthangtruoc)
        sonuocthangtruoc = int(CTHD.get_sonuoc_thangtruoc(thang, nam, self.id_phong))
            # print("so nuocthangtruoc: ", sonuocthangtruoc)

        ngayxuathoadon = datetime.strptime(self.entry_ngaydukienthutien.get(), '%d-%m-%Y').strftime('%Y-%m-%d')
        #print("ngày xuất hóa đơn: ", ngayxuathoadon)
        # gọi hàm lưu vào cơ sở dữ liệu
        CTHD.save_CTHD(sodien_use, sonuoc_use, so_ngay_o_trong_thang, tien_nha, chiphiphatsinh, chiphirac,
                  giamgia, sodienthangtruoc, sonuocthangtruoc, self.id_phong, ghichu, ngayxuathoadon)


    def get_all_entries(self):
        chi_phi_rac = float(self.entry_chiphirac.get()) if self.entry_chiphirac.get() else 0
        giamgia = float(self.entry_giamgia.get()) if self.entry_giamgia.get() else 0
        ghichu = self.entry_tenhoadon.get()
        chi_phi_phat_sinh_1 = self.entry_chiphiphatsinh1.get()
        chi_phi_phat_sinh_2 = self.entry_chiphiphatsinh2.get()
        chi_phi_phat_sinh = HoadonController.xu_ly_chiphiphatsinh(chi_phi_phat_sinh_1, chi_phi_phat_sinh_2)

        return {
            "chi_phi_rac": chi_phi_rac,
            "giamgia": giamgia,
            "ghichu": ghichu,
            "chi_phi_phat_sinh": chi_phi_phat_sinh
        }

    def get_entry_ngay_thang_nam(self):
        ngay_du_kien = datetime.strptime(self.entry_ngaydukienthutien.get(), '%d-%m-%Y')
        thang, nam = HoadonController.get_ngay_thang_nam(ngay_du_kien)
        return thang, nam


    def hien_thi_ket_qua(self):
        thang , nam = self.get_entry_ngay_thang_nam()
        """Hiển thị kết quả số điện và số nước sau khi tính toán"""
        sodienthangtruoc = CTHD.get_sodien_thangtruoc((thang-1), nam,self.id_phong)  # Tính toán dựa trên tháng và năm
        sonuocthangtruoc = CTHD.get_sonuoc_thangtruoc((thang-1), nam,self.id_phong)  #CTHD.get_sonuoc_thangtruoc(self.ngay_du_kien.month, self.ngay_du_kien.year,self.id_phong)
        sodiendasudung = CTHD.get_sodien_dasudung(thang, nam,self.id_phong)
        sonuocdasudung = CTHD.get_sonuocdasudung(thang, nam, self.id_phong)
        tiennha = CTHD.get_tien_nha_from_TTPhong(self.id_phong)

        self.label_sodienthangtruoc.config(text="Chỉ số điện tháng trước: {}".format(sodienthangtruoc))
        self.label_sonuocthangtruoc.config(text="Chỉ số nước tháng trước: {}".format(sonuocthangtruoc))
        self.label_sodiendasudung.config(text="Số điện đã sử dụng: {}".format(sodiendasudung))
        self.label_sonuocdasudung.config(text="Số nước đã sử dụng: {}".format(sonuocdasudung))
        self.label_tiennha.config(text = " Tiền thuê nhà:{:,.0f} VNĐ".format(tiennha))
    # Lấy số điện tháng trước




    # xử lý số điện đã sử dụng

    # Xử lý số nước đã xử dụng



    # Xử lý lưu được database

      # Xử lý lấy số điện nước tháng trước





if __name__ == '__main__':
    root = tk.Tk()
    CreateHoadon_update(root, 2)
    root.mainloop()