# Xuống dòng trong chuỗi
print("Hello\nWorld") #Kết quả: Hello
                      #        World

# Cách muốn in dấu nháy kép trong chuỗi
print("He said: \"Hello World\"") #Kết quả: He said: "Hello World"

# Các hàm xử lý chuỗi cơ bản
my_string = "Hello World" # Luôn luôn bắt đầu là 0
print(my_string.lower())      # Kết quả: hello world
print(my_string.upper())      # Kết quả: HELLO WORLD
print(my_string.strip())      # Kết quả: Hello World
print(my_string.replace("World", "Python")) # Kết quả:   Hello Python
print(my_string.split())      # Kết quả: ['Hello', 'World']
print(my_string[0].isupper())  # Kết quả: True
print(len(my_string))        # Kết quả: 11 (độ dài chuỗi bao gồm cả dấu cách)
print(my_string.index("W"))  # Kết quả: 6 (vị trí của chữ 'W' trong chuỗi)
print(my_string.count("o"))  # Kết quả: 2 (chữ 'o' xuất hiện 2 lần)
