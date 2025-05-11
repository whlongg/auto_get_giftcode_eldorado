# Hướng dẫn sử dụng script nhập gift code Eldorado

## Yêu cầu

- Python 3.x
- Thư viện `requests` (cài bằng lệnh: `pip install requests`)

## Cách sử dụng

1. **Điền ID tài khoản của bạn**  
   Mở file `test.py`, sửa dòng sau thành ID của bạn:
   ```python
   ur_id = "user123@example.com" #Nhập id của bạn ở đây
   ```

2. **Thêm các gift code**  
   Thêm các gift code (mỗi code một dòng) vào file `code.txt`.

3. **Chạy script**  
   Mở terminal/cmd tại thư mục chứa file và chạy:
   ```
   python test.py
   ```

4. **Kết quả**  
   Script sẽ tự động gửi từng gift code và in ra kết quả trả về từ server.

## Lưu ý

- Mỗi gift code chỉ sử dụng được một lần cho mỗi tài khoản.
- Nếu gặp lỗi kết nối, kiểm tra lại mạng hoặc thử lại sau.
