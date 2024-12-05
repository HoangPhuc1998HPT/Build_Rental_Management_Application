
import pyodbc

from backend.models.db import create_database_connection, connection


def info_show_detail_hoadon(id_hoadon, connection):
    cursor = connection.cursor()
    # lấy thông tin từ hóa đơn
    query = '''
                    SELECT *
                    FROM Hoadon
                    WHERE BillID = ?
                    ORDER BY Ngayxuathoadon DESC
                  '''
    cursor.execute(query, (id_hoadon,))
    result = cursor.fetchone()
    # BillID[0] Tiennha[1] Tiendien[2] Tiennuoc[3] Tienrac[4] chiphikhac[5]
    # giamgia[6] ## tongchiphi[7] ngayxuathoadon[8] idphong[9] idcthd[10]
    # lấy thông tin bổ sung từ TTPhong và CThoadon

    query1 = '''
                    select CTHoadon.sodienused, CTHoadon.sonuocused, TTPhongtro.giadien, TTPhongtro.gianuoc, CTHoadon.ghichu, TTPhongtro.Idchutro, TTPhongtro.idnguoithue
                    from CTHoadon
                    join TTPhongtro on CTHoadon.idphong = TTPhongtro.idphong
                    where idCTHD = ?

                    '''
    cursor.execute(query1, (result[9],))
    result1 = cursor.fetchone()

    # Lấy thông tin từ người thuê trọ và chủ trọ
    query2 = "SELECT * FROM Chutro WHERE IDchutro = ?"
    cursor.execute(query2, (result1[5],))
    result2 = cursor.fetchone()

    query3 = "SELECT * FROM NguoiThueTro WHERE IDnguoithue = ?"
    cursor.execute(query3, (result1[6],))
    result3 = cursor.fetchone()
    return result, result1, result2, result3

def Get_id_phongtro_from_id_nguoithue(id_nguoithue):
    connection = create_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query="SELECT IDphong, IDchutro FROM TTPhongtro WHERE IDnguoithue = ?"
            cursor.execute(query, (id_nguoithue,))
            result = cursor.fetchone()
            if result:
                return result[0], result[1]  # Trả về ID phongtro  Id chutro
            else:
                print("Người thuê trọ chưa được thêm vào phòng trọ.")
                return None
        except Exception as e:
            print("Lỗi khi truy vấn CSDL:", e)
            return None

def get_chutro_id_by_username(username):
    connection = create_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = '''
            SELECT 
                IDChutro
            FROM
                Chutro
            join
                Users on users.UserID = Chutro.UserID
            WHERE
                Username = ?
            '''
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            if result:
                return result[0]  # IDChutro is an integer
        except pyodbc.Error as e:
            print(f"Lỗi khi truy vấn username: {e}")
        finally:
            connection.close()
    return None  # Return None if not found

def get_admin_id_by_username(username):
    connection = create_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Truy vấn để lấy IDAdmin dựa vào Username của bảng Users và Admin
            query = '''
            SELECT Admins.AdminID
            FROM Admins
            JOIN Users ON Admins.UserID = Users.UserID
            WHERE Users.Username = ?'''
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            if result:
                return result[0]  # Trả về IDAdmin
            else:
                print("Không tìm thấy admin với username không.")
                return None
        except pyodbc.Error as e:
            print(f"Lỗi khi truy vấn IDAdmin: {e}")
        finally:
            connection.close()

def Get_id_nguoithue_from_username(username):
    connection = create_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT UserID FROM Users WHERE username = ?"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            if result:
                query1 = "select IDnguoithue from NguoiThueTro where UserID = ?"
                cursor.execute(query1, (result[0],))
                result1 = cursor.fetchone()
                if result1:
                    return result1[0]
                else:
                    print("Người thuê chưa được cập nhật.")
                    return None
            else:
                print("Không tìm thấy userID.")
                return None
        except Exception as e:
            print("Lỗi khi truy vấn CSDL:", e)
            return None
        finally:
            connection.close()


    # dashboard chủ trọ y/c username
    # get usename từ id_chủ trọ
    # laasys id chủ trọ get userID
    # lấy userID get username

def get_username_from_id_chutro(id_chutro):
    connection = create_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = '''
            SELECT Username
            FROM Users
            JOIN Chutro ON Chutro.UserID = Users.UserID
            WHERE Chutro.IDChutro = ?'''
            cursor.execute(query, (id_chutro,))
            result = cursor.fetchone()
            if result:
                #print(f"Username: {result[0]}")
                return result[0]  # Trả về username

            else:
                print("Không tìm thấy chủ trọ với IDChutro không.")
                return None
        except pyodbc.Error as e:
            print(f"Lỗi khi truy vấn username: {e}")
        finally:
            connection.close()

