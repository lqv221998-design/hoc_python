#---XỬ LÝ LIST NHIỀU DICT    (Cách này đang tự ý xuống dòng)
import csv

file_name = "Danh sach bai viet jsonplaceholder.csv"
rows = []
found = False
#Đọc toàn bộ dữ liệu ra biến row
with open(file_name, "r", newline="", encoding="utf-8-sig") as rf:
    read = csv.reader(rf)
    rows = list(read)

for i in range(1, len(rows)):
    current_id = rows[i][1]
    if current_id == "1":
        print(f"đã tìm thấy id cũ: {rows[i][1]}")
        found = True
        break
if found:
    with open(file_name, mode='w', newline='', encoding='utf-8-sig') as wf:
        write = csv.writer(wf)
        write.writerows(rows)
    print("Đã cập nhật file")
else:
    print("Không tìm có ID = 1")