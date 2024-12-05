
import tkinter as tk
from backend.utils import clear_screen, get_username_from_id_chutro
from backend.utils import get_chutro_id_by_username
from frontend.views.Admin_show_all_hoadon import Admin_show_all_hoadon
from frontend.views.admin_show_all_chutro import Admin_show_all_chutro
from frontend.views.admin_show_all_nguoithuetro import Admin_show_all_nguoithuetro
from frontend.views.admin_show_all_phongtro import Admin_show_all_phongtro
from frontend.views.createRoomView import CreateRoomView




def Xem_danh_sach_tat_ca_cac_chutro(root):
    new_window = tk.Toplevel(root)
    new_window.title("Danh sách hóa đơn")
    new_window.geometry("1800x1000")
    Admin_show_all_chutro(new_window)

def Xem_danh_sach_tat_ca_cac_phongtro(root):
    new_window = tk.Toplevel(root)
    new_window.title("Danh sách hóa đơn")
    new_window.geometry("1800x1000")
    Admin_show_all_phongtro(new_window)

def Xem_danh_sach_tat_ca_cac_nguoithuetro(root):
    new_window = tk.Toplevel(root)
    new_window.title("Danh sách hóa đơn")
    new_window.geometry("1800x1000")
    Admin_show_all_nguoithuetro(new_window)

def Go_to_xem_danh_sach_hoadon(root,username):
    id_chutro = get_chutro_id_by_username(username)
    clear_screen(root)
    from frontend.views.createHoadon_showDSHoaDon import CreateHoadon_showDSHoaDon
    CreateHoadon_showDSHoaDon(root, id_chutro)

def Go_to_tao_phongtro(root, username):
    id_chutro = get_chutro_id_by_username(username)
    # điều hướng đi tới trang tạo phòng trọ class tao_phongtro
    # method create_phongtro
    clear_screen(root)
    CreateRoomView(root,id_chutro)

#Go_to_show_danh_sach_nhatro lỗi

def go_to_XuatHoaDon(root,id_chutro ,id_phong):
    print(f"Xuat hoa don cho phong {id_phong}")
    clear_screen(root)
    from frontend.views.createHoadon_XuatHoaDon import CreateHoadon_XuatHoaDon
    CreateHoadon_XuatHoaDon(root, id_chutro, id_phong)

def go_to_update_hoadon(root, id_phong):
    print(f"Cập nhật hóa đơn cho phòng {id_phong}")
    clear_screen(root)
    from frontend.views.createHoadon_update import CreateHoadon_update
    CreateHoadon_update(root, id_phong)

def Go_to_xem_danh_sach_tat_ca_cac_hoadon(root):
    new_window = tk.Toplevel(root)
    new_window.title("Danh sách hóa đơn")
    new_window.geometry("1800x1000")

    # Mở Admin_show_all_hoadon trên cửa sổ mới
    Admin_show_all_hoadon(new_window)

def go_to_back_dashboard_chutro(root, username):
    from frontend.views.dashboard_chutro import DashboardChutro
    clear_screen(root)
    DashboardChutro(root, username)  # Khởi tạo lại DashboardChutro với username

def go_to_update_nguoithue(root, id_chutro, id_phong):
    print(f"Cập nhật người thuê cho phòng {id_phong}")
    clear_screen(root)
    from frontend.views.createRoomThemnguoithue import CreateRoomThemnguoithue
    CreateRoomThemnguoithue(root, id_chutro, id_phong)

def update_infor_room(root,id_chutro, id_phong):
    print(f"Cập nhật thông tin phòng {id_phong}")
    clear_screen(root)  # Xóa các widget hiện tại
    from frontend.views.createRoomupdateTT_Phong import CreateRoomupdateTT_Phong
    CreateRoomupdateTT_Phong(root, id_chutro, id_phong)
    # Đợi tạo trang update thông tin người thuê

def Go_to_dangxuat(root):
    clear_screen(root)
    from frontend.views.homelogin import Homelogin
    Homelogin(root)





