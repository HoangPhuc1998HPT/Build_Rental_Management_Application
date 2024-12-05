import tkinter as tk
from frontend.views.homelogin import Homelogin


def main():
    root = tk.Tk()
    root.title("Quản lý thuê nhà trọ")
    app = Homelogin(root)
    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()  # Tạo cửa sổ chính
    app = Homelogin(root)  # Khởi tạo giao diện View
    root.mainloop()  # Chạy vòng lặp chính của Tkinter