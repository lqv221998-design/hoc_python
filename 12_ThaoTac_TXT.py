# Tên file cần xử lý
ten_file = "danh_sach_demo.txt"

# --- BƯỚC CHUẨN BỊ: Tạo một file mẫu để test ---
with open(ten_file, "w", encoding="utf-8") as f:
    f.write("Dòng 1: Nguyễn Văn A - 0901234567\n")
    f.write("Dòng 2: Trần Thị B - 0909999999\n") # <--- Chúng ta sẽ sửa dòng này
    f.write("Dòng 3: Lê Văn C - 0908888888\n")
print("Đã tạo file mẫu ban đầu.")

# --- BẮT ĐẦU QUY TRÌNH SỬA FILE ---

# 1. Đọc toàn bộ nội dung file vào một danh sách (List)
with open(ten_file, "r", encoding="utf-8") as f:
    # readlines() sẽ tách mỗi dòng thành 1 phần tử trong list
    danh_sach_dong = f.readlines()

print("\n--- Trước khi sửa ---")
print("".join(danh_sach_dong))

# 2. Sửa đổi nội dung trong List (trên bộ nhớ RAM)
# Lưu ý: Lập trình đếm từ 0. Muốn sửa dòng 2 thì index là 1.
index_can_sua = 1 

# Kiểm tra xem file có đủ dòng để sửa không
if index_can_sua < len(danh_sach_dong):
    # Quan trọng: Phải thêm ký tự xuống dòng '\n' ở cuối câu mới
    noi_dung_moi = "Dòng 2: ĐÃ ĐƯỢC CẬP NHẬT - Số mới: 0912345678\n"
    
    danh_sach_dong[index_can_sua] = noi_dung_moi
    print(f"Đã sửa nội dung dòng {index_can_sua + 1} trong bộ nhớ.")
else:
    print("Dòng cần sửa không tồn tại!")

# 3. Ghi đè lại danh sách đã sửa vào file
# Dùng mode 'w' để xóa nội dung cũ và ghi danh sách mới vào
with open(ten_file, "w", encoding="utf-8") as f:
    f.writelines(danh_sach_dong)

print("\n--- Sau khi sửa và lưu file ---")
# Đọc lại để kiểm tra kết quả
with open(ten_file, "r", encoding="utf-8") as f:
    print(f.read())