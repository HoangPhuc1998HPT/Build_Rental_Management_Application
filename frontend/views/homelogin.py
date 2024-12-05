import tkinter as tk

from Controller.login_controller import show_register_view, show_login_view

class Homelogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý thuê nhà trọ")
        self.root.geometry("800x600")
        # tao cac nut sign and register
        tk.Label(self.root, text="Chào mừng bạn đến với quản lý thuê nhà trọ", font=('Arial', 16)).pack(pady=40)

        self.register_button = tk.Button(self.root, text="Đăng kí tài khoản",  command=lambda: show_register_view(self.root))
        self.register_button.pack(pady=40)

        self.login_button = tk.Button(self.root, text="Đăng nhập tài khoản", command=lambda: show_login_view(self.root))
        self.login_button.pack(pady=40)


if __name__ == "__main__":
    root = tk.Tk()  # Tạo cửa sổ chính
    app = Homelogin(root)  # Khởi tạo giao diện View
    root.mainloop()  # Chạy vòng lặp chính của Tkinter