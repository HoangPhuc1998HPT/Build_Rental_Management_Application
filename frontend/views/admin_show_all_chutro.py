import tkinter as tk
from tkinter import ttk

import pyodbc

from backend.models.db import create_database_connection


class Admin_show_all_chutro:
    def __init__(self, root):
        # Gọi __init__ của lớp cha và truyền các đối số cần thiết
        self.root = root
        self.root.title("Danh sách chủ trọ")
        self.root.geometry("800x600")

        tk.Label(self.root, text="Danh sách chủ trọ", font=("Arial", 18, "bold")).pack(pady=10)

        self.tree_show_chu_tro = ttk.Treeview(self.root, columns=("Username", "Họ tên chủ trọ", "CCCD", "Số điện thoại", "Tổng số phòng trọ"),show="headings", height=25)
        self.tree_show_chu_tro.heading("Username", text="Username")
        self.tree_show_chu_tro.heading("Họ tên chủ trọ", text="Họ tên chủ trọ")
        self.tree_show_chu_tro.heading("CCCD", text="CCCD")
        self.tree_show_chu_tro.heading("Số điện thoại", text="Số điện thoại")
        self.tree_show_chu_tro.heading("Tổng số phòng trọ", text="Tổng số phòng trọ")

        self.tree_show_chu_tro.column("Username", width=100)
        self.tree_show_chu_tro.column("Họ tên chủ trọ", width=160, anchor="center")
        self.tree_show_chu_tro.column("CCCD", width=100, anchor="center")
        self.tree_show_chu_tro.column("Số điện thoại", width=100,anchor="center")
        self.tree_show_chu_tro.column("Tổng số phòng trọ", width=100, anchor="center")
        self.load_du_lieu_chutro()
        self.tree_show_chu_tro.pack(fill='x', padx=100, pady=5)

        # Nội dung cơ sở dữ liệu không
    def load_du_lieu_chutro(self):
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
                rows = cursor.fetchall()
                self.tree_show_chu_tro.delete(*self.tree_show_chu_tro.get_children())
                for row in rows:
                    self.tree_show_chu_tro.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4]), tags=(row[0],))
                cursor.close()
            except pyodbc.Error as e:
                print(f"Lỗi khi kết nối cơ sở dữ liệu: {e}")
            finally:
                connection.close()


if __name__ == '__main__':
    root = tk.Tk()
    app = Admin_show_all_chutro(root)
    root.mainloop()