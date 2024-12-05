import pyodbc

def create_database_connection():
    try:
        # Tạo chuỗi kết nối tới SQL Server
        connection = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=DESKTOP-C7M760B\\SQLEXPRESS;'  # Tên hoặc địa chỉ IP của SQL Server
            'DATABASE=QLThueNhaTro;'  # Tên cơ sở dữ liệu
            'Trusted_Connection=yes;'  # Sử dụng Windows Authentication
        )
        print("Kết nối thành công tới cơ sở dữ liệu.")
        return connection
    except pyodbc.Error as e:
        print("Lỗi kết nối tới cơ sở dữ liệu:", e)
        return None

# Kết nối tới CSDL
connection = create_database_connection()
