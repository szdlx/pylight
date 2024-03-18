import cv2
import rospy
from std_msgs.msg import Float32
import numpy as np 
import time
import yaml
# 定义红灯、绿灯和橙灯的颜色值
RED = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (0, 165, 255)  # 橙色
last_msg_time = 0
# 全局变量，用于存储图像数据
red_black_image = None
yellow_black_image = None
green_black_image = None
def load_images():
    global red_black_image
    global yellow_black_image
    global green_black_image
    red_black_image = cv2.imread("red_black_image.jpeg")
    yellow_black_image = cv2.imread("yellow_black_image.jpeg")
    green_black_image = cv2.imread("green_black_image.jpeg")

def draw_traffic_light(color, text):
    img = np.zeros((260, 200, 3), dtype=np.uint8)  
    
    cv2.rectangle(img, (10, 10), (190, 250), (50, 50, 50), -1)  # 灰色背景框
    
    cv2.circle(img, (100, 100), 70, (255, 255, 255), -1)  # 白色圆
    
    cv2.circle(img, (100, 100), 60, color, -1)  # 灯的颜色
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, 0.6, 1)[0]  # 设置更小的字体大小
    text_x = (img.shape[1] - text_size[0]) // 2
    text_y = 220
    cv2.putText(img, text, (text_x, text_y), font, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.imshow("distance Light", img)
    cv2.waitKey(1)


def callback(data):
    global last_msg_time
    signal_value = data.data
    last_msg_time = time.time()
    # 重新加载YAML文件以获取最新的阈值
    with open("thresholds.yaml", 'r') as stream:
        thresholds = yaml.safe_load(stream)
    if signal_value < thresholds['danger']:
        cv2.putText(red_black_image, "Distance: Danger", (10, red_black_image.shape[0]-11), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.imshow("Traffic Light", red_black_image)
        cv2.waitKey(100)  # 等待100毫秒
    elif signal_value < thresholds['warning']:
        cv2.putText(yellow_black_image, "Distance: warning", (10, yellow_black_image.shape[0]-11), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)       
        cv2.imshow("Traffic Light", yellow_black_image)
        cv2.waitKey(100)  # 等待100毫秒
    else:
        cv2.putText(green_black_image, "Distance: safe", (10, yellow_black_image.shape[0]-11), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)   
        cv2.imshow("Traffic Light", green_black_image)
        cv2.waitKey(100)  # 等待100毫秒

def main():
    rospy.init_node('traffic_light_node', anonymous=True)
    rospy.Subscriber("/detection_info", Float32, callback)
    load_images()
    rate = rospy.Rate(10)  
    while not rospy.is_shutdown():
        rospy.sleep(0.1)
        current_time = time.time()
            # 重新加载YAML文件以获取最新的阈值
        # with open("thresholds.yaml", 'r') as stream:
        #     thresholds = yaml.safe_load(stream)
        # if current_time - last_msg_time > thresholds['interval']:
        #     draw_traffic_light(GREEN, "Distance: Safe") 
        rate.sleep()

if __name__ == '__main__':
    main()
