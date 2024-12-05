from tkinter import messagebox

import pyodbc

from Controller.login_controller import go_back_to_login
from backend.models.User import User
from backend.models.db import create_database_connection, connection
from backend.models.role import Role


class Admin(User):
    def __init__(self, username, password, fullname):
        super().__init__(username, password, Role.ADMIN)
        self.__fullname = fullname
        self.__admin_id = None  # ID admin sẽ được tạo tự động trong cơ sở dữ liệu

    @property
    def admin_id(self):
        return self.__admin_id
    @property
    def fullname(self):
        return self.__fullname
    @property
    def username(self):
        return self.__username
    @property
    def password(self):
        return self.__password
    @fullname.setter
    def fullname(self, new_fullname):
        self.__fullname = new_fullname
    @password.setter
    def password(self, new_password):
        self.__password = new_password

    # Phương thức lưu admin vào CSDL
    def save_info_admin(root,user_id,hoten):
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                sql = "InSERT INTO Admins (UserID, FullName) VALUES (?, ?)"
                cursor.execute(sql, (user_id, hoten))
                connection.commit()
                connection.close()
                go_back_to_login(root)
            except pyodbc.Error as e:
                print(f"Lỗi khi cập nhật: {e}")
            finally:
                connection.close()
            # Xóa các widget hiện tại sau khi cập nhật

def active_user(username, window):
    connection = create_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = '''UPdate Users SET is_active = 1 WHERE username = ?'''
            cursor.execute(query, (username,))
            connection.commit()
            window.destroy()
        except pyodbc.Error as e:
            print(f"Lỗi khi kết nối cơ sở dữ liệu: {e}")
        finally:
            connection.close()


def delete_user(username, window):
    connection = create_database_connection()
    if connection:
        try:
            cursor = connection.cursor()

            # Get UserID by Username
            query_get_user_id = '''SELECT UserID FROM Users WHERE username = ?'''
            cursor.execute(query_get_user_id, (username,))
            result = cursor.fetchone()

            if result:
                user_id = result[0]

                # Delete records in related tables first (Chutro table in this example)
                query_delete_chutro = '''DELETE FROM Chutro WHERE UserID = ?'''
                cursor.execute(query_delete_chutro, (user_id,))

                # You can add more queries here to delete from other related tables if needed

                # Delete the user from Users table
                query_delete_user = '''DELETE FROM Users WHERE username = ?'''
                cursor.execute(query_delete_user, (username,))

                # Commit changes
                connection.commit()

                # Close the window after successful deletion
                window.destroy()

        except pyodbc.Error as e:
            print(f"Lỗi khi kết nối cơ sở dữ liệu: {e}")
        finally:
            connection.close()
