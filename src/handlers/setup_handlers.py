import shutil
import platform
import colorlog

logger = colorlog.getLogger("default-logger")

GIT: str = "git"
PYTHON: str = "python"
PIO: str = "pio"
PIO_EXE: str = "pio.exe"


class SetupHandler:
    def __init__(self, ui):
        self.ui = ui

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

    def check_pio(self):
        if self.is_pio_exist():
            self.ui.pioStatusLabel.setText("OK")
            self.ui.pioStatusLabel.setStyleSheet("background-color: green;")
        else:
            self.ui.pioStatusLabel.setText("KO")
            self.ui.pioStatusLabel.setStyleSheet("background-color: red;")
            self.ui.pioInstallButton.setEnabled(True)
