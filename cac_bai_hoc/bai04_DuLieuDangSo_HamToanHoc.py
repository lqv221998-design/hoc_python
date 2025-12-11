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


# Hàm sum() tính tổng các phần tử trong một iterable
numbers = [1, 2, 3, 4, 5]
print("Tổng của các số trong danh sách là:", sum(numbers)) #Kết quả: 15


# Hàm min() và max() tìm giá trị nhỏ nhất và lớn nhất trong một iterable
print("Giá trị nhỏ nhất trong danh sách là:", min(numbers)) #Kết quả: 1
print("Giá trị lớn nhất trong danh sách là:", max(numbers)) #Kết quả: 5


#Hàm round() làm tròn số đến chữ số thập phân nhất định
num_to_round = 3.14159
print("Làm tròn số đến 2 chữ số thập phân:", round(num_to_round, 2)) #Kết quả: 3.14


#Hàm int(), float(), complex() chuyển đổi kiểu dữ liệu
str_num = "42"
print("Chuyển chuỗi sang int:", int(str_num))       #Kết quả: 42
print("Chuyển chuỗi sang float:", float(str_num))   #Kết quả: 42.0
print("Chuyển chuỗi sang complex:", complex(str_num)) #Kết quả: (42+0j)


#Hàm math.factorial() tính giai thừa
fact_num = 5
print("Giai thừa của", fact_num, "là:", math.factorial(fact_num)) #Kết quả: 120


#Hàm math.gcd() tính ước số chung lớn nhất
num1 = 48
num2 = 18
print("Ước số chung lớn nhất của", num1, "và", num2, "là:", math.gcd(num1, num2)) #Kết quả: 6


#Hàm math.lcm() tính bội số chung nhỏ nhất (Python 3.9+)
print("Bội số chung nhỏ nhất của", num1, "và", num2, "là:", math.lcm(num1, num2)) #Kết quả: 144


#Hàm math.radians() và math.degrees() chuyển đổi giữa độ và radian
degrees = 180
radians = math.radians(degrees)
print(degrees, "độ bằng", radians, "radian") #Kết quả: 180 độ bằng 3.141592653589793 radian
print(radians, "radian bằng", math.degrees(radians), "độ") #Kết quả: 3.141592653589793 radian bằng 180.0 độ


#Hàm math.exp() tính e mũ x
exp_value = 2
print("Giá trị e mũ", exp_value, "là:", math.exp(exp_value)) #Kết quả: 7.38905609893065


#Hàm math.sin(), math.cos(), math.tan() tính giá trị lượng giác
angle_deg = 30
angle_rad = math.radians(angle_deg)
print("Sin của", angle_deg, "độ là:", math.sin(angle_rad)) #Kết quả: 0.49999999999999994
print("Cos của", angle_deg, "độ là:", math.cos(angle_rad)) #Kết quả: 0.8660254037844387
print("Tan của", angle_deg, "độ là:", math.tan(angle_rad)) #Kết quả: 0.5773502691896257


#Hàm math.asin(), math.acos(), math.atan() tính giá trị ngược lượng giác
value = 0.5
print("Arcsin của", value, "là:", math.degrees(math.asin(value))) #Kết quả: 30.000000000000004
print("Arccos của", value, "là:", math.degrees(math.acos(value))) #Kết quả: 60.0
print("Arctan của", value, "là:", math.degrees(math.atan(value))) #Kết quả: 26.56505117707799


#Hàm math.hypot() tính độ dài cạnh huyền của tam giác vuông
a = 3
b = 4
print("Độ dài cạnh huyền là:", math.hypot(a, b)) #Kết quả: 5.0


#Hàm math.isqrt() tính căn bậc hai nguyên (Python 3.8+)
n = 20
print("Căn bậc hai nguyên của", n, "là:", math.isqrt(n)) #Kết quả: 4


#Hàm math.modf() tách phần nguyên và phần thập phân của số thực
num = 5.75
fractional, integer = math.modf(num)
print("Phần thập phân của", num, "là:", fractional) #Kết quả: 0.75
print("Phần nguyên của", num, "là:", integer)       #Kết quả: 5.0


#Hàm math.copysign() sao chép dấu của một số sang số khác
magnitude = 3.5
sign_source = -2.0
result = math.copysign(magnitude, sign_source)
print("Kết quả của copysign là:", result) #Kết quả: -3.5


#Hàm math.trunc() loại bỏ phần thập phân của số thực
float_num = 7.89
print("Giá trị sau khi trunc là:", math.trunc(float_num)) #Kết quả: 7


#Hàm math.prod() tính tích các phần tử trong một iterable (Python 3.8+)
num_list = [1, 2, 3, 4]
print("Tích của các số trong danh sách là:", math.prod(num_list)) #Kết quả: 24


#Hàm math.dist() tính khoảng cách Euclid giữa hai điểm trong không gian n chiều (Python 3.8+)
point1 = (1, 2)
point2 = (4, 6)
print("Khoảng cách giữa hai điểm là:", math.dist(point1, point2)) #Kết quả: 5.0


#Hàm math.perm() tính số hoán vị (Python 3.8+)
n = 5
k = 2
print("Số hoán vị P({}, {}) là:".format(n, k), math.perm(n, k)) #Kết quả: 20


#Hàm math.comb() tính số tổ hợp (Python 3.8+)
n = 5
k = 2
print("Số tổ hợp C({}, {}) là:".format(n, k), math.comb(n, k)) #Kết quả: 10


#Hàm math.ulp() trả về đơn vị cuối cùng của số thực (Python 3.9+)
num = 1.0
print("Đơn vị cuối cùng của", num, "là:", math.ulp(num)) #Kết quả: 2.220446049250313e-16


#Hàm math.nextafter() trả về số thực tiếp theo về phía một số khác (Python 3.9+)
start = 1.0
direction = 2.0
print("Số thực tiếp theo sau", start, "về phía", direction, "là:", math.nextafter(start, direction)) #Kết quả: 1.0000000000000002


