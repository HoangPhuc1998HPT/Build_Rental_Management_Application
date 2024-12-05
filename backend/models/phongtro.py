from tkinter import messagebox

import pyodbc


from backend.models.db import create_database_connection


class PhongTro:
    def __init__(self,idPhong, ten_phong, address, giadien, gianuoc, giaphong,id_chutro ,sodienhientai = None, sonuochientai = None , id_nguoithue=None, tinhtrang=None):
        self.__idPhong = idPhong
        self.__ten_phong = ten_phong
        self.__address = address
        self.__giadien = giadien
        self.__gianuoc = gianuoc
        self.__giaphong = giaphong
        self.__sodienhientai = sodienhientai
        self.__sonuochientai = sonuochientai
        self.__id_chutro = id_chutro
        self.__id_nguoithue = id_nguoithue
        self.__tinhtrang = tinhtrang

    @property
    def idPhong(self):
        return self.__idPhong

    @property
    def ten_phong(self):
        return self.__ten_phong
    @property
    def address(self):
        return self.__address
    @property
    def giadien(self):
        return self.__giadien
    @property
    def gianuoc(self):
        return self.__gianuoc
    @property
    def giaphong(self):
        return self.__giaphong
    @property
    def sodienhientai(self):
        return self.__sodienhientai
    @property
    def sonuochientai(self):
        return self.__sonuochientai
    @property
    def id_chutro(self):
        return self.__id_chutro
    @property
    def id_nguoithue(self):
        return self.__id_nguoithue
    @property
    def tinhtrang(self):
        return self.__tinhtrang

    @ten_phong.setter
    def ten_phong(self, ten_phong):
        self.__ten_phong = ten_phong

    @address.setter
    def address(self, address):
        self.__address = address
    @giadien.setter
    def giadien(self, giadien):
        self.__giadien = giadien
    @gianuoc.setter
    def gianuoc(self, gianuoc):
        self.__gianuoc = gianuoc
    @giaphong.setter
    def giaphong(self, giaphong):
        self.__giaphong = giaphong

    @sodienhientai.setter
    def sodienhientai(self, sodienhientai):
        if sodienhientai is not None:
            self.__sodienhientai = sodienhientai
        else:
            self.__sodienhientai = 0

    @sonuochientai.setter
    def sonuochientai(self, sonuochientai):
        if sonuochientai is not None:
            self.__sonuochientai = sonuochientai
        else:
            self.__sonuochientai = 0

    @tinhtrang.setter
    def tinhtrang(self, tinhtrang):
        if tinhtrang is not None:
            self.__tinhtrang = 'Trống'

    @staticmethod
    def get_room_list_from_db(id_chutro):
        connection = create_database_connection()
        room_list = []
        if connection:
            try:
                cursor = connection.cursor()
                query = '''SELECT IDPhong, TenPhong FROM TTPhongtro WHERE IDChutro = ?'''
                cursor.execute(query, (id_chutro,))  # Correctly passing an integer IDChutro
                result = cursor.fetchall()
                for row in result:
                    room = {
                        'IDPhong': row[0],
                        'TenPhong': row[1],
                    }
                    room_list.append(room)
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn phòng trọ: {e}")
            finally:
                connection.close()
        return room_list

    def save_room(root,ten_phong, address, giadien, gianuoc, giaphong, id_chutro, username):
        connection = create_database_connection()
        from Controller.navigation import go_to_back_dashboard_chutro
        if connection:
            try:
                cursor = connection.cursor()
                query = '''
                   INSERT INTO TTPhongtro (TenPhong, Address, Giadien, GIanuoc, GiaPhong, IDChutro) 
                   VALUES (?, ?, ?, ?, ?, ?)'''
                cursor.execute(query, (ten_phong, address, giadien, gianuoc, giaphong, id_chutro))
                connection.commit()
                messagebox.showinfo("Thành công", "Phòng trọ đã được thêm!")
                go_to_back_dashboard_chutro(root, username)
            except pyodbc.Error as e:
                print(f"Lỗi khi thêm phòng trọ: {e}")
            finally:
                connection.close()

    def verify_and_update(root,id_chutro,id_phong,sodienhientai,sonuochientai):
        connection = create_database_connection()
        from Controller.navigation_until import go_back_to_create_show_rooms_view
        if connection:
            try:
                cursor = connection.cursor()
                query = "UPDATE TTPhongtro SET Sodienhientai = ?, Sonuochientai = ? WHERE IDPhong = ?"
                cursor.execute(query, (sodienhientai, sonuochientai,id_phong))
                connection.commit()
                messagebox.showinfo("Thống báo", "Số điện hiện tại và Số nước hiện tại đã được cập nhật")
                go_back_to_create_show_rooms_view(root,id_chutro)
            except pyodbc.Error as e:
                print(f"Loại khi truy vấn số điện hiện tại và số nước hiện tại: {e}")
            finally:
                connection.close()

    @staticmethod
    def getgiadien(id_phong):
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT Giadien FROM TTPhongtro WHERE IDPhong = ?"
                cursor.execute(query, (id_phong,))
                result = cursor.fetchone()
                if result:
                    return result[0]
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
            finally:
                connection.close()
        return 0  # Giá trị mặc định nếu không có dữ liệu

    @staticmethod
    def getgianuoc(id_phong):
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT Gianuoc FROM TTPhongtro WHERE IDPhong = ?"
                cursor.execute(query, (id_phong,))
                result = cursor.fetchone()
                if result:
                    return result[0]
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
            finally:
                connection.close()
        return 0  # Giá trị mặc định nếu không có dữ liệu
    @staticmethod
    def get_info_all_phongtro() -> object:
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = '''
                        SELECT 
                            TTphongtro.Tenphong, TTphongtro.Address, TTphongtro.Giaphong, Chutro.Hoten, NguoiThueTro.Hoten, TTphongtro.idphong
                        FROM
                            TTphongtro
                        JOIN
                            Chutro ON TTphongtro.Idchutro = Chutro.IDchutro 
                        JOIN
                            NguoiThueTro ON TTphongtro.IDnguoithue = NguoiThueTro.IDnguoithue
                            
                        '''
                cursor.execute(query)
                return cursor.fetchall()
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
            finally:
                connection.close()

