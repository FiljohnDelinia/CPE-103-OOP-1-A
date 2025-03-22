import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "PyQt line Edit"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('media_social_tiktok_icon_124256.ico'))

        self.textboxlbl = QLabel("Hello World! ", self)
        self.textboxlbl.move(125, 25)

        self.textboxlbl1 = QLabel("This program is written in Pycharm ", self)
        self.textboxlbl1.move(68, 50)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())