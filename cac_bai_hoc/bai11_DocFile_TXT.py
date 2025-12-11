# Cú pháp open("Danhsach_SĐT.txt","w")

# Tên file mẫu để thao tác
ten_file = "Danhsach_SĐT.txt"

# ---------------------------------------------------------
# 1. Chế độ 'w' (Write): Ghi file
# Lưu ý: Nếu file chưa có -> Tạo mới. Nếu có rồi -> Xóa hết nội dung cũ và ghi mới.
# ---------------------------------------------------------
print("--- 1. Chế độ Write ('w') ---")
with open(ten_file, "w", encoding="utf-8") as f:
    f.write("Dòng 1: Xin chào Python!\n")
    f.write("Dòng 2: Học lập trình rất thú vị.")
    # Kết quả: File demo_file.txt được tạo với 2 dòng trên.
print("Đã ghi file thành công (đè nội dung cũ nếu có).")


# ---------------------------------------------------------
# 2. Chế độ 'a' (Append): Ghi nối tiếp
# Lưu ý: Giữ nguyên nội dung cũ, viết tiếp vào cuối file.
# ---------------------------------------------------------
print("\n--- 2. Chế độ Append ('a') ---")
with open(ten_file, "a", encoding="utf-8") as f:
    f.write("\nDòng 3: Đây là dòng được nối thêm.")
    # Kết quả: File giờ có 3 dòng.
print("Đã nối thêm nội dung vào cuối file.")


# ---------------------------------------------------------
# 3. Chế độ 'r' (Read): Đọc file (Mặc định)
# Lưu ý: Chỉ đọc, không được sửa. Nếu file không tồn tại sẽ báo lỗi.
# ---------------------------------------------------------
print("\n--- 3. Chế độ Read ('r') ---")
with open(ten_file, "r", encoding="utf-8") as f:
    content = f.read() # Đọc toàn bộ nội dung
    print("Nội dung file hiện tại:\n" + content)
    # Kết quả: In ra toàn bộ 3 dòng đã ghi ở trên.


# ---------------------------------------------------------
# 4. Chế độ 'r+' (Read + Write): Đọc và Ghi (Cập nhật)
# Lưu ý: Con trỏ chuột nằm ở đầu file. Ghi sẽ đè lên ký tự có sẵn tại vị trí đó.
# ---------------------------------------------------------
print("\n--- 4. Chế độ Update ('r+') ---")
with open(ten_file, "r+", encoding="utf-8") as f:
    f.write("Alo") # Ghi đè chữ "Alo" lên 3 ký tự đầu tiên ("Dòn")
    # Kết quả: "Dòng 1..." sẽ thành "Alo g 1..."
print("Đã cập nhật 3 ký tự đầu tiên của file.")


# ---------------------------------------------------------
# 5. Chế độ 'x' (Exclusive creation): Tạo mới độc quyền
# Lưu ý: Chỉ tạo nếu file CHƯA tồn tại. Nếu file đã có, sẽ báo lỗi (giúp tránh ghi đè nhầm).
# ---------------------------------------------------------
print("\n--- 5. Chế độ Exclusive ('x') ---")
try:
    with open(ten_file, "x", encoding="utf-8") as f:
        f.write("Nội dung mới")
except FileExistsError:
    print(f"Lỗi: File '{ten_file}' đã tồn tại, không thể tạo mới bằng chế độ 'x'.")
    # Kết quả: Sẽ in ra dòng thông báo lỗi này vì file đã tạo ở bước 1.