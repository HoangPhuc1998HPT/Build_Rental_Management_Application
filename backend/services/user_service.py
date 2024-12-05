
def info_check_login(username, password, connection):
    cursor = connection.cursor()
    # kiểm tra is_active  'chutro'
    query = '''SELECT Role, is_active FROM Users WHERE Username = ? AND Password = ?'''
    cursor.execute(query, (username, password))
    return cursor.fetchone()
def info_check_register(username, password, role, connection):
    cursor = connection.cursor()

    query = '''SELECT COUNT(*) FROM Users WHERE Username = ?'''
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result[0] > 0:
        return False
    else:
        # chèn thong tin vao bang Users
        query = '''INSERT INTO Users (Username, Password, Role)  VALUES (?, ?, ?)'''
        cursor.execute(query, (username, password, role))
        connection.commit()

        query_useid = '''SELECT UserID FROM Users WHERE Username = ?'''
        cursor.execute(query_useid, (username,))
        return cursor.fetchone()[0]
