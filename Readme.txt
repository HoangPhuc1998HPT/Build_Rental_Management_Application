________Note : chạy bằng File Main -----------------

Ngày 15/9/2024 xóa làm lại lần 2

 mô tả về App Quản lý thuê trọ trên desktop:
Chủ thể: Chủ trọ, người thuê trọ, Admin, Phòng trọ, Hóa đơn, Chi tiết hóa đơn

Thực hiện theo cấu trúc MVC - modul  - Controller - View 
1. Trang đăng kí ( đăng kí với 1 trong 3 role cho phép người dùng tùy chọn:admin, chỉ trọ, người thuê trọ)
- Chức năng kiểm tra trùng tài khoản: chỉ có duy nhất 1 tên tài khoản
- Chức năng kiểm tra xác nhận mật khẩu lần 2 không khớp
- Trang đăng kí gồm (tên tài khoản, mật khẩu, xác nhận mật khẩu) - Tạo UserID - trả về UserID
- Sau đăng kí sẽ chuyển hướng đến trang cập nhật thông tin cá nhân cho user (hoàn thiện bước này mới cập nhật cơ sở dữ liệu vào User và vào Class với role tương ứng)
- Cập nhật thông tin cho user: sau khi nhấn đăng kí chuyển đến trang này
+ Với admin: Cập nhật thêm fullname, Admin ID được tạo tự động và UserID truyền CSDL admin, admin giới thiệu phòng trống cho người thuê
+ Với chủ trọ: Cập nhật thêm Họ Tên, CCCD, Phone, IDChutro được tạo tự động, UserID được truyền vào CSDL Chủ trọ, quản lý các hóa đơn do mình tạo
+ Với người thuê trọ: Cập nhật thêm Họ Tên, CCCD, Phone, IDNguoithue được tạo tự động, UserID được truyền vào CSDL Người thuê trọ (các thuộc tính còn lại cho phép null), Thực hiện các chức năng complant, đánh giá nhà trọ phục vụ công tác quảng cáo.
2 Trang đăng nhập (đăng nhập sẽ nhận role để điều hướng đến đúng dashboard sử dụng)
- Sau khi đăng nhập sẽ chuyển hướng đến các trang View.Dashboard - đi theo role
+ DashboardAdmin: Với các chức năng của admin (để trống sẽ cập nhật sau)
+ DashboardChutro: Với các chức năng (Tạo phòng trọ, Thêm người thuê trọ, Tạo hóa đơn, Xuất hóa đơn, Xem danh sách phòng trọ- thuộc user chủ trọ)
+ DashboardNguoiThuetro: Với các chức năng ( Xem thông tin phòng trọ, xem hóa đơn, Xem danh sách hóa đơn)
3. Còn nhiều chức năng và kết cấu khác sẽ được tạo ra trong quá trình thực hiện ...
-
-
-




__________________________________________________
cấu trúc sơ bộ:
project/
│
├── backend/              			# Thư mục chứa các phần backend, xử lý cơ sở dữ liệu
│   ├── models/           			# Thư mục chứa các models đại diện cho các bảng cơ sở dữ liệu
│   │   ├── __init__.py  		 	# Tệp để biến thư mục này thành package Python
│   │   ├── db.py         			# Kết nối với cơ sở dữ liệu và khởi tạo database
│   │   ├── user.py      		 	# Model User và các lớp kế thừa
│   │   ├── admin.py     		 	# Model Admin kế thừa từ User
│   │   ├── chutro.py    		 	# Model Chutro kế thừa từ User
│   │   ├── nguoi_thue_tro.py 		# Model NguoiThueTro kế thừa từ User
│   │   ├── phong_tro.py  			# Model PhongTro đại diện cho bảng phòng trọ
│   │   └── hoadon.py     			# Model Hoadon đại diện cho bảng hóa đơn
│   └── services/         		
│       ├── auth_service.py 		# Xử lý xác thực người dùng (đăng ký, đăng nhập)
│       └── user_service.py 		# Xử lý các thao tác liên quan đến User
│
└── main.py               			# Tệp chạy chính của ứng dụng




