# Dự liệu dang danh sách trong Python
# Tạo danh sách
my_list = [1, 2, 3, 4, 5]
print("Danh sách ban đầu:", my_list)  # Kết quả: [1, 2, 3, 4, 5]

# Truy cập phần tử trong danh sách
first_element = my_list[0]  # Phần tử đầu tiên
last_element = my_list[-1]  # Phần tử cuối cùng
print("Phần tử đầu tiên:", first_element)  # Kết quả: 1
print("Phần tử cuối cùng:", last_element)   # Kết quả: 5


# Thêm phần tử vào danh sách
my_list.append(6)
print("Danh sách sau khi thêm phần tử:", my_list)  # Kết quả: [1, 2, 3, 4, 5, 6]


# Xóa phần tử khỏi danh sách
my_list.remove(3)
print("Danh sách sau khi xóa phần tử 3:", my_list)  # Kết quả: [1, 2, 4, 5, 6]


# Lặp qua các phần tử trong danh sách
print("Các phần tử trong danh sách:")
for item in my_list:
    print(item)  # Kết quả: 1 2 4 5 6 (mỗi số trên một dòng)


# Kích thước của danh sách
print("Kích thước của danh sách:", len(my_list))  # Kết quả: 5


# Kiểm tra sự tồn tại của phần tử trong danh sách
check_value = 4
if check_value in my_list:
    print(f"{check_value} tồn tại trong danh sách.")  # Kết quả: 4 tồn tại trong danh sách.
else:
    print(f"{check_value} không tồn tại trong danh sách.")


# Sắp xếp danh sách
my_list.sort()
print("Danh sách sau khi sắp xếp:", my_list)  # Kết quả: [1, 2, 4, 5, 6]


# Đảo ngược danh sách
my_list.reverse()
print("Danh sách sau khi đảo ngược:", my_list)  # Kết quả: [6, 5, 4, 2, 1]


# Sao chép danh sách
copied_list = my_list.copy()
print("Danh sách sao chép:", copied_list)  # Kết quả: [6, 5, 4, 2, 1]


# Xóa tất cả phần tử trong danh sách
my_list.clear()
print("Danh sách sau khi xóa tất cả phần tử:", my_list)  # Kết quả: []


# Nối danh sách
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Danh sách sau khi nối:", combined_list)  # Kết quả: [1, 2, 3, 4, 5, 6]


# Lấy phần tử con từ danh sách (slicing)
sub_list = combined_list[1:4]  # Lấy từ phần tử thứ 1 đến 3
print("Phần tử con từ danh sách:", sub_list)  # Kết quả: [2, 3, 4]


# Lặp qua các chỉ số và phần tử trong danh sách
print("Chỉ số và phần tử trong danh sách:")
for index, value in enumerate(combined_list):
    print(f"Chỉ số: {index}, Giá trị: {value}") # Chỉ số: 0, Giá trị: 1
                                                # Chỉ số: 1, Giá trị: 2
                                                # Chỉ số: 2, Giá trị: 3
                                                # Chỉ số: 3, Giá trị: 4
                                                # Chỉ số: 4, Giá trị: 5
                                                # Chỉ số: 5, Giá trị: 6



# Tìm vị trí của phần tử trong danh sách
value_to_find = 5
position = combined_list.index(value_to_find)
print(f"Vị trí của {value_to_find} trong danh sách là:", position)  # Kết quả: 4


# Đếm số lần xuất hiện của phần tử trong danh sách
count_value = 2
occurrences = combined_list.count(count_value)
print(f"Số lần xuất hiện của {count_value} trong danh sách là:", occurrences)  # Kết quả: 1



# Chuyển đổi chuỗi thành danh sách
string_data = "Python,Java,C++,JavaScript"
language_list = string_data.split(",")
print("Danh sách ngôn ngữ lập trình:", language_list)  # Kết quả: ['Python', 'Java', 'C++', 'JavaScript']


# Chuyển đổi danh sách thành chuỗi
joined_string = ",".join(language_list)
print("Chuỗi sau khi nối từ danh sách:", joined_string)  # Kết quả: Python,Java,C++,JavaScript


# Lặp qua danh sách với list comprehension
squared_list = [x**2 for x in range(1, 6)]
print("Danh sách các số bình phương:", squared_list)  # Kết quả: [1, 4, 9, 16, 25]


