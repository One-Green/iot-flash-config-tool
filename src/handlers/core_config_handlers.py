import os
import colorlog
from PyQt6.QtWidgets import QFileDialog
from src.main_ui import Ui_MainWindow

logger = colorlog.getLogger("default-logger")


class CoreConfigHandler:
    def __init__(self, ui):
        self.ui: Ui_MainWindow = ui

    @staticmethod
    def load_file():
        _ = QFileDialog.getOpenFileName(
            directory=os.getcwd(), filter="YAML (*.yaml *.yml)"
        )
        print(f"selected file {_}")

    @staticmethod
    def save_file():
        _ = QFileDialog.getSaveFileName(
            directory=os.getcwd(), filter="YAML (*.yaml *.yml)"
        )
        print(f"selected file {_}")
