import os
import colorlog
import logging

LOCAL_REPO: str = os.path.join(os.getcwd(), "_firmware")

handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter("%(log_color)s%(levelname)s:%(name)s: %(message)s")
)
logger = colorlog.getLogger("default-logger")
logger.addHandler(handler)
logger.setLevel(colorlog.DEBUG)

pio_logger = colorlog.getLogger("pio-logger")
pio_logger.addHandler(handler)
pio_logger.addHandler(logging.FileHandler("pio.log"))
pio_logger.setLevel(colorlog.DEBUG)
