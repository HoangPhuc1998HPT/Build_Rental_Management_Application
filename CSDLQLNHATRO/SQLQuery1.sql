create database QLThueNhaTro;
-- Tạo table user
Create table Users (
	UserID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(50),
    Password NVARCHAR(255),
	Role NVARCHAR(12)
	CONSTRAINT chk_role CHECK (Role IN ('admin', 'chutro', 'nguoithuetro'))
);
ALTER TABLE Users ADD is_active BIT DEFAULT 0;
select * from Users
select * from Chutro
select * from NguoiThueTro
select * from Admins
select * from TTPhongtro

SELECT IDChutro FROM Chutro join Users on users.UserID  = Chutro.UserID WHERE Username = 'testchutro10';

SELECT users.username, users.role, users.UserID, chutro.hoten, chutro.cccd, chutro.Phone
FROM users
JOIN chutro ON users.UserID = chutro.UserID

SELECT users.username, users.role, users.UserID
FROM users
WHERE (users.is_active IS NULL OR users.is_active != 1)


SELECT * FROM TTPhongtro
WHERE is_active = 1;

DELETE FROM Users
WHERE is_active IS NULL;

SELECT * FROM Users
WHERE UserID IN (SELECT UserID FROM Users WHERE is_active IS NULL);


DELETE FROM Admins
WHERE UserID IN (SELECT UserID FROM Users WHERE is_active IS NULL);

DELETE FROM Chutro
WHERE UserID IN (SELECT UserID FROM Users WHERE is_active IS NULL);

DELETE FROM Users
WHERE is_active IS NULL;

-- Tạo admin 
CREATE TABLE Admins (
    AdminID INT PRIMARY KEY IDENTITY(1,1),
    FullName NVARCHAR(255),
    Username NVARCHAR(50),
    Password NVARCHAR(255)
);

select* from Admins

ALTER TABLE Admins ADD IsRoot BIT DEFAULT 0;
ALTER TABLE Admins ADD UserID INT;
ALTER TABLE Admins ADD CONSTRAINT FK_Admins_UserID
FOREIGN KEY (UserID) REFERENCES Users(UserID);
-- Tạo người cho thuê nhà trọ
CREATE TABLE Chutro (
    IDChutro INT PRIMARY KEY IDENTITY(1,1),
    HoTen NVARCHAR(255),
    CCCD NVARCHAR(12) UNIQUE,
    Phone NVARCHAR(15)
);
ALter table Chutro add UserID INT;
ALTER TABLE Chutro ADD CONSTRAINT FK_Chutro_UserID
FOREIGN KEY (UserID) REFERENCES Users(UserID);

-- Tạo thông tin phòng trọ
CREATE TABLE TTPhongtro (
    IDPhong INT PRIMARY KEY IDENTITY(1,1),
    TenPhong NVARCHAR(100),
    Address NVARCHAR(255),
    Giadien DECIMAL(10,2),
    GIanuoc DECIMAL(10,2),
    GiaPhong DECIMAL(10,2),
    Sodienhientai INT,
    Sonuochientai INT
);

ALter table TTPhongtro add Tinhtrang NVARCHAR(50);
ALter table TTPhongtro add IDChutro INT;
ALTER TABLE TTPhongtro ADD CONSTRAINT FK_TTPhongtro_IDChutro
FOREIGN KEY (IDChutro) REFERENCES Chutro(IDChutro);




-- Tạo Người thuê trọ
CREATE TABLE NguoiThueTro (
    IDnguoithue INT PRIMARY KEY IDENTITY(1,1), -- IDnguoithue
    Hoten NVARCHAR(255),
    CCCD NVARCHAR(12) UNIQUE,
    Phone NVARCHAR(15),
    Ngaybatdauthue DATE,
    Ngayketthucthue DATE
);
ALter table NguoiThueTro add UserID INT;
ALTER TABLE NguoiThueTro ADD CONSTRAINT FK_NguoiThueTro_UserID
FOREIGN KEY (UserID) REFERENCES Users(UserID);



