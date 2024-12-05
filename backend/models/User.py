from tkinter import messagebox

import tkinter as tk

from backend.models.role import Role
from backend.models.db import create_database_connection
import pyodbc




class User:
    def __init__(self, username, password, role, user_id=None):
        self.__username = username
        self.__password = password
        self.__role = Role(role)
        self.__user_id = user_id  # Lưu UserID sau khi tạo tài khoản


    # Các getter và setter cho các thuộc tính
    @property
    def username(self):
        return self.__username

    @property
    def role(self):
        return self.__role

    @property
    def user_id(self):
        return self.__user_id

        # Setter for password
    def set_password(self, new_password):
        if len(new_password) > 6:
            self.__password = new_password
        else:
            raise ValueError("Mật khẩu tối thiểu 6 ký tự.")

        # Check password
    def check_password(self, password):
        return self.__password == password

    # Các phương thức xử lý cơ sở dữ liệu như kiểm tra trùng username, tạo user, v.v.
        # Check if the username already exists in the database
    @staticmethod
    def username_exists(username):
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = '''SELECT COUNT(*) FROM Users WHERE Username = ?'''
                cursor.execute(query, (username,))
                result = cursor.fetchone()
                return result[0] > 0  # Returns True if username exists
            except pyodbc.Error as e:
                print(f"Lỗi khi kiểm tra username: {e}")
                return False
            finally:
                connection.close()


    def Create_user(self):
        # Tạo tài khoản người dùng trong cơ sở dữ liệu
        connection = create_database_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = '''INSERT INTO Users (Username, Password, Role) VALUES (?, ?, ?)'''
                cursor.execute(query, (self.__username, self.__password, self.__role.role_name))
                connection.commit()
                self.__user_id = cursor.fetchone()[0]  # Lấy giá trị UserID vừa được tạo
            except pyodbc.Error as e:
                print(f"Lỗi khi tạo tài khoản: {e}")
            finally:
                connection.close()
        return self.__user_id

