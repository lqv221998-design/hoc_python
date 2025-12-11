import smtplib
from email.mime.text import MIMEText
"""
Các bước gửi email
1. khởi tạo kết nối
2. nâng cấp kết nối an toàn
3. đăng nhập
4. gửi mail
5. ngắt kết nối

"""
#1. khởi tạo kết nối
server = smtplib.SMTP("smtp.gmail.com", 587)

#2. nâng cấp kết nối an toàn
server.starttls()

#3. đăng nhập
server.local_hostname(smtp_login_email, smtp_login_password)

#4. gửi mail
    #4.1 các thành phần trong mail
        # From, to, tiêu đề, nội dung
from_email = "lqv221998@gmail.com"
to_email_list = ["vu.32232060tpe2@oude.edu.vn"]
subject = "Nội dung của tiêu đề: gửi mail tự động"
body = "Gửi mail tự động"
msg = MIMEText(body)
msg["subject"] = subject
msg["From"] = from_email
msg["to"] = ",".join(to_email_list)
server.sendmail(from_email, to_email_list, msg.as_string())

#5. ngắt kết nối 
server.quit()




