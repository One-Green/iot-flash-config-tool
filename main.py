import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from lib.main_ui import Ui_MainWindow
from lib.setup_fct import setup_fct
import colorlog

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter('%(log_color)s%(levelname)s:%(name)s:%(message)s'))
logger = colorlog.getLogger('default-logger')
logger.addHandler(handler)
logger.setLevel(colorlog.DEBUG)


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # build ui
        logger.debug("loading ui")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        logger.debug("ui loaded")

        # handler
        logger.debug("loading handlers classes")
        self.setup_tab = self.InnerSetupTabHandler(ui=self.ui)
        logger.debug("loading handlers classes: done")

        # --- button method link
        # ----- tab: setup
        logger.debug("linking button to actions")
        self.ui.gitCheckButton.clicked.connect(self.setup_tab.check_git)
        self.ui.gitInstallButton.setEnabled(False)
        # ----- Python
        self.ui.pythonCheckButton.clicked.connect(self.setup_tab.check_python)
        self.ui.pythonInstallButton.setEnabled(False)
        # ----- Platform IO
        self.ui.pioCheckButton.clicked.connect(self.setup_tab.check_pio)
        self.ui.pioInstallButton.setEnabled(False)
        logger.debug("linking button to actions done")

    class InnerSetupTabHandler:
        def __init__(self, ui):
            self.ui = ui

        def check_git(self):
            if setup_fct.is_git_exist():
                self.ui.gitStatusLabel.setText("OK")
                self.ui.gitStatusLabel.setStyleSheet("background-color: green;")
            else:
                self.ui.gitStatusLabel.setText("KO")
                self.ui.gitStatusLabel.setStyleSheet("background-color: red;")
                self.ui.gitInstallButton.setEnabled(True)

        def check_python(self):
            if setup_fct.is_python_exist():
                self.ui.pythonStatusLabel.setText("OK")
                self.ui.pythonStatusLabel.setStyleSheet("background-color: green;")
            else:
                self.ui.pythonStatusLabel.setText("KO")
                self.ui.pythonStatusLabel.setStyleSheet("background-color: red;")
                self.ui.pythonInstallButton.setEnabled(True)

        def check_pio(self):
            if setup_fct.is_pio_exist():
                self.ui.pioStatusLabel.setText("OK")
                self.ui.pioStatusLabel.setStyleSheet("background-color: green;")
            else:
                self.ui.pioStatusLabel.setText("KO")
                self.ui.pioStatusLabel.setStyleSheet("background-color: red;")
                self.ui.pioInstallButton.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
