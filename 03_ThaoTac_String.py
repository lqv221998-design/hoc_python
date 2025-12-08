
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
