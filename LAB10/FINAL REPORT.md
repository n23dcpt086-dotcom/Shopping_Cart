Final Report – Mini Project ATM


1. Giới thiệu ATM mini-project

ATM mini-project được thực hiện trong Lab 10 nhằm tích hợp toàn bộ các kết quả từ những Lab trước để tạo thành một hệ thống mô phỏng ATM cơ bản. Hệ thống này giúp sinh viên rèn luyện khả năng phân tích – thiết kế bằng UML, thiết kế cơ sở dữ liệu, lập trình giao diện kết nối DB, kiểm thử phần mềm và quản lý tiến độ bằng Jira.

   Các chức năng chính của hệ thống bao gồm:

   
   + Đăng nhập tài khoản bằng thông tin có sẵn trong cơ sở dữ liệu.

   + Thực hiện rút tiền từ tài khoản, kiểm tra số dư, cập nhật lại sau giao dịch.

   + Lưu lại lịch sử giao dịch trong cơ sở dữ liệu.

   + Quản lý tiến độ dự án với mô hình Scrum thông qua Jira.
  

2. Mô hình UML
Hệ thống được phân tích và thiết kế với các sơ đồ UML sau:

- Use Case Diagram (Lab 02): mô tả các chức năng mà người dùng có thể thực hiện, bao gồm Đăng nhập, Rút tiền, Kiểm tra số dư. Hệ thống có nhiệm vụ xác thực và cập nhật dữ liệu.

- Sequence Diagram (Lab 03): mô tả chi tiết luồng thực hiện của chức năng rút tiền: người dùng nhập số tiền → hệ thống kiểm tra số dư trong DB → nếu đủ thì thực hiện trừ tiền và ghi giao dịch → trả kết quả cho người dùng.

- Class Diagram (Lab 06): gồm các lớp chính User, Account, Transaction và ATMController.

- Mỗi User có một Account.

- Một Account có thể có nhiều Transaction.

- ATMController quản lý toàn bộ logic xử lý.

Các mô hình UML này là nền tảng quan trọng để triển khai database và code sau đó.


3. Database & code minh hoạ

ERD (Lab 05):
Cơ sở dữ liệu của hệ thống bao gồm 3 bảng:

+ Users: lưu username và password.

+ Accounts: lưu số dư, liên kết với Users.

+ Transactions: lưu thông tin giao dịch (số tiền, loại giao dịch, thời gian).

Script SQL mẫu:

CREATE TABLE Users (
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50) UNIQUE,
  password VARCHAR(50)
);

CREATE TABLE Accounts (
  account_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT,
  balance DECIMAL(15,2),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Transactions (
  trans_id INT PRIMARY KEY AUTO_INCREMENT,
  account_id INT,
  amount DECIMAL(15,2),
  trans_type VARCHAR(20),
  trans_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);


Code minh hoạ:

Form Login (Lab 04): người dùng nhập username/password, hệ thống xác thực trong bảng Users. Nếu hợp lệ thì vào màn hình chính, nếu sai thì báo lỗi.

Withdraw Module (Lab 07): người dùng nhập số tiền rút, hệ thống kiểm tra số dư trong Accounts, nếu đủ thì trừ số dư và thêm một bản ghi vào Transactions.


4. Kết quả test & sprint report

Test (Lab 08):

+Đăng nhập với tài khoản hợp lệ → Pass.

+Đăng nhập sai mật khẩu → Fail như mong đợi.

+Rút tiền với số dư không đủ → Bị từ chối, Pass.

+Rút tiền hợp lệ → Thành công, số dư được cập nhật, Pass.

Sprint report (Lab 09):
Quản lý công việc bằng Jira, chia thành nhiều Sprint:

+Sprint 1: Phân tích yêu cầu, Use Case và Database.

+Sprint 2: Thiết kế và cài đặt form Login.

+Sprint 3: Cài đặt Withdraw module và kết nối DB.

+Sprint 4: Viết test case, chạy thử nghiệm, viết báo cáo.

Jira board thể hiện đầy đủ backlog, công việc đang làm, công việc hoàn thành, cùng velocity chart để theo dõi tiến độ.


5. Kết luận & định hướng mở rộng

Kết luận:
ATM mini-project đã tích hợp thành công toàn bộ artifacts từ Lab 02 đến Lab 09. Hệ thống có thể demo luồng cơ bản: đăng nhập và rút tiền có kết nối DB. Đây là bước mô phỏng quan trọng, củng cố kiến thức UML, cơ sở dữ liệu, lập trình, kiểm thử và quản lý dự án.

Định hướng mở rộng:

-Thêm chức năng chuyển khoản giữa các tài khoản.

-Cho phép người dùng in hoặc xuất sao kê giao dịch.

-Tăng cường bảo mật với mã hoá mật khẩu, xác thực hai lớp (OTP).

-Quản lý nhiều loại tài khoản (thanh toán, tiết kiệm).

-Nâng cấp giao diện trực quan, thân thiện với người dùng.
