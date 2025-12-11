# Cấu trúc dữ liệu Dictionary trong Python
my_dict = {
    "name": "Alice",          # Khóa 'name' với giá trị 'Alice'
    "age": 30,                # Khóa 'age' với giá trị 30
    "city": "New York"        # Khóa 'city' với giá trị 'New York'
}
print("Tên:", my_dict["name"])  # Truy cập giá trị bằng khóa 'name' Kết quả: Alice
print("Tuổi:", my_dict["age"])   # Truy cập giá trị bằng khóa 'age' Kết quả: 30

# Thêm một cặp khóa-giá trị mới
my_dict["job"] = "Engineer"  # Thêm khóa 'job' với giá trị 'Engineer'
print("Công việc:", my_dict["job"])  # Kết quả: Engineer

# Cập nhật giá trị của một khóa
my_dict["age"] = 31  # Cập nhật tuổi thành 31
print("Tuổi mới:", my_dict["age"])  # Kết quả: 31

# Xóa một cặp khóa-giá trị
del my_dict["city"]  # Xóa khóa 'city'
print("Dictionary sau khi xóa city:", my_dict)  # Kết quả: {'name': 'Alice', 'age': 31, 'job': 'Engineer'}




# Lặp qua các khóa và giá trị trong dictionary
for key, value in my_dict.items(): # .items() để lấy ra từng 
    print(f"{key}: {value}")  # In từng cặp khóa-giá trị


# Ví dụ cụ thể khi sử dụng items()
sinh_vien = {
    "ten": "Nam",
    "tuoi": 22,
    "lop": "12A1"
}
# Cách 1: Không dùng .items() (Cách cũ)
for k in sinh_vien:
    # k chỉ là key ("ten", "tuoi"...)
    # Muốn lấy value phải gọi lại dict
    print(f"{k}: {sinh_vien[k]}")

#Cách 2: Dùng .items() (Cách chuyên nghiệp)
# k là Key, v là Value (tự động tách ra)
for k, v in sinh_vien.items():
    print(f"{k}: {v}")
# ten: Nam
# tuoi: 22
# lop: 12A1

print(sinh_vien.items())
# Kết quả: dict_items([('ten', 'Nam'), ('tuoi', 22), ('lop', '12A1')])




# Kiểm tra sự tồn tại của một khóa
if "name" in my_dict:
    print("Khóa 'name' tồn tại trong dictionary")  # Kết quả: Khóa 'name' tồn tại trong dictionary
if "city" not in my_dict:
    print("Khóa 'city' không tồn tại trong dictionary")  # Kết quả: Khóa 'city' không tồn tại trong dictionary



# Lấy tất cả các khóa và giá trị
keys = my_dict.keys()
values = my_dict.values()   
print("Các khóa:", list(keys))      # Kết quả: ['name', 'age', 'job']
print("Các giá trị:", list(values))  # Kết quả: ['Alice', 31, 'Engineer']


# Kích thước của dictionary
size = len(my_dict) # Lấy số lượng cặp khóa-giá trị
print("Kích thước của dictionary:", size)  # Kết quả: 3


# Xóa tất cả các phần tử trong dictionary
my_dict.clear()  # Xóa tất cả các phần tử
print("Dictionary sau khi xóa tất cả phần tử:", my_dict)  # Kết quả: {}


# Tạo một dictionary mới từ các cặp khóa-giá trị
new_dict = dict([("a", 1), ("b", 2), ("c", 3)])  # Tạo dictionary từ danh sách các tuple
print("Dictionary mới:", new_dict)  # Kết quả: {'a': 1, 'b': 2, 'c': 3}


# Sử dụng phương thức get để truy cập giá trị
value = new_dict.get("b")  # Lấy giá trị của khóa 'b'
print("Giá trị của khóa 'b':", value)  # Kết quả: 2
missing_value = new_dict.get("d", "Not Found")  # Lấy giá trị của khóa 'd' với giá trị mặc định
print("Giá trị của khóa 'd':", missing_value)  # Kết quả: Not Found

# Sao chép một dictionary
copied_dict = new_dict.copy()  # Sao chép dictionary
print("Dictionary sao chép:", copied_dict)  # Kết quả: {'a': 1, 'b': 2, 'c': 3}


# Cập nhật một dictionary với các cặp khóa-giá trị từ một dictionary khác
update_dict = {"b": 20, "d": 4}  # Dictionary để cập nhật
new_dict.update(update_dict)  # Cập nhật new_dict với update_dict
print("Dictionary sau khi cập nhật:", new_dict)  # Kết quả: {'a': 1, 'b': 20, 'c': 3, 'd': 4}


# Tạo một dictionary với các khóa từ một danh sách và giá trị mặc định
keys_list = ["x", "y", "z"]  # Danh sách các khóa
default_dict = dict.fromkeys(keys_list, 0)  # Tạo dictionary với giá trị mặc định là 0
print("Dictionary với giá trị mặc định:", default_dict)  # Kết quả: {'x': 0, 'y': 0, 'z': 0}


# Loại bỏ và trả về một cặp khóa-giá trị
removed_value = new_dict.pop("c")  # Loại bỏ khóa 'c' và trả về giá trị của nó
print("Giá trị bị loại bỏ của khóa 'c':", removed_value)  # Kết quả: 3
print("Dictionary sau khi loại bỏ khóa 'c':", new_dict)  # Kết quả: {'a': 1, 'b': 20, 'd': 4}



# Loại bỏ và trả về một cặp khóa-giá trị cuối cùng được thêm vào
last_item = new_dict.popitem()  # Loại bỏ và trả về cặp khóa-giá trị cuối cùng
print("Cặp khóa-giá trị bị loại bỏ cuối cùng:", last_item)  # Kết quả: ('d', 4)
print("Dictionary sau khi popitem:", new_dict)  # Kết quả: {'a': 1, 'b': 20}


