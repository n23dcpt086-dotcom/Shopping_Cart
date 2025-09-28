# Báo cáo Lab 05 — Tích hợp, Quản lý và Báo cáo

## Thành viên nhóm:
- **Trần Thị Thuận Kiều** – N23DCPT086 – Trưởng nhóm, chịu trách nhiệm phân công nhiệm vụ, quản lý tiến độ và tổng hợp báo cáo.  
- **Lê Thị Thanh Bình** – N23DCPT063 – Phụ trách chính về giao diện người dùng, xây dựng form đăng nhập và xử lý tương tác bằng HTML/CSS/JS.  
- **Nguyễn Thị Diệp** – N23DCPT070 – Chịu trách nhiệm thiết kế luồng xử lý nghiệp vụ, xây dựng và quản lý dữ liệu, hỗ trợ backend.

## Mục tiêu thực hiện
Hoàn thiện một chu trình phát triển phần mềm cơ bản, thiết kế UML, hiện thực hóa giao diện người dùng bằng HTML, CSS và JavaScript, đồng thời tích hợp quản lý mã nguồn với Git/GitHub. Kết quả cuối cùng là một phiên bản ổn định của dự án được phát hành với nhãn **v1.0**.

## Kết quả và sản phẩm
Trong quá trình thực hiện, nhóm đã xây dựng được các artifacts quan trọng sau:

- **Biểu đồ Use Case**: minh họa các chức năng chính của hệ thống Shopping Cart và cách mà người dùng hoặc quản trị viên tương tác với chúng.  
  ![Use Case Diagram](lab-5/artifacts/usecase.png)

- **Biểu đồ Sequence (Checkout)**: mô tả tuần tự các bước khi khách hàng tiến hành thanh toán, từ thao tác giao diện đến việc xác nhận đơn hàng.  
  ![Sequence Diagram](lab-5/artifacts/sequence_checkout.png)

- **Form đăng nhập**: được phát triển bằng HTML/CSS/JS, bao gồm ô nhập Username, Password, checkbox “Remember me”, cùng các nút Login và Cancel. JavaScript được sử dụng để kiểm tra dữ liệu hợp lệ trước khi xử lý.  
  File nguồn: `lab-5/artifacts/form_login.html`

## Quy trình làm việc
Để hoàn thành Lab, nhóm tiến hành theo các giai đoạn sau:
1. Lên kế hoạch phân công và thảo luận yêu cầu đề bài.  
2. Thiết kế các sơ đồ UML bằng PlantUML/draw.io, sau đó xuất thành file ảnh để dễ tích hợp báo cáo.  
3. Xây dựng form đăng nhập đáp ứng đúng yêu cầu đề, đồng thời viết kiểm tra dữ liệu bằng JavaScript.  
4. Quản lý mã nguồn thông qua GitHub, với quy tắc commit rõ ràng và tổ chức repo gọn gàng.  
5. Tổng hợp artifacts và soạn báo cáo bằng Markdown.  

Công cụ được sử dụng xuyên suốt bao gồm: **Visual Studio Code**, **Git**, **GitHub** và **PlantUML/draw.io**.

## Cách chạy và kiểm thử
