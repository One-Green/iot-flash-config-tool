import shutil
import platform
import colorlog
import webbrowser
from src.main_ui import Ui_MainWindow

logger = colorlog.getLogger("default-logger")

NOT_FOUND_MOD: bool = False

if NOT_FOUND_MOD:
    # Mock enable install buttons
    GIT: str = "git_should_not_work"
    PYTHON: str = "python_should_not_work"
    PIP: str = "pip_should_not_work"
    PIO: str = "pio_should_not_work"
    PIO_EXE: str = "pio.exe_should_not_work"
else:
    GIT: str = "git"
    PYTHON: str = "python"
    PIP: str = "pip"
    PIO: str = "pio"
    PIO_EXE: str = "pio.exe"


# Setup Link
GIT_SETUP_URL = "https://git-scm.com/downloads"
PYTHON_SETUP_URL = "https://www.python.org/downloads/release/python-3910/"
PIP_SETUP_URL = "https://pip.pypa.io/en/stable/installation/"
PIO_SETUP_URL = "https://docs.platformio.org/en/latest//core/installation.html#installation-installer-script"


class SetupHandler:
    def __init__(self, ui):
        self.ui: Ui_MainWindow = ui

    @staticmethod
    def is_git_exist() -> bool:
        _ = shutil.which(GIT)
        if _:
            logger.info(f"{GIT} found: '{_}'")
            return True
        else:
            return False

    @staticmethod
    def is_python_exist() -> bool:
        _ = shutil.which(PYTHON)
        if _:
            logger.info(f"{PYTHON} found: '{_}'")
            return True
        else:
            return False

    @staticmethod
    def is_pip_exist() -> bool:
        _ = shutil.which(PIP)
        if _:
            logger.info(f"{PIP} found: '{_}'")
            return True
        else:
            return False

    @staticmethod
    def is_pio_exist() -> bool:
        _platform = platform.system()

        if _platform == ("Linux" or "Darwin"):
            _ = shutil.which(PIO)
            if _:
                logger.info(f"{PIO} for {_platform} found: '{_}'")
                return True
            else:
                return False
        elif platform.system() == "Windows":
            _ = shutil.which(PIO)
            if _:
                logger.info(f"{PIO} for {_platform} found: '{_}'")
                return True
            else:
                return False
        else:
            logger.error(f"This platform '{_platform}' is not handled by this tool")
            return False

    def check_git(self):
        if self.is_git_exist():
            self.ui.gitStatusLabel.setText("OK")
            self.ui.gitStatusLabel.setStyleSheet("background-color: green;")
        else:
            self.ui.gitStatusLabel.setText("KO")
            self.ui.gitStatusLabel.setStyleSheet("background-color: red;")
            self.ui.gitInstallButton.setEnabled(True)

    def check_python(self):
        if self.is_python_exist():
            self.ui.pythonStatusLabel.setText("OK")
            self.ui.pythonStatusLabel.setStyleSheet("background-color: green;")
        else:
            self.ui.pythonStatusLabel.setText("KO")
            self.ui.pythonStatusLabel.setStyleSheet("background-color: red;")
            self.ui.pythonInstallButton.setEnabled(True)

    def check_pip(self):
        if self.is_pip_exist():
            self.ui.pipStatusLabel.setText("OK")
            self.ui.pipStatusLabel.setStyleSheet("background-color: green;")
        else:
            self.ui.pipStatusLabel.setText("KO")
            self.ui.pipStatusLabel.setStyleSheet("background-color: red;")
            self.ui.pipInstallButton.setEnabled(True)

    def check_pio(self):
        if self.is_pio_exist():
            self.ui.pioStatusLabel.setText("OK")
            self.ui.pioStatusLabel.setStyleSheet("background-color: green;")
        else:
            self.ui.pioStatusLabel.setText("KO")
            self.ui.pioStatusLabel.setStyleSheet("background-color: red;")
            self.ui.pioInstallButton.setEnabled(True)

    def check_all(self):
        self. check_git()
        self.check_python()
        self.check_pip()
        self.check_pio()

    @staticmethod
    def setup_git():
        webbrowser.open(GIT_SETUP_URL)

    @staticmethod
    def setup_python():
        webbrowser.open(PYTHON_SETUP_URL)

    @staticmethod
    def setup_pip():
        webbrowser.open(PIP_SETUP_URL)

    @staticmethod
    def setup_pio():
        webbrowser.open(PIO_SETUP_URL)