def get_nguoithue_by_cccd(cccd):
    connection = create_database_connection()
    thong_tin_nguoithue = None
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT IDnguoithue, Hoten, UserID FROM NguoiThueTro WHERE CCCD = ?"
            cursor.execute(query, (cccd,))
            return cursor.fetchone()
            #resut[0] - IDnguoithue - result[1] - Họ ten - result[2] - user ID
        except pyodbc.Error as e:
            print(f"Loại khi truy vấn người thuê trọ: {e}")
        finally:
            connection.close()
    return thong_tin_nguoithue

def clear_screen(root):
    # Clear all widgets in the root window
    for widget in root.winfo_children():
        widget.destroy()

def info_show_danh_sach_hoadon(id_nguoithue):
    connection = create_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = '''
                            select Hoadon.Ngayxuathoadon, HoaDon.BillID, CTHoadon.ghichu, Hoadon.Tongchiphi, TTPhongtro.TenPhong, 
                            TTphongtro.Address, Chutro.hoten, Chutro.Phone
                            from Hoadon
                            join CTHoadon on CTHoadon.idCTHD = Hoadon.idCTHD
                            join TTPhongtro on TTPhongtro.IDphong = CTHoadon.IDphong
                            join Chutro on Chutro.IDchutro = TTPhongtro.IDchutro
                            where TTPhongtro.IDnguoithue = ?
                            order by HoaDon.BillID DESC 
        
                            '''
            cursor.execute(query, (id_nguoithue,))
            return cursor.fetchall()

        except pyodbc.Error as e:
            print(f"Lỗi khi truy vấn dữ liệu: {e}")
        finally:
            connection.close()

def infor_duyet_tao_user(Thong_tin_duyet_active, connection):
    cursor = connection.cursor()
    query_user = '''
                    SELECT users.username, users.role, users.UserID
                    FROM users
                    WHERE (users.is_active IS NULL OR users.is_active != 1)
                    '''
    cursor.execute(query_user)  # Lấy những người dùng chưa active
    result = cursor.fetchall()

    for row in result:
        print(row)  # Kiểm tra dữ liệu từ truy vấn chính
        if row[1] == 'chutro':  # Nếu là chủ trọ
            query = '''
                            SELECT users.username, users.role, chutro.hoten, chutro.cccd, chutro.Phone
                            FROM users
                            JOIN chutro ON users.UserID = chutro.UserID
                            WHERE users.UserID = ?
                            '''
            cursor.execute(query, (row[2],))  # Dùng UserID để lấy thông tin chủ trọ
            chutro_info = cursor.fetchall()
            print(chutro_info)  # Kiểm tra kết quả truy vấn của chủ trọ
            Thong_tin_duyet_active.extend(chutro_info)

        elif row[1] == 'nguoithuetro':  # Nếu là người thuê trọ
            query = '''
                            SELECT users.username, users.role, nguoithuetro.hoten, nguoithuetro.CCCD, nguoithuetro.Phone
                            FROM users
                            JOIN nguoithuetro ON users.UserID = nguoithuetro.UserID
                            WHERE users.UserID = ?
                            '''
            cursor.execute(query, (row[2],))  # Dùng UserID để lấy thông tin người thuê trọ
            nguoithue_info = cursor.fetchall()
            print(nguoithue_info)  # Kiểm tra kết quả truy vấn của người thuê trọ
            Thong_tin_duyet_active.extend(nguoithue_info)

def xoa_phong(root, id_phong, id_chutro,username):
    print(f"Xóa phòng {id_phong}")
    connection = create_database_connection()
    from Controller.navigation import go_to_back_dashboard_chutro
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM TTPhongtro WHERE IDPhong = ? AND IDChutro = ?"
            cursor.execute(query, (id_phong, id_chutro))
            connection.commit()
            go_to_back_dashboard_chutro(root, username)
        except pyodbc.Error as e:
            print(f"Lỗi khi truy vấn database: {e}")
        finally:
            connection.close()

def get_id_nguoithue_from_id_phong(id_phong):
    connection = create_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "Select TTPhongtro.IDnguoithue from TTPhongtro where IDPhong = ? "
            cursor.execute(query, (id_phong,))  # Truyền đúng tham số
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return 0  # Nếu không có kết quả, trả về 0 hoặc một giá trị mặc định
        except pyodbc.Error as e:
            print(f"Lỗi khi truy vấn database: {e}")
        finally:
            connection.close()
    return 0  # Nếu không thể kết nối với cơ sở dữ liệu

def get_id_chutro_from_id_phong(id_phong):
    connection = create_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT IDchutro FROM TTPhongtro WHERE IDPhong = ?"
            cursor.execute(query, (id_phong,))
            result = cursor.fetchone()
            if result:
                return result[0]  # Return only the ID, not the tuple
            else:
                return None  # Return None if no result
        except pyodbc.Error as e:
            print(f"Lỗi khi truy vấn database: {e}")
        finally:
            connection.close()
    return None  # Return None if there's no connection