from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QApplication
import sys

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Account Registration")
        self.setGeometry(400, 200, 400, 400)

        self.title_label = QLabel("Account Registration Form", self)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.title_label.move(120, 10)

        # LABELS
        self.first_name_label = QLabel("First Name:", self)
        self.last_name_label = QLabel("Last Name:", self)
        self.username_label = QLabel("Username:", self)
        self.password_label = QLabel("Password:", self)
        self.email_label = QLabel("Email Address:", self)
        self.contact_label = QLabel("Contact Number:", self)

        # BUTTONS
        self.submit_button = QPushButton("Submit", self)
        self.clear_button = QPushButton("Clear", self)

        # INFO BAR
        self.first_name_bar = QLineEdit(self)
        self.last_name_bar = QLineEdit(self)
        self.username_bar = QLineEdit(self)
        self.password_bar = QLineEdit(self)
        self.email_bar = QLineEdit(self)
        self.contact_bar = QLineEdit(self)

        # PASS FILTER/BAR
        self.password_bar.setEchoMode(QLineEdit.Password)

        self.first_name_label.move(30, 50)
        self.first_name_bar.move(150, 50)

        self.last_name_label.move(30, 90)
        self.last_name_bar.move(150, 90)

        self.username_label.move(30, 130)
        self.username_bar.move(150, 130)

        self.password_label.move(30, 170)
        self.password_bar.move(150, 170)

        self.email_label.move(30, 210)
        self.email_bar.move(150, 210)

        self.contact_label.move(30, 250)
        self.contact_bar.move(150, 250)

        self.submit_button.move(100, 300)
        self.clear_button.move(200, 300)

        #BUTTON TO FUNCTIONS
        self.submit_button.clicked.connect(self.submit_form)
        self.clear_button.clicked.connect(self.clear_form)

    def submit_form(self):
        print("Form submitted")

    def clear_form(self):
        self.first_name_bar.clear()
        self.last_name_bar.clear()
        self.username_bar.clear()
        self.password_bar.clear()
        self.email_bar.clear()
        self.contact_bar.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = RegistrationForm()
    form.show()
    sys.exit(app.exec_())
