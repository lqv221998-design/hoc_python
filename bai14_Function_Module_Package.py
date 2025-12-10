# Function hay còn gọi là hàm, cấu trúc như sau:
'''
def function_name (par1 ,par2, ...):
    body_func
    return
'''

# Ví dụ hàm (function):
def infomation (name, age, chieu_cao, can_nang):    # Khởi tạo hàm tên infomation
    BMI = can_nang/chieu_cao                        # Tính chỉ số BIM
    return f"Hello {name}, với chiều cao {chieu_cao} và cân nặng {can_nang} thì chỉ số BMI của bạn là: {round(BMI,2)}" #Trả về kết quả từ các parameter

name = input("Hãy nhập tên của bạn: ")              # Dữ liệu đầu vào mà người dùng nhập 
age = int(input("Hãy nhập tuổi của bạn: "))
chieu_cao = int(input("Hãy nhập chiều cao của bạn: "))
can_nang = int(input("Hãy nhập cân nặng của bạn: "))

print(infomation(name, age, chieu_cao, can_nang))   # In ra kết quả thông tin



# Gọi các hàm từ các file khác trong thư mục:
from bai06_ThaoTacVoiHam import add
TinhTongHaiSo = add(3,4)
print(TinhTongHaiSo)

# Gọi hàm từ các file trong thư mục khác: Hay còn gọi là Package (Thư mục này phải chứ file __init__.py)
# from [Thư mục].[Tên_File_Không_Đuôi_Py] import [Tên_Hàm]


# Cho trước giá trị cho hàm, hàm thay đổi khi truyền giá trị mới:
import math   # import thư viện
def TinhCanBac2 (a = 5):  #Khởi tạo hàm với giá trị cho trước
    pheptinh = math.sqrt(a)  #Thực hiện phép tính
    return pheptinh

ketqua = TinhCanBac2(4) 
print(ketqua)
