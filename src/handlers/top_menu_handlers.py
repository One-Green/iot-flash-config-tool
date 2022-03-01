import colorlog
import webbrowser
from src.main_ui import Ui_MainWindow

logger = colorlog.getLogger("default-logger")


class MenuHandler:
    def __init__(self, ui):
        self.ui: Ui_MainWindow = ui

    @staticmethod
    def documentation_action():
        webbrowser.open("https://one-green.readthedocs.io/en/latest/?badge=latest")

    @staticmethod
    def code_source_action():
        webbrowser.open("https://github.com/One-Green/iot-flash-config-tool")

    @staticmethod
    def licence_action():
        webbrowser.open(
            "https://github.com/One-Green/iot-flash-config-tool/blob/main/LICENCE"
        )

    @staticmethod
    def about_action():
        webbrowser.open("https://one-green.io/")
