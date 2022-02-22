# related to this project
# https://github.com/One-Green/iot-edge-agent


class BaseMicroController(object):
    def __init__(self, caption_name, platform, src_path):
        self.name: str = caption_name
        self.platform: str = platform
        self.src_path: str = src_path


SprinklerNodes = [
    BaseMicroController(caption_name="default", platform="esp32", src_path="sprinkler")
]

WaterTankNodes = [
    BaseMicroController(
        caption_name="default", platform="esp32", src_path="water/master_esp32"
    ),
    BaseMicroController(
        caption_name="mega-slave-1", platform="esp32", src_path="water/i2c_slave_mega"
    ),
]
