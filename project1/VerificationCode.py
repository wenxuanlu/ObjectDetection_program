from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class Stats:
    def __init__(self):
        # 获取 UI 文件的绝对路径
        ui_file_path = '/Users/jennifierx/Desktop/python/project1/untitled.ui'  # 将路径替换为实际的 UI 文件路径

        # 打开 UI 文件
        ui_file = QFile(ui_file_path)
        if not ui_file.open(QFile.ReadOnly):
            QMessageBox.critical(None, 'Error', 'Could not open UI file.')
            return

        # 创建一个 QUiLoader 对象并加载 UI 定义
        ui_loader = QUiLoader()
        self.ui = ui_loader.load(ui_file)

        # 关闭 UI 文件
        ui_file.close()

        #self.ui.button.clicked.connect(self.handleCalc)

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec()


       
            