--Thêm khóa khoại IDPhong vào Chutro
alter table TTPhongtro add IDnguoithue INT Null;
ALTER TABLE TTPhongtro ADD CONSTRAINT FK_TTPhongtro_IDnguoithue
FOREIGN KEY (IDnguoithue) REFERENCES NguoiThueTro(IDnguoithue);

ALTER TABLE TTPhongtro
DROP CONSTRAINT FK_TTPhongtro_IDnguoithue;






- Tạo bảng hóa đơn
CREATE TABLE HoaDon (
    BillID INT PRIMARY KEY IDENTITY(1,1), -- Mã hóa đơn tự động tăng
    Tiennha DECIMAL(10,2),               -- Phí thuê nhà hàng tháng
    Tiendien DECIMAL(10,2),        -- Phí điện
    Tiennuoc DECIMAL(10,2),              -- Phí nước
    Tienrac DECIMAL(10,2),              -- Phí rác
    Chiphikhac DECIMAL(10,2),             -- Các phí khác
    Giamgia DECIMAL(10,2),              -- Giảm giá
    Tongchiphi DECIMAL(10,2),           -- Tổng số tiền phải trả
    Ngayxuathoadon DATE                        -- Ngày xuất hóa đơn
);
-- Them khoa ngoai idPhong cho Bills
alter table HoaDon add IDPhong INT;

ALTER TABLE HoaDon ADD CONSTRAINT FK_HoaDon_IDPhong
FOREIGN KEY (IDPhong) REFERENCES TTPhongtro(IDPhong);

alter table HoaDon add idCTHD INT;


-- Bang chi tiet hoa don

CREATE TABLE CTHoadon (
    idCTHD INT PRIMARY KEY IDENTITY(1,1),
    BillID INT FOREIGN KEY REFERENCES HoaDon(BillID),
    SodienUsed INT, -- Số điện tiêu thụ = số hiện tại - số trước
    SonuocUsed INT,       -- Số nước tiêu thụ = số hiện tại - số trước
    DaysInMonth INT,     -- Số ngày ở trong tháng
    Tiennha DECIMAL(10,2), -- Tiền nhà = giá phòng / 30 * số ngày
    Ngaythutienthangtruoc DATE, -- Ngày thu tiền tháng trước
    Ngaykiemtrasodiennuoc DATE,     -- Ngày kiểm tra số điện nước
    Chiphiphatsinh DECIMAL(10,2),  -- Chi phí phát sinh
    Tienrac DECIMAL(10,2),
    Giamgia DECIMAL(10,2)
);

alter table CTHoadon Drop CONSTRAINT FK__CTHoadon__BillID__59FA5E80
alter table CTHoadon Drop column BillID

ALTER TABLE CTHoadon
DROP COLUMN Ngaythutienthangtruoc, Ngaykiemtrasodiennuoc;

alter table CTHoadon add IDPhong INT;

ALTER TABLE CTHoadon ADD CONSTRAINT FK_CTHoadon_IDPhong
FOREIGN KEY (IDPhong) REFERENCES TTPhongtro(IDPhong);

alter table CTHoadon add Ghichu NVARCHAR(250);

ALTER TABLE CTHoadon
ADD sodienthangtruoc INT, 
    sonuocthangtruoc INT;

ALTER TABLE CTHoadon
ADD ngaythutiendukien DATE

-- Khoi tao  bang complant

CREATE TABLE Complaints (
    ComplaintID INT PRIMARY KEY IDENTITY(1,1),
    IDphong INT FOREIGN KEY REFERENCES TTPhongtro(IDphong),
    AdminID INT FOREIGN KEY REFERENCES Admins(AdminID),
    ComplaintText NVARCHAR(255),
    ComplaintDate DATE,
    ResolutionDate DATE NULL -- Ngày giải quyết, có thể NULL
);


-- Khoi tao bang danh gia

CREATE TABLE Ratings (
    RatingID INT PRIMARY KEY IDENTITY(1,1),
    IDPhong INT FOREIGN KEY REFERENCES TTPhongtro(IDPhong),
    IDChutro INT FOREIGN KEY REFERENCES Chutro(IDChutro),
    RatingScore INT CHECK (RatingScore BETWEEN 1 AND 10)
);

