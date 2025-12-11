# import thư viện requests
import requests
import json
import csv

#Kết nối với đường dẫn 
#Lấy danh sách nhiều bài viết
url = "https://jsonplaceholder.typicode.com/posts"
list_posts = requests.get(url)                      #lấy dữ liệu về 

#chuyển đổi danh sách trả về thành json (Kiểu dist trong py)
transform_list_posts = list_posts.json()  #Chuyển đổi sang List các Dictionary

#kết nối dữ liệu này ra file máy tính
file_name = "Danh sach bai viet jsonplaceholder.csv"

#tạo mới file và ghi dữ liệu bằng w
with open(file_name,"w", newline="", encoding="utf-8") as wf:   #Mở file, ghi dữ liệu vào đặt tên viết tắt là wf
                                                                # newline="" giúp tránh bị dư dòng trống giữa các hàng trong Excel
    write = csv.writer(wf)   # lấy hàm csv.write() sau đó truyền dữ wf vào

#Tạo tiêu đề cho cột
    header = ["userId", "id", "title", "body"]
#    write.writerow("userId", "id", "title", "body")   #Lưu ý không thể ghi trực tiếp vào các giá trị dạng chuỗi
    write.writerow(header)

#Duyệt qua từng bài viết để ghi dữ liệu
    for key in transform_list_posts:    #vòng lặp này đang lặp qua các dict chứ không phải lặp qua key trong 1 dict
                                    #ở đây key là một dictionary: {"userId": 1, "id": 1, "title": "...", ...}
        row_data = [
            key["userId"],
            key["id"],
            key["title"],
            key["body"]
        ]
    write.writerow(row_data)
# Lưu ý cách này là sai: writer.writerow([post['id'], post['userId'], post['title']]) không thể đưa nhiều arguments (đối số) vào hàm này


print(f"Đã lưu {len(transform_list_posts)} bài viết vào file {file_name} thành công!")