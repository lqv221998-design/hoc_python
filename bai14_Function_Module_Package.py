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


# Ví dụ cho continue và exit trong hàm và vòng lặp:
import sys # Cần thư viện này để dùng sys.exit() chuẩn nhất

def kiem_tra_so(danh_sach):
    print("--- Bắt đầu kiểm tra ---")
    
    for so in danh_sach:
        # TRƯỜNG HỢP 1: Gặp số 0 thì bỏ qua (dùng continue)
        if so == 0:
            print("Gặp số 0 -> Bỏ qua, không xử lý!")
            continue   # khi vòng lặp lặp đến giá trị bằng 0 trong chuỗi sẽ bỏ qua nó và tiếp tục chạy chương trình 
        
        # TRƯỜNG HỢP 2: Gặp số âm thì DỪNG CHƯƠNG TRÌNH (dùng exit)
        if so < 0:
            print(f"Lỗi nguy hiểm: Gặp số âm {so} -> Tắt chương trình ngay!")
            exit() # khi chạy đến số nhỏ hơn 0 đúng với điều kiện thì chương trình tắt hoàn toàn
            
        # Nếu không dính 2 lệnh trên thì dòng này mới được chạy
        print(f"Đã xử lý xong số: {so}")

    print("--- Kết thúc hàm ---") # Dòng này sẽ KHÔNG chạy nếu gặp exit()

# Chạy thử
my_list = [10, 20, 0, 30, -5, 40]
kiem_tra_so(my_list)


