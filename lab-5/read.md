# Lab 05 – Tích hợp, Quản lý & Báo cáo

## 1. Mục tiêu
Hoàn thiện quy trình phát triển phần mềm từ thiết kế đến triển khai:
- Gom tất cả artifacts (Use Case, Sequence, Form Login code).
- Viết báo cáo mô tả quy trình làm việc nhóm.
- Quản lý mã nguồn trên GitHub: push code, update README, tạo tag phiên bản v1.0.
- Chuẩn bị demo và review.

---

## 2. Artifacts đã xây dựng

### Use Case Diagram
Mô tả các chức năng chính của hệ thống Shopping Cart.  
![Use Case Diagram](../lab-2/UseCaseDiagram.jpg)

### Sequence Diagram (Checkout)
Mô tả luồng tương tác khi người dùng thực hiện thanh toán.  
![Sequence Diagram](../Lab%2003/SequenceDiagram.jpg)

### Form Login (HTML/CSS/JS)
Form đăng nhập với các thành phần:
- Input: Username, Password  
- Checkbox: Remember me  
- Nút: Login, Cancel  
- Kiểm tra dữ liệu bằng JavaScript  

👉 Source code: `lab-5/artifacts/form_login.html`

---

## 3. Project Report

### 3.1 Quy trình làm việc
1. **Phân tích yêu cầu**: Xác định chức năng hệ thống.  
2. **Thiết kế UML**: Use Case & Sequence Diagram.  
3. **Hiện thực form đăng nhập** bằng HTML/CSS/JS.  
4. **Kiểm thử**: xác minh dữ liệu nhập, chỉnh sửa form.  
5. **Quản lý mã nguồn trên GitHub**: commit rõ ràng, push code, update README.  
6. **Đóng gói & phát hành**: tạo tag v1.0 để đánh dấu phiên bản ổn định.  

### 3.2 Vai trò thành viên
- **Kiều**: Phân tích yêu cầu, thiết kế Use Case Diagram.  
- **Diệp**: Thiết kế Sequence Diagram, hỗ trợ kiểm thử form.  
- **Bình**: Hiện thực Form Login và tích hợp lên GitHub.  

---

## 4. Hướng dẫn GitHub

### Clone repo
```bash
git clone <repo-url>
