"""
Python Learning Assistant - Trợ lý học tập Python
Giúp bạn học và thực hành lập trình Python với các bài tập và hướng dẫn
"""

import random
from typing import List, Dict, Any
from datetime import datetime

# Thêm màu sắc cho giao diện console để sinh động hơn
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_color(text, color):
    print(f"{color}{text}{Colors.ENDC}")
class PythonLearningAssistant:
    """Lớp trợ lý học tập Python"""
    
    def __init__(self, user_name: str = "Học viên"):
        """Khởi tạo trợ lý học tập"""
        self.user_name = user_name
        self.score = 0
        self.completed_lessons = []
        self.start_time = datetime.now()
        print_color(f"🎓 Chào {self.user_name}! Tôi là trợ lý học tập Python của bạn.\n", Colors.BOLD)
    
    def show_menu(self):
        """Hiển thị menu chính"""
        menu = f"""
╔════════════════════════════════════════════════════════════════╗
║         {Colors.HEADER}{Colors.BOLD}TRỢ LÝ HỌC TẬP PYTHON - MENU CHÍNH{Colors.ENDC}                    ║
╠════════════════════════════════════════════════════════════════╣
║ {Colors.CYAN}1. 📚 Bài học cơ bản{Colors.ENDC}                                           ║
║ {Colors.CYAN}2. 💻 Luyện tập viết code{Colors.ENDC}                                     ║
║ {Colors.CYAN}3. 🧩 Giải quyết vấn đề (Problem Solving){Colors.ENDC}                    ║
║ {Colors.CYAN}4. 📝 Hướng dẫn chi tiết{Colors.ENDC}                                       ║
║ {Colors.GREEN}5. 🏆 Xem tiến độ học tập{Colors.ENDC}                                      ║
║ {Colors.FAIL}6. ❌ Thoát chương trình{Colors.ENDC}                                       ║
╚════════════════════════════════════════════════════════════════╝
        """
        print(menu)
    
    def basic_lessons(self):
        """Các bài học cơ bản"""
        lessons = {
            "1": {
                "title": "Biến và Kiểu Dữ Liệu",
                "content": """
📖 BIẾN VÀ KIỂU DỮ LIỆU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ BIẾN (Variables):
   - Biến là nơi lưu trữ dữ liệu trong Python
   - Đặt tên: viết thường, dùng underscore (_) nếu có nhiều từ
   
   Ví dụ:
   ──────
   age = 20          # Lưu số nguyên
   name = "Python"   # Lưu chuỗi ký tự
   height = 1.75     # Lưu số thực

2️⃣ KIỂU DỮ LIỆU:
   📍 int       - Số nguyên (5, -10, 0)
   📍 float     - Số thực (3.14, -2.5)
   📍 str       - Chuỗi ký tự ("Hello", 'Python')
   📍 bool      - Logic (True, False)
   📍 list      - Danh sách ([1, 2, 3])
   📍 dict      - Từ điển ({"name": "John"})
   📍 tuple     - Bộ dữ liệu ((1, 2, 3))

3️⃣ KIỂM TRA KIỂU DỮ LIỆU:
   type(age)         # <class 'int'>
   type("Hello")     # <class 'str'>
   type(3.14)        # <class 'float'>

💡 MẸO: Dùng hàm type() để kiểm tra kiểu dữ liệu bất kỳ lúc nào!
                """
            },
            "2": {
                "title": "Vòng Lặp (Loops)",
                "content": """
📖 VÒNG LẶP (LOOPS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ VÒNG LẶP FOR:
   Dùng khi biết trước số lần lặp
   
   Cú pháp:
   for i in range(5):
       print(i)  # In ra: 0, 1, 2, 3, 4
   
   Lặp qua danh sách:
   for item in [1, 2, 3]:
       print(item * 2)  # In ra: 2, 4, 6

2️⃣ VÒNG LẶP WHILE:
   Lặp khi điều kiện còn đúng
   
   Cú pháp:
   count = 0
   while count < 5:
       print(count)
       count += 1

3️⃣ BREAK và CONTINUE:
   - break     : Thoát vòng lặp ngay lập tức
   - continue  : Bỏ qua lần lặp hiện tại
   
   Ví dụ:
   for i in range(10):
       if i == 5:
           break      # Dừng khi i = 5
       print(i)

💡 MẸO: range(start, end, step) - tạo dãy số từ start đến end-1
                """
            },
            "3": {
                "title": "Hàm (Functions)",
                "content": """
📖 HÀM (FUNCTIONS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ ĐỊNH NGHĨA HÀM:
   Cú pháp:
   def tên_hàm(tham_số):
       # Phần thân hàm
       return kết_quả
   
   Ví dụ:
   def greet(name):
       return f"Xin chào {name}!"
   
   print(greet("Python"))  # Xin chào Python!

2️⃣ THAM SỐ MẶC ĐỊNH:
   def hello(name="Bạn"):
       print(f"Hi {name}")
   
   hello()           # Hi Bạn
   hello("Tuấn")     # Hi Tuấn

3️⃣ NHIỀU THAM SỐ:
   def add(a, b):
       return a + b
   
   result = add(5, 3)  # 8

4️⃣ RETURN - TRẢ VỀ GIÁ TRỊ:
   def calculate(x, y):
       sum_val = x + y
       return sum_val  # Trả về kết quả
   
   Hàm không có return thì trả về None

💡 MẸO: Tên hàm nên mô tả rõ chức năng của nó!
                """
            }
        }
        
        print_color("\n📚 CÁC BÀI HỌC CƠ BẢN:", Colors.HEADER)
        for key, lesson in lessons.items():
            print(f"{key}. {lesson['title']}")
        
        choice = input("\nChọn bài học (1-3) hoặc 0 để quay lại: ").strip()
        if choice in lessons:
            print_color(lessons[choice]['content'], Colors.GREEN)
            self.completed_lessons.append(lessons[choice]['title'])
            self.score += 10
            input("\nNhấn Enter để tiếp tục...")
        return choice != "0"
    
    def practice_coding(self):
        """Phần luyện tập viết code"""
        exercises = [
            {
                "title": "Bài 1: Tính tổng hai số",
                "problem": "Viết hàm cộng hai số và trả về kết quả",
                "solution": """
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8
                """
            },
            {
                "title": "Bài 2: Kiểm tra số chẵn lẻ",
                "problem": "Viết hàm kiểm tra số có phải chẵn không",
                "solution": """
def is_even(n):
    return n % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False
                """
            },
            {
                "title": "Bài 3: Tính giai thừa",
                "problem": "Viết hàm tính giai thừa của số n (n!)",
                "solution": """
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
                """
            }
        ]
        
        print_color("\n💻 LUYỆN TẬP VIẾT CODE:", Colors.HEADER)
        for idx, ex in enumerate(exercises, 1):
            print(f"{idx}. {ex['title']}")
        
        choice = input("\nChọn bài (1-3) hoặc 0 để quay lại: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= 3:
            idx = int(choice) - 1
            print(f"\n📝 {exercises[idx]['title']}")
            print(f"Yêu cầu: {exercises[idx]['problem']}")
            print("\n✅ Giải pháp tham khảo:")
            print_color(exercises[idx]['solution'], Colors.GREEN)
            self.score += 20
            input("\nNhấn Enter để tiếp tục...")
            return True
        return choice != "0"
    
    def problem_solving(self):
        """Phần giải quyết vấn đề"""
        print_color("\n🧩 GIẢI QUYẾT VẤN ĐỀ - HƯỚNG DẪN:", Colors.HEADER)
        print_color("""
1️⃣ ĐỌC VÀ HIỂU VẤN ĐỀ:
   - Đọc kỹ yêu cầu
   - Xác định Input và Output
   - Tìm các ràng buộc

2️⃣ PHÂN TÍCH:
   - Chia nhỏ vấn đề
   - Tìm giải pháp từng phần
   - Vẽ sơ đồ nếu cần

3️⃣ VIẾT CODE:
   - Bắt đầu từ đơn giản
   - Test từng phần
   - Tối ưu hóa

4️⃣ KIỂM TRA:
   - Test với các input khác nhau
   - Tìm trường hợp đặc biệt
   - Đảm bảo kết quả đúng

📌 VÍ DỤ:
Bài toán: Tìm số lớn nhất trong danh sách
→ Input: [3, 7, 2, 9, 1]
→ Output: 9

Giải pháp:
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(max_num) 
        """)
        input("\nNhấn Enter để quay lại...")
        return True
    
    def show_guide(self):
        """Hiển thị hướng dẫn chi tiết"""
        guides = {
            "1": ("Comment trong Python", """
# Đây là comment một dòng
# Dùng # để thêm ghi chú

\"\"\"
Đây là comment nhiều dòng
Dùng ba dấu ngoặc kép để comment
nhiều dòng cùng một lúc
\"\"\"
            """),
            "2": ("F-string - Định dạng chuỗi", """
name = "Python"
age = 30

# Cách cũ:
print("Tên: " + name + ", Tuổi: " + str(age))

# Cách mới (f-string):
print(f"Tên: {name}, Tuổi: {age}")

# Với phép toán:
print(f"Năm sau sẽ {age + 1} tuổi")
            """),
            "3": ("List Comprehension", """
# Tạo danh sách bình thường:
squares = []
for i in range(5):
    squares.append(i ** 2)

# Dùng List Comprehension (ngắn gọn hơn):
squares = [i ** 2 for i in range(5)]
# [0, 1, 4, 9, 16]

# Với điều kiện:
even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
            """)
        }
        
        print_color("\n📝 HƯỚNG DẪN CHI TIẾT:", Colors.HEADER)
        for key, (title, _) in guides.items():
            print(f"{key}. {title}")
        
        choice = input("\nChọn hướng dẫn (1-3) hoặc 0 để quay lại: ").strip()
        if choice in guides:
            print(f"\n{'='*50}")
            print_color(guides[choice][0].upper(), Colors.BOLD)
            print(f"{'='*50}\n")
            print_color(guides[choice][1], Colors.GREEN)
            self.score += 5
            input("\nNhấn Enter để tiếp tục...")
            return True
        return choice != "0"
    
    def show_progress(self):
        """Hiển thị tiến độ học tập"""
        elapsed = (datetime.now() - self.start_time).total_seconds() / 60
        progress_card = f"""
╔════════════════════════════════════════════════════════════════╗
║               {Colors.GREEN}{Colors.BOLD}📊 TIẾN ĐỘ HỌC TẬP CỦA BẠN{Colors.ENDC}                     ║
╠════════════════════════════════════════════════════════════════╣
║ Tên học viên: {Colors.CYAN}{self.user_name:<45}{Colors.ENDC} ║
║ Điểm tích lũy: {Colors.CYAN}{self.score:<44}{Colors.ENDC} ║
║ Thời gian học: {Colors.CYAN}{elapsed:.1f} phút{' '*(40-len(str(int(elapsed))))}{Colors.ENDC} ║
║ Bài học hoàn thành: {Colors.CYAN}{len(self.completed_lessons):<36}{Colors.ENDC} ║
╠════════════════════════════════════════════════════════════════╣
║ Các bài học đã hoàn thành:                                     ║
"""
        print(progress_card)
        
        if self.completed_lessons:
            for i, lesson in enumerate(self.completed_lessons, 1):
                print(f"║ {i}. {Colors.GREEN}✓ {lesson:<52}{Colors.ENDC} ║")
        else:
            print(f"║ {Colors.WARNING}Chưa có bài học nào hoàn thành{Colors.ENDC}                         ║")
        
        print("╚════════════════════════════════════════════════════════════════╝")
        input("\nNhấn Enter để tiếp tục...")
    
    def run(self):
        """Chạy chương trình chính"""
        while True:
            self.show_menu()
            choice = input("Chọn tùy chọn (1-6): ").strip()
            
            if choice == "1":
                if self.basic_lessons():
                    continue
            elif choice == "2":
                if self.practice_coding():
                    continue
            elif choice == "3":
                if self.problem_solving():
                    continue
            elif choice == "4":
                if self.show_guide():
                    continue
            elif choice == "5":
                self.show_progress()
            elif choice == "6":
                print_color(f"\n👋 Tạm biệt {self.user_name}! Hẹn gặp lại! 🎓", Colors.BOLD)
                print_color(f"   Bạn đã học được {self.score} điểm! Tiếp tục cố gắng!", Colors.GREEN)
                break
            else:
                print_color("❌ Lựa chọn không hợp lệ. Vui lòng chọn từ 1-6!", Colors.FAIL)


def main():
    """Hàm chính"""
    print_color("╔════════════════════════════════════════════════════════════════╗", Colors.HEADER)
    print_color("║   🎓 TRỢ LÝ HỌC TẬP PYTHON - PYTHON LEARNING ASSISTANT 🎓     ║", Colors.HEADER)
    print_color("╚════════════════════════════════════════════════════════════════╝\n", Colors.HEADER)
    
    user_name = input("Xin chào! Tên của bạn là gì? ").strip()
    if not user_name:
        user_name = "Học viên"
    
    assistant = PythonLearningAssistant(user_name)
    assistant.run()


if __name__ == "__main__":
    main()
