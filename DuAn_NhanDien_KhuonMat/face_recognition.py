#Cài đặt pip install CMake trước
# cài pip install https://github.com/omwaman1/dlib/releases/download/dlib/dlib-19.24.99-cp313-cp313-win_amd64.whl
# cài pip install --upgrade pip setuptools wheel
#Cài đặt thư viện: pip install opencv-python
#Cài đặt thư viện: pip install dlib

import cv2
import dlib

#read the image
img = cv2.imread("vu.png")

#Thay đổi kích thước ảnh
(h, w, d) = img.shape
r = 800.0 / w 
dim = (800, int(h * r))
img = cv2.resize(img,dim)

#Chuyển bức ảnh thành dạng đen trắng (), bỏ qua màu sắc
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#dlib: là modun trí tuệ nhân tạo giúp nhận diện khuôn mặt 
nhan_dien = dlib.get_frontal_face_detector()

faces = nhan_dien(gray_image)
print(len(faces))
for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
    cv2.rectangle(img=gray_image, pt1=(x1,y1), pt2=(x2,y2), color=(255,0, 0), thickness=3)
    
#show image
#winname: đặt tên cho app
# ---cv2.imshow(winname="face recognition App", mat=img)--- Code cũ lấy đúng màu ảnh
cv2.imshow(winname="face recognition App", mat= gray_image)   #Code mới chuyển thành ảnh đen trắng


#câu lệnh đóng ảnh sau khi bấm 1 nút bất kỳ
cv2.waitKey(delay=0)

#sau khi thực hiện lệnh trên sẽ xuống dòng này và đóng cửa sổ
cv2.destroyAllWindows()