import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from lib.main_ui import Ui_MainWindow
from lib.setup_fct import setup_fct


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # build ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # button method link
        self.ui.pushButton.clicked.connect(self.check_git)

    def check_git(self):
        if setup_fct.is_git_exist():
            self.ui.label_7.setText("OK")
            self.ui.label_7.setStyleSheet("background-color: green;")
        else:
            self.ui.label_7.setText("KO")
            self.ui.label_7.setStyleSheet("background-color: red;")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
