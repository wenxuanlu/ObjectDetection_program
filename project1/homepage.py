from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox, QLineEdit, QProgressBar, QHBoxLayout, QWidget, QFileDialog
from PySide6.QtCore import Qt, QFile, QCoreApplication, Slot, QSize
from PySide6.QtGui import QPalette, QLinearGradient, QColor, QPixmap
from PySide6.QtUiTools import QUiLoader

class VerificationCodeWindow(QMainWindow):
    def __init__(self, homepage):
        super().__init__()
        self.homepage = homepage  # 保存 Homepage 的引用
        self.setWindowTitle("VerificationCode")
        self.setGeometry(300, 310, 517, 509)
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.pushButton = QPushButton("开始识别", self.central_widget)
        self.pushButton.setGeometry(140, 350, 81, 40)
        
        self.label = QLabel("请上传图片", self.central_widget)
        self.label.setGeometry(20, 70, 361, 211)
        self.label.setAlignment(Qt.AlignCenter)  # 设置文本居中显示
        self.label.setStyleSheet("border: 1px solid black;")


        
        self.progress_layout = QHBoxLayout()
        self.progress_widget = QWidget(self.central_widget)
        self.progress_widget.setGeometry(20, 310, 341, 40)
        self.progress_widget.setLayout(self.progress_layout)
        
        self.label_3 = QLabel("识别进度", self.progress_widget)
        self.progressBar = QProgressBar(self.progress_widget)
        self.progressBar.setValue(24)
        self.progress_layout.addWidget(self.label_3)
        self.progress_layout.addWidget(self.progressBar)
        
        self.path_layout = QHBoxLayout()
        self.path_widget = QWidget(self.central_widget)
        self.path_widget.setGeometry(20, 10, 421, 40)
        self.path_widget.setLayout(self.path_layout)
        
        self.label_2 = QLabel("图片路径", self.path_widget)
        self.lineEdit = QLineEdit(self.path_widget)
        self.pushButton_2 = QPushButton("选择图片", self.path_widget)
        self.pushButton_2.clicked.connect(self.selectImage)  # 连接选择图片按钮的点击事件
        self.path_layout.addWidget(self.label_2)
        self.path_layout.addWidget(self.lineEdit)
        self.path_layout.addWidget(self.pushButton_2)
        
        self.result_layout = QHBoxLayout()
        self.result_widget = QWidget(self.central_widget)
        self.result_widget.setGeometry(20, 390, 291, 40)
        self.result_widget.setLayout(self.result_layout)
        
        self.label_4 = QLabel("识别结果：", self.result_widget)
        self.lineEdit_2 = QLineEdit(self.result_widget)
        self.result_layout.addWidget(self.label_4)
        self.result_layout.addWidget(self.lineEdit_2)
        
        self.return_button = QPushButton("返回", self.central_widget)
        self.return_button.setGeometry(20, 450, 81, 40)
        self.return_button.clicked.connect(self.returnToHomepage)  # 连接返回按钮的点击事件

    @Slot()
    def returnToHomepage(self):
        self.close()  # 关闭当前窗口
        self.homepage.show()  # 显示 Homepage 窗口

    @Slot()
    def selectImage(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "选择图片")  # 打开文件选择对话框
        self.lineEdit.setText(image_path)

        # 加载图片并显示在 TextLabel 组件中
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(QSize(361, 211), Qt.KeepAspectRatio)  # 调整图片尺寸
        self.label.setPixmap(scaled_pixmap)

class Homepage:
    def handleCalc1(self):
        self.homepage.hide()  # 隐藏 Homepage 窗口
        self.reg1 = VerificationCodeWindow(self.homepage)
        self.reg1.show()
        

    def handleCalc2(self):
        self.homepage.hide()  # 隐藏 Homepage 窗口
        self.reg2 = ContainerInspectionWindow(self.homepage)
        self.reg2.show()

    def show(self):
        self.app.exec()

    def __init__(self):
        self.app = QApplication([])
        self.homepage = QMainWindow()
        self.homepage.setWindowTitle('Object Detection')
        self.homepage.resize(517, 509)
        self.homepage.move(300, 310)
        gradient = QLinearGradient(0, 0, 0, self.homepage.height())
        gradient.setColorAt(0, QColor(130, 130, 130))
        gradient.setColorAt(1, QColor(42, 68, 86))
        palette = QPalette()
        palette.setBrush(self.homepage.backgroundRole(), gradient)
        self.homepage.setPalette(palette)

        self.label = QLabel('Object Detection System', self.homepage)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(50, 50, 400, 100)
        self.label.setStyleSheet("font-size: 30px; color: white;")

        self.button1 = QPushButton('验证码识别', self.homepage)
        self.button1.resize(150, 50)
        self.button1.move(175, 230)
        self.button1.clicked.connect(self.handleCalc1)
        self.button1.setStyleSheet("background-color: transparent; color: white;font-size:20px;font-weight:bold;")

        self.button2 = QPushButton('港口箱号识别', self.homepage)
        self.button2.resize(150, 50)
        self.button2.move(175, 360)
        self.button2.clicked.connect(self.handleCalc2)
        self.button2.setStyleSheet("background-color: transparent; color: white;font-size:20px;font-weight:bold;")

        self.homepage.show()

homepage = Homepage()
homepage.show()
