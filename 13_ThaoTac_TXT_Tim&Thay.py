# Tìm nội dung và thay thế trong file TXT
# Giả sử file 'danh_sach_demo.txt' đã tồn tại từ ví dụ trước
# với nội dung tương tự như sau:
# Dòng 1: Nguyễn Văn A - 0901234567
# Dòng 2: ĐÃ ĐƯỢC CẬP NHẬT - Số mới: 0912345678
# Dòng 3: Lê Văn C - 0908888888

ten_file = "danh_sach_demo.txt"

# 1. Đọc toàn bộ nội dung file vào một biến chuỗi
print("--- Nội dung file TRƯỚC khi thay thế ---")
with open(ten_file, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 2. Sử dụng phương thức .replace() để tìm và thay thế
noi_dung_can_tim = "ĐÃ ĐƯỢC CẬP NHẬT"
noi_dung_thay_the = "Thông tin mới"
content_moi = content.replace(noi_dung_can_tim, noi_dung_thay_the)

# 3. Mở file ở chế độ 'w' để ghi đè nội dung mới
with open(ten_file, "w", encoding="utf-8") as f:
    f.write(content_moi)

print(f"\nĐã thay thế và lưu file thành công.")

# 4. Đọc lại file để kiểm tra kết quả
print("\n--- Nội dung file SAU khi thay thế ---")
with open(ten_file, "r", encoding="utf-8") as f:
    print(f.read())