Lưu ý các chức năng: Tạo mới  xóa  update data 

Tính trừu tượng - tính đóng gói -  tính đa hình 

__________________________________________________
Cấu trúc project với các hàm
project/
│
├── backend/              # Thư mục chứa các phần backend, xử lý cơ sở dữ liệu
│   ├── models/           # Thư mục chứa các models đại diện cho các bảng cơ sở dữ liệu
│   ├── utils
		def get_chutro_id_by_username		


│   │   ├── __init__.py   # Tệp để biến thư mục này thành package Python
│   │   ├── db.py         # Kết nối với cơ sở dữ liệu và khởi tạo session
		def create_database_connection
 
│   │   ├── user.py       # Model User và các lớp kế thừa
		def check_password
		def username_exists
		def create_user

│   │   ├── admin.py      # Model Admin kế thừa từ User
		def save_to_database 		-- null

│   │   ├── chutro.py     # Model Chutro kế thừa từ User
		def save_to_database		-- null
 		def check_unique_cccd_phone
│   │   ├── nguoi_thue_tro.py # Model NguoiThueTro kế thừa từ User
		def save_to_database		-- null

│   │   ├── phong_tro.py  # Model PhongTro đại diện cho bảng phòng trọ
		def save_to_database 		-- null
		def add_+tenant 		-- null

│   │   └── hoadon.py     # Model Hoadon đại diện cho bảng hóa đơn
		def save_to_database		-- null

│   │   └── role.py		# Role( admin, chutro, nguoithuetro)
		def get_all_role()

│   └── services/         # Các dịch vụ (services) cung cấp phương thức CRUD, xác thực, v.v.
│       ├── auth_service.py # Xử lý xác thực người dùng (đăng ký, đăng nhập)
│       └── user_service.py # Xử lý các thao tác liên quan đến User
│
└── main.py               # Tệp chạy chính của ứng dụng
├── frontend/
	└── views/
		├── homelogin.py 		# giao diện chứa 2 nút đăng kí và đăng nhập
			- đăng kí ==>  command=self.go_to_login
			def go_to_login 
			- đăng nhập ==> command=self.go_to_dashboard
		├── login.py
			- def check_login 	# Kiểm tra và điều hướng đến đúng dashboard người dùng

		├── register.py
			- Chọn Admin / chủ trọ / người thuê trọ
				- Tên tài khoản
				- Mật khẩu 	
				- Xác nhận mật khẩu
			
			- def check_register_user 	# Khi chọn vai trò để tài khoản sẽ dẫn đến giao 
			Hàm này trả về	UpdateInfomationView  diện cập nhật thông tin giành cho tài khoản
			- def go_back_to_login ==> quay về trang homelogin

			
		├── update_infomation_user.py		# get cái role
			- def go_to_login		# di chuyển tới trang login
			- def save_info_admin		# lưu thông tin về CSDL
			- def save_info_chutro		# lưu thông tin về CSDL
			- def save_info_nguoi_thue	# lưu thông tin về CSDL

		├── dashboard_admin.py	(username)		# hiển thị chức năng admin
#			
			- def Duyet_tao_user(self)
			- def on_double_click(self, event)
			- def show_active_user(self, username):
			- def Go_to_xem_danh_sach_tat_ca_cac_hoadon(self):
			- def Xem_danh_sach_tat_ca_cac_chutro(self):
			- def Xem_danh_sach_tat_ca_cac_phongtro(self):
			- def Xem_danh_sach_tat_ca_cac_nguoithuetro(self):
			- def reload_admin_dashboard(self):




			- def Go_to_dangxuat(self):
			- 
			
		- Tạo 1 form mẫu cho xem thông tin (chủ trọ, người thuê, phòng)
			- chủ trọ cần hiển thị những thông tin gì:
				- Username - Họ tên - CCCD - SĐT - Số phòng trọ (double click vào là lên danh sách) 
				- Trang hiển thị danh sách phòng trọ: tên phòng - giá phòng - tình trạng
			- Hiển thị danh sách người thuê trọ:
				- Username - Họ tên - CCCD - SĐT - Tên phòng đang trọ(nếu chưa có phòng thì Null)


			- Duyệt user_chutro  
				+ Tận thêm column is_active cho database User - Khi tài khoản được tạo mặc định User  == 0
				+ Tạo def active user cho các tài khoản (chủ trọ và người thuê trọ) ==> update id_active == 1
					- tạo def active user
					- Tạo danh sách hiển thị username chưa active => khi bấm vào nút active để active.
					- nếu là chủ trọ
					- nếu là người thuê trọ
				+ Trong checklogin - Thêm kiểm tra is_active == 1 mới cho phép đăng nhập
				+ 
				==> tạo thêm database
