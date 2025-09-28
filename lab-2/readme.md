# Use Case Descriptions – Shopping Cart System

## UC-01: Thêm sản phẩm vào giỏ hàng
**Actor:** Người dùng  
**Mục tiêu:** Người dùng có thể thêm sản phẩm muốn mua vào giỏ hàng.  

**Điều kiện tiên quyết:**  
- Người dùng đã đăng nhập.  
- Sản phẩm còn tồn kho.  

**Luồng chính:**  
1. Người dùng truy cập trang danh mục sản phẩm.  
2. Người dùng chọn một sản phẩm cụ thể.  
3. Hệ thống hiển thị thông tin chi tiết (tên, mô tả, giá, số lượng tồn kho).  
4. Người dùng nhập số lượng cần mua và nhấn **"Thêm vào giỏ hàng"**.  
5. Hệ thống kiểm tra số lượng hợp lệ.  
6. Hệ thống thêm sản phẩm vào giỏ hàng và cập nhật tổng giá trị.  
7. Hệ thống báo thành công.  

**Luồng thay thế:**  
- (a) Nếu số lượng vượt tồn kho → Hệ thống báo lỗi.  
- (b) Người dùng chưa đăng nhập → Hệ thống yêu cầu đăng nhập.  

---

## UC-02: Xóa sản phẩm khỏi giỏ hàng
**Actor:** Người dùng  
**Mục tiêu:** Người dùng có thể xóa sản phẩm không mong muốn khỏi giỏ hàng.  

**Điều kiện tiên quyết:**  
- Người dùng đã đăng nhập.  
- Trong giỏ hàng có ít nhất một sản phẩm.  

**Luồng chính:**  
1. Người dùng mở trang giỏ hàng.  
2. Người dùng chọn sản phẩm muốn xóa.  
3. Người dùng nhấn nút **"Xóa"**.  
4. Hệ thống loại bỏ sản phẩm khỏi giỏ hàng.  
5. Hệ thống cập nhật lại tổng số tiền.  

**Luồng thay thế:**  
- Nếu giỏ hàng rỗng → Hệ thống hiển thị thông báo.  

---

## UC-03: Sửa thông tin sản phẩm
**Actor:** Admin  
**Mục tiêu:** Quản trị viên có thể chỉnh sửa thông tin sản phẩm (tên, giá, mô tả, số lượng tồn kho).  

**Điều kiện tiên quyết:**  
- Admin đã đăng nhập vào hệ thống.  

**Luồng chính:**  
1. Admin truy cập trang quản lý sản phẩm.  
2. Admin chọn một sản phẩm cần chỉnh sửa.  
3. Hệ thống hiển thị form chỉnh sửa thông tin.  
4. Admin nhập thông tin mới (tên, mô tả, giá, số lượng tồn kho).  
5. Admin nhấn nút **"Lưu"**.  
6. Hệ thống kiểm tra dữ liệu nhập vào.  
7. Hệ thống cập nhật sản phẩm trong cơ sở dữ liệu.  
8. Hệ thống hiển thị thông báo thành công.  

**Luồng thay thế:**  
- (a) Nếu dữ liệu không hợp lệ → Hệ thống báo lỗi và yêu cầu nhập lại.  
- (b) Nếu sản phẩm không tồn tại → Hệ thống báo lỗi.
