import cv2
import numpy as np 
import time

def draw_traffic_light(color, text):
    img = np.zeros((260, 200, 3), dtype=np.uint8)  
    
    cv2.rectangle(img, (10, 10), (190, 250), (50, 50, 50), -1)  # 灰色背景框
    
    cv2.circle(img, (100, 100), 70, (255, 255, 255), -1)  # 白色圆
    
    current_time = time.time()
    if color == (0, 0, 255) and int(current_time * 2) % 2 == 0:  # 如果是红色灯，且当前时间的整数部分*2为偶数
        cv2.circle(img, (100, 100), 60, color, -1)  # 红灯显示
    else:
        cv2.circle(img, (100, 100), 60, color, -1)  # 其他颜色灯

    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, 0.6, 1)[0]  # 设置字体大小
    text_x = (img.shape[1] - text_size[0]) // 2
    text_y = 220
    cv2.putText(img, text, (text_x, text_y), font, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.imshow("Traffic Light", img)
    cv2.waitKey(1000)  # 每秒刷新一次

# 测试代码
while True:
    draw_traffic_light((0, 0, 255), "Distance: Danger")  # 红灯
    time.sleep(10)  # 保持红灯状态10秒
