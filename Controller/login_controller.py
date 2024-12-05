from tkinter import messagebox

import pyodbc

from backend.models.db import create_database_connection
from backend.services.user_service import info_check_login, info_check_register
from backend.utils import clear_screen




def check_login(root,username,password):
    # Check if fields are empty
    if not username or not password:
        messagebox.showwarning("Đăng nhập", "Vui lòng nhập tên tài khoản và mật khẩu!")
        return

    connection = create_database_connection()
    if connection:
        try:
            result = info_check_login(username,password,connection)
            if result:
                role, is_active = result
                print(f"Vai trò: {role}, Trạng thái: {is_active}")

                if role == 'admin':
                    from frontend.views import dashboard_admin
                    messagebox.showinfo("Đăng nhập", "Đăng nhập thành công! \n Vai trò: Admin")
                    clear_screen(root)
                    dashboard_admin.DashboardAdmin(root, username)

                elif role == 'chutro':
                    if is_active == 1:
                        from frontend.views import dashboard_chutro
                        messagebox.showinfo("Đăng nhập", "Đăng nhập thành công! \n Vai trò: Chủ trọ")
                        clear_screen(root)
                        dashboard_chutro.DashboardChutro(root, username)
                    else:
                        messagebox.showerror("Đăng nhập", "Tài khoản chưa được kích hoạt!")

                elif role == 'nguoithuetro':
                    from frontend.views import dashboard_thuetro
                    messagebox.showinfo("Đăng nhập", "Đăng nhập thành công! \n Vai trò: Người thuê trọ")
                    clear_screen(root)
                    dashboard_thuetro.DashboardNguoithuetro(root, username)

            else:
                messagebox.showerror("Đăng nhập", "Tên tài khoản hoặc mật khẩu không chính xác!")

        except pyodbc.Error as e:
            messagebox.showerror("Lỗi", f"Lỗi khi kết nối cơ sở dữ liệu: {e}")
        finally:
            connection.close()

def show_register_view(root):
    from frontend.views.register import RegisterView
    clear_screen(root)
    RegisterView(root)

def show_login_view(root):
    from frontend.views.login import Loginview
    clear_screen(root)
    Loginview(root)

def go_back_to_login(root):
    from frontend.views.homelogin import Homelogin
    clear_screen(root)
    Homelogin(root)

def check_register_user(root,username,password,role,entry_confirm_password):
    from frontend.views.update_infomation_user import UpdateInfomationView# check ussername and password
    if not username or not password:
        messagebox.showerror("Đăng ký", "Vui lòng điền đầy đủ thông tin.")
        return

    if password != entry_confirm_password.get():
        messagebox.showerror("Đăng ký", "Xác nhận mật khẩu không khớp!")
        return

    connection = create_database_connection()
    if connection:
        try:
            user_id = info_check_register(username,password,role,connection)

            if user_id:  # Check if the user was successfully registered
                print(user_id)
                clear_screen(root)
                UpdateInfomationView(root, role, user_id)
            else:
                messagebox.showerror("Đăng ký", "Tên tài khoản đã tồn tại!")

        except pyodbc.Error as e:
            print(f"Lỗi khi đăng ký tài khoản: {e}")
        finally:
            connection.close()