# Form implementation generated from reading ui file 'src/main.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 507)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Flash = QtWidgets.QTabWidget(self.centralwidget)
        self.Flash.setGeometry(QtCore.QRect(0, 0, 481, 461))
        self.Flash.setObjectName("Flash")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 481, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 481, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 90, 481, 120))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gitLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gitLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gitLabel.setObjectName("gitLabel")
        self.gridLayout.addWidget(self.gitLabel, 0, 0, 1, 1)
        self.gitInstallButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.gitInstallButton.setObjectName("gitInstallButton")
        self.gridLayout.addWidget(self.gitInstallButton, 0, 2, 1, 1)
        self.pythonLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pythonLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pythonLabel.setObjectName("pythonLabel")
        self.gridLayout.addWidget(self.pythonLabel, 1, 0, 1, 1)
        self.pythonInstallButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pythonInstallButton.setObjectName("pythonInstallButton")
        self.gridLayout.addWidget(self.pythonInstallButton, 1, 2, 1, 1)
        self.gitCheckButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.gitCheckButton.setObjectName("gitCheckButton")
        self.gridLayout.addWidget(self.gitCheckButton, 0, 1, 1, 1)
        self.gitStatusLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gitStatusLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gitStatusLabel.setObjectName("gitStatusLabel")
        self.gridLayout.addWidget(self.gitStatusLabel, 0, 3, 1, 1)
        self.pioCheckButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pioCheckButton.setObjectName("pioCheckButton")
        self.gridLayout.addWidget(self.pioCheckButton, 3, 1, 1, 1)
        self.pioInstallButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pioInstallButton.setObjectName("pioInstallButton")
        self.gridLayout.addWidget(self.pioInstallButton, 3, 2, 1, 1)
        self.pythonStatusLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pythonStatusLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pythonStatusLabel.setObjectName("pythonStatusLabel")
        self.gridLayout.addWidget(self.pythonStatusLabel, 1, 3, 1, 1)
        self.pythonCheckButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pythonCheckButton.setObjectName("pythonCheckButton")
        self.gridLayout.addWidget(self.pythonCheckButton, 1, 1, 1, 1)
        self.pioLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pioLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pioLabel.setObjectName("pioLabel")
        self.gridLayout.addWidget(self.pioLabel, 3, 0, 1, 1)
        self.pioStatusLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pioStatusLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pioStatusLabel.setObjectName("pioStatusLabel")
        self.gridLayout.addWidget(self.pioStatusLabel, 3, 3, 1, 1)
        self.pipLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pipLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pipLabel.setObjectName("pipLabel")
        self.gridLayout.addWidget(self.pipLabel, 2, 0, 1, 1)
        self.pipCheckButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pipCheckButton.setObjectName("pipCheckButton")
        self.gridLayout.addWidget(self.pipCheckButton, 2, 1, 1, 1)
        self.pipInstallButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pipInstallButton.setObjectName("pipInstallButton")
        self.gridLayout.addWidget(self.pipInstallButton, 2, 2, 1, 1)
        self.pipStatusLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pipStatusLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pipStatusLabel.setObjectName("pipStatusLabel")
        self.gridLayout.addWidget(self.pipStatusLabel, 2, 3, 1, 1)
        self.checkAllButton = QtWidgets.QPushButton(self.tab)
        self.checkAllButton.setGeometry(QtCore.QRect(170, 390, 129, 29))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkAllButton.sizePolicy().hasHeightForWidth()
        )
        self.checkAllButton.setSizePolicy(sizePolicy)
        self.checkAllButton.setObjectName("checkAllButton")
        self.Flash.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 461, 111))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 451, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gitCloneOrFetchButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.gitCloneOrFetchButton.setObjectName("gitCloneOrFetchButton")
        self.gridLayout_2.addWidget(self.gitCloneOrFetchButton, 0, 0, 1, 1)
        self.gitCloneOrFetchStatus = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.gitCloneOrFetchStatus.setObjectName("gitCloneOrFetchStatus")
        self.gridLayout_2.addWidget(self.gitCloneOrFetchStatus, 0, 2, 1, 1)
        self.gitCloneOrFetchStatusLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.gitCloneOrFetchStatusLabel.setObjectName("gitCloneOrFetchStatusLabel")
        self.gridLayout_2.addWidget(self.gitCloneOrFetchStatusLabel, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 51, 21))
        self.label_6.setObjectName("label_6")
        self.lineFirmwareGitRepo = QtWidgets.QLineEdit(self.groupBox)
        self.lineFirmwareGitRepo.setGeometry(QtCore.QRect(60, 30, 391, 25))
        self.lineFirmwareGitRepo.setObjectName("lineFirmwareGitRepo")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 130, 461, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 220, 451, 41))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gitCheckOutButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.gitCheckOutButton.setObjectName("gitCheckOutButton")
        self.gridLayout_3.addWidget(self.gitCheckOutButton, 0, 0, 1, 1)
        self.gitCheckOutStatus = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.gitCheckOutStatus.setObjectName("gitCheckOutStatus")
        self.gridLayout_3.addWidget(self.gitCheckOutStatus, 0, 2, 1, 1)
        self.gitCheckOutStatusLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.gitCheckOutStatusLabel.setObjectName("gitCheckOutStatusLabel")
        self.gridLayout_3.addWidget(self.gitCheckOutStatusLabel, 0, 1, 1, 1)
        self.gitTagListWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.gitTagListWidget.setGeometry(QtCore.QRect(10, 30, 151, 181))
        self.gitTagListWidget.setObjectName("gitTagListWidget")
        self.Flash.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Flash.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.Flash.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 487, 22))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionSetup_depdencies = QtGui.QAction(MainWindow)
        self.actionSetup_depdencies.setObjectName("actionSetup_depdencies")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSprinkler = QtGui.QAction(MainWindow)
        self.actionSprinkler.setObjectName("actionSprinkler")
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionWater_esp32 = QtGui.QAction(MainWindow)
        self.actionWater_esp32.setObjectName("actionWater_esp32")
        self.actionWater_mege = QtGui.QAction(MainWindow)
        self.actionWater_mege.setObjectName("actionWater_mege")
        self.actionLight_esp32 = QtGui.QAction(MainWindow)
        self.actionLight_esp32.setObjectName("actionLight_esp32")
        self.actionCode_source = QtGui.QAction(MainWindow)
        self.actionCode_source.setObjectName("actionCode_source")
        self.actionCode_source_2 = QtGui.QAction(MainWindow)
        self.actionCode_source_2.setObjectName("actionCode_source_2")
        self.actionAbout_one_green_io = QtGui.QAction(MainWindow)
        self.actionAbout_one_green_io.setObjectName("actionAbout_one_green_io")
        self.actionDownload_latest = QtGui.QAction(MainWindow)
        self.actionDownload_latest.setObjectName("actionDownload_latest")
        self.menuHelp.addAction(self.actionCode_source)
        self.menuHelp.addAction(self.actionCode_source_2)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_one_green_io)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.Flash.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(
            _translate("MainWindow", "Check and install depdencies needed for flash")
        )
        self.label_2.setText(_translate("MainWindow", "Tool"))
        self.label_3.setText(_translate("MainWindow", "Check"))
        self.label_4.setText(_translate("MainWindow", "Install"))
        self.label_5.setText(_translate("MainWindow", "Status"))
        self.gitLabel.setText(_translate("MainWindow", "Git"))
        self.gitInstallButton.setText(_translate("MainWindow", "install"))
        self.pythonLabel.setText(_translate("MainWindow", "Python"))
        self.pythonInstallButton.setText(_translate("MainWindow", "install"))
        self.gitCheckButton.setText(_translate("MainWindow", "check"))
        self.gitStatusLabel.setText(_translate("MainWindow", "unknown"))
        self.pioCheckButton.setText(_translate("MainWindow", "check"))
        self.pioInstallButton.setText(_translate("MainWindow", "install"))
        self.pythonStatusLabel.setText(_translate("MainWindow", "unknown"))
        self.pythonCheckButton.setText(_translate("MainWindow", "check"))
        self.pioLabel.setText(_translate("MainWindow", "Platformio"))
        self.pioStatusLabel.setText(_translate("MainWindow", "unknown"))
        self.pipLabel.setText(_translate("MainWindow", "Pip"))
        self.pipCheckButton.setText(_translate("MainWindow", "check"))
        self.pipInstallButton.setText(_translate("MainWindow", "install"))
        self.pipStatusLabel.setText(_translate("MainWindow", "unknown"))
        self.checkAllButton.setText(_translate("MainWindow", "Check all"))
        self.Flash.setTabText(
            self.Flash.indexOf(self.tab), _translate("MainWindow", "Setup")
        )
        self.groupBox.setTitle(_translate("MainWindow", "Code source"))
        self.gitCloneOrFetchButton.setText(_translate("MainWindow", "Download/Update"))
        self.gitCloneOrFetchStatus.setText(_translate("MainWindow", "unknow"))
        self.gitCloneOrFetchStatusLabel.setText(_translate("MainWindow", "status:"))
        self.label_6.setText(_translate("MainWindow", "Repo:"))
        self.lineFirmwareGitRepo.setText(
            _translate("MainWindow", "https://github.com/One-Green/iot-edge-agent.git")
        )
        self.groupBox_2.setTitle(_translate("MainWindow", "Select version to flash"))
        self.gitCheckOutButton.setText(_translate("MainWindow", "Set version"))
        self.gitCheckOutStatus.setText(_translate("MainWindow", "unknow"))
        self.gitCheckOutStatusLabel.setText(_translate("MainWindow", "status:"))
        self.Flash.setTabText(
            self.Flash.indexOf(self.tab_3),
            _translate("MainWindow", "Download firmware"),
        )
        self.Flash.setTabText(
            self.Flash.indexOf(self.tab_2),
            _translate("MainWindow", "Core Configuration"),
        )
        self.Flash.setTabText(
            self.Flash.indexOf(self.tab_4), _translate("MainWindow", "Flash")
        )
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSetup_depdencies.setText(_translate("MainWindow", "New core"))
        self.actionAbout.setText(_translate("MainWindow", "Load core"))
        self.actionSprinkler.setText(_translate("MainWindow", "Sprinkler - esp32"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionWater_esp32.setText(_translate("MainWindow", "Water - esp32"))
        self.actionWater_mege.setText(_translate("MainWindow", "Water - mega"))
        self.actionLight_esp32.setText(_translate("MainWindow", "Light - esp32"))
        self.actionCode_source.setText(_translate("MainWindow", "Doc"))
        self.actionCode_source_2.setText(_translate("MainWindow", "Code source"))
        self.actionAbout_one_green_io.setText(
            _translate("MainWindow", "About one-green.io")
        )
        self.actionDownload_latest.setText(_translate("MainWindow", "Download latest"))
