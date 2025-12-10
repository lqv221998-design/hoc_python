# Vòng lặp While trong Python
count = 0  # Khởi tạo biến đếm
while count < 5:  # Điều kiện vòng lặp
    print("Giá trị của count là:", count)  # In giá trị hiện tại của count
    count += 1  # Tăng biến đếm lên 1
print("Vòng lặp kết thúc khi count =", count)  # In giá trị cuối cùng của count. Kết quả: 

# Vòng lặp While với câu lệnh break
num = 0
while True:  # Vòng lặp vô hạn
    print("Số hiện tại là:", num)
    num += 1
    if num >= 3:  # Điều kiện để thoát vòng lặp
        print("Thoát vòng lặp khi num =", num) # Kết quả: 
        break  # Thoát khỏi vòng lặp

# Vòng lặp While với câu lệnh continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Bỏ qua số 3")
        continue  # Bỏ qua phần còn lại của vòng lặp khi i bằng 3
    print("Số hiện tại là:", i)  # Kết quả:


