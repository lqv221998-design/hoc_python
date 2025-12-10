# Function hay còn gọi là hàm, cấu trúc như sau:
'''
def function_name (par1 ,par2, ...):
    body_func
    return
'''
# Ví dụ hàm (function):
def infomation (name, age, chieu_cao, can_nang):
    BMI = can_nang/chieu_cao
    return f"Hello {name}, với chiều cao {chieu_cao} và cân nặng {can_nang} thì chỉ số BMI của bạn là: {round(BMI,2)}"

name = input("Hãy nhập tên của bạn: ")
age = int(input("Hãy nhập tuổi của bạn: "))
chieu_cao = int(input("Hãy nhập chiều cao của bạn: "))
can_nang = int(input("Hãy nhập cân nặng của bạn: "))

print(infomation(name, age, chieu_cao, can_nang))


