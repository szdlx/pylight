from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer
class TrafficLight(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Traffic Light')
        self.show()
        
        self.timer = QTimer(self) 
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)  # 每秒更新一次
        
        self.color = 'red'  # 初始状态为红灯
        self.countdown = 10  # 倒计时从10开始
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawTrafficLight(qp)
        qp.end()
    def drawTrafficLight(self, qp):
        if self.color == 'red':
            qp.setBrush(QColor(255, 0, 0))  # 设置画刷为红色
        elif self.color == 'yellow':
            qp.setBrush(QColor(255, 255, 0))  # 设置画刷为黄色
        else:
            qp.setBrush(QColor(0, 255, 0))  # 设置画刷为绿色
            
        qp.drawEllipse(100, 50, 100, 100)  # 画圆
        qp.drawRect(125, 150, 50, 100)  # 画长方形
    def update(self):
        if self.countdown > 0:
            self.countdown -= 1
        else:
            if self.color == 'red':
                self.color = 'green'
            elif self.color == 'yellow':
                self.color = 'red'
            else:
                self.color = 'yellow'
            self.countdown = 10
        self.update()
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
if __name__ == '__main__':
    app = QApplication([])
    tl = TrafficLight()
    app.exec_()