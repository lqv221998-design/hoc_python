# Xử lý ngoại lệ:
"""
try:
    print(text)
except:
    print("Có lỗi xảy ra, vui lòng liên hệ lập trình viên")
"""

# Có thể sử dụng nhiều except để bắt các lỗi trong code
ten = input("Nhập tên của bạn: ")
try:
    nam_hien_tai = 2025
    nam_sinh = int(input("Nhập năm sinh của bạn: "))  #Lưu ý try phải bao lấy dòng có exception
    thuong_nam_sinh = nam_hien_tai/nam_sinh
    print(f"Tên của bạn là: {ten}. Tuổi của bạn là: {nam_hien_tai-nam_sinh}. Thương của năm sinh là: {thuong_nam_sinh}")
except ValueError:
    print("Bạn phải nhập 1 số")
except ZeroDivisionError:
    print("Năm sinh của bạn phải khác 0")
except:
    print("Vui lòng liên hệ lập trình viên")