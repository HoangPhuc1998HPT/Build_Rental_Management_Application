
from tkinter import messagebox
from backend.utils import clear_screen, get_username_from_id_chutro, get_chutro_id_by_username



def go_to_show_danh_sach_nhatro(root, username):
    id_chutro = get_chutro_id_by_username(username)
    clear_screen(root)
    from frontend.views.createShowRoomsView import CreateShowRoomsView
    CreateShowRoomsView(root, id_chutro)

def go_back_to_create_show_rooms_view(root,id_chutro):
    # Điều hướng quay lại trang CreateShowRoomsView
    clear_screen(root)
    from frontend.views.createShowRoomsView import CreateShowRoomsView
    CreateShowRoomsView(root,id_chutro)  # Khởi tạo lại CreateShowRoomsView với IDChutro
    messagebox.showinfo("Quay lại", "Đã quay lại trang danh sách phòng trọ.")

def go_to_Dashboardchutro(root,id_chutro):
    clear_screen(root)
    username = get_username_from_id_chutro(id_chutro)
    from frontend.views.dashboard_chutro import DashboardChutro
    DashboardChutro(root, username)  # Sử dụng lại root