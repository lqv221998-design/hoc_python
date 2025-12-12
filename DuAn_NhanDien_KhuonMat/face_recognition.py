import cv2
import dlib

#read the image
img = cv2.imread("vu.png")
(h, w, d) = img.shape
#Chuyển bức ảnh thành dạng đen trắng (), bỏ qua màu sắc


#show image
#winname: đặt tên cho app
cv2.imshow(winname="face recognition App", mat=img)
r = 300.0 / w 
dim = (300, int(h * r))
cv2.resize(img, dim)

#câu lệnh đóng ảnh sau khi bấm 1 nút bất kỳ
cv2.waitKey(delay=0)

#sau khi thực hiện lệnh trên sẽ xuống dòng này và đóng cửa sổ
cv2.destroyAllWindows()