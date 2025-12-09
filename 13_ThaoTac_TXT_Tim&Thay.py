# Tìm nội dung và thay thế trong file TXT
# Đọc file: Đưa toàn bộ nội dung vào danh sách rỗng
danh_sach = "danh_sach_demo.txt"
with open(danh_sach, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

