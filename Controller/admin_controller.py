# Controller/admin_controller.py
import tkinter as tk
from backend.models.db import create_database_connection
from backend.utils import infor_duyet_tao_user
from backend.models.admin import active_user, delete_user


class AdminController:
    def __init__(self, root, view):
        self.root = root
        self.view = view

    def duyet_tao_user(self, tree):
        # Clear existing entries
        tree.delete(*tree.get_children())

        # Fetch user data and populate the Treeview
        connection = create_database_connection()
        if connection:
            Thong_tin_duyet_active = []
            try:
                infor_duyet_tao_user(Thong_tin_duyet_active, connection)

                # Insert the fetched data into the Treeview
                for row in Thong_tin_duyet_active:
                    tree.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4], "click vào để active"))

            except Exception as e:
                print("Lỗi khi truy vấn CSDL:", e)
            finally:
                connection.close()
        return

    def on_double_click(self, event, tree):
        # Handle double-click event
        selected_item = tree.selection()
        if selected_item:
            user_info = tree.item(selected_item, "values")  # Get selected row data
            username = user_info[0]  # Extract username from the first column
            print(f"Selected user: {username}")
            self.show_active_user(username)  # Open modal window for user actions
        else:
            print("No user selected.")

    def show_active_user(self, username):
        # Open modal for user actions
        action_window = tk.Toplevel(self.root)
        action_window.title(f"Kích hoạt cho username:  {username}")
        action_window.geometry("300x300")

        tk.Label(action_window, text=f"Kích hoạt cho username: {username}").pack(pady=10)

        # Button to activate user
        tk.Button(action_window, text="Kích hoạt User", command=lambda: active_user(username, action_window)).pack(
            pady=5)

        # Button to delete user
        tk.Button(action_window, text="Xóa User", command=lambda: delete_user(username, action_window)).pack(pady=5)

    def reload_admin_dashboard(self, tree):
        # Refresh the Treeview by reloading user data
        self.duyet_tao_user(tree)
