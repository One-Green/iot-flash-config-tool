import sys
import colorlog
from PyQt6.QtWidgets import QMainWindow, QApplication
from src.main_ui import Ui_MainWindow

# Handler classes
from src.handlers.setup_handlers import SetupHandler
from src.handlers.firmware_handlers import FirmwareHandler
from src.handlers.core_config_handlers import CoreConfigHandler

handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter("%(log_color)s%(levelname)s:%(name)s:%(message)s")
)
logger = colorlog.getLogger("default-logger")
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
        self.firmware_tab = FirmwareHandler(ui=self.ui)
        self.core_config_tab = CoreConfigHandler(ui=self.ui)
        logger.debug("loading handlers classes: done")

        # --- button method link
        # ----- tab: setup
        logger.debug("linking button to actions")
        self.ui.gitCheckButton.clicked.connect(self.setup_tab.check_git)
        self.ui.gitInstallButton.clicked.connect(self.setup_tab.setup_git)
        self.ui.gitInstallButton.setEnabled(False)
        # ----- Python
        self.ui.pythonCheckButton.clicked.connect(self.setup_tab.check_python)
        self.ui.pythonInstallButton.clicked.connect(self.setup_tab.setup_python)
        self.ui.pythonInstallButton.setEnabled(False)
        # ----- Pip
        self.ui.pipCheckButton.clicked.connect(self.setup_tab.check_pip)
        self.ui.pipInstallButton.clicked.connect(self.setup_tab.setup_pip)
        self.ui.pipInstallButton.setEnabled(False)
        # ----- Platform IO
        self.ui.pioCheckButton.clicked.connect(self.setup_tab.check_pio)
        self.ui.pioInstallButton.clicked.connect(self.setup_tab.setup_pio)
        self.ui.pioInstallButton.setEnabled(False)
        # ----- Check all
        self.ui.checkAllButton.clicked.connect(self.setup_tab.check_all)

        # ----- tab: firmware
        self.ui.gitCloneOrFetchButton.clicked.connect(self.firmware_tab.clone_or_update)
        self.ui.gitTagListWidget.itemClicked.connect(self.firmware_tab.set_tag)
        self.ui.gitCheckOutButton.clicked.connect(self.firmware_tab.checkout)

        # ----- tab: core configuration
        self.ui.pushButton.clicked.connect(self.core_config_tab.load_file)
        self.ui.pushButton_2.clicked.connect(self.core_config_tab.save_file)

        logger.debug("linking button to actions done")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
