#Dữ liệu dạng số và các hàm toán học trong Python
import math

#Các kiểu dữ liệu số trong Python
a = 10          #Kiểu int (số nguyên)
b = 3.14        #Kiểu float (số thực)
c = 2 + 3j     #Kiểu complex (số phức)
print("Kiểu dữ liệu của a:", type(a)) #Kếtquả: <class 'int'>
print("Kiểu dữ liệu của b:", type(b)) #Kếtquả: <class 'float'>
print("Kiểu dữ liệu của c:", type(c)) #Kếtquả: <class 'complex'>
    # Ví dụ về số phức
real_part = c.real   #Phần thực
imag_part = c.imag   #Phần ảo
print("Phần thực của c:", real_part) #Kếtquả: 2.0
print("Phần ảo của c:", imag_part)   #Kếtquả: 3.0


#Các phép toán cơ bản với số
x = 15
y = 4
print("Phép cộng:", x + y)          #Kếtquả: 19
print("Phép trừ:", x - y)           #Kếtquả: 11
print("Phép nhân:", x * y)          #Kếtquả: 60
print("Phép chia:", x / y)          #Kếtquả: 3.75
print("Phép chia lấy phần nguyên:", x // y) #Kếtquả: 3
print("Phép chia lấy phần dư:", x % y)      #Kếtquả: 3
print("Phép lũy thừa:", x ** y)      #Kếtquả: 50625


#Sử dụng các hàm toán học từ thư viện math
num = 16
print("Căn bậc hai của", num, "là:", math.sqrt(num)) #Kếtquả: 4.0
angle = math.pi / 4  #45 độ
print("Giá trị sin của 45 độ là:", math.sin(angle)) #Kếtquả: 0.7071067811865475
print("Giá trị cos của 45 độ là:", math.cos(angle)) #Kếtquả: 0.7071067811865476
print("Giá trị logarit cơ số e của", num, "là:", math.log(num)) #Kếtquả: 2.772588722239781
print("Giá trị logarit cơ số 10 của", num, "là:", math.log10(num)) #Kếtquả: 1.2041199826559248


#Làm tròn số    
val = 5.6789
print("Làm tròn lên:", math.ceil(val))   #Kếtquả: 6
print("Làm tròn xuống:", math.floor(val)) #Kếtquả: 5
print("Làm tròn theo giá trị gần nhất:", round(val, 3)) #Kếtquả: 5.679       


#Hàm abs() trả về giá trị tuyệt đối
neg_num = -20       
print("Giá trị tuyệt đối của", neg_num, "là:", abs(neg_num)) #Kếtquả: 20


#Hàm pow() tính lũy thừa
base = 2
exponent = 5
print(base, "mũ", exponent, "là:", pow(base, exponent)) #Kếtquả: 32
#Hàm divmod() trả về thương và số dư của phép chia
dividend = 17
divisor = 3
quotient, remainder = divmod(dividend, divisor)
print("Thương và số dư của", dividend, "chia cho", divisor, "là:", (quotient, remainder)) #Kếtquả: (5, 2)
# Hàm round() làm tròn số
