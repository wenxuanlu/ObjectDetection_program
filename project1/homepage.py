import os
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox, QLineEdit, QProgressBar, QHBoxLayout, QWidget, QFileDialog, QMenuBar, QStatusBar, QDialog, QListWidget, QListWidgetItem
from PySide6.QtCore import Qt, QFile, QCoreApplication, Slot, QSize, QFileInfo
from PySide6.QtGui import QPalette, QLinearGradient, QColor, QPixmap
from PySide6.QtUiTools import QUiLoader


class VerificationCodeWindow(QMainWindow):
    def __init__(self, homepage):
        super().__init__()
        self.homepage = homepage  # 保存 Homepage 的引用
        self.setWindowTitle("VerificationCode")
        self.setGeometry(300, 310, 1200, 1000)
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.pushButton = QPushButton("开始识别", self.central_widget)
        self.pushButton.setGeometry(720, 540, 81, 40)
        
        self.label = QLabel("请上传图片", self.central_widget)
        self.label.setGeometry(420, 70, 700, 450)
        self.label.setAlignment(Qt.AlignCenter)  # 设置文本居中显示
        self.label.setStyleSheet("border: 1px solid black;")

        
        
        self.list_widget = QListWidget(self.central_widget)
        self.list_widget.setGeometry(80, 100, 250, 600)
        self.list_widget.itemClicked.connect(self.onListItemClicked)  # 连接列表项的点击事件到槽函数
        
  


        
        self.progress_layout = QHBoxLayout()
        self.progress_widget = QWidget(self.central_widget)
        self.progress_widget.setGeometry(580, 580, 341, 40)
        self.progress_widget.setLayout(self.progress_layout)
        
        self.label_3 = QLabel("识别进度", self.progress_widget)
        self.progressBar = QProgressBar(self.progress_widget)
        self.progressBar.setValue(0)
        self.progress_layout.addWidget(self.label_3)
        self.progress_layout.addWidget(self.progressBar)
        
        self.path_layout = QHBoxLayout()
        self.path_widget = QWidget(self.central_widget)
        self.path_widget.setGeometry(520, 10, 421, 40)
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
        self.result_widget.setGeometry(580, 630, 291, 80)
        self.result_widget.setLayout(self.result_layout)
        
        self.label_4 = QLabel("识别结果：", self.result_widget)
        self.lineEdit_2 = QLineEdit(self.result_widget)
        self.result_layout.addWidget(self.label_4)
        self.result_layout.addWidget(self.lineEdit_2)
        
        self.return_button = QPushButton("返回", self.central_widget)
        self.return_button.setGeometry(730, 700, 81, 40)
        self.return_button.clicked.connect(self.returnToHomepage)  # 连接返回按钮的点击事件
    '''
    self.resizeEvent(None)  # 初始化组件的大小和位置

    def resizeEvent(self, event):
        self.adjustComponents()

    def adjustComponents(self):
        # 根据窗口大小调整组件的大小和位置
        window_width = self.central_widget.width()
        window_height = self.central_widget.height()

        # 调整按钮的位置
        button_width = 81
        button_height = 40
        button_x = int((window_width - button_width) / 1.5)
        button_y = int(window_height * 0.7)
        self.pushButton.setGeometry(button_x, button_y, button_width, button_height)

        # 调整 Label 的位置
        label_width = 361
        label_height = 211
        label_x = int((window_width - label_width) / 1.5)
        label_y = int(window_height * 0.15)
        self.label.setGeometry(label_x, label_y, label_width, label_height)

        # 调整进度条和路径输入框的位置
        progress_width = 341
        progress_height = 40
        progress_x = int((window_width - progress_width) / 1.5)
        progress_y = int(window_height * 0.6)
        self.progress_widget.setGeometry(progress_x, progress_y, progress_width, progress_height)

        path_width = 421
        path_height = 40
        path_x = int((window_width - path_width) / 1.5)
        path_y = int(window_height * 0.05)
        self.path_widget.setGeometry(path_x, path_y, path_width, path_height)

        # 调整结果和返回按钮的位置
        result_width = 291
        result_height = 40
        result_x = int((window_width - result_width) / 1.5)
        result_y = int(window_height * 0.75)
        self.result_widget.setGeometry(result_x, result_y, result_width, result_height)

        return_width = 81
        return_height = 40
        return_x = int((window_width - return_width) / 1.5)
        return_y = int(window_height * 0.85)
        self.return_button.setGeometry(return_x, return_y, return_width, return_height)
    '''
        
    @Slot()
    def returnToHomepage(self):
        self.close()  # 关闭当前窗口
        self.homepage.show()  # 显示 Homepage 窗口

    
    @Slot(QListWidgetItem)
    def onListItemClicked(self, item):
        file_path = item.data(Qt.UserRole)  # 获取保存在 item 的 UserRole 中的文件路径
        if file_path:
            self.lineEdit.setText(f"选择的图片路径：{file_path}")  # 在第一个 QLineEdit 中显示选择的图片路径

            # 加载图片并显示在 Label 组件中
            pixmap = QPixmap(file_path)
            scaled_pixmap = pixmap.scaled(QSize(650, 400), Qt.KeepAspectRatio)  # 调整图片尺寸
            self.label.setPixmap(scaled_pixmap)

            # 保存图片路径
            self.selected_image_path = file_path

    @Slot()
    def selectImage(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)  # 设置文件选择对话框模式为选择任意文件
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.jpeg);;All Files (*)")  # 设置文件过滤器，只显示图片文件
        result = file_dialog.exec_()  # 打开文件选择对话框并获取结果
        if result == QDialog.Accepted:
            selected_files = file_dialog.selectedFiles()  # 获取选择的文件路径列表
            if selected_files:
                file_path = selected_files[0]  # 获取第一个选择的文件路径
                file_info = QFileInfo(file_path)
                if file_info.isFile():  # 判断是否为文件
                    if file_info.suffix().lower() in ["png", "xpm", "jpg", "jpeg"]:
                        self.lineEdit.setText(file_path)  # 将图片路径显示在文本框中

                        # 加载图片并显示在 Label 组件中
                        pixmap = QPixmap(file_path)
                        scaled_pixmap = pixmap.scaled(QSize(221, 221), Qt.KeepAspectRatio)  # 调整图片尺寸
                        self.label.setPixmap(scaled_pixmap)

                        # 保存图片路径
                        self.selected_image_path = file_path

                        # 清空之前选择的文件夹路径
                        self.selected_directory = None

                        self.lineEdit.setText(f"选择的图片路径：{file_path}")  # 在第一个 QLineEdit 中显示选择的图片路径
                elif file_info.isDir():  # 判断是否为文件夹

                    self.selected_directory = file_path

                    self.lineEdit.setText(f"选择的文件夹路径：{file_path}")  # 在第一个 QLineEdit 中显示选择的文件夹路径

                    # 清空 QListWidget 中的项
                    self.list_widget.clear()

                    # 加载文件夹中的图片文件并添加到 QListWidget 中
                    image_files = self.getImageFilesFromDirectory(file_path)
                    for image_file in image_files:
                        item = QListWidgetItem(os.path.basename(image_file))
                        item.setData(Qt.UserRole, image_file)  # 保存文件路径到 item 的 UserRole 中
                        self.list_widget.addItem(item)

    def getImageFilesFromDirectory(self, directory):
        image_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(('.png', '.xpm', '.jpg', '.jpeg')):
                    image_files.append(os.path.join(root, file))
        return image_files



