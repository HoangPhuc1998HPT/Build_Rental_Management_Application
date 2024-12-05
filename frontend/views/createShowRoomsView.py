import tkinter as tk
from tkinter import messagebox

from Controller.phongtro_controller import PhongTroController
from Controller.navigation import go_to_back_dashboard_chutro, go_to_update_nguoithue, update_infor_room,go_to_XuatHoaDon, go_to_update_hoadon
from backend.models.nguoithuetro import NguoiThueTro
from backend.utils import xoa_phong, get_username_from_id_chutro


class CreateShowRoomsView:
    def __init__(self, root, id_chutro):
        self.root = root
        self.root.title("Danh sách phòng trọ")
        self.id_chutro = id_chutro
        self.root.geometry("1800x1000")
        self.username = get_username_from_id_chutro(self.id_chutro)
        # Initialize the controller
        self.controller = PhongTroController(self)

        # Create Canvas
        canvas = tk.Canvas(self.root)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Horizontal Scrollbar
        h_scrollbar = tk.Scrollbar(self.root, orient=tk.HORIZONTAL, command=canvas.xview)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.configure(xscrollcommand=h_scrollbar.set)

        # Create Frame inside the Canvas
        self.room_frame = tk.Frame(canvas)
        self.room_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.room_frame, anchor="nw")

        # Fetch and display room data via the controller
        self.controller.get_room_list(id_chutro)

    def display_rooms(self, room_list):
        frame_width = 250
        frame_height = 300
        button_width = 20
        button_height = 2
        num_columns = 5
        username = get_username_from_id_chutro(self.id_chutro)
        # 'IDPhong': row[0], 'TenPhong': row[1],
        for idx, room in enumerate(room_list):
            frame = tk.Frame(self.room_frame, bg="#d9d2e9", bd=2, relief="solid", width=frame_width, height=frame_height)
            frame.grid(row=idx // num_columns, column=idx % num_columns, padx=20, pady=20)
            frame.grid_propagate(False)

            # Display Room Name
            title_label = tk.Label(frame, text=f"Tên phòng: {room['TenPhong']}", font=("Arial", 13, "bold"), bg="#d9d2e9", width=30)
            title_label.pack(pady=(10, 20))

            # hiển thị tên người thuê nếu có

            id_phong = room['IDPhong']
            self.create_room_buttons(frame, id_phong, button_width, button_height,username)

    def create_room_buttons(self, frame, id_phong, button_width, button_height,username):
        # Tạo các nút chức năng cho mỗi phòng trọ với `id_phong` tương ứng
        #
        ten_nguoi_thue_label = tk.Label(frame, text="Tên Người Thuê: ", font=("Arial", 8, "bold"), bg="#d9d2e9",
                                        width=35)
        ten_nguoi_thue_label.pack(pady=5)

        tenant_name = NguoiThueTro.get_ten_nguoi_thue_in_room(id_phong)
        if tenant_name:
            ten_nguoi_thue_label.config(text=f"Tên Người Thuê: {tenant_name}")
        else:
            ten_nguoi_thue_label.config(text="Tên Người Thuê: Không có")

        #
        btn_update_tenant = tk.Button(frame, text="Cập nhật người thuê", bg="#a4d3f4", width=button_width,
                                      height=button_height,
                                      command=lambda: go_to_update_nguoithue(self.root, self.id_chutro, id_phong))
        btn_update_tenant.pack(pady=10)

        btn_update_room = tk.Button(frame, text="Cập nhật thông tin phòng", bg="#a4d3f4", width=button_width,
                                    height=button_height,
                                    command=lambda: update_infor_room(self.root,self.id_chutro, id_phong))
        btn_update_room.pack(pady=10)

        btn_update_invoice = tk.Button(frame, text="Cập nhật hóa đơn", bg="#a4d3f4", width=button_width,
                                       height=button_height,
                                       command=lambda: go_to_update_hoadon(self.root, id_phong))
        btn_update_invoice.pack(pady=10)

        btn_export_invoice = tk.Button(frame, text="Xuất hóa đơn", bg="#a4d3f4", width=button_width,
                                       height=button_height,
                                       command=lambda: go_to_XuatHoaDon(self.root,self.id_chutro ,id_phong))
        btn_export_invoice.pack(pady=10)

        btn_delete_room = tk.Button(frame, text="Xóa phòng", bg="#f4a4a4", width=button_width, height=button_height,
                                    command=lambda: xoa_phong(self.root, id_phong, self.id_chutro,username))
        btn_delete_room.pack(pady=(20, 10))

        btn_back_dashboard = tk.Button(frame, text="Quay lại", bg="#f4a4a4", width=button_width, height=button_height,
                                       command=lambda: go_to_back_dashboard_chutro(self.root, username))

        btn_back_dashboard.pack(pady=(20, 10)) #btn_back_dashboard

    def show_error(self, message):
        # This method will display the error messages in a popup window
        messagebox.showerror("Error", message)



    # Các hàm xử lý khi các nút chức năng được nhấn, truyền IDPhong cho từng chức năng


#CreateShowRoomsView







if __name__ == "__main__":
    root = tk.Tk()
    app = CreateShowRoomsView(root, 4)
    root.mainloop()