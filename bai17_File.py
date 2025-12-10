# 1. Xử lý file JSON (Lưu trữ dữ liệu có cấu trúc)
import json

# Dữ liệu phức tạp (Dictionary lồng nhau)
ho_so = {
    "ten": "Nguyen Van A",
    "tuoi": 25,
    "ky_nang": ["Python", "Excel", "Data"],
    "da_ket_hon": False
}

ten_file = "data_user.json"

# --- 1. GHI FILE JSON ---
# indent=4 giúp file đẹp, dễ đọc (thụt đầu dòng 4 dấu cách)
# ensure_ascii=False giúp hiển thị tiếng Việt không bị lỗi mã hóa
with open(ten_file, "w", encoding="utf-8") as f:
    json.dump(ho_so, f, indent=4, ensure_ascii=False)
    print("Đã lưu file JSON thành công!")

# --- 2. ĐỌC FILE JSON ---
with open(ten_file, "r", encoding="utf-8") as f:
    du_lieu_doc_duoc = json.load(f)
    
    # Python tự hiểu đây là Dictionary, không phải String
    print(f"Tên: {du_lieu_doc_duoc['ten']}")
    print(f"Kỹ năng đầu tiên: {du_lieu_doc_duoc['ky_nang'][0]}")

# 2. Điều khiển "Con trỏ" (seek và tell)
with open("thu_nghiem.txt", "w+", encoding="utf-8") as f:
    # w+: Chế độ vừa Ghi vừa Đọc
    f.write("1234567890")
    
    print(f"Vị trí hiện tại sau khi ghi: {f.tell()}") 
    # -> 10 (đang ở cuối file)
    
    # Muốn đọc lại? Phải tua về đầu (vị trí 0)
    f.seek(0)
    print(f"Vị trí sau khi tua: {f.tell()}")
    
    # Đọc 5 ký tự đầu
    data = f.read(5)
    print(f"Dữ liệu đọc được: {data}") # -> 12345



# 3. Sao chép và Di chuyển File (shutil)
import shutil
import os

# Tạo file mẫu để test
with open("ban_goc.txt", "w") as f:
    f.write("Dữ liệu quan trọng")

# 1. Sao chép file (Copy)
# Copy "ban_goc.txt" thành "ban_sao.txt"
shutil.copy("ban_goc.txt", "ban_sao.txt") 
print("Đã copy xong.")

# 2. Di chuyển file (Move/Cut)
# Tạo thư mục mới nếu chưa có
if not os.path.exists("ThuMucLuuTru"):
    os.makedirs("ThuMucLuuTru")

# Chuyển file vào thư mục đó
shutil.move("ban_sao.txt", "ThuMucLuuTru/ban_sao_moi.txt")
print("Đã di chuyển file vào thư mục.")