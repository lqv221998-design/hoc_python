# Tìm nội dung và thay thế trong file TXT
# Đọc file: Đưa toàn bộ nội dung vào danh sách rỗng
# Tên file dữ liệu
ten_file = "kho_hang.txt"

# --- BƯỚC CHUẨN BỊ: Tạo file mẫu ---
with open(ten_file, "w", encoding="utf-8") as f:
    f.write("Samsung Galaxy S23 - Giá: 20tr\n")
    f.write("Iphone 14 - Giá: 18tr\n")  # <--- Dòng cần tìm và sửa
    f.write("Xiaomi 13 - Giá: 15tr\n")
print("Đã tạo file kho hàng mẫu.")


# --- BẮT ĐẦU TÌM VÀ SỬA ---

# Thông tin cần tìm và nội dung thay thế
tu_khoa_tim_kiem = "Iphone 14"
noi_dung_moi = "Iphone 14 - Giá: ĐÃ GIẢM CÒN 16tr (Hot!)\n" # Nhớ thêm \n

# Danh sách chứa nội dung sẽ ghi lại vào file
danh_sach_moi = []
tim_thay = False # Biến cờ để kiểm tra xem có tìm thấy không

print(f"\nĐang tìm kiếm '{tu_khoa_tim_kiem}' để sửa đổi...")

# 1. Đọc file cũ
with open(ten_file, "r", encoding="utf-8") as f:
    cac_dong_cu = f.readlines()

# 2. Xử lý từng dòng (Logic Tìm kiếm)
for dong in cac_dong_cu:
    # Kiểm tra xem từ khóa có nằm trong dòng hiện tại không
    if tu_khoa_tim_kiem in dong:
        # NẾU TÌM THẤY: Thêm nội dung mới vào danh sách
        danh_sach_moi.append(noi_dung_moi)
        tim_thay = True
        print(f"-> Đã tìm thấy và sửa dòng: {dong.strip()}")
    else:
        # NẾU KHÔNG TÌM THẤY: Giữ nguyên dòng cũ
        danh_sach_moi.append(dong)

# 3. Ghi lại vào file (Chỉ ghi nếu đã tìm thấy để tránh mở file vô ích)
if tim_thay:
    with open(ten_file, "w", encoding="utf-8") as f:
        f.writelines(danh_sach_moi)
    print("\nCập nhật file thành công!")
else:
    print(f"\nKhông tìm thấy từ khóa '{tu_khoa_tim_kiem}' trong file.")

# --- KIỂM TRA KẾT QUẢ ---
print("-" * 30)
with open(ten_file, "r", encoding="utf-8") as f:
    print(f.read())

