#---CẤP ĐỘ 1 TRONG XỬ LÝ DỮ LIỆU---
#Sử dụng Append
import csv


#---XỬ LÝ 1 DICT CÁCH 1  (Cách này đang tự ý xuống dòng)
# Cách tự suy nghĩ
#Nội dung muốn thêm vào kiểu dict
content = {
    "userId": 3,
    "id": 3,
    "title": "dòng thêm mới",
    "body": "vũ đã thêm mới một dòng"
    }

#Mở file, ở chế độ append
file_name = "Danh sach bai viet jsonplaceholder.csv"
with open(file_name, "a", encoding="utf-8-sig") as af:

    #Tạo biến chứa hàm viết nội dung
    write = csv.writer(af)

    #Xử lý dict thành list
    row_data = [
        content["userId"],
        content["id"],
        content["title"],
        content["body"]
    ]
    #Gọi hàm để viết nội dung vào file
    write.writerow(row_data)
    print("Đã thêm thành công nội dung")



#XỬ LÝ 1 DICT CÁCH 2    (Cách này đang tự ý xuống dòng)
import csv
content = {
    "userId": 3,
    "id": 3,
    "title": "dòng thêm mới",
    "body": "vũ đã thêm mới một dòng"
}
handle = ["userId", "id", "title", "body"]
#Mở file, ở chế độ append
file_name = "Danh sach bai viet jsonplaceholder.csv"
with open(file_name, mode="a",newline="", encoding="utf-8-sig") as af:
    #Tạo biến chứa hàm viết nội dung
    write = csv.DictWriter(af, fieldnames=handle)
    #Gọi hàm để viết nội dung vào file
    write.writerow(content)
print("Đã thêm thành công nội dung")



#---XỬ LÝ LIST NHIỀU DICT CÁCH 1    (Cách này đang tự ý xuống dòng)
content = [
    {
    "userId": 0,
    "id": 0,
    "title": "dòng thêm mới 1",
    "body": "vũ đã thêm mới một dòng 1"
    },
    {
    "userId": 3,
    "id": 3,
    "title": "dòng thêm mới 2",
    "body": "vũ đã thêm mới một dòng 2"
    }
] 
file_name = "Danh sach bai viet jsonplaceholder.csv"
with open(file_name, "a", encoding="utf-8-sig") as af:
    wr = csv.writer(af)
    for key in content:
        value = [
            key["userId"],
            key["id"],
            key["title"],
            key["body"]
        ]
        wr.writerow(value)
    print("Đã thêm mới nội dung")

#---XỬ LÝ LIST NHIỀU DICT CÁCH 1    (fix lỗi tự ý xuống dòng)
content = [
    {
    "userId": 0,
    "id": 0,
    "title": "dòng thêm mới 1",
    "body": "vũ đã thêm mới một dòng 1"
    },
    {
    "userId": 3,
    "id": 3,
    "title": "dòng thêm mới 2",
    "body": "vũ đã thêm mới một dòng 2"
    }
] 
file_name = "Danh sach bai viet jsonplaceholder.csv"
handle = ["userId", "id", "title", "body"]
with open(file_name, "a", newline="", encoding="utf-8-sig") as af:
    wr = csv.DictWriter(af, fieldnames=handle)
    list_empty = []
    for lis in content:
        list_copy = lis.copy()
        list_copy["body"].replace("\n", "").replace("\r", "")
        list_empty.append(list_copy)
        wr.writerows(list_empty)
    print("Đã thêm mới nội dung")
