import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from registration import RegistrationForm

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Account Registration System"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(200, 200, 450, 400)
        self.setWindowIcon(QIcon('account-circle_119476.ico'))

        self.registration_form = RegistrationForm()
        self.setCentralWidget(self.registration_form)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = App()
    sys.exit(app.exec_())