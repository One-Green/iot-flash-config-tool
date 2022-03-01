import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from project_settings import logger
from src.main_ui import Ui_MainWindow

# Handler classes
from src.handlers.top_menu_handlers import MenuHandler
from src.handlers.setup_handlers import SetupHandler
from src.handlers.firmware_handlers import FirmwareHandler
from src.handlers.core_config_handlers import CoreConfigHandler
from src.handlers.flash_handlers import FlashHandler


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
        self.top_menu_handler = MenuHandler(ui=self.ui)
        self.setup_tab = SetupHandler(ui=self.ui)
        self.firmware_tab = FirmwareHandler(ui=self.ui)
        self.core_config_tab = CoreConfigHandler(ui=self.ui)
        self.flash_config_tab = FlashHandler(ui=self.ui)
        logger.debug("loading handlers classes: done")

        # --- top menu link
        logger.debug("linking button to actions")
        self.ui.docAction.triggered.connect(self.top_menu_handler.documentation_action)
        self.ui.codeSourceAction.triggered.connect(
            self.top_menu_handler.code_source_action
        )
        self.ui.licenceAction.triggered.connect(self.top_menu_handler.licence_action)
        self.ui.aboutAction.triggered.connect(self.top_menu_handler.about_action)
        # --- button method link
        # ----- tab: setup
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
        self.ui.testApiConnexionButton.clicked.connect(
            self.core_config_tab.check_api_connexion
        )
        self.ui.testMqttConnexionButton.clicked.connect(
            self.core_config_tab.check_mqtt_connexion
        )
        self.ui.loadCoreConfigFileButton.clicked.connect(self.core_config_tab.load_file)
        self.ui.saveCoreConfigFileButton.clicked.connect(self.core_config_tab.save_file)

        # ----- tab: flash
        self.ui.nodeTypeList.itemClicked.connect(self.flash_config_tab.set_firmwares)
        self.ui.firmwareList.itemClicked.connect(
            self.flash_config_tab.set_firmware_src_path
        )
        self.ui.refreshDevicespushButton.clicked.connect(
            self.flash_config_tab.list_serial_ports
        )
        self.ui.testCommandpushButton.clicked.connect(self.flash_config_tab.display_cmd)
        self.ui.flashButton.clicked.connect(self.flash_config_tab.flash)
        logger.debug("linking button to actions done")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
