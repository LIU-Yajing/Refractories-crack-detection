import cv2
import numpy as np
#读取原始图片
src = cv2.imread('111sharped03.jpg')

laplacian = cv2.Laplacian(src, cv2.CV_32F, ksize=5)
#print('3. 拉普拉斯算子过滤。')
Laplacian_img = cv2.convertScaleAbs(laplacian)

cv2.imwrite("114laplacian05.jpg", Laplacian_img)
#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()