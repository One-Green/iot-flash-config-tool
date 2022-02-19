import shutil
import platform
import colorlog

logger = colorlog.getLogger("default-logger")

GIT: str = "git"
PYTHON: str = "python"
PIO: str = "pio"
PIO_EXE: str = "pio.exe"


def is_git_exist() -> bool:
    _ = shutil.which(GIT)
    if _:
        logger.info(f"{GIT} found: '{_}'")
        return True
    else:
        return False


def is_python_exist() -> bool:
    _ = shutil.which(PYTHON)
    if _:
        logger.info(f"{PYTHON} found: '{_}'")
        return True
    else:
        return False


def is_pio_exist() -> bool:
    _platform = platform.system()

    if _platform == ("Linux" or "Darwin"):
        _ = shutil.which(PIO)
        if _:
            logger.info(f"{PIO} for {_platform} found: '{_}'")
            return True
        else:
            return False
    elif platform.system() == "Windows":
        _ = shutil.which(PIO)
        if _:
            logger.info(f"{PIO} for {_platform} found: '{_}'")
            return True
        else:
            return False
    else:
        logger.error(f"This platform '{_platform}' is not handled by this tool")
        return False
