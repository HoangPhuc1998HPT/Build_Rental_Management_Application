import tkinter as tk
from tkinter import messagebox

from Controller.login_controller import check_login

class Loginview:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng nhập")
        self.root.geometry("400x300")

        # Labels and Entry Fields
        self.label_username = tk.Label(root, text="Tên tài khoản")
        self.label_username.pack(pady=5)
        self.entry_username = tk.Entry(root, width=30)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(root, text="Mật khẩu")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(root, show="*", width=30)
        self.entry_password.pack(pady=5)

     # Login Button
        self.button_login = tk.Button(root, text="Đăng nhập", command=self.submit_login)
        self.button_login.pack(pady=20)

        # Bind Enter key to login action
        self.root.bind('<Return>', lambda event: self.submit_login())

    #def submit_login(self):
        # Fetch user input dynamically
        #username = self.entry_username.get().strip()
        #password = self.entry_password.get().strip()
        #check_login(self.root, username, password)  # Delegate to Controller

    def submit_login(self):
        try:
            # Safeguard to check if widget still exists
            if hasattr(self, 'entry_username') and self.entry_username.winfo_exists():
                username = self.entry_username.get().strip()

            else:
                raise Exception("Username entry widget no longer exists")

            if hasattr(self, 'entry_password') and self.entry_password.winfo_exists():
                password = self.entry_password.get().strip()

            else:
                raise Exception("Password entry widget no longer exists")

            # Proceed with authentication logic
            if username and password:
                # Simulate a successful login process
                print(f"Logging in with Username: {username}, Password: {password}")
                check_login(self.root, username, password)
            else:
                messagebox.showerror("Login Error", "Please fill in both username and password.")

        except Exception as e:
            print(f"Error in submit_login: {e}")
            messagebox.showerror("Error", str(e))




if __name__ == "__main__":
    root = tk.Tk()
    app = Loginview(root)
    root.mainloop()
