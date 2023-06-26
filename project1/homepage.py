from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QLinearGradient, QColor

class VerificationCodeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('VerificationCode Window')
        self.resize(1000, 600)

class ContainerInspectionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ContainerInspection Window')
        self.resize(1000, 600)

class Homepage:
    def handleCalc1(self):
        self.reg1 = VerificationCodeWindow()
        self.reg1.show()

    def handleCalc2(self):
        self.reg2 = ContainerInspectionWindow()
        self.reg2.show()

    def __init__(self):
        self.app = QApplication([])
        self.window = QMainWindow()
        self.window.setWindowTitle('Object Detection')
        self.window.resize(500, 400)
        self.window.move(300, 310)
        #self.window.setStyleSheet("background-color: darkgreen;")
        # 创建线性渐变对象
        gradient = QLinearGradient(0, 0, 0, self.window.height())
        gradient.setColorAt(0, QColor(130, 130, 130))  # 起始颜色，蓝灰色
        gradient.setColorAt(1, QColor(42, 68, 86))  # 终止颜色，深蓝灰色

        # 创建调色板对象
        palette = QPalette()
        palette.setBrush(self.window.backgroundRole(), gradient)

        # 将调色板设置为窗口的背景
        self.window.setPalette(palette)


        self.label = QLabel('Object Detection System', self.window)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(50, 50, 400, 100)
        self.label.setStyleSheet("font-size: 30px; color: white;")

        self.button1 = QPushButton('验证码识别', self.window)
        self.button1.resize(150, 50)
        self.button1.move(175, 200)
        self.button1.clicked.connect(self.handleCalc1)
        self.button1.setStyleSheet("background-color: transparent; color: white;font-size:20px;font-weight:bold;")

        self.button2 = QPushButton('港口箱号识别', self.window)
        self.button2.resize(150, 50)
        self.button2.move(175, 300)
        self.button2.clicked.connect(self.handleCalc2)
        self.button2.setStyleSheet("background-color: transparent; color: white;font-size:20px;font-weight:bold;")


        self.window.show()
        self.app.exec()

homepage = Homepage()
