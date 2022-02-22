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
