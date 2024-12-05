import tkinter as tk


from Controller.login_controller import go_back_to_login, check_register_user



class RegisterView():
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng ký tài khoản")
        self.root.geometry("400x600")

        # Vai trò
        self.label_role = tk.Label(root, text="Chọn vai trò")
        self.label_role.pack(pady=5)

        self.role_var = tk.StringVar(value="admin")
        #tk.Radiobutton(root, text="Admin", variable=self.role_var, value="admin").pack(anchor="w")
        tk.Radiobutton(root, text="Chủ trọ", variable=self.role_var, value="chutro").pack(anchor="w")
        tk.Radiobutton(root, text="Người thuê trọ", variable=self.role_var, value="nguoithuetro").pack(anchor="w")

        # Tên tài khoản và mật khẩu
        self.label_username = tk.Label(root, text="Tên tài khoản")
        self.label_username.pack(pady=5)
        self.entry_username = tk.Entry(root, width=30)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(root, text="Mật khẩu")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(root, show="*", width=30)
        self.entry_password.pack(pady=5)

        self.label_confirm_password = tk.Label(root, text="Xác nhận mật khẩu")
        self.label_confirm_password.pack(pady=5)
        self.entry_confirm_password = tk.Entry(root, show="*", width=30)
        self.entry_confirm_password.pack(pady=5)

        # Nút đăng ký
        self.button_register = tk.Button(root, text="Đăng ký", command=self.submit_register)
        self.button_register.pack(pady=20)

        # Nut quay lai trang homelogin

        self.button_back = tk.Button(root, text="Quay lai", command=lambda : go_back_to_login(self.root))
        self.button_back.pack(pady=20)

    def submit_register(self):
        username = self.entry_username.get().strip()  # dùng .strip() để loại bỏ khoảng trắng thừa
        password = self.entry_password.get().strip()
        role = self.role_var.get()
        check_register_user(self.root, username, password,role,self.entry_confirm_password)







if __name__ == "__main__":
    root = tk.Tk()  # Tạo cửa sổ chính
    app = RegisterView(root)  # Khởi tạo giao diện View
    root.mainloop()  # Chạy vòng lặp chính của Tkinter