#			- Xem thông tin tất cả các phòng
			- Xem thông tin all chủ trọ
			- Xem thông tin all người thuê
			- Xem danh sách tất cả các người thuê

			
			- def go_to_dangxuat 			# tạo nút đăng xuất về homelogin


		├── dashboard_chutro.py (username)		# hiển thị chức năng chủ trọ
			- def Go_to_tao_phongtro		# chức năng tạo phòng trọ
			- def Go_to_show_danh_sach_nhatro	# Hiển thị tất cả các phòng thuộc idchutro (đang lỗi)
			- def Go_to_add_nguoithuetro		
			- def Go_to_create_hoadon
			- def Go_to_xuat_hoadon
			- def Go_to_xem_danh_sach_hoadon
			- def Go_to_login 

		├── dashboard_thuetro.py (usename)		# hiển thị chức năng người thuê trọ
#
#			- def go_to_dangxuat			# tạo nút đăng xuất về homelogin
		Có 2 trường hợp: 
			1 - Người thuê trọ chưa có phòng thuê # chỉ được thêm khi chủ trọ thêm vào (iactive_nguoithue == True)
				- Hiển thị danh sách phòng (table - list - tất cả các phòng trọ còn trống)
					+ Tên phòng trọ - giá nhà - địa chỉ - Tên chủ trọ - số điện thoại
				- Chi tiết phòng (table)
					+ Tên phòng trọ - địa chỉ
					+ Giá nhà : giá thuê phòng - giá điện - giá nước - chi phí khác
				
				- Gửi request xem phòng

			2 - Người thuê trọ đã có phòng thuê
				- Xem thông tin phòng
				- Xem danh sách hóa đơn ==> Hiện danh sách hóa đơn


			- Xem hóa đơn mới nhất
			- Danh sách hóa đơn cũ
			- Danh sách tất cả các phòng trống
			
			- def Get_id_nguoithue_from_username(self,username):
			- def Get_id_phongtro_from_id_nguoithue(self,id_nguoithue):
			- def Show_danh_sach_hoadon(self, id_nguoithue):
			- def on_row_double_click(self, id_nguoithue, event):
			- def open_bill_detail(self, bill_id, id_chutro, id_phong):



			- def Go_to_dangxuat(self):



		├── CreateRoomView.py		
			- def save_room
			- def go_to_Dashboardchutro
			
		├── CreateShowRoomView.py	
			- Hiển thị giao diện theo danh sách phòng
			- def create_room_buttons	# Tạo các button cho kiểm soát phòng trọ
			- def get_room_list_from_db  	# lấy danh sách phòng _ id_phòng		
			- def update_nguoithue		# update người thuê/ngày thuê theo cccd
			- def xuat_hoadon
			- def update_hoadon
			- def update_infor_room
			- def xoa_phong			# sau khi xóa sẽ quay lại dashboard_chutro
			- def go_to_back_dashboard_chutro 	# quay lại dashboard chủ trọ

		├── CreateRoomThemnguoithue.py
			- def verify_and_update			# kiểm tra CCCD trong cơ sở dữ liệu
			- def get_nguoithue_by_cccd		# lấy thông tin người thuê từ cccd
			- def update_room_tenant		# update dữ liệu
			- def go_to_back_create_ShowRoomsView 	# quay về trang ShowRoomsView
			- 
			- 

		├── CreateRoomupdateTT_Phong.py

			- def verify_and_update
			- def go_back_to_create_show_rooms_view
			-
			-
			-
		├── createHoadon_update.py
			- def tao_CTHD(self,id_phong):					# xử lý tiền nhà 
			- def get_id_nguoithue_from_id_phong(self,id_phong):		# Lấy id người thuê
			- def get_id_nguoithue_from_id_phong(self,id_phong):		# xử lý chuyển đổi dịnh dạng ngày tháng
			- def Xu_Ly_So_ngay_o_trong_thang(self, id_nguoithuetro):	# Lấy tiền nhà từ file TT Phòng
			- def get_tien_nha_from_TTPhong(self, id_phong):		# Xử lý chi phí phát sinh
			- def xu_ly_chiphiphatsinh(self):				# Xử lý bước thanh toán
			- def tinh_toan(self):						# Xuất kết quả xử lý
			- def hien_thi_ket_qua(self, thang, nam):			# Lấy số điện tháng trước
			- def sodienthangtruoc(self, thang, nam):			# lấy số nước tháng trước
			- def sodiendasudung(self, thang, nam):				# xử lý số điện đã sử dụng
			- def sonuocdasudung(self, thang, nam):				# Xử lý số nước đã xử dụng
			- def get_id_chutro_from_id_phong(self, id_phong):		# Lấy id_chủ trọ
			- def go_to_back_create_ShowRoomsView(self):			# trở về màn hình dashboard xem ds phòng trọ


 		├── createHoadon_XuatHoaDon.py
			- def Go_to_show_danh_sach_nhatro(self):
			-  def load_thongtin_hoadon(self):
			- def getgiadien(self, id_phong)
			- def getgianuoc(self, id_phong):
			- def load_thongtin_chutro(self, id_chutro):
			- def load_thongtin_nguoithue(self, id_nguoithue):
			- def get_id_nguoithue_from_id_phong(self,id_phong):
			- def Nhaphoadon(self):
		├── show_detall_hoadon.py
			- def load_thongtin_hoadon(self):

		├── admin_show_all_chutro.py
			- def load_du_lieu_chutro(self):



			Cấu trúc Hóa đơn
			- Số hóa đơn
			- Ngày xuất hóa đơn
		Người bán:
			- Họ Tên: (chủ trọ) truy xuất id chủ trọ => HỌ TÊN CHỦ TRỌ,...
			- Địa chỉ: Địa chỉ 
			- Sđt liên hệ: 
			- CCCD:
		Người mua:
			- Tên khách hàng
			- Địa chỉ
			- CCCD
			- Số điện thoại
		Nội dung hóa đơn: hiển thị 1 table 4 cột( Nội dung - số lượng - đơn giá - thành tiền)
			- Tiền thuê phòng : 	Số lượng 	Đơn giá		Thành tiền
			- Tiền điện
			- Tiền nước
			- Tiền rác
			- Chi phí khác
			- Giảm giá
			- Tổng cộng 
				
		

