import os
import sys
import glob
import serial
import colorlog
from src.main_ui import Ui_MainWindow
from src.handlers.firmware_def import SprinklerNodes
from src.handlers.firmware_def import WaterTankNodes
from project_settings import LOCAL_REPO

logger = colorlog.getLogger("default-logger")


class FlashHandler:
    def __init__(self, ui):
        self.ui: Ui_MainWindow = ui
        self.sprinkler_nodes = SprinklerNodes
        self.water_tank_nodes = WaterTankNodes
        self.node_type: str = ""
        self.firmware_type: str = ""
        self.firmware_src_path = ""
        self.list_serial_ports()

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
        self.ui.flashStatus.setText("devices list updated")
