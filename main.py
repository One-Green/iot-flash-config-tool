import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
import colorlog
from src.main_ui import Ui_MainWindow
from src.handlers.setup_handlers import SetupHandler


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
        self.setup_tab = SetupHandler(ui=self.ui)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
