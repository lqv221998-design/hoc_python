#cài đặt thư viện: pip install requests
import requests


url = "http://google.com?price=asc&category=iphone"
# Khai báo 1 parameter kiểu từ điển
params = {
    "id" : 1,
    "sort" : "price"
}
data = requests.get(url, params= params)
#print(data)
print(data.status_code)
print(data.content)
#print(data.text)




'''
GET	/posts              # Lấy dữ liệu về
GET	/posts/1            # Lấy dữ liệu về chi tiết của 1 bài viết
GET	/posts/1/comments   # Lấy danh sách các comment của 1 bài viết
GET	/comments?postId=1  # Lấy danh sách các comment của 1 bài viết
POST	/posts          # Tạo mới 1 bài viết
PUT	/posts/1            # Cập nhật 1 bài viết
PATCH	/posts/1        # Cập nhật 1 bài viết 
DELETE	/posts/1        # Xóa 1 bài viết
'''
import requests # 1. Nhập thư viện 'requests' - công cụ để gọi người phục vụ

# 2. Định nghĩa điểm cuối (Endpoint/URL)
# Đây là địa chỉ cụ thể nơi chứa dữ liệu bạn muốn lấy
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    # 3. Gửi yêu cầu GET (Lấy dữ liệu)
    # requests.get(url) giống như việc nói với người phục vụ: "Hãy đến địa chỉ này lấy đồ cho tôi"
    response = requests.get(url)

    # 4. Kiểm tra trạng thái (Status Code)
    # 200 có nghĩa là "OK" (Thành công).
    # 404 là "Not Found" (Không tìm thấy).
    # 500 là "Server Error" (Lỗi từ nhà bếp).
    print(f"Mã trạng thái: {response.status_code}")

    if response.status_code == 200:
        # 5. Xử lý dữ liệu trả về
        # Dữ liệu gốc từ API thường ở dạng text hoặc bytes.
        # .json() giúp chuyển nó thành Dictionary hoặc List trong Python để dễ dùng.
        data = response.json()
        
        print("-" * 30)
        print("Dữ liệu thô (Dictionary):")
        print(data) # In toàn bộ cục dữ liệu
        
        print("-" * 30)
        print("Truy cập từng phần tử:")
        # Bây giờ ta có thể dùng key để lấy value như bình thường trong Python
        print(f"Tiêu đề (Title): {data['title']}")
        print(f"Nội dung (Body): {data['body']}")
        
    else:
        print("Không lấy được dữ liệu. Vui lòng kiểm tra lại đường dẫn.")

except Exception as e:
    # Bắt lỗi nếu mất mạng hoặc đường dẫn sai format
    print(f"Đã xảy ra lỗi kết nối: {e}")


