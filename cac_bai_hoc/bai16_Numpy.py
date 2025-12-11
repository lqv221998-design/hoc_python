
# 1. NHẬP THƯ VIỆN CẦN THIẾT
import numpy as np               # Thư viện toán học để tạo mảng/vector
import matplotlib.pyplot as plt  # Thư viện vẽ đồ thị

# 2. KHỞI TẠO DỮ LIỆU (Bước quan trọng để tránh lỗi NameError)
# Tạo vector v có tọa độ x=1, y=2
v = np.array([1, 2])      
# Tạo vector v_R (vector màu đỏ) có tọa độ x=-2, y=1
v_R = np.array([-2, 1])   

# 3. THIẾT LẬP KHUNG VẼ
# figsize=(5, 4): Tạo khung hình rộng 5 inch, cao 4 inch
# tight_layout=True: Tự động căn lề cho đẹp, không bị mất chữ
fig, ax = plt.subplots(figsize=(5, 4), tight_layout=True)

# 4. VẼ CÁC VECTOR (MŨI TÊN)
# Cú pháp: ax.arrow(x_gốc, y_gốc, độ_dài_x, độ_dài_y, ...)
# *v là kỹ thuật "Unpacking": tách mảng [1, 2] thành 2 số riêng biệt 1 và 2
ax.arrow(0, 0, *v, color="k", length_includes_head=True, head_width=0.1)
# Ghi chú thích cho vector v (dùng cú pháp LaTeX r"$\vec{v}$" để có dấu mũi tên trên đầu chữ v)
ax.text(*v, r"$\vec{v}$", fontsize=16, va="bottom", ha="left")

# Vẽ vector v_R màu đỏ (color="r")
ax.arrow(0, 0, *v_R, color="r", length_includes_head=True, head_width=0.1)
ax.text(*v_R, r"$\vec{v_R}$", color="r", fontsize=16, va="bottom", ha="right")


# 5. CẤU HÌNH TRỤC TỌA ĐỘ (SPINES) - Phần tạo nên trục Tung/Hoành
# Dời trục trái (Left - Trục tung) về vị trí 0 (giữa hình)
ax.spines['left'].set_position('zero')
# Dời trục dưới (Bottom - Trục hoành) về vị trí 0 (giữa hình)
ax.spines['bottom'].set_position('zero')

# Ẩn trục phải (Right) và trục trên (Top) đi cho giống hệ trục toán học
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


# 6. TÙY CHỈNH GIỚI HẠN VÀ VẠCH CHIA
# Cài đặt giới hạn trục x (từ -3 đến 2) và trục y (từ -1 đến 3) để vector nằm gọn trong hình
ax.set_xlim(-3, 2)
ax.set_ylim(-1, 3)

# Tạo lưới mờ (grid) để dễ nhìn tọa độ (tùy chọn)
ax.grid(True, linestyle=':', alpha=0.6)

# 7. HIỂN THỊ ĐỒ THỊ
plt.show()