class ContainerInspectionWindow(QMainWindow):
    def __init__(self, homepage):
        super().__init__()
        self.homepage = homepage  # 保存 Homepage 的引用
        self.setWindowTitle("ContainerInspection")
        self.setGeometry(300, 310, 1200, 1000)
        self.centralwidget = QWidget(self)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)  # 设置 central widget



        self.list_widget = QListWidget(self.centralwidget)
        self.list_widget.setGeometry(80, 100, 250, 600)
        self.list_widget.itemClicked.connect(self.onListItemClicked)  # 连接列表项的点击事件到槽函数

        

        self.label = QLabel("图片路径", self.centralwidget)
        self.label.setGeometry(400, 30, 54, 40)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(460, 40, 411, 20)

        self.pushButton = QPushButton("选择图片", self.centralwidget)
        self.pushButton.setGeometry(880, 30, 81, 40)
        self.pushButton.clicked.connect(self.selectImage)  # 连接选择图片按钮的点击事件


        self.label_2 = QLabel("请上传您的图片", self.centralwidget)
        self.label_2.setGeometry(350, 70, 350, 300)
        self.label_2.setStyleSheet("border: 1px solid black;")

        self.label_3 = QLabel("箱号标记图片", self.centralwidget)
        self.label_3.setGeometry(730, 70, 350, 300)
        self.label_3.setStyleSheet("border: 1px solid black;")

        self.pushButton_2 = QPushButton("开始识别", self.centralwidget)
        self.pushButton_2.setGeometry(670, 440, 100, 40)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(470, 500, 611, 40)
        self.progressBar.setValue(0)

        self.label_4 = QLabel("识别结果", self.centralwidget)
        self.label_4.setGeometry(600, 590, 51, 40)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(680, 590, 180, 40)

        self.pushButton_3 = QPushButton("返回", self.centralwidget)
        self.pushButton_3.setGeometry(670, 710, 100, 40)
        self.pushButton_3.clicked.connect(self.returnToHomepage)  # 连接返回按钮的点击事件

        self.label_5 = QLabel("识别进度", self.centralwidget)
        self.label_5.setGeometry(400, 500, 54, 40)

        self.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(0, 0, 514, 40)
        self.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        
        self.original_size = self.size()  # 记录原始窗口大小
    

    @Slot(QListWidgetItem)
    def onListItemClicked(self, item):
        file_path = item.data(Qt.UserRole)  # 获取保存在 item 的 UserRole 中的文件路径
        if file_path:
            self.lineEdit.setText(f"选择的图片路径：{file_path}")  # 在第一个 QLineEdit 中显示选择的图片路径

            # 加载图片并显示在 Label 组件中
            pixmap = QPixmap(file_path)
            scaled_pixmap = pixmap.scaled(QSize(330, 280), Qt.KeepAspectRatio)  # 调整图片尺寸
            self.label_2.setPixmap(scaled_pixmap)

            # 保存图片路径
            self.selected_image_path = file_path
    


    @Slot()
    def selectImage(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)  # 设置文件选择对话框模式为选择任意文件
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.jpeg);;All Files (*)")  # 设置文件过滤器，只显示图片文件
        result = file_dialog.exec_()  # 打开文件选择对话框并获取结果
        if result == QDialog.Accepted:
            selected_files = file_dialog.selectedFiles()  # 获取选择的文件路径列表
            if selected_files:
                file_path = selected_files[0]  # 获取第一个选择的文件路径
                file_info = QFileInfo(file_path)
                if file_info.isFile():  # 判断是否为文件
                    if file_info.suffix().lower() in ["png", "xpm", "jpg", "jpeg"]:
                        self.lineEdit.setText(file_path)  # 将图片路径显示在文本框中

                        # 加载图片并显示在 Label 组件中
                        pixmap = QPixmap(file_path)
                        scaled_pixmap = pixmap.scaled(QSize(330,280), Qt.KeepAspectRatio)  # 调整图片尺寸
                        self.label_2.setPixmap(scaled_pixmap)

                        # 保存图片路径
                        self.selected_image_path = file_path

                        # 清空之前选择的文件夹路径
                        self.selected_directory = None

                        self.lineEdit.setText(f"选择的图片路径：{file_path}")  # 在第一个 QLineEdit 中显示选择的图片路径
                elif file_info.isDir():  # 判断是否为文件夹

                    self.selected_directory = file_path

                    self.lineEdit.setText(f"选择的文件夹路径：{file_path}")  # 在第一个 QLineEdit 中显示选择的文件夹路径

                    # 清空 QListWidget 中的项
                    self.list_widget.clear()

                    # 加载文件夹中的图片文件并添加到 QListWidget 中
                    image_files = self.getImageFilesFromDirectory(file_path)
                    for image_file in image_files:
                        item = QListWidgetItem(os.path.basename(image_file))
                        item.setData(Qt.UserRole, image_file)  # 保存文件路径到 item 的 UserRole 中
                        self.list_widget.addItem(item)

    def getImageFilesFromDirectory(self, directory):
        image_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(('.png', '.xpm', '.jpg', '.jpeg')):
                    image_files.append(os.path.join(root, file))
        return image_files



    @Slot()
    def returnToHomepage(self):
        self.close()  # 关闭当前窗口
        self.homepage.show()  # 显示 Homepage 窗口


    
class Homepage:
    def handleCalc1(self):
        self.homepage.hide()  # 隐藏 Homepage 窗口
        self.reg1 = VerificationCodeWindow(self.homepage)
        self.reg1.show()
        

    def handleCalc2(self):
        self.homepage.hide()  # 隐藏 Homepage 窗口
        self.container_inspection_window = ContainerInspectionWindow(self.homepage)
        self.container_inspection_window.show()


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
