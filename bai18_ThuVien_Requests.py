#cài đặt thư viện: pip install requests
import requests

'''
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


'''
GET	/posts
GET	/posts/1
GET	/posts/1/comments
GET	/comments?postId=1
POST	/posts
PUT	/posts/1
PATCH	/posts/1
DELETE	/posts/1
'''

url = "https://jsonplaceholder.typicode.com/posts/1"
data = requests.get(url)
print(data.status_code)
data = data.json()
print(data)
print(type(data))