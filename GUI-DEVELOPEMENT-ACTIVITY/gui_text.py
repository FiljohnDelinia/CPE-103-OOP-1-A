import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLineEdit
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt Line Edit"
        self.x = 200  # or left
        self.y = 200  # or top
        self.width = 300
        self.height = 200  # Adjusting the window height for a better fit
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('media_social_tiktok_icon_124256'))  # Make sure the icon exists or replace

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)

        # Resize the textbox to fit the text height and window width
        text_height = 30  # Estimated height for the text
        self.textbox.resize(self.width - 40, text_height)  # Leave some margin (20px on each side)

        # Set text in the textbox
        self.textbox.setText("Set this text value")  # Set default text

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
