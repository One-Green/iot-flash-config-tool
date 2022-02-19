import subprocess


def __binary_probe(_bin: str) -> bool:
    try:
        subprocess.call(
            [_bin],
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False


def is_git_exist() -> bool:
    return __binary_probe("git")


def is_python_exist() -> bool:
    return __binary_probe("python")