login (usename) - > dashboard_chutro - get id chủ trọ --> CreateRoomView(go_to_tao_phongtro) --> 


chủ trọ muốn xuất được hóa đơn phải vào cập nhật số điện hiện tại + số nước hiện tại
==> khi có số điện hiện tại + số nước hiện tại thì ở tiến hành cập nhật chi tiết hóa đơn.

Ở CThoadon : (lấy id phòng)
	+ sodienUsed = số điện hiện tại - số 



					Mô hình MVC



Model - View - Controller

- Model : dữ liệu và logic nghiệp vụ. Quản lý trạng thái của dữ liệu, xử lý các phép tính hoặc các quy tắc nghiệp vụ
Quản lý dữ liệu trên ứng dụng - Xử lý logic nghiệp vụ - Cập nhật trạng thái thông báo cho controller và View

- View: Hiển thị dữ liệu từ Model và nhận dữ liệu từ người dùng. Không tương tác với dữ liệu, nhận dữ liệu từ controller
Hiển thị dữ liệu - Nhận thao tác người dùng

- Controller
Trung gian giữa Model và View, nhận các y/c từ người dùng thông qua View, xử lý các yêu cầu thông qua Model và trả lại cho View
Nhận yêu cầu từ VIEW - Tương tác với Model - Cập nhật View với dữ liệu từ Model

