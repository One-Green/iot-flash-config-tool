import os
import sys
import glob
import serial
from subprocess import Popen, PIPE, STDOUT, CalledProcessError
from project_settings import LOCAL_REPO, logger, pio_logger
from PyQt6.QtWidgets import QMessageBox
from src.main_ui import Ui_MainWindow
from src.handlers.firmware_def import SprinklerNodes
from src.handlers.firmware_def import WaterTankNodes
from src.handlers.flash_cmd import FlashCmd


class FlashHandler:
    def __init__(self, ui):
        self.ui: Ui_MainWindow = ui
        self.flash_cmd: FlashCmd = FlashCmd()
        self.sprinkler_nodes = SprinklerNodes
        self.water_tank_nodes = WaterTankNodes
        self.node_type: str = ""
        self.firmware_type: str = ""
        self.firmware_src_path = ""
        self.list_serial_ports()
        self.set_default_node_and_firmware()

    def set_default_node_and_firmware(self):
        # set Sprinkler node and default firmware
        self.ui.nodeTypeList.setCurrentRow(0)
        self.ui.firmwareList.addItems(
            [getattr(_, "caption_name") for _ in SprinklerNodes]
        )
        self.ui.firmwareList.setCurrentRow(0)
        self.firmware_src_path = os.path.join(LOCAL_REPO, SprinklerNodes[0].src_path)

    def set_firmwares(self, node_type):
        logger.debug(f"selected node '{node_type.text()}'")
        self.ui.firmwareList.clear()
        if node_type.text() == "Sprinkler":
            self.ui.firmwareList.addItems(
                [getattr(_, "caption_name") for _ in SprinklerNodes]
            )
        elif node_type.text() == "Water tank":
            self.ui.firmwareList.addItems(
                [getattr(_, "caption_name") for _ in WaterTankNodes]
            )
        self.node_type = node_type.text()

    def set_firmware_src_path(self, firmware_type):
        logger.debug(f"selected firmware '{firmware_type.text()}'")
        if self.node_type == "Sprinkler":
            for _ in SprinklerNodes:
                if _.caption_name == firmware_type.text():
                    self.firmware_src_path = os.path.join(LOCAL_REPO, _.src_path)
                    logger.debug(f"firmware source is '{self.firmware_src_path}'")
                    break
        elif self.node_type == "Water tank":
            for _ in WaterTankNodes:
                if _.caption_name == firmware_type.text():
                    self.firmware_src_path = os.path.join(LOCAL_REPO, _.src_path)
                    logger.debug(f"firmware source is '{self.firmware_src_path}'")
                    break

    def list_serial_ports(self):
        # source : https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
        # thanks to https://github.com/tfeldmann !
        ports = []
        logger.debug("listing usb tty")
        try:
            if sys.platform.startswith("win"):
                ports = ["COM%s" % (i + 1) for i in range(256)]
            elif sys.platform.startswith("linux") or sys.platform.startswith("cygwin"):
                # this excludes your current terminal "/dev/tty"
                ports = glob.glob("/dev/tty[A-Za-z]*")
            elif sys.platform.startswith("darwin"):
                ports = glob.glob("/dev/tty.*")
        except EnvironmentError:
            pass

        result = []
        for _ in ports:
            try:
                s = serial.Serial(_)
                s.close()
                result.append(_)
            except (OSError, serial.SerialException):
                pass
        logger.debug(f"port list {result}")
        self.ui.deviceListcomboBox.clear()
        self.ui.deviceListcomboBox.addItems(result)
        self.ui.flashStatus.setStyleSheet("")
        self.ui.flashStatus.setText("devices list updated")

    def flash(self):
        known_err_msg: list = ["Traceback", "FAILED"]
        err: bool = False

        process = Popen(self.generate_cmd(), shell=True, stdout=PIPE, stderr=STDOUT)
        with process.stdout:
            try:
                for line in iter(process.stdout.readline, b""):
                    line = line.decode("utf-8").strip()
                    self.ui.flashStatus.setStyleSheet("color: blue;")
                    self.ui.flashStatus.setText(line)
                    self.ui.flashStatus.repaint()
                    pio_logger.debug(f"{line}")
                    if any(_ in line for _ in known_err_msg):
                        err = True
            except CalledProcessError as e:
                self.ui.flashStatus.setStyleSheet("background-color: red;")
                self.ui.flashStatus.setText("process error: check 'pio.log' file")
                pio_logger.error(f"{str(e)}")
        if err:
            self.ui.flashStatus.setStyleSheet("background-color: red;")
            self.ui.flashStatus.setText("flash failed: check 'pio.log' file")
        else:
            self.ui.flashStatus.setStyleSheet("background-color: green;")
            self.ui.flashStatus.setText("Flashed successfully")

    def display_cmd(self):
        logger.debug("cmd test clicked")
        info_window = QMessageBox()
        info_window.setIcon(QMessageBox.Icon.Question)
        info_window.setWindowTitle("Flash command details")
        info_window.setText(
            "Pio cmd check: click on details and share (without wifi ssid and wifi password) for "
            "troubleshooting "
        )
        info_window.setDetailedText(self.generate_cmd())
        info_window.exec()

    def generate_cmd(self) -> str:
        logger.debug("generating flash command ")
        # override water tank node type
        # not scalable for now
        if self.node_type == "Water tank":
            node_tag = "default"
            logger.warning(f"water tank node detected, overriding {node_tag=}")
        else:
            node_tag = self.ui.uniqueTaglineEdit.text()

        cmd = self.flash_cmd.get_main_microchip_cmd(
            src_path=self.firmware_src_path,
            upload_port=self.ui.deviceListcomboBox.currentText(),
            wifi_ssid=self.ui.wifiSSIDLineEdit.text(),
            wifi_password=self.ui.wifiPasswordEditLine.text(),
            api_gateway_url=self.ui.apiHostLineEdit.text(),
            api_gateway_basic_auth_user=self.ui.apiUsernameLineEdit.text(),
            api_gateway_basic_auth_password=self.ui.apiPasswordLineEdit.text(),
            node_tag=node_tag,
            mqtt_server=self.ui.mqttHostLineEdit.text(),
            mqtt_port=self.ui.mqttPortLineEdit.text(),
            mqtt_user=self.ui.mqttUsernameLineEdit.text(),
            mqtt_password=self.ui.mqttPasswordLineEdit.text(),
        )
        logger.debug("generated command")
        logger.debug(cmd)
        return cmd
