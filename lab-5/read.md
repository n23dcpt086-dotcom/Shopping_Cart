
## Project Report

### 1. Quy trình làm việc
1. **Phân tích yêu cầu**: Xác định chức năng hệ thống.  
2. **Thiết kế UML**: Use Case & Sequence Diagram.  
3. **Hiện thực form đăng nhập** bằng HTML/CSS/JS.  
4. **Kiểm thử**: xác minh dữ liệu nhập, chỉnh sửa form.  
5. **Quản lý mã nguồn trên GitHub**: commit rõ ràng, push code, update README.  
6. **Đóng gói & phát hành**: tạo tag v1.0 để đánh dấu phiên bản ổn định.  

### 2. Vai trò thành viên
- **Trần Thị Thuận Kiều** – N23DCPT086 – Phân tích yêu cầu, thiết kế Use Case Diagram.  
- **Nguyễn Thị Diệp** – N23DCPT070 – Thiết kế Sequence Diagram, hỗ trợ kiểm thử form.  
- **Lê Thị Thanh Bình** – N23DCPT063 – Hiện thực Form Login và tích hợp lên GitHub.  

---

## 3. Hướng dẫn push & tạo tag version
```bash
# Clone repo
git clone https://github.com/n23dcpt086-dotcom/Shopping_Cart.git
cd Shopping_Cart

# Commit thay đổi
git add .
git commit -m "Add Lab 5 report"
git push origin main

# Tạo tag version v1.0
git tag v1.0
git push origin v1.0
