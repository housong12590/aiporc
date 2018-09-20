import sys
import os
from config import conf
from PyQt5.QtWidgets import QMainWindow, QApplication
from main_page import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None, ):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.select_file.clicked.connect(self.select_dir)
        self.start.clicked.connect(self.start_click)
        self.is_start = False
        self.init()

    def init(self):
        work_dir = conf.get('work_dir')
        self.work_dir.setText(work_dir)

    def select_dir(self):
        work_dir = QFileDialog.getExistingDirectory(self, "选择工作路径", os.getcwd())
        if work_dir:
            self.work_dir.setText(work_dir)
            conf.put('work_dir', work_dir)

    def start_click(self):
        if self.is_start:
            self.start.setText('开始')
        else:
            self.start.setText('停止')
        self.is_start = not self.is_start


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
