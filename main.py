import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from lib.main_ui import Ui_MainWindow


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # build ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
