
from tkinter import messagebox
from datetime import datetime
from backend.models.db import create_database_connection
from backend.models.phongtro import PhongTro
from backend.models.hoadon import Hoadon
from backend.utils import get_id_nguoithue_from_id_phong

class HoadonController:
    def __init__(self, view, id_chutro, id_phong):
        self.view = view
        self.id_chutro = id_chutro
        self.id_phong = id_phong
        self.giadien = PhongTro.getgiadien(id_phong)
        self.gianuoc = PhongTro.getgianuoc(id_phong)
        self.id_nguoithue = get_id_nguoithue_from_id_phong(id_phong)

    def load_thongtin_hoadon(self):
        # Tạo kết nối tới cơ sở dữ liệu
        connection = create_database_connection()

        if connection:
            try:
                # Truyền kết nối và id_phong vào phương thức
                result = Hoadon.info_load_thongtin_hoadon(connection, self.id_phong)

                if result:
                    tongchiphi = result[4] + result[1] * self.giadien + result[2] * self.gianuoc + result[6] + result[5] - result[7]
                    self.view.update_view(result, self.giadien, self.gianuoc, tongchiphi)
                    return (
                    result[4], result[1] * self.giadien, result[2] * self.gianuoc, result[6], result[5], result[7],
                    tongchiphi, result[12], result[0])
                    # 0-Tiền nhà, 1-Tiền điện 2-Tiền nước 3-Tiền rác,4-Chi phí khác, 5-Giảm giá,6- Tổng chi phí,7-ngày dự kiến, 8-idphon, 9 - billid
            finally:
                # Đảm bảo đóng kết nối sau khi sử dụng
                connection.close()

    def go_to_nhaphoadon(self):
        data_hoadon = self.view.get_hoadon_data()
        if data_hoadon is None:
            messagebox.showerror("Lỗi", "Không tìm thấy dữ liệu hóa đơn để nhập!")
            return
        Hoadon.nhap_hoadon(data_hoadon)
        self.view.show_success_message("Hóa đơn đã được lưu thành công!")

    @staticmethod
    def xu_ly_chiphiphatsinh(chiphiphatsinh1, chiphiphatsinh2):

        # Kiểm tra xem trường chi phí phát sinh có trống không
        chiphiphatsinh1 = float(chiphiphatsinh1) if chiphiphatsinh1 else 0
        chiphiphatsinh2 = float(chiphiphatsinh2) if chiphiphatsinh2 else 0

        chiphiphatsinh = chiphiphatsinh1 + chiphiphatsinh2
        return chiphiphatsinh

    @staticmethod
    def get_ngay_thang_nam(ngay_du_kien):
        """Hàm này sẽ tính toán số điện và số nước sau khi nhấn nút 'Tính toán'"""
        try:
            # Sử dụng biến này để lấy tháng, năm hoặc các thông tin khác
            thang = ngay_du_kien.month  # Lấy tháng
            nam = ngay_du_kien.year  # Lấy năm

            # Truyền thang và nam vào các phép tính
            return thang, nam
        except ValueError:
            messagebox.showerror("Lỗi", "Ngày dự kiến không hợp lệ! Vui lòng nhập theo định dạng DD-MM-YYYY")
