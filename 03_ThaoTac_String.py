
# Xuống dòng trong chuỗi
print("Hello\nWorld") #Kết quả: Hello
                      #        World

# Cách muốn in dấu nháy kép trong chuỗi
print("He said: \"Hello World\"") #Kết quả: He said: "Hello World"

# Tất cả các hàm thao tác với chuỗi
my_string = "Hello World" # Luôn luôn bắt đầu là 0
print(my_string.lower())      # Kết quả: hello world
print(my_string.upper())      # Kết quả: HELLO WORLD
print(my_string.strip())      # Kết quả: Hello World
print(my_string.replace("World", "Python")) # Kết quả:   Hello Python
print(my_string.split())      # Kết quả: ['Hello', 'World']
print(my_string[0].isupper())  # Kết quả: True
print(len(my_string))        # Kết quả: 11 (độ dài chuỗi bao gồm cả dấu cách)
print(my_string.index("W"))  # Kết quả: 6 (vị trí của chữ 'W' trong chuỗi)
print(my_string.index("World"))  # Kết quả: 6 (vị trí của từ 'World' trong chuỗi)
print(my_string.index("wor"))
print(my_string.count("o"))  # Kết quả: 2 (chữ 'o' xuất hiện 2 lần)
print(my_string.startswith("Hello")) # Kết quả: True (bắt đầu bằng "Hello")
print(my_string.endswith("World"))   # Kết quả: True (kết thúc bằng "World")
print(my_string.find("o"))   # Kết quả: 4 (vị trí đầu tiên của chữ 'o')
print(my_string.capitalize()) # Kết quả: Hello world (chữ cái đầu viết hoa)
print(my_string.title())      # Kết quả: Hello World (mỗi từ viết hoa chữ cái đầu)
print(my_string.center(15))  # Kết quả: '   Hello World   ' (căn giữa trong chuỗi dài 15 ký tự)
print(my_string.encode())      # Kết quả: b'Hello World' (mã hóa chuỗi thành bytes)

# Nối chuỗi
str1 = "Hello"
str2 = "Python"
result = str1 + " " + str2
print(result)  # Kết quả: Hello Python

# Định dạng chuỗi
name = "Alice"
age = 30
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print(formatted_str)  # Kết quả: My name is Alice and I am 30 years old.

# xử lý chuỗi f-string (Python 3.6+)
formatted_str_f = f"My name is {name} and I am {age} years old."
print(formatted_str_f)  # Kết quả: My name is Alice and I am 30 years old.

# Kiểu dữ liệu chuỗi trong Python
sample_str = "Hello, Python!"
print("Kiểu dữ liệu của sample_str:", type(sample_str)) #Kết quả: <class 'str'>

# Truy cập ký tự trong chuỗi
first_char = sample_str[0]  #Ký tự đầu tiên
last_char = sample_str[-1]  #Ký tự cuối cùng
print("Ký tự đầu tiên:", first_char) #Kết quả: H
print("Ký tự cuối cùng:", last_char)  #Kết quả: !

# Cắt chuỗi (slicing)
vidu = "Hello, Python!"
substring = vidu[7:13]  #Lấy từ ký tự thứ 7 đến 12
print("Chuỗi con:", substring)  #Kết quả: Python