# Sắp xếp danh sách theo thứ tự giảm dần
unsorted_list = [3, 1, 4, 5, 2]
unsorted_list.sort(reverse=True)
print("Danh sách sau khi sắp xếp giảm dần:", unsorted_list)  # Kết quả: [5, 4, 3, 2, 1]


# Tạo danh sách đa chiều (danh sách trong danh sách)
multi_dimensional_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Danh sách đa chiều:", multi_dimensional_list)  # Kết quả: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Ứng dụng danh sách đa chiều
print("Phần tử ở hàng 1, cột 2:", multi_dimensional_list[1][2])  # Kết quả: 6
print("Phần tử ở hàng 2, cột 2:", multi_dimensional_list[2][3])  # Kết quả: 9


# Sao chép danh sách đa chiều (sao chép sâu)
import copy
deep_copied_list = copy.deepcopy(multi_dimensional_list)
print("Danh sách đa chiều sau khi sao chép sâu:", deep_copied_list)  # Kết quả: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

coppy_list = multi_dimensional_list.copy()
print("Danh sách đa chiều sau khi sao chép nông:", coppy_list)

# Thay đổi phần tử trong danh sách đa chiều gốc
multi_dimensional_list[0][0] = 99
print("Danh sách đa chiều gốc sau khi thay đổi:", multi_dimensional_list)  # Kết quả: [[99, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Danh sách đa chiều sao chép sâu không bị ảnh hưởng:", deep_copied_list)  # Kết quả: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]multi_dimensional_list = [[1, 2, 3], [4, 5,
print("Danh sách đa chiều sao chép nông bị ảnh hưởng:", coppy_list)  # Kết quả: [[99, 2, 3], [4, 5, 6], [7, 8, 9]]


# Ứng dụng nâng cao: Lọc phần tử trong danh sách
original_list = [10, 15, 20, 25, 30, 35, 40]
filtered_list = [x*2 for x in original_list if x > 25]
print("Danh sách sau khi lọc các phần tử lớn hơn 25:", filtered_list)  # Kết quả: [60, 70, 80] (nhân đôi các phần tử lớn hơn 25)

# Ứng dụng nâng cao: Tìm phần tử lớn nhất và nhỏ nhất trong danh sách
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
max_value = max(numbers)
min_value = min(numbers)
print("Phần tử lớn nhất trong danh sách:", max_value)  # Kết quả: 9
print("Phần tử nhỏ nhất trong danh sách:", min_value)  # Kết quả: 1


# Ứng dụng nâng cao: Tính tổng và trung bình của các phần tử trong danh sách
total_sum = sum(numbers)
average = total_sum / len(numbers)
print("Tổng các phần tử trong danh sách:", total_sum)  # Kết quả: 36
print("Trung bình các phần tử trong danh sách:", average)  # Kết quả: 4.0

# Ứng dụng nâng cao: Loại bỏ phần tử trùng lặp trong danh sách
dup_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(dup_list))
print("Danh sách sau khi loại bỏ phần tử trùng lặp:", unique_list)  # Kết quả: [1, 2, 3, 4, 5] (thứ tự có thể khác nhau do set không giữ thứ tự)


# Ứng dụng nâng cao: Sử dụng hàm lambda với danh sách
sorted_list = sorted(numbers, key=lambda x: -x)  # Sắp xếp giảm dần
print("Danh sách sau khi sắp xếp giảm dần bằng hàm lambda:", sorted_list)  # Kết quả: [9, 6, 5, 5, 4, 3, 2, 1, 1]
# Thêm ví dụ sử dụng hàm lambda để lọc phần tử chẵn
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Danh sách các số chẵn:", even_numbers)  # Kết quả: [4, 2, 6]

# Ứng dụng nâng cao: Tạo danh sách các tuple từ hai danh sách
list_a = ['a', 'b', 'c']
list_b = [1, 2, 3]
zipped_list = list(zip(list_a, list_b))
print("Danh sách các tuple từ hai danh sách:", zipped_list)     # Kết quả: [('a', 1), ('b', 2), ('c', 3)] 
                                                                # cách suy luận: ghép từng phần tử tương ứng từ hai danh sách