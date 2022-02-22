# related to this project
# https://github.com/One-Green/iot-edge-agent

from dataclasses import dataclass


@dataclass
class Platform:
    esp_32: str = "esp32"
    arduino_nano: str = "arduino-nano"
    arduino_mega: str = "arduino-mega"


class BaseMicroController(object):
    def __init__(self, name, platform, src_path):
        self.name: str = name
        self.platform: str = platform
        self.src_path: str = src_path

    @property
    def caption_name(self):
        return f"{self.name}-{self.platform}"


SprinklerNodes = [
    BaseMicroController(name="default", platform=Platform.esp_32, src_path="sprinkler")
]

WaterTankNodes = [
    BaseMicroController(
        name="default", platform=Platform.esp_32, src_path="water/master_esp32"
    ),
    BaseMicroController(
        name="slave-1", platform=Platform.arduino_mega, src_path="water/i2c_slave_mega"
    ),
]
