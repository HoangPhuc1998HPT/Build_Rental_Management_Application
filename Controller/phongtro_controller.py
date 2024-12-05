#from tkinter import messagebox
from tkinter import messagebox

from backend.models.phongtro import PhongTro

class PhongTroController:
    def __init__(self, view):
        self.view = view  # Reference to the view instance

    def get_room_list(self, id_chutro):
        # Fetch the room list from the model
        room_list = PhongTro.get_room_list_from_db(id_chutro)
        # 'IDPhong': row[0], 'TenPhong': row[1],
        if room_list:
            self.view.display_rooms(room_list)  # Delegate displaying rooms to the view
        else:
            messagebox.showerror("Error")

