import os
import colorlog

LOCAL_REPO: str = os.path.join(os.getcwd(), "_firmware")

handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter("%(log_color)s%(levelname)s:%(name)s: %(message)s")
)
logger = colorlog.getLogger("default-logger")
logger.addHandler(handler)
logger.setLevel(colorlog.DEBUG)