Lợi ích của MVC
Tách biệt trách nhiệm, Tái sử dụng Model và View, Dể bảo trì và mở rộng - Kiểm thử dể dàng hơn
 
phân tích 
active_user, delete_user ==> nghiệp vụ Controller	=> services.py
check_login 		==> nghiệp vụ  Controller	=> create LoginController.py
Các chức năng chuyển đổi màn hình ==> controller 	=> navigation.py


View
	- Creating forms and layouts 
	- Gathering user inputs (text, selections, etc.) and forwarding them to the appropriate Controller.
Controller
	- Handle user input (like login requests).
	- Query the Model for user data or perform database updates.
	- Update the View
Model 
	- The Model should only manage data-related operations
	- 
Remove business logic from views

backend/
    models/
        admin.py  # Models only handle data logic
        chutro.py
        user.py
    controllers/
        login_controller.py  # Controllers handle business logic
        admin_controller.py
frontend/
    views/
        login.py  # Views handle UI
        dashboard_admin.py
    navigation.py  # Responsible for handling view transitions
		

		---		Chuyển đổi 		---

'admin_show_all_chutro.py',			# xong
  'Admin_show_all_hoadon.py',			# xong
  'admin_show_all_nguoithuetro.py',		# xong
  'admin_show_all_phongtro.py',			# xong
  'createHoadon_showDSHoaDon.py',		# xong
  'createHoadon_update.py',			# xong
  'createHoadon_XuatHoaDon.py',			# xong
  'createRoomThemnguoithue.py',			# xong
  'createRoomupdateTT_Phong.py',		# xong
  'createRoomView.py',				# xong
  'createShowRoomsView.py',			# xong
  'dashboard_admin.py',				# xong
  'dashboard_chutro.py',			# xong
  'dashboard_thuetro.py',			# xong

  'homelogin.py',				# xong
  'login.py',					# xong
  'navigation.py',				# chuyển
  'register.py',				# xong
  'show_detail_hoadon.py',			# xong
  'update_infomation_user.py'])




Login -> đã chuyển xong				# login_controller.py
Homelogin -> OK					# login_controller.py
register -> ok					# login_controller.py
login_controller --> OK
các select - insert data from until
Show_detall_hoadon --> OK			# utils.py
save_info_nguoi_thue(self)  --> 		# nguoithuetro.pyy
UpdateInfomationView --> OK 			# chutro.py, nguoithuetro.py, admin.py
dashboard_thuetro
	- on_row_double_click	--> nguoithuetro	
	- Get_id_nguoithue_from_username --> utils
	- Get_id_phongtro_from_id_nguoithue --> utils
	- Show_danh_sach_hoadon --> hoadon
	- show_danh_sach_hoadon(self, tree): -> nguoithuetro_controller
	- on_row_double_click(self, tree, event):-> nguoithuetro_controller
	- open_bill_detail(self, bill_id): -> nguoithuetro_controller


	
dashboard_chutro
	- Go_to_xem_danh_sach_hoadon(root,username): --> navigation
	- Go_to_tao_phongtro(root, username): --> navigation
	- Go_to_show_danh_sach_nhatro(root, u	sername): --> navigation
dashboard_admin
	- Xem_danh_sach_tat_ca_cac_chutro(root) 	--> navigation
	- duyet_tao_user(self, tree):			--> admin_controller
	- def on_double_click(self, event, tree):	--> admin_controller
	- def show_active_user(self, username):		--> admin_controller
	- def reload_admin_dashboard(self, tree):	--> admin_controller

CreateShowrommView.py
	- xoa_phong(root, id_phong, id_chutro,username)		--> navigation
	- go_to_update_nguoithue(root, id_chutro, id_phong)	--> navigation
	- go_to_back_dashboard_chutro(root, username)		--> navigation
	- go_to_XuatHoaDon(root,id_chutro ,id_phong)		--> navigation
	- go_to_update_hoadon(root, id_phong)			--> navigation
	- get_room_list_from_db(self, id_chutro)		--> PhongTroController
	- get_room_list_from_db					--> phongtro
