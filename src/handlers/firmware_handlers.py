import os
import time
import colorlog
from git import Repo, Git
from git.exc import GitCommandError
from src.main_ui import Ui_MainWindow
from project_settings import LOCAL_REPO

logger = colorlog.getLogger("default-logger")


class FirmwareHandler:
    def __init__(self, ui):
        self.ui: Ui_MainWindow = ui
        self.origin: str = ""
        self.git_tag: str = ""

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

    def set_tag(self, item):
        self.git_tag = item.text()
        logger.debug(f"clicked version {self.git_tag}")

    def checkout(self):
        logger.info(f"Git checkout version {self.git_tag}")
        self.ui.gitCheckOutStatus.setStyleSheet("color: blue;")
        self.ui.gitCheckOutStatus.setText("changing version ...")
        self.ui.gitCheckOutStatus.repaint()
        time.sleep(0.5)
        try:
            Git(LOCAL_REPO).checkout(self.git_tag, force=True)
            self.ui.gitCheckOutStatus.setStyleSheet("background-color: green;")
            self.ui.gitCheckOutStatus.setText("version selected")
            logger.info(f"Git checkout version {self.git_tag} done")
        except GitCommandError:
            logger.error(
                "can not checkout without tag reference, run 'download/update' and select a version"
            )
            self.ui.gitCheckOutStatus.setFixedWidth(280)
            self.ui.gitCheckOutStatus.setFixedHeight(50)
            self.ui.gitCheckOutStatus.setWordWrap(True)
            self.ui.gitCheckOutStatus.setStyleSheet("background-color: red;")
            self.ui.gitCheckOutStatus.setText(
                "'Download/Update' and select version first"
            )
            logger.info(f"Git checkout version {self.git_tag} done")

    def clone_or_update(self):
        self.clone()
        self.fetch()
        self.enum_versions()
