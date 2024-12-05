import pyodbc

from Controller.login_controller import go_back_to_login
from backend.models.User import User
from backend.models.db import create_database_connection
from backend.models.role import Role


class Chutro(User):
    def __init__(self, id_chutro, username, password, ho_ten, cccd, phone):
        super().__init__(username, password, Role.CHUTRO)
        self.__ho_ten = ho_ten
        self.__id_chutro = id_chutro
        self.__cccd = cccd
        self.__phone = phone

    @property
    def ho_ten(self):
        return self.__ho_ten
    @property
    def cccd(self):
        return self.__cccd
    @property
    def phone(self):
        return self.__phone
    @property
    def id_chutro(self):
        return self.__id_chutro


    def check_unique_cccd_phone(self):
        connection = create_database_connection()
        cursor = connection.cursor()

        # Kiểm tra CCCD
        query_cccd = "SELECT COUNT(*) FROM Chutro WHERE cccd = ? AND UserID != ?"
        cursor.execute(query_cccd, (self.__cccd, self.user_id))
        result_cccd = cursor.fetchone()

        # Kiểm tra Số điện thoại
        query_phone = "SELECT COUNT(*) FROM Chutro WHERE phone = ? AND UserID != ?"
        cursor.execute(query_phone, (self.__phone, self.user_id))
        result_phone = cursor.fetchone()

        connection.close()

        if result_cccd[0] > 0:
            return "CCCD đã tồn tại"
        elif result_phone[0] > 0:
            return "Số điện thoại đã tồn tại"
        else:
            return None  # Không có trùng lặp

    @staticmethod
    def save_info_chutro(root,hoten,cccd,phone,user_id):
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                sql = "INSERT INTO Chutro (UserID, hoten, cccd, phone) VALUES (?, ?, ?, ?)"
                cursor.execute(sql, (user_id, hoten, cccd, phone))
                connection.commit()
                print("Đã cập nhật!")
            except pyodbc.Error as e:
                print(f"Lỗi khi cập nhật: {e}")
            finally:
                connection.close()
                go_back_to_login(root)

    @staticmethod
    def load_thongtin_chutro(id_chutro,tree_info):
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT * FROM Chutro WHERE IDchutro = ?"
                cursor.execute(query, (id_chutro,))
                result = cursor.fetchone()
                if result:
                    tree_info.insert("", "end", values=(result[1], "Chủ trọ", result[2], result[3]))
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
            finally:
                connection.close()

    @staticmethod
    def load_thongtin_all_chutro(self):
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute('''
                        Select 
                            Users.Username, chutro.hoten, chutro.CCCD, chutro.Phone, count(TTphongtro.IDPhong) as Tongsophongtro
                        from 
                            Chutro
                        left join 
                            TTPhongtro on Chutro.IDChutro = TTphongtro.IDChutro
                        left join
                            Users on Chutro.UserID = Users.UserID
                        group by 
                            chutro.hoten, chutro.CCCD, chutro.Phone, Users.Username   
                        ''')
                return cursor.fetchall()
            except pyodbc.Error as e:
                print(f"Lỗi khi truy vấn database: {e}")
            finally:
                connection.close()
