# Báo cáo cuối kỳ: ATM Mini-Project

## 1. Giới thiệu ATM Mini-Project

[cite_start]Dự án **ATM Mini-Project** là một mô hình hóa và triển khai các chức năng cơ bản của một hệ thống máy rút tiền tự động (ATM)[cite: 1, 11, 13]. [cite_start]Mục tiêu chính là xây dựng một hệ thống phần mềm đáng tin cậy, có khả năng xử lý các giao dịch tài chính chính như **xác thực thẻ/PIN**, **rút tiền**, **gửi tiền** và **chuyển khoản**[cite: 11].

**Phạm vi chính của dự án:**
* [cite_start]**Thiết kế kiến trúc hệ thống** bằng mô hình UML, bao gồm Class Diagram, Package Diagram, và Use Case[cite: 2, 10, 11].
* [cite_start]**Triển khai module nghiệp vụ quan trọng**, cụ thể là module **Rút tiền** bằng Python[cite: 13].
* [cite_start]**Thực hiện kiểm thử đơn vị** (Unit Test) cho các luồng xử lý chính của module Rút tiền[cite: 14].

---

## 2. Mô hình UML

### 2.1. [cite_start]Mô hình Phân Rã Gói (Package Diagram) [cite: 10]

Hệ thống được tổ chức thành bốn gói (Package) chính để phân tách trách nhiệm và module hóa:
* [cite_start]**UI (User Interface):** Chịu trách nhiệm về giao diện người dùng[cite: 10].
* [cite_start]**Controller:** Xử lý logic điều phối giữa UI và các dịch vụ nghiệp vụ, đồng thời tương tác với cả `BankService` và `Hardware`[cite: 10].
* [cite_start]**BankService:** Chứa các logic nghiệp vụ lõi của ngân hàng, bao gồm xác thực và các giao dịch[cite: 10].
* [cite_start]**Hardware:** Mô phỏng tương tác với các thành phần vật lý của ATM[cite: 10].

### 2.2. [cite_start]Mô hình Lớp (Class Diagram) [cite: 11]

Mô hình lớp xác định các thực thể chính và các mối quan hệ trong hệ thống:

| Lớp (Class) | Thuộc tính (Attributes) | Phương thức (Methods) |
| :--- | :--- | :--- |
| **ATM** | `atmId: int`, `location: String`, `cashLevel: double` | [cite_start]`authenticate(card, pin): boolean`, `withdraw(card, amount): Transaction`, `deposit(card, amount): Transaction`, `transfer(from, to, amount): Transaction` [cite: 11] |
| **Card** | `cardNo: String`, `pinHash: String`, `status: String` | (Không có phương thức hiển thị) [cite_start][cite: 11] |
| **Account** | `accountNo: String`, `balance: double` | [cite_start]`deposit(amount): double`, `credit(amount): double` (Có thể là lỗi gõ, nên là `debit` và `credit`) [cite: 11] |
| **Transaction** | `txId: int`, `type: String`, `amount: double`, `time: DateTime`, `status: String` | (Không có phương thức hiển thị) [cite_start][cite: 11] |

[cite_start]Mối quan hệ chính: `ATM` liên kết với `Card`, `Account`, và `Transaction`[cite: 11].

### 2.3. [cite_start]Use Case Diagram (Hệ thống bán hàng online) [cite: 2]

Mặc dù tài liệu cung cấp là của hệ thống bán hàng online, nó minh họa việc sử dụng Use Case để xác định các chức năng theo vai trò (Actor):
* [cite_start]**Admin:** Quản lý sản phẩm (Thêm, Sửa, Xóa)[cite: 2].
* [cite_start]**User:** Thao tác mua hàng (Tìm kiếm, Thêm/Xóa sản phẩm, Thay đổi số lượng trong giỏ hàng)[cite: 2].

**Áp dụng cho ATM:** Use Case chính sẽ là `Rút tiền`, `Gửi tiền`, `Chuyển khoản` và `Kiểm tra số dư`.

---

## 3. Database & Code Minh hoạ

### 3.1. Database (Giả định cấu trúc)

Cơ sở dữ liệu sẽ bao gồm các bảng tương ứng với mô hình lớp ATM để lưu trữ thông tin giao dịch và tài khoản:
* `Cards`: Lưu thông tin thẻ và PIN đã hash.
* `Accounts`: Lưu thông tin số dư tài khoản.
* `Transactions`: Lưu lịch sử giao dịch.

