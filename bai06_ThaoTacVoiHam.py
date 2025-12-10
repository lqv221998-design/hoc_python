# Thao tác với hàm def trong Python

# Hàm đơn giản để chào hỏi
def greet(name):   # Hàm chào hỏi
    return f"Hello, {name}!"   # Trả về chuỗi chào hỏi
if __name__ == "__main__":
    print(greet("Alice"))   # Gọi hàm và in kết quả: Hello, Alice!

# Hàm tính tổng hai số
def add(a, b):  # Hàm cộng hai số add là tên hàm, a và b là các tham số
    return a + b  # Trả về tổng của a và b
if __name__ == "__main__":
    print("Tổng của 3 và 5 là:", add(3, 5))  # Gọi hàm và in kết quả: 8


# Hàm kiểm tra số chẵn lẻ
def is_even(number):  # Hàm kiểm tra số chẵn
    return number % 2 == 0  # Trả về True nếu số chẵn, False nếu số lẻ
print("4 là số chẵn:", is_even(4))  # Gọi hàm và in kết quả: True
print("7 là số chẵn:", is_even(7))  # Gọi hàm và in kết quả: False


# Hàm tính giai thừa
def factorial(n):  # Hàm tính giai thừa
    if n == 0 or n == 1:  # Giai thừa của 0 hoặc 1 là 1
        return 1
    else:
        return n * factorial(n - 1)  # Gọi đệ quy để tính giai thừa
print("Giai thừa của 5 là:", factorial(5))  # Gọi hàm và in kết quả: 120


# Hàm tìm giá trị lớn nhất trong danh sách
def find_max(numbers):  # Hàm tìm giá trị lớn nhất
    max_value = numbers[0]  # Giả sử giá trị đầu tiên là lớn nhất
    for num in numbers:  # Duyệt qua từng số trong danh sách
        if num > max_value:  # Nếu số hiện tại lớn hơn max_value
            max_value = num  # Cập nhật max_value
    return max_value  # Trả về giá trị lớn nhất
print("Giá trị lớn nhất là:", find_max([3, 1, 4, 1, 5, 9, 2, 6]))  # Gọi hàm và in kết quả: 9


# Hàm sắp xếp danh sách theo thứ tự tăng dần
def sort_list(numbers):  # Hàm sắp xếp danh sách
    return sorted(numbers)  # Sử dụng hàm sorted để sắp xếp
print("Danh sách sau khi sắp xếp:", sort_list([3, 1, 4, 1, 5, 9, 2, 6]))  # Gọi hàm và in kết quả: [1, 1, 2, 3, 4, 5, 6, 9]

# Hàm kết hợp hai danh sách thành danh sách các tuple
def zip_lists(list1, list2):  # Hàm kết hợp hai danh sách
    return list(zip(list1, list2))  # Sử dụng hàm zip để kết hợp
print("Danh sách các tuple từ hai danh sách:", zip_lists(['a', 'b', 'c'], [1, 2, 3]))  # Gọi hàm và in kết quả: [('a', 1), ('b', 2), ('c', 3)]


# Hàm đếm số từ trong một chuỗi
def count_words(text):  # Hàm đếm số từ
    words = text.split()  # Tách chuỗi thành danh sách từ
    return len(words)  # Trả về số lượng từ
print("Số từ trong chuỗi là:", count_words("Học Python rất thú vị"))  # Gọi hàm và in kết quả: 4
# Hàm kiểm tra số nguyên tố



def is_prime(n):  # Hàm kiểm tra số nguyên tố
    if n <= 1:  # Số nhỏ hơn hoặc bằng 1 không phải số nguyên tố
        return False
    for i in range(2, int(n**0.5) + 1):  # Kiểm tra từ 2 đến căn bậc hai của n
        if n % i == 0:  # Nếu n chia hết cho i
            return False  # Không phải số nguyên tố
    return True  # Là số nguyên tố
