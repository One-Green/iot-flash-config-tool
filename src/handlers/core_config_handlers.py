import os
import yaml
import colorlog
from PyQt6.QtWidgets import QFileDialog
from src.main_ui import Ui_MainWindow

logger = colorlog.getLogger("default-logger")


class CoreConfigHandler:
    def __init__(self, ui):
        self.ui: Ui_MainWindow = ui
        self.api_host: str = ""
        self.api_port: str = ""
        self.api_username: str = ""
        self.api_password: str = ""
        self.mqtt_host: str = ""
        self.mqtt_port: str = ""
        self.mqtt_username: str = ""
        self.mqtt_password: str = ""

    @staticmethod
    def __read_yaml(_file_path: str) -> dict:
        logger.info(f"parsing yaml file '{_file_path}'")
        with open(_file_path, "r+") as _:
            try:
                d = yaml.safe_load(_)
                logger.info(f"yaml file '{_file_path}' successfully parsed")
                return d
            except yaml.YAMLError:
                logger.error(f"can not yaml parse file {_file_path}")

    def __get_ui_values(self):
        self.api_host: str = self.ui.apiHostLineEdit.text()
        self.api_port: str = self.ui.apiPortLineEdit.text()
        self.api_username: str = self.ui.apiUsernameLineEdit.text()
        self.api_password: str = self.ui.apiPasswordLineEdit.text()
        self.mqtt_host: str = self.ui.mqttHostLineEdit.text()
        self.mqtt_port: str = self.ui.mqttPortLineEdit.text()
        self.mqtt_username: str = self.ui.mqttUsernameLineEdit.text()
        self.mqtt_password: str = self.ui.mqttPasswordLineEdit.text()

    def __set_ui_values(self):
        self.ui.apiHostLineEdit.setText(self.api_host)
        self.ui.apiPortLineEdit.setText(self.api_port)
        self.ui.apiUsernameLineEdit.setText(self.api_username)
        self.ui.apiPasswordLineEdit.setText(self.api_password)
        self.ui.mqttHostLineEdit.setText(self.mqtt_host)
        self.ui.mqttPortLineEdit.setText(self.mqtt_port)
        self.ui.mqttUsernameLineEdit.setText(self.mqtt_username)
        self.ui.mqttPasswordLineEdit.setText(self.mqtt_password)

    def __set_cls_attribute(self, d: dict) -> bool:
        try:
            # api configs
            self.api_host: str = d["api"]["host"]
            self.api_port: str = d["api"]["port"]
            self.api_username: str = d["api"]["username"]
            self.api_password: str = d["api"]["password"]
            # mqtt configs
            self.mqtt_host: str = d["mqtt"]["host"]
            self.mqtt_port: str = d["mqtt"]["port"]
            self.mqtt_username: str = d["mqtt"]["username"]
            self.mqtt_password: str = d["mqtt"]["password"]
            return True
        except (TypeError, KeyError):
            return False

    def __dump_yaml(self, _file_path: str):
        logger.info(f"dumping to yaml file '{_file_path}'")
        with open(_file_path, "w") as _:
            yaml.dump(
                {
                    "api": {
                        "host": self.api_host,
                        "port": self.api_port,
                        "username": self.api_username,
                        "password": self.api_password,
                    },
                    "mqtt": {
                        "host": self.mqtt_host,
                        "port": self.mqtt_port,
                        "username": self.mqtt_username,
                        "password": self.mqtt_password,
                    },
                },
                _,
            )

    def load_file(self):
        _: str = QFileDialog.getOpenFileName(directory=os.getcwd())[0]
        if _:
            logger.info(f"load file selected '{_}'")
            config: dict = self.__read_yaml(_)
            if self.__set_cls_attribute(config):
                logger.debug(f"affecting config to ui edit line '{_}'")
                self.__set_ui_values()
                self.ui.saveLoadStatus.setStyleSheet("background-color: green;")
                self.ui.saveLoadStatus.setText(" load successfully")
            else:
                self.ui.saveLoadStatus.setStyleSheet("background-color: red;")
                self.ui.saveLoadStatus.setText("file not compatible")
                logger.error(f"error while affecting config to ui edit line")
        else:
            self.ui.saveLoadStatus.setStyleSheet("color: blue;")
            self.ui.saveLoadStatus.setText("nothing loaded")

    def save_file(self):
        _: str = QFileDialog.getSaveFileName(directory=os.getcwd())[0]
        if _:
            logger.info(f"save file selected '{_}'")
            self.__get_ui_values()
            self.__dump_yaml(_)
            self.ui.saveLoadStatus.setStyleSheet("background-color: green;")
            self.ui.saveLoadStatus.setText("saved successfully")
            logger.info(f"saved file to '{_}' successfully")
        else:
            self.ui.saveLoadStatus.setStyleSheet("color: blue;")
            self.ui.saveLoadStatus.setText("nothing saved")