### 3.2. Code Minh hoạ (Python - Module Rút tiền)

[cite_start]Logic nghiệp vụ quan trọng nhất là **Rút tiền** được triển khai trong `withdraw_module.py`[cite: 13]. Code thực hiện các bước:
1.  **Lấy dữ liệu:** Lấy số PIN và số tiền muốn rút.
2.  **Xác thực:** Kiểm tra tính hợp lệ của PIN.
3.  **Kiểm tra Số dư:** So sánh số tiền yêu cầu với số dư hiện tại.
4.  **Thực hiện Giao dịch:** Nếu đủ điều kiện, số dư sẽ được cập nhật.

---

## 4. Kết quả Test & Sprint Report

### 4.1. Kết quả Test (Module Rút tiền - LAB 07)

[cite_start]Quá trình kiểm thử đơn vị cho module rút tiền đã kiểm tra ba luồng chính[cite: 14]:

| STT | Tên Test Case | Kết quả thực tế | Tình trạng |
| :--- | :--- | :--- | :--- |
| 1 | **TEST PIN SAI** | Xác thực PIN thất bại như dự kiến. | [cite_start]**PASS** [cite: 14] |
| 2 | **TEST RÚT TIỀN THÀNH CÔNG** (Rút 500K) | Rút tiền thành công. Số dư mới: **4,000,000 VND**. | [cite_start]**PASS** [cite: 14] |
| 3 | **TEST KHÔNG ĐỦ SỐ DƯ** (Yêu cầu 6M) | Lỗi giao dịch: Số dư không đủ. Số dư hiện tại: 4,000,000 VND. | [cite_start]**PASS** [cite: 14] |

### 4.2. Sprint Report (Giả định dựa trên Artifacts)

Dự án đã tuân thủ quy trình phát triển lặp (Agile/Scrum), sử dụng các công cụ quản lý dự án (Jira Report - LAB 09) và tạo ra các Artifacts (LAB 02, 03, 04, 06, 07) qua nhiều Sprint.

| Sprint/LAB | Công việc chính | Kết quả đầu ra |
| :--- | :--- | :--- |
| **LAB 02** | Phân tích yêu cầu | [cite_start]Use Case Diagram [cite: 2] |
| **LAB 03/04** | Thiết kế tương tác & Giao diện | [cite_start]Sequence Diagram, Form Đăng nhập (LAB04/Form\_login) [cite: 4, 8] |
| **LAB 06/07** | Thiết kế kiến trúc & Code | [cite_start]Package Diagram, Class Diagram, Code Module Rút tiền [cite: 10, 11, 13] |
| **LAB 07** | Kiểm thử | [cite_start]Kết quả chạy Test Module Rút tiền [cite: 14] |
| **LAB 09** | Quản lý dự án | [cite_start]Jira Report [cite: 18] |

---

## 5. Kết luận & Định hướng mở rộng

### 5.1. Kết luận

Dự án ATM Mini-Project đã thành công trong việc thiết kế kiến trúc hệ thống (UML) và triển khai module nghiệp vụ cốt lõi (**Rút tiền**) với tính ổn định cao. Kết quả kiểm thử cho thấy module hoạt động chính xác theo các quy tắc nghiệp vụ về xác thực và kiểm tra số dư. Việc sử dụng các mô hình UML (Package, Class) đảm bảo tính mở rộng và dễ bảo trì của hệ thống.

### 5.2. Định hướng mở rộng

1.  [cite_start]**Hoàn thiện Giao dịch**: Triển khai đầy đủ các phương thức `deposit` (Gửi tiền) và `transfer` (Chuyển khoản) như đã định nghĩa trong Class `ATM`[cite: 11].
2.  **Tích hợp UI/UX**: Phát triển giao diện người dùng hoàn chỉnh (dựa trên LAB04/Form\_login) để kết nối với các Controller, tạo trải nghiệm người dùng thân thiện.
3.  [cite_start]**Bảo mật Hashing**: Triển khai mã hóa mạnh (ví dụ: SHA-256) cho thuộc tính `pinHash` trong Class `Card` để đảm bảo an toàn thông tin[cite: 11].
4.  **Kết nối Database/API**: Thay thế logic dữ liệu cục bộ bằng việc kết nối với một hệ thống Database/Core Banking System thực tế, chuyển `BankService` thành một Microservice độc lập.