print("5 là số nguyên tố:", is_prime(5))  # Gọi hàm và in kết quả: True
print("10 là số nguyên tố:", is_prime(10))  # Gọi hàm và in kết quả: False


# Hàm chuyển đổi độ C sang độ F
def celsius_to_fahrenheit(celsius):  # Hàm chuyển đổi độ C sang độ F
    return (celsius * 9/5) + 32  # Công thức chuyển đổi
print("25 độ C bằng độ F là:", celsius_to_fahrenheit(25))  # Gọi hàm và in kết quả: 77.0


# Hàm tính lũy thừa
def power(base, exponent):  # Hàm tính lũy thừa
    return base ** exponent  # Trả về base mũ exponent
print("2 mũ 3 là:", power(2, 3))  # Gọi hàm và in kết quả: 8


# Hàm lọc số chẵn từ danh sách
def filter_even_numbers(numbers):  # Hàm lọc số chẵn
    return [num for num in numbers if num % 2 == 0]  # Trả về danh sách số chẵn
print("Số chẵn trong danh sách là:", filter_even_numbers([1, 2, 3, 4, 5, 6]))  # Gọi hàm và in kết quả: [2, 4, 6]


# Hàm tính trung bình cộng của danh sách số
def average(numbers):  # Hàm tính trung bình cộng
    return sum(numbers) / len(numbers)  # Trả về tổng chia cho số lượng
print("Trung bình cộng là:", average([1, 2, 3, 4, 5]))  # Gọi hàm và in kết quả: 3.0

# Hàm đảo ngược chuỗi
def reverse_string(s):  # Hàm đảo ngược chuỗi
    return s[::-1]  # Trả về chuỗi đảo ngược
print("Chuỗi đảo ngược là:", reverse_string("Python"))  # Gọi hàm và in kết quả: nohtyP

# Hàm phức tạp hơn: Hàm tính tổng các số nguyên tố trong một phạm vi
def sum_of_primes(limit):  # Hàm tính tổng số nguyên tố
    total = 0
    for num in range(2, limit):  # Duyệt qua các số từ 2 đến limit-1
        if is_prime(num):  # Sử dụng hàm is_prime để kiểm tra
            total += num  # Cộng số nguyên tố vào tổng
    return total  # Trả về tổng các số nguyên tố
print("Tổng các số nguyên tố dưới 20 là:", sum_of_primes(20))  # Gọi hàm và in kết quả: 77


# Hàm sử dụng tham số mặc định: Hàm tính diện tích hình chữ nhật
def rectangle_area(length, width=1):  # Hàm tính diện tích với tham số mặc định
    return length * width  # Trả về diện tích   
print("Diện tích hình chữ nhật 5x3 là:", rectangle_area(5, 3))  # Gọi hàm và in kết quả: 15
print("Diện tích hình vuông cạnh 4 là:", rectangle_area(4))  # Gọi hàm với tham số mặc định và in kết quả: 4


# Sử dụng các hàm đã định nghĩa
numbers = [10, 15, 23, 42, 8, 16]
print("Danh sách số ban đầu:", numbers)  # In danh sách ban đầu
print("Số chẵn trong danh sách:", filter_even_numbers(numbers))  # Lọc và in số chẵn
print("Giá trị lớn nhất trong danh sách:", find_max(numbers))  # Tìm và in giá trị lớn nhất
print("Danh sách sau khi sắp xếp:", sort_list(numbers))  # Sắp xếp và in danh sách
print("Trung bình cộng của danh sách:", average(numbers))  # Tính và in trung bình cộng


# Truyền nhiều giá trị vào trong hàm, kiểu tuple
def tinhtong_dayso (*numbers):
    tong = sum(numbers)
    return tong
numbers = (1,1,1,1,1)
print(tinhtong_dayso(*numbers))


#Truyền vào kiểu từ điển:
def tudien (**tudiennhap):
    return tudiennhap
tudiennhap = {
    "ten" : "vu",
    "tuoi" : "27"
}
print(tudien(**tudiennhap))

