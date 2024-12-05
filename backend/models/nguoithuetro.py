from tkinter import messagebox

import pyodbc
from datetime import datetime
from Controller.login_controller import go_back_to_login

from backend.models.User import User
from backend.models.db import create_database_connection, connection

from backend.models.role import Role
from backend.utils import get_nguoithue_by_cccd


class NguoiThueTro(User):
    def __init__(self, username, password, ho_ten, cccd, phone):
        super().__init__(username, password, Role.NGUOITHUETRO)
        self.__ho_ten = ho_ten
        self.__cccd = cccd
        self.__phone = phone

    # Phương thức lưu người thuê trọ vào CSDL
    def save_info_nguoi_thue(root,user_id,fullname,cccd,phone):
        connection = create_database_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO NguoiThueTro (UserID, hoten, cccd, phone) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, (user_id, fullname, cccd, phone))
        connection.commit()
        connection.close()
        go_back_to_login(root)
    @staticmethod
    def update_room_nguoithue(IDnguoithue, id_phong):
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query1 = '''Update TTPhongtro SET IDnguoithue = ?, Tinhtrang = ?
                                where IDPhong = ?
                                '''  # Giả sử bạn có IDPhong
                cursor.execute(query1, (IDnguoithue,"đã thuê", id_phong))  # Thay 1 bằng ID phòng trọ

                query2 = ''' Update NguoiThueTro SET Ngaybatdauthue = GETDATE()
                                where IDnguoithue = ?'''
                cursor.execute(query2, (IDnguoithue,))
                connection.commit()
                messagebox.showinfo("Thành công", "Đã cập nhật thông tin phòng trọ và ngày thuê!")
            except pyodbc.Error as e:
                messagebox.showerror("Lỗi", f"Lỗi khi cập nhật thông tin phòng trọ: {e}")
            finally:
                connection.close()
        else:
            messagebox.showerror("Lỗi", "Không thể kết nối tới cơ sở dữ liệu")

    @staticmethod
    def verify_and_update(root,id_chutro,id_phong,cccd):
        if not cccd:
            messagebox.showerror("Loại", "Vui lý nhap CCCD!")
            return
        # kiểm tra CCCD trong cơ sở dữ liệu
        # thong_tin_nguoithue = [IDnguoithue, Hoten, UserID]
        thong_tin_nguoi_thue = get_nguoithue_by_cccd(cccd)
        # thong_tin_nguoi_thue[0] = IDnguoithue - thong_tin_nguoi_thue[1] = Họ ten - thong_tin_nguoi_thue[2]= user I

        if thong_tin_nguoi_thue:
            IDnguoithue, Hoten, UserID = thong_tin_nguoi_thue
            # Nếu tìm thấy người thuê, cập nhật thông tin thuê trọ
            NguoiThueTro.update_room_nguoithue(IDnguoithue ,id_phong)
            messagebox.showinfo("Thành công", "Đã thêm người thuê trọ!")
            from Controller.navigation_until import go_back_to_create_show_rooms_view
            go_back_to_create_show_rooms_view(root,id_chutro)
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy người thuê trọ với CCCD này!")

    def load_thongtin_nguoithue(self, id_nguoithue,tree_info):
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT * FROM NguoiThueTro WHERE IDnguoithue = ?"
                cursor.execute(query, (id_nguoithue,))
                result = cursor.fetchone()
                if result:
                    tree_info.insert("", "end", values=(result[1], "Ngưởi thuê", result[2], result[3]))
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
            finally:
                connection.close()

    @staticmethod
    def Xu_Ly_So_ngay_o_trong_thang(id_nguoithuetro,ngaydutinhthutien):
        # lấy ngày tính thu tiền - ngày được thêm vào phòng
        #ngaydutinhthutien = self.entry_ngaydukienthutien.get()

        try:
            # Chuyển đổi ngày dự kiến thu tiền sang định dạng datetime để tính toán
            ngaydutinhthutien = datetime.strptime(ngaydutinhthutien, '%d-%m-%Y')
        except ValueError:
            messagebox.showerror("Lỗi", "Ngày dự kiến thu tiền không hợp lệ. Vui lòng nhập theo định dạng DD-MM-YYYY.")
            return 0

        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = '''
                        SELECT Nguoithuetro.Ngaybatdauthue
                        FROM Nguoithuetro
                        WHERE Nguoithuetro.IDnguoithue = ?
                        '''
                cursor.execute(query, (id_nguoithuetro,))
                result = cursor.fetchone()

                if result:
                    ngaybatdauthue = result[0]

                    # Chuyển đổi `Ngaybatdauthue` từ CSDL thành dạng `datetime`
                    ngaybatdauthue = datetime.strptime(str(ngaybatdauthue), '%Y-%m-%d')

                    # Tính toán số ngày ở bằng cách lấy hiệu giữa `ngaydutinhthutien` và `ngaybatdauthue`
                    so_ngay_o = (ngaydutinhthutien - ngaybatdauthue).days
                    return so_ngay_o
                else:
                    return 0  # Nếu không có kết quả, trả về 0 hoặc một giá trị mặc định
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
            finally:
                connection.close()
        return 0
    @staticmethod
    def get_info_all_nguoithue():
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = '''
                        SELECT 
                            Users.username, NguoiThueTro.Hoten, NguoiThueTro.cccd, NguoiThueTro.phone, TTphongtro.Tenphong
                        FROM 
                            NguoiThueTro
                        JOIN 
                            TTphongtro ON NguoiThueTro.IDnguoithue = TTphongtro.IDnguoithue
                        JOIN 
                            Users ON NguoiThueTro.UserID = Users.UserID
        
                        '''
                cursor.execute(query)
                return cursor.fetchall()
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
            finally:
                connection.close()

    @staticmethod
    def get_ten_nguoi_thue_in_room(id_phong):
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = '''
                    SELECT Nguoithuetro.Hoten
                    FROM nguoithuetro
                    JOIN TTPhongtro ON TTPhongtro.idnguoithue = Nguoithuetro.idnguoithue
                    WHERE TTPhongtro.IDPhong = ?
                '''
                cursor.execute(query, (id_phong,))
                result = cursor.fetchone()
                if result:
                    return result[0]  # Return the tenant's name
                else:
                    return None  # If no result is found
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
                return None
            finally:
                connection.close()
        else:
            messagebox.showerror("Lỗi", "Không thể kết nối tới cơ sở dữ liệu")
            return None

                

