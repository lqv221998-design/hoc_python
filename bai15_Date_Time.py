from datetime import datetime as dt # Đổi tên datetime thành 'dt' cho ngắn gọn

# 1. Khởi tạo thời gian hiện tại
DT = dt.now() 
print(f"Thời gian đầy đủ: {DT}") 
# -> Kết quả: 2023-10-27 15:30:45.123456 (Năm-Tháng-Ngày Giờ:Phút:Giây.Vi_giây)

print("-" * 30) # Gạch phân cách cho dễ nhìn

# 2. Nhóm Ngày - Tháng - Năm
print(f"Năm: {DT.year}")   
# -> Kết quả: 2023 (Trả về số năm)

print(f"Tháng: {DT.month}")  
# -> Kết quả: 10 (Trả về số tháng từ 1 đến 12)

print(f"Ngày: {DT.day}")    
# -> Kết quả: 27 (Trả về ngày trong tháng)

# 3. Nhóm Giờ - Phút - Giây
print(f"Giờ: {DT.hour}")   
# -> Kết quả: 15 (Trả về giờ theo định dạng 24h, từ 0 đến 23)

print(f"Phút: {DT.minute}") 
# -> Kết quả: 30 (Trả về phút từ 0 đến 59)

print(f"Giây: {DT.second}") 
# -> Kết quả: 45 (Trả về giây từ 0 đến 59)

print(f"Vi giây: {DT.microsecond}") 
# -> Kết quả: 123456 (1 giây = 1 triệu vi giây, phần này giúp tính giờ siêu chính xác)

print("-" * 30)

# 4. Nhóm Thứ trong tuần (Rất quan trọng cần lưu ý!)
print(f"Weekday (0-6): {DT.weekday()}") 
# -> Giải thích: Máy tính đếm từ 0. 
# 0 là Thứ Hai, 1 là Thứ Ba, ..., 6 là Chủ Nhật.

print(f"ISO Weekday (1-7): {DT.isoweekday()}") 
# -> Giải thích: Chuẩn quốc tế (ISO). Đếm giống người thường.
# 1 là Thứ Hai, ..., 7 là Chủ Nhật.

# 5. Bộ lịch ISO (Năm, Tuần thứ mấy, Thứ mấy)
print(f"ISO Calendar: {DT.isocalendar()}")
# -> Kết quả ví dụ: datetime.IsoCalendarDate(year=2023, week=43, weekday=5)
# Nghĩa là: Năm 2023, Tuần thứ 43 của năm, Thứ 6.



# 1. Định dạng & Chuyển đổi (Quan trọng nhất)
from datetime import timedelta # Cần nhập thêm cái này để cộng trừ ngày

now = dt.now()

print("--- 1. ĐỊNH DẠNG & CHUYỂN ĐỔI ---")
# A. Từ Thời gian -> Chuỗi (strftime)
# %d: ngày, %m: tháng, %Y: năm, %H: giờ, %M: phút
chuoi_dep = now.strftime("Hôm nay là ngày %d/%m/%Y, lúc %H giờ %M phút")
print(chuoi_dep) 

# B. Từ Chuỗi -> Thời gian (strptime)
str_input = "20/11/2025"
ngay_le = dt.strptime(str_input, "%d/%m/%Y")
print(f"Máy đã hiểu ngày lễ là: {ngay_le} (Kiểu: {type(ngay_le)})")


# 2. Tính toán thời gian (Cộng/Trừ ngày tháng)
print("\n--- 2. TÍNH TOÁN THỜI GIAN (TIMEDELTA) ---")
# Cộng thêm 10 ngày
muoi_ngay_sau = now + timedelta(days=10)
print(f"10 ngày nữa là: {muoi_ngay_sau.date()}")

# Trừ đi 2 tuần
hai_tuan_truoc = now - timedelta(weeks=2)
print(f"2 tuần trước là: {hai_tuan_truoc.date()}")

# Tính khoảng cách giữa 2 ngày (Trừ 2 mốc thời gian cho nhau)
tet_nguyen_dan = dt(2025, 1, 29) # Giả sử mùng 1 Tết 2025
dem_nguoc = tet_nguyen_dan - now
print(f"Còn {dem_nguoc.days} ngày nữa là đến Tết 2025!")


# 3. Chỉnh sửa thời gian (replace)
# Dùng khi bạn muốn giữ nguyên giờ phút giây, nhưng chỉ muốn đổi năm hoặc đổi tháng.
print("\n--- 3. CHỈNH SỬA THỜI GIAN (REPLACE) ---")
# Ví dụ: Hạn chót nộp báo cáo là cùng giờ này, nhưng vào năm sau
deadline = now.replace(year=now.year + 1)
print(f"Deadline năm sau: {deadline}")