CreateRoomView
	- save_room						--> phongtro

CreateRoomupdateTT_Phong
	- verify_and_update(root,id_...) 			--> photro

createRToomThemnguoithue:
	- verify_and_update(self,root,id_chutro,id_phong,cccd): --> nguoithuetro
	- update_room_nguoithue(self, thong_tin_nguoithue,id_phong): -->nguoithuetro
	- go_back_to_create_show_rooms_view(root,id_chutro):	--> navigation

CreateHoadon_XuatHoaDon
	- load_thongtin_hoadon(self) 				--> hoadon
	- nhaphoadon(self): --> hoaon --> 
CreateUpdate_hoadon:
	- sonuocdasudung(self, thang, nam):
	- sonuocthangtruoc(self, thang, nam)
	- sodienthangtruoc(self, thang, nam)
	- sodiendasudung(self, thang, nam)
	- get_tien_nha_from_TTPhong(self, id_phong)
	- Xu_Ly_So_ngay_o_trong_thang(self, id_nguoithuetro)
	- go_to_back_create_ShowRoomsView(self)
	- get_id_chutro_from_id_phong(self, id_phong)

CreateHoadon_showDSHoaDon
	- 


#eerooorrrrr

- Không xóa user được trong Admin Dashboard khi active 		==> đã xong
Lỗi khi kết nối cơ sở dữ liệu: ('23000', '[23000] [Microsoft][ODBC SQL Server Driver][SQL Server]The DELETE statement conflicted with the REFERENCE constraint "FK_Chutro_UserID". The conflict occurred in database "QLThueNhaTro", table "dbo.Chutro", column \'UserID\'. (547) (SQLExecDirectW); [23000] [Microsoft][ODBC SQL Server Driver][SQL Server]The statement has been terminated. (3621)')
- Xem danh sach phòng trọ trong Admin Dashboard lỗi: hiển thị user chủ trọ chưa active


- Tạo phòng trọ thiếu chức năng quay về
- detail hóa đơn gặp lỗi truy vấn SQL do thay đổi địa chỉ truy xuất 
	line 28, in info_show_detail_hoadon
    cursor.execute(query1, (result[10],))
- lỗi dashboard người thuê trọ  --> OK

- Lỗi cập nhật người thuê - đã fixx
- Lôi dashboard người thuê không get được thông tin ->  show_danh_sach_hoadon -> info_show_danh_sach_hoadon
- Lỗi tạo hóa đơn -->DashboardChutro-->CreateShowRoomsView-->go_to_update_hoadon-->CreateHoadon_update-->hien_thi_ket_qua--> OK
- Dashboard người thuê trọ không hiện thông tin phòng và danh sách hóa đơn -=-> DashboardNguoithuetro-->show_danh_sach_hoadon-->info_show_danh_sach_hoadon --> lỗi ở chủ trọ --> OK
- Bấm xuất hóa đơn không insert vào CSDL Hóa đơn --> dashboard chủ trọ -->go_to_show_danh_sach_nhatro-->CreateShowRoomsView-->go_to_XuatHoaDon-->OK CreateHoadon_XuatHoaDon--> OK
Lỗi khi thêm hóa đơn: ('42S22', "[42S22] [Microsoft][ODBC SQL Server Driver][SQL Server]Invalid column name 'IDPhong'. (207) (SQLExecDirectW); [42S22] [Microsoft][ODBC SQL Server Driver][SQL Server]Statement(s) could not be prepared. (8180)") --> OK
xuat
self.controller.go_to_nhaphoadon-->lỗi sau khi sửa CSDL - hoadon bỏ id_phong --> đã fix xong OK


##
- Thiếu bước quay lại danh sách phòng trọ ở bước cập nhật thông tin phòng - số điện, số nước -> OK
- xem danh sách hóa đơn -> chủ trọ -> không hiện danh sách hóa đơn -> OK
##

- Thiếu chức năng đổi mặt khẩu cho người dùng
- Xây dựng chức năng hiển thị các phòng trọ trống cho người thuê trọ xem
- 


















































   
