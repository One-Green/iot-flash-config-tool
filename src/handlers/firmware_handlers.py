import os
from git import Repo
import colorlog
from src.main_ui import Ui_MainWindow
import time

logger = colorlog.getLogger("default-logger")

LOCAL_REPO: str = os.path.join(os.getcwd(), "_firmware")


class FirmwareHandler:
    def __init__(self, ui):
        self.ui: Ui_MainWindow = ui
        self.origin: str = ""

    def clone(self):
        if not os.path.isdir(LOCAL_REPO):
            self.ui.gitCloneOrFetchStatus.setStyleSheet("color: blue;")
            self.ui.gitCloneOrFetchStatus.setText("source not found")
            self.ui.gitCloneOrFetchStatus.repaint()
            time.sleep(0.5)
            self.ui.gitCloneOrFetchStatus.setText("cloning project ...")
            self.ui.gitCloneOrFetchStatus.repaint()
            self.origin: str = self.ui.lineFirmwareGitRepo.text()

            logger.info(f"Cloning firmware code source from '{self.origin}'")
            Repo.clone_from(self.origin, LOCAL_REPO)
            logger.info(f"Cloning ok")

            self.ui.gitCloneOrFetchStatus.setStyleSheet("color: black;")
            self.ui.gitCloneOrFetchStatus.setStyleSheet("background-color: green;")
            self.ui.gitCloneOrFetchStatus.setText("firmware src ok")
            self.ui.gitCloneOrFetchStatus.repaint()
        else:
            self.ui.gitCloneOrFetchStatus.setStyleSheet("color: black;")
            self.ui.gitCloneOrFetchStatus.setStyleSheet("background-color: green;")
            self.ui.gitCloneOrFetchStatus.setText("firmware src exist")
            self.ui.gitCloneOrFetchStatus.repaint()
            logger.warning(f"code source already exist at '{LOCAL_REPO}', don't clone")

    def fetch(self):
        if os.path.isdir(LOCAL_REPO):
            logger.info(f"Fetching latest code source")
            self.ui.gitCloneOrFetchStatus.setStyleSheet("color: blue;")
            self.ui.gitCloneOrFetchStatus.setText("fetch updates ...")
            self.ui.gitCloneOrFetchStatus.repaint()
            repo = Repo(LOCAL_REPO)
            for remote in repo.remotes:
                remote.fetch()
            self.ui.gitCloneOrFetchStatus.setStyleSheet("color: black;")
            self.ui.gitCloneOrFetchStatus.setStyleSheet("background-color: green;")
            self.ui.gitCloneOrFetchStatus.setText("firmware src updated")
            self.ui.gitCloneOrFetchStatus.repaint()
            logger.info(f"Fetching latest code source done ")
        else:
            logger.warning(
                f"Can not fetch check if code source is available at '{LOCAL_REPO}' "
            )

    def enum_versions(self):
        self.ui.gitTagListWidget.clear()
        logger.info(f"Enumerating available tags in repo")
        self.ui.gitCloneOrFetchStatus.setStyleSheet("color: blue;")
        self.ui.gitCloneOrFetchStatus.setText("listing versions ...")
        self.ui.gitCloneOrFetchStatus.repaint()
        if os.path.isdir(LOCAL_REPO):
            self.ui.gitTagListWidget.addItems(
                map(
                    str,
                    sorted(
                        Repo(LOCAL_REPO).tags,
                        key=lambda t: t.commit.committed_datetime,
                    ),
                )
            )
            logger.info(f"Enumerating available tags in repo")
            self.ui.gitCloneOrFetchStatus.setStyleSheet("color: black;")
            self.ui.gitCloneOrFetchStatus.setStyleSheet("background-color: green;")
            self.ui.gitCloneOrFetchStatus.setText("all good !")
            self.ui.gitCloneOrFetchStatus.repaint()
        else:
            logger.error("can not found git repo to enum tags/versions")
            self.ui.gitTagListWidget.addItem(["repo not found"])

    def clone_or_update(self):
        self.clone()
        self.fetch()
        self.enum_versions()