-- chưa chạy
--SELECT CONVERT(VARCHAR, Ngaybatdauthue, 105) AS Ngaybatdauthue FROM NguoiThueTro
--

insert into Users (Username,Password,Role) values ('hoangphuc','123456','admin');

select* from TTPhongtro
select* from Chutro
select* from Users
select* from Admins
	

Select Users.Username, chutro.hoten, chutro.CCCD, chutro.Phone, count(TTphongtro.IDPhong) as Tongsophongtro
from Chutro
left join TTPhongtro on Chutro.IDChutro = TTphongtro.IDChutro
left join Users on Chutro.UserID = Users.UserID
group by chutro.hoten, chutro.CCCD, chutro.Phone, Users.Username  

SELECT 
Users.username, NguoiThueTro.Hoten, NguoiThueTro.cccd, NguoiThueTro.phone, TTphongtro.Tenphong
FROM NguoiThueTro
JOIN TTphongtro ON NguoiThueTro.IDnguoithue = TTphongtro.IDnguoithue
JOIN Users ON NguoiThueTro.UserID = Users.UserID

SELECT 
TTphongtro.Tenphong, TTphongtro.Address, TTphongtro.Giaphong, Chutro.Hoten, NguoiThueTro.Hoten
FROM TTphongtro
JOIN Chutro ON TTphongtro.Idchutro = Chutro.IDchutro 
JOIN NguoiThueTro ON TTphongtro.IDnguoithue = NguoiThueTro.IDnguoithue





SELECT IDChutro FROM Chutro JOIN Users ON Chutro.UserID = Users.UserID

SELECT IDChutro
FROM Chutro
JOIN Users ON Chutro.UserID = Users.UserID

SELECT Admins.AdminID
FROM Admins
JOIN Users ON Admins.UserID = Users.UserID

SELECT NguoiThueTro.IDnguoithue
FROM NguoiThueTro
JOIN Users ON NguoiThueTro.UserID = Users.UserID

select* from HoaDon

SELECT IDnguoithue, Hoten, UserID FROM NguoiThueTro WHERE CCCD =123456789

select * from TTPhongtro

Update TTPhongtro SET IDnguoithue = '68'
where IDPhong = '7' 




select TTPhongtro.IDPhong
from TTPhongtro

select CTHoadon.SodienUsed, CTHoadon.sodienthangtruoc
from CTHoadon
join HoaDon on CTHoadon.idCTHD = HoaDon.idCTHD
where 7 -1  = HoaDon.Ngayxuathoadon

INSERT INTO CTHoadon 
    ( SodienUsed, SonuocUsed, DaysInMonth, Tiennha, Chiphiphatsinh, Tienrac, Giamgia, sodienthangtruoc, sonuocthangtruoc, IDPhong, Ghichu,ngaythutiendukien)
VALUES 
    ( 150 , 150, 30, 1500000, 0, 30000, 0, 0, 0, 1, 'test1','2024-5-9');


	
INSERT INTO HoaDon (Tiennha, Tiendien, Tiennuoc, Tienrac, Chiphikhac, Giamgia, Tongchiphi, Ngayxuathoadon, IDPhong, idCTHD)
VALUES (1500000, 450000, 3000000, 30000, 0, 0, 5950000, '2024-08-29', 1,2);

SELECT TOP 1 *
FROM CTHoadon
WHERE IDPhong = 1
ORDER BY Ngaythutiendukien DESC;





select Hoadon.Ngayxuathoadon, HoaDon.BillID, CTHoadon.ghichu, Hoadon.Tongchiphi, TTPhongtro.TenPhong, 
                TTphongtro.Address, Chutro.hoten, Chutro.Phone
                from Hoadon
                join CTHoadon on CTHoadon.idCTHD = Hoadon.idCTHD
                join TTPhongtro on TTPhongtro.IDphong = CTHoadon.IDphong
                join Chutro on Chutro.IDchutro = TTPhongtro.IDchutro
                where TTPhongtro.IDnguoithue = 2
	
select * from Chutro
select * from HoaDon	
select * from CTHoadon
select* from NguoiThueTro
select * from TTPhongtro	
select* from Users
select* from Admins

