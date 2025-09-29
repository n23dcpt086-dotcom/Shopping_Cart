# Báo cáo cuối kỳ: ATM Mini-Project

## 1. Giới thiệu ATM Mini-Project

Dự án **ATM Mini-Project** là một mô hình hóa và triển khai các chức năng cơ bản của một hệ thống máy rút tiền tự động (ATM). Mục tiêu chính là xây dựng một hệ thống phần mềm đáng tin cậy, có khả năng xử lý các giao dịch tài chính chính như **xác thực thẻ/PIN**, **rút tiền**, **gửi tiền** và **chuyển khoản**.

**Phạm vi chính của dự án:**
* **Thiết kế kiến trúc hệ thống** bằng mô hình UML, bao gồm Class Diagram, Package Diagram, và Use Case.
* **Triển khai module nghiệp vụ quan trọng**, cụ thể là module **Rút tiền** bằng Python.
* **Thực hiện kiểm thử đơn vị** (Unit Test) cho các luồng xử lý chính của module Rút tiền.

---

## 2. Mô hình UML

### 2.1. Mô hình Phân Rã Gói (Package Diagram)

Hệ thống được tổ chức thành bốn gói (Package) chính để phân tách trách nhiệm và module hóa:
* **UI (User Interface):** Chịu trách nhiệm về giao diện người dùng.
* **Controller:** Xử lý logic điều phối giữa UI và các dịch vụ nghiệp vụ, đồng thời tương tác với cả `BankService` và `Hardware`.
* **BankService:** Chứa các logic nghiệp vụ lõi của ngân hàng, bao gồm xác thực và các giao dịch.
* **Hardware:** Mô phỏng tương tác với các thành phần vật lý của ATM.

### 2.2. Mô hình Lớp (Class Diagram)

Mô hình lớp xác định các thực thể chính và các mối quan hệ trong hệ thống:

| Lớp (Class) | Thuộc tính (Attributes) | Phương thức (Methods) |
| :--- | :--- | :--- |
| **ATM** | `atmId: int`, `location: String`, `cashLevel: double` | `authenticate(card, pin): boolean`, `withdraw(card, amount): Transaction`, `deposit(card, amount): Transaction`, `transfer(from, to, amount): Transaction` |
| **Card** | `cardNo: String`, `pinHash: String`, `status: String` | (Không có phương thức hiển thị) |
| **Account** | `accountNo: String`, `balance: double` | `deposit(amount): double`, `credit(amount): double` |
| **Transaction** | `txId: int`, `type: String`, `amount: double`, `time: DateTime`, `status: String` | (Không có phương thức hiển thị) |

Mối quan hệ chính: `ATM` liên kết với `Card`, `Account`, và `Transaction`.

### 2.3. Use Case Diagram (Giả định)

Dựa trên tài liệu Use Case Diagram của Hệ thống bán hàng online, nếu áp dụng cho ATM, các Use Case chính sẽ tập trung vào vai trò **Customer** (Khách hàng) với các chức năng như **Rút tiền**, **Gửi tiền**, **Chuyển khoản** và **Kiểm tra số dư**.

---

## 3. Database & Code Minh hoạ

### 3.1. Database (Giả định cấu trúc)

Cơ sở dữ liệu sẽ bao gồm các bảng tương ứng với mô hình lớp ATM để lưu trữ thông tin giao dịch và tài khoản:
* `Cards`: Lưu thông tin thẻ và PIN đã hash.
* `Accounts`: Lưu thông tin số dư tài khoản.
* `Transactions`: Lưu lịch sử giao dịch.

### 3.2. Code Minh hoạ (Python - Module Rút tiền)

Logic nghiệp vụ quan trọng nhất là **Rút tiền** được triển khai trong `withdraw_module.py`. Code thực hiện các bước:
1.  **Lấy dữ liệu:** Lấy số PIN và số tiền muốn rút.
2.  **Xác thực:** Kiểm tra tính hợp lệ của PIN.
3.  **Kiểm tra Số dư:** So sánh số tiền yêu cầu với số dư hiện tại.
4.  **Thực hiện Giao dịch:** Nếu đủ điều kiện, số dư sẽ được cập nhật.

---

## 4. Kết quả Test & Sprint Report

### 4.1. Kết quả Test (Module Rút tiền - LAB 07)

Quá trình kiểm thử đơn vị cho module rút tiền đã kiểm tra ba luồng chính:

| STT | Tên Test Case | Kết quả thực tế | Tình trạng |
| :--- | :--- | :--- | :--- |
| 1 | **TEST PIN SAI** | Xác thực PIN thất bại như dự kiến. | **PASS** |
| 2 | **TEST RÚT TIỀN THÀNH CÔNG** (Rút 500K) | Rút tiền thành công. Số dư mới: **4,000,000 VND**. | **PASS** |
| 3 | **TEST KHÔNG ĐỦ SỐ DƯ** (Yêu cầu 6M) | Lỗi giao dịch: Số dư không đủ. Số dư hiện tại: 4,000,000 VND. | **PASS** |

### 4.2. Sprint Report (Giả định dựa trên Artifacts)

Dự án đã tuân thủ quy trình phát triển lặp, sử dụng các công cụ quản lý dự án (như thể hiện qua Jira Report) và tạo ra các Artifacts quan trọng qua các Lab khác nhau.

| Sprint/LAB | Công việc chính | Kết quả đầu ra |
| :--- | :--- | :--- |
| **LAB 02** | Phân tích yêu cầu | Use Case Diagram |
| **LAB 03/04** | Thiết kế tương tác & Giao diện | Sequence Diagram, Form Đăng nhập |
| **LAB 06/07** | Thiết kế kiến trúc & Code | Package Diagram, Class Diagram, Code Module Rút tiền |
| **LAB 07** | Kiểm thử | Kết quả chạy Test Module Rút tiền |
| **LAB 09** | Quản lý dự án | Jira Report |

---

## 5. Kết luận & Định hướng mở rộng

### 5.1. Kết luận

Dự án ATM Mini-Project đã thành công trong việc thiết kế kiến trúc hệ thống (UML) và triển khai module nghiệp vụ cốt lõi (**Rút tiền**) với tính ổn định cao. Kết quả kiểm thử cho thấy module hoạt động chính xác theo các quy tắc nghiệp vụ về xác thực và kiểm tra số dư. Việc sử dụng các mô hình UML (Package, Class) đảm bảo tính mở rộng và dễ bảo trì của hệ thống.

### 5.2. Định hướng mở rộng

1.  **Hoàn thiện Giao dịch**: Triển khai đầy đủ các phương thức `deposit` (Gửi tiền) và `transfer` (Chuyển khoản) như đã định nghĩa trong Class `ATM`.
2.  **Tích hợp UI/UX**: Phát triển giao diện người dùng hoàn chỉnh để kết nối với các Controller, tạo trải nghiệm người dùng thân thiện.
3.  **Bảo mật Hashing**: Triển khai mã hóa mạnh (ví dụ: SHA-256) cho thuộc tính `pinHash` trong Class `Card` để đảm bảo an toàn thông tin.
4.  **Kết nối Database/API**: Thay thế logic dữ liệu cục bộ bằng việc kết nối với một hệ thống Database/Core Banking System thực tế, chuyển `BankService` thành một Microservice độc lập.
