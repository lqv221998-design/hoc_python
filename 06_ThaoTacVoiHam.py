# Thao tác với hàm def trong Python

# Hàm đơn giản để chào hỏi
def greet(name):   # Hàm chào hỏi
    return f"Hello, {name}!"   # Trả về chuỗi chào hỏi
print(greet("Alice"))   # Gọi hàm và in kết quả: Hello, Alice!

# Hàm tính tổng hai số
def add(a, b):  # Hàm cộng hai số add là tên hàm, a và b là các tham số
    return a + b  # Trả về tổng của a và b
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