Insert Admins(FullName,Username,Password,IsRoot,UserID)values ('Trần Hoàng Phúc',' admin_01', 'pass123',1,69)

DELETE FROM HoaDon WHERE Ngayxuathoadon IS NULL;
DELETE FROM Users WHERE username ='None' ;
DELETE FROM Chutro
WHERE UserID IN (SELECT UserID FROM Users WHERE username IS NULL OR username IN (
    SELECT username 
    FROM Users 
    GROUP BY username 
    HAVING COUNT(*) > 1
));
DELETE FROM NguoiThueTro
WHERE UserID IN (SELECT UserID FROM Users WHERE username IS NULL OR username IN (
    SELECT username 
    FROM Users 
    GROUP BY username 
    HAVING COUNT(*) > 1
));
WITH CTE AS (
    SELECT 
        username,
        UserID,  -- Assuming UserID is the primary key
        ROW_NUMBER() OVER (PARTITION BY username ORDER BY UserID) AS row_num
    FROM 
        Users
    WHERE username IS NOT NULL
)
DELETE FROM CTE
WHERE row_num > 1;

-- Nhập dữ liệu ảo:
INSERT INTO Users (Username, Password, Role)
VALUES 
('admin_1', 'pass123', 'admin'),
('admin_2', 'pass123', 'admin'),


INSERT INTO Admins (FullName, Username, Password, IsRoot, UserID)
VALUES 
('Admin One', 'admin_1', 'pass123', 1, 1),
('Admin Two', 'admin_2', 'pass123', 0, 2);

INSERT INTO Chutro (HoTen, CCCD, Phone, UserID)
VALUES 
('Nguyen Van A', '012345678901', '0901234567', 3),
('Tran Thi B', '012345678902', '0902234567', 4),
('Le Van C', '012345678903', '0903234567', 5),
('Hoang Van D', '012345678904', '0904234567', 6),
('Pham Thi E', '012345678905', '0905234567', 7);


SELECT 
                    TTPhongtro.TenPhong, 
                    NguoiThueTro.Hoten, 
                    NguoiThueTro.Phone, 
                    HoaDon.Tongchiphi, 
                    HoaDon.Ngayxuathoadon,
                    HoaDon.BillID,
                    TTPhongtro.Idchutro,
                    CTHoaDon.Idphong
                FROM 
                    TTPhongtro
                JOIN 
                    NguoiThueTro ON TTPhongtro.IDnguoithue = NguoiThueTro.IDnguoithue
                JOIN 
                    CTHoaDon ON TTPhongtro.IDPhong = CTHoaDon.IDPhong 
				JOIN
					HoaDon on HoaDon.idCTHD = CTHoadon.idCTHD


					select
							Hoadon.Ngayxuathoadon, HoaDon.BillID, CTHoadon.ghichu, Hoadon.Tongchiphi, TTPhongtro.TenPhong, TTphongtro.Address, Chutro.hoten, Chutro.Phone
                    from Hoadon
					join 
						CTHoadon on CTHoadon.idCTHD = Hoadon.idCTHD
                    join 
						TTPhongtro on TTPhongtro.IDphong = CTHoadon.IDphong
                    join 
						Chutro on Chutro.IDchutro = TTPhongtro.IDchutro
                    order by HoaDon.BillID DESC 

SELECT 
                        TTPhongtro.TenPhong, 
                        NguoiThueTro.Hoten, 
                        NguoiThueTro.Phone, 
                        HoaDon.Tongchiphi, 
                        HoaDon.Ngayxuathoadon,
                        HoaDon.BillID,
                        TTPhongtro.Idchutro,
                        CTHoaDon.Idphong
                    FROM 
                        TTPhongtro
                    JOIN 
                        NguoiThueTro ON TTPhongtro.IDnguoithue = NguoiThueTro.IDnguoithue
                    JOIN
                        CTHoadon ON CTHoadon.IDPhong = TTPhongtro.IDPhong
                    JOIN
                        HoaDon ON CTHoadon.idCTHD = HoaDon.idCTHD 