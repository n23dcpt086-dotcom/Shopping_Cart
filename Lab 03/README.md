# Giải thích các đối tượng tham gia & thông điệp trao đổi

## Đối tượng tham gia

- **User / Admin**: actor thực hiện các hành vi qua giao diện.  
- **WebClient (Browser / Frontend)**: giao diện người dùng — gửi request tới backend và hiển thị kết quả.  
- **CartController / ProductController**: lớp điều khiển (API endpoint) xử lý HTTP request, gọi service phù hợp.  
- **ProductService**: truy vấn dữ liệu sản phẩm (chi tiết, cập nhật).  
- **InventoryService**: chịu trách nhiệm nghiệp vụ tồn kho (kiểm tra, đặt giữ).  
- **CartService**: nghiệp vụ giỏ hàng (thêm, xóa, tính tổng).  
- **ValidationService**: kiểm tra tính hợp lệ dữ liệu (dùng khi admin sửa sản phẩm).  
- **Database**: lưu trữ dữ liệu (bảng `products`, `cart_items`, `users`...).  

---

## Thông điệp chính (Message Types)

- `GET /products/{id}` → lấy thông tin sản phẩm.  
- `POST /cart/add` → yêu cầu thêm sản phẩm vào giỏ.  
- `POST /cart/remove` → xóa sản phẩm khỏi giỏ.  
- `POST /admin/products/{id}/update` → cập nhật thông tin sản phẩm.  

---

## Thông điệp nội bộ (Service-to-Service)

- `checkStock(productId, qty)` → kiểm tra tồn kho.  
- `insert/update cart items` → thêm hoặc cập nhật sản phẩm trong giỏ.  
- `recalcCartTotal(userId)` → tính lại tổng tiền giỏ hàng.  
- `validate(payload)` → kiểm tra dữ liệu nhập vào khi admin chỉnh sửa sản phẩm.  
