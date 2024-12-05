import pyodbc

from backend.models.db import create_database_connection


class Hoadon:
    def __init__(self,BillID, tiennha, tiendien, tiennuoc, tienrac, chiphikhac, giamgia, Ngayxuathoadon, id_phong,id_cthd):
        self.__BillID = BillID
        self.__tiennha = tiennha
        self.__tiendien = tiendien
        self.__tiennuoc = tiennuoc
        self.__tienrac = tienrac
        self.__chiphikhac = chiphikhac
        self.__giamgia = giamgia
        self.__ngayxuathoadon = Ngayxuathoadon
        self.__id_phong = id_phong
        self.__id_cthd = id_cthd
        tongchiphi = self.__tiennha + self.__tiendien + self.__tiennuoc + self.__tienrac + self.__chiphikhac - self.__giamgia


    @property
    def BillID(self):
        return self.__BillID

    @property
    def Ngayxuathoadon(self):  # Use consistent case
        return self.__ngayxuathoadon

    @property
    def idCTHD(self):
        return self.__id_cthd
    @property
    def tiennha(self):
        return self.__tiennha

    @property
    def tiendien(self):
        return self.__tiendien

    @property
    def tiennuoc(self):
        return self.__tiennuoc

    @property
    def tienrac(self):
        return self.__tienrac

    @property
    def chiphikhac(self):
        return self.__chiphikhac

    @property
    def giamgia(self):
        return self.__giamgia

    @property
    def id_phong(self):
        return self.__id_phong

    #setter
    @tiennha.setter
    def tiennha(self, tiennha):
        if tiennha is not None:
            self.__tiennha = tiennha
        else:
            self.__tiennha = 0


    @tiendien.setter
    def tiendien(self, tiendien):
        if tiendien is not None:
            self.__tiendien = tiendien
        else:
            self.__tiendien = 0

    @tiennuoc.setter
    def tiennuoc(self, tiennuoc):
        if tiennuoc is not None:
            self.__tiennuoc = tiennuoc
        else:
            self.__tiennuoc = 0

    @tienrac.setter
    def tienrac(self, tienrac):
        if tienrac is not None:
            self.__tienrac = tienrac
        else:
            self.__tienrac = 0

    @chiphikhac.setter
    def chiphikhac(self, chiphikhac):
        if chiphikhac is not None:
            self.__chiphikhac = chiphikhac
        else:
            self.__chiphikhac = 0

    @Ngayxuathoadon.setter  # The setter must match the property name
    def Ngayxuathoadon(self, Ngayxuathoadon):
        if Ngayxuathoadon is not None:
            self.__ngayxuathoadon = Ngayxuathoadon
        else:
            self.__ngayxuathoadon = None


    @giamgia.setter
    def giamgia(self, giamgia):
        if giamgia is not None:
            self.__giamgia = giamgia
        else:
            self.__giamgia = 0

    @staticmethod
    def info_load_thongtin_hoadon(connection, id_phong):
        cursor = connection.cursor()
        query = '''
                SELECT TOP 1 *
                FROM CTHoadon
                WHERE IDPhong = ?
                ORDER BY Ngaythutiendukien DESC
            '''
        cursor.execute(query, (id_phong,))
        return cursor.fetchone()


    def update_hoadon(self, id_phong):
        print(f"Cập nhật hóa đơn cho phòng {id_phong}")
        pass
    def xuat_hoadon(self, id_phong):
        print(f"Xuất hóa đơn cho phòng {id_phong}")
        pass

    @staticmethod
    def nhap_hoadon(data_hoadon):
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO HoaDon (Tiennha,Tiendien ,Tiennuoc, Tienrac, Chiphikhac, Giamgia, Tongchiphi, Ngayxuathoadon, idCTHD) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
                cursor.execute(query, (
                data_hoadon[0], data_hoadon[1], data_hoadon[2], data_hoadon[3], data_hoadon[4], data_hoadon[5],
                data_hoadon[6], data_hoadon[7], data_hoadon[8]))
                connection.commit()
                print("Hóa đơn đã được nhập thành công!")
            except pyodbc.Error as e:
                print(f"Lỗi khi thêm hóa đơn: {e}")
            finally:
                connection.close()
    @staticmethod
    def get_hoadon_by_chutro(id_chutro):
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = '''
                    SELECT 
                        TTPhongtro.TenPhong, 
                        NguoiThueTro.Hoten, 
                        NguoiThueTro.Phone, 
                        HoaDon.Tongchiphi, 
                        HoaDon.Ngayxuathoadon,
                        HoaDon.BillID,
                        TTPhongtro.Idchutro,
                        CTHoaDon.Idphong
                    FROM 
                        TTPhongtro
                    JOIN 
                        NguoiThueTro ON TTPhongtro.IDnguoithue = NguoiThueTro.IDnguoithue
                    JOIN
                        CTHoadon ON CTHoadon.IDPhong = TTPhongtro.IDPhong
                    JOIN
                        HoaDon ON CTHoadon.idCTHD = HoaDon.idCTHD 
                    WHERE 
                        TTPhongtro.Idchutro = ?;
                '''
                cursor.execute(query, (id_chutro,))
                return cursor.fetchall()
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
            finally:
                connection.close()
        return []
    @staticmethod
    def get_info_all_hoadon():
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = '''
                            SELECT 
                                    TTPhongtro.TenPhong, 
                                    Chutro.Hoten,
                                    NguoiThueTro.Hoten, 
                                    NguoiThueTro.Phone, 
                                    HoaDon.Tongchiphi, 
                                    HoaDon.Ngayxuathoadon,
                                    HoaDon.BillID,
                                    TTPhongtro.Idchutro,
                                    CTHoadon.Idphong
                                FROM 
                                    TTPhongtro
                                JOIN 
                                    NguoiThueTro ON TTPhongtro.IDnguoithue = NguoiThueTro.IDnguoithue
                                JOIN 
                                    CTHoaDon ON TTPhongtro.IDPhong = CTHoaDon.IDPhong
                                JOIN 
                                    HoaDon ON CTHoaDon.idCTHD = HoaDon.idCTHD
                                JOIN 
                                    Chutro ON TTPhongtro.Idchutro = Chutro.IDchutro 

                            '''
                cursor.execute(query)
                return cursor.fetchall()
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
            finally:
                connection.close()
