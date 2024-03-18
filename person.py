import cv2
import numpy as np

# 读取图像
image_path = "300.jpeg"
image = cv2.imread(image_path)

# 转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 创建一个与灰度图像相同大小的数组，用于绘制黄色和黑色
yellow_black_image = np.zeros_like(image)

# 将像素值在0到70之间的部分设置为黄色
yellow_black_image[(gray_image >= 0) & (gray_image <= 70)] = (0, 255, 255)

# 显示结果图像
cv2.imshow("Yellow and Black Image", yellow_black_image)

# 保存结果图像
cv2.imwrite("yellow_black_image.jpeg", yellow_black_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
