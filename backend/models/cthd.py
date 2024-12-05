from tkinter import messagebox

import pyodbc

from backend.models.db import create_database_connection


class CTHD:
    def __init__(self, id_cthd,sodienused, sonuocused,dayinmonth, tiennha, chiphiphatsinh, tienrac, giamgia,sodienthangtruoc,sonuocthangtruoc,id_phong,ghichu,ngaythutiendukien):
        self.__id_cthd = id_cthd
        self.__sodienused = sodienused
        self.__sonuocused = sonuocused
        self.__dayinmonth = dayinmonth
        self.__tiennha = tiennha
        self.__chiphiphatsinh = chiphiphatsinh
        self.__tienrac = tienrac
        self.__giamgia = giamgia
        self.__sodienthangtruoc = sodienthangtruoc
        self.__sonuocthangtruoc = sonuocthangtruoc
        self.__id_phong = id_phong
        self.__ghichu = ghichu
        self.__ngaythutiendukien = ngaythutiendukien

    @property
    def id_cthd(self):
        return self.__id_cthd

    @property
    def sodienused(self):
        return self.__sodienused

    @property
    def sonuocused(self):
        return self.__sonuocused

    @property
    def dayinmonth(self):
        return self.__dayinmonth

    @property
    def tiennha(self):
        return self.__tiennha

    @property
    def chiphiphatsinh(self):
        return self.__chiphiphatsinh

    @property
    def tienrac(self):
        return self.__tienrac

    @property
    def giamgia(self):
        return self.__giamgia

    @property
    def sodienthangtruoc(self):
        return self.__sodienthangtruoc

    @property
    def sonuocthangtruoc(self):
        return self.__sonuocthangtruoc

    @property
    def id_phong(self):
        return self.__id_phong

    @property
    def ghichu(self):
        return self.__ghichu

    @property
    def ngaythutiendukien(self):
        return self.__ngaythutiendukien

    @ngaythutiendukien.setter
    def ngaythutiendukien(self, ngaythutiendukien):
        self.__ngaythutiendukien = ngaythutiendukien

    @sodienthangtruoc.setter
    def sodienthangtruoc(self, sodienthangtruoc):
        self.__sodienthangtruoc = sodienthangtruoc

    @sonuocthangtruoc.setter
    def sonuocthangtruoc(self, sonuocthangtruoc):
        self.__sonuocthangtruoc = sonuocthangtruoc

    @sodienused.setter
    def sodienused(self, sodienused):
        self.__sodienused = sodienused

    @sonuocused.setter
    def sonuocused(self, sonuocused):
        self.__sonuocused = sonuocused

    @dayinmonth.setter
    def dayinmonth(self, dayinmonth):
        self.__dayinmonth = dayinmonth

    @tiennha.setter
    def tiennha(self, tiennha):
        self.__tiennha = tiennha

    @chiphiphatsinh.setter
    def chiphiphatsinh(self, chiphiphatsinh):
        self.__chiphiphatsinh = chiphiphatsinh

    @tienrac.setter
    def tienrac(self, tienrac):
        self.__tienrac = tienrac

    @giamgia.setter
    def giamgia(self, giamgia):
        self.__giamgia = giamgia

    @ghichu.setter
    def ghichu(self, ghichu):
        self.__ghichu = ghichu

    @staticmethod
    def get_sodien_dasudung(thang, nam, id_phong):
        """
        Calculates the electricity usage for a given room for the given month and year.
        """
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT sodienhientai FROM TTPhongtro WHERE IDPhong = ?"
                cursor.execute(query, (id_phong,))

                result = cursor.fetchone()
                if result:  # Check if there is a result
                    sodienhientai = result[0]
                    # Get the previous month's value, considering year boundaries
                    get_month, get_year = CTHD._get_previous_month_and_year(thang, nam)
                    sodienthangtruoc = CTHD.get_sodien_thangtruoc(get_month, get_year,id_phong) or 0
                    sodienuse = sodienhientai - sodienthangtruoc
                    return max(sodienuse, 0)  # Ensure the result is non-negative
                else:
                    return 0
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
            finally:
                connection.close()
        return 0

    @staticmethod
    def get_sodien_thangtruoc(thang, nam, id_phong):
        """
        Gets the electricity usage data for the previous month.
        """
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = '''
                        SELECT CTHoadon.SodienUsed, CTHoadon.sodienthangtruoc
                        FROM CTHoadon
                        WHERE MONTH(Ngaythutiendukien) = ? AND YEAR(Ngaythutiendukien) = ? AND IDPhong = ?
                    '''
                cursor.execute(query, (thang, nam, id_phong))
                result = cursor.fetchone()
                if result:
                    sodienmoithangcu = result[0] + result[1]
                    return sodienmoithangcu
                return 0
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
            finally:
                connection.close()
        return 0

    # fix tu đây
    @staticmethod
    def get_sonuocdasudung(thang, nam, id_phong):
        """
        Calculates the water usage for a given room for the given month and year.
        """
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT sonuochientai FROM TTPhongtro WHERE IDPhong = ?"
                cursor.execute(query, (id_phong,))

                result = cursor.fetchone()
                if result:  # Check if there is a result
                    sonuochientai = result[0]
                    # Get the previous month's value, considering year boundaries
                    get_month, get_year = CTHD._get_previous_month_and_year(thang, nam)
                    sonuocthangtruoc = CTHD.get_sonuoc_thangtruoc(get_month, get_year,id_phong) or 0
                    sonuocuse = sonuochientai - sonuocthangtruoc
                    return max(sonuocuse, 0)  # Ensure the result is non-negative
                else:
                    return 0
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
            finally:
                connection.close()
        return 0

    @staticmethod
    def get_sonuoc_thangtruoc(thang, nam, id_phong):
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = '''
                        SELECT CTHoadon.SonuocUsed, CTHoadon.sonuocthangtruoc
                        FROM CTHoadon
                        WHERE MONTH(Ngaythutiendukien) = ? AND YEAR(Ngaythutiendukien) = ? AND IDPhong = ?
                    '''
                cursor.execute(query, (thang, nam, id_phong))
                result = cursor.fetchone()
                if result:
                    sonuocmoithangcu = result[0] + result[1]
                    return sonuocmoithangcu
                return 0
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
            finally:
                connection.close()
        return 0

    @staticmethod
    def _get_previous_month_and_year(thang, nam):
        if thang == 1:
            return 12, nam - 1  # Go back to December of the previous year
        else:
            return thang - 1, nam

    @staticmethod
    def get_tien_nha_from_TTPhong(id_phong):
            connection = create_database_connection()
            if connection:
                try:
                    cursor = connection.cursor()
                    query = '''
                            SELECT TTPhongtro.Giaphong
                            FROM TTPhongtro
                            WHERE TTPhongtro.IDPhong = ?  
                        '''
                    cursor.execute(query, (id_phong,))
                    result = cursor.fetchone()

                    if result:
                        return result[0]
                    else:
                        return 0  # Nếu không có kết quả, trả về 0 hoặc một giá trị mặc định
                except pyodbc.Error as e:
                    print(f"Lỗi khi truy vấn database: {e}")
                finally:
                    connection.close()
            return 0  # Nếu không thể kết nối với cơ sở dữ liệu

    @staticmethod
    def save_CTHD(sodien_use, sonuoc_use, so_ngay_o_trong_thang, tien_nha, chiphiphatsinh, chiphirac,
                                giamgia, sodienthangtruoc, sonuocthangtruoc, id_phong, ghichu, ngayxuathoadon):
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = '''
                               INSERT INTO CTHoadon 
                               (SodienUsed, SonuocUsed, DaysInMonth, Tiennha, Chiphiphatsinh, Tienrac, Giamgia, sodienthangtruoc, sonuocthangtruoc, IDPhong, Ghichu ,ngaythutiendukien)
                               VALUES 
                                   (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?);
                               '''
                cursor.execute(query,
                               (sodien_use, sonuoc_use, so_ngay_o_trong_thang, tien_nha, chiphiphatsinh, chiphirac,
                                giamgia, sodienthangtruoc, sonuocthangtruoc, id_phong, ghichu, ngayxuathoadon))
                connection.commit()
                messagebox.showinfo("Thành công", "Dữ liệu đã được lưu thành công!")
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
            finally:
                connection.close()