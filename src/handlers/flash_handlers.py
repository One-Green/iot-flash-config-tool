import sys
import glob
import serial
import colorlog
from src.main_ui import Ui_MainWindow
from src.handlers.firmware_def import SprinklerNodes
from src.handlers.firmware_def import WaterTankNodes

logger = colorlog.getLogger("default-logger")


class FlashHandler:
    def __init__(self, ui):
        self.ui: Ui_MainWindow = ui
        self.sprinkler_nodes = SprinklerNodes
        self.water_tank_nodes = WaterTankNodes
        self.list_serial_ports()

    def set_firmwares(self, v):
        logger.debug(f"selected node '{v.text()}'")
        self.ui.firmwareList.clear()

        if v.text() == "Sprinkler":

            self.ui.firmwareList.addItems(
                [getattr(_, "caption_name") for _ in SprinklerNodes]
            )
        elif v.text() == "Water tank":
            self.ui.firmwareList.addItems(
                [getattr(_, "caption_name") for _ in WaterTankNodes]
            )

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
