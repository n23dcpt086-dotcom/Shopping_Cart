# Lab 05 – Tích hợp, quản lý và báo cáo

## Giới thiệu thành viên nhóm:  
- **Trần Thị Thuận Kiều** – N23DCPT086 – Trưởng nhóm, điều phối công việc.  
- **Lê Thị Thanh Bình** – N23DCPT063 – Phát triển giao diện và trải nghiệm người dùng.  
- **Nguyễn Thị Diệp** – N23DCPT070 – Xây dựng API và quản lý cơ sở dữ liệu.  

## Mục tiêu:
Hoàn thiện quy trình phát triển phần mềm: từ thiết kế UML (Use Case, Sequence) đến triển khai giao diện HTML/CSS/JS.  
Ngoài lập trình, nhóm cũng cần quản lý source code bằng Git/GitHub, viết báo cáo và phát hành sản phẩm với version **v1.0**.  

## Artifacts đã xây dựng

### Use Case Diagram
![Use Case Diagram](lab-5/artifacts/usecase.png)

### Sequence Diagram (Checkout)
![Sequence Diagram](lab-5/artifacts/sequence_checkout.png)

### Form đăng nhập
Form được xây dựng bằng HTML, CSS, JS, bao gồm:  
- Input: Username, Password  
- Checkbox: Remember me  
- Nút: Login, Cancel  
- Kiểm tra dữ liệu bằng JavaScript  

File mã nguồn: `lab-5/artifacts/form_login.html`

## Quy trình làm việc
- Khởi tạo repo GitHub, tổ chức thư mục.  
- Vẽ UML diagrams bằng PlantUML.  
- Tạo form login.  
- Gom artifacts, viết báo cáo.  
- Quản lý version bằng Git (commit, push, tag).  

## Cách chạy demo
- Mở file `form_login.html` trực tiếp trong trình duyệt.  
- Có thể triển khai GitHub Pages để demo online.  

## Quản lý Git
```bash
git add .
git commit -m "Lab05 - tích hợp UML, form login, báo cáo REPORT.md"
git push origin main

# Tạo tag version v1.0
git tag v1.0
git push origin v1.0
```

## Kết quả
- Use Case Diagram, Sequence Diagram và Form Login đã hoàn thành.  
- Báo cáo REPORT.md mô tả toàn bộ quá trình.  
- Repo được gắn tag **v1.0**, đánh dấu phiên bản ổn định.  

👉 Link repo: https://github.com/n23dcpt086-dotcom/Shopping_Cart.git
