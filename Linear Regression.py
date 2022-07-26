from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt
# height (cm)
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T
#-------------------------------------
# Tạo ma trận X
one = np.ones_like(X)
Xbar= np.concatenate((one, X),axis=1)#gộp 2 ma trận lại với nhau với axis=1 là 2 ma trận dọc

# tính trọng số của đường thẳng
A=np.dot(Xbar.T,Xbar)
b=np.dot(Xbar.T,y)
w = np.dot(np.linalg.pinv(A), b)
print('w =',w)

#chuẩn bị vẽ hàm
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(145, 185, 2)#trả về khoản giá trị cần vẽ hàm
y0 = w_0 + w_1*x0

#vẽ hàm
plt.plot(X, y, 'ro')     # dữ liệu ro là red điểm trên đồ thị là chấm, có thể thay đổi thành g: green, b: blue +, x, s để thành dấu +, x, ô vuông
plt.plot(x0, y0)               # đường dự đoán
plt.axis([140, 190, 45, 75])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

#dự đoán cân nặng khi có chiều cao
y1 = 158*w_1 + w_0
print(u'%.2f'%(y1))
