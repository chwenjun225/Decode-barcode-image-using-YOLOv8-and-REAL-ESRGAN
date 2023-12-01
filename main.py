# Form implementation generated from reading ui file 'ui/myui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
import os

ROOT_PATH = os.getcwd() + "/"
TITLE_WINDOW = "AICT-LAB-705 - National Kaohsiung University Science and Technology"
ICON_WINDOW = ROOT_PATH + "icons/nkust.ico"


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow1.setEnabled(True)
        MainWindow1.resize(1450, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow1.sizePolicy().hasHeightForWidth())
        MainWindow1.setSizePolicy(sizePolicy)
        MainWindow1.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow1.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        MainWindow1.setFont(font)
        MainWindow1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        MainWindow1.setMouseTracking(True)
        MainWindow1.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        MainWindow1.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        MainWindow1.setAcceptDrops(False)
        icon = QtGui.QIcon.fromTheme(ICON_WINDOW)
        MainWindow1.setWindowIcon(icon)
        MainWindow1.setStatusTip("")
        MainWindow1.setAutoFillBackground(False)
        MainWindow1.setStyleSheet("")
        MainWindow1.setIconSize(QtCore.QSize(64, 64))
        MainWindow1.setAnimated(True)
        MainWindow1.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.label_quality_ok = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_quality_ok.setGeometry(QtCore.QRect(10, 420, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_quality_ok.setFont(font)
        self.label_quality_ok.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.label_quality_ok.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_quality_ok.setObjectName("label_quality_ok")
        self.label_quality_ng = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_quality_ng.setGeometry(QtCore.QRect(10, 490, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_quality_ng.setFont(font)
        self.label_quality_ng.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.label_quality_ng.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_quality_ng.setObjectName("label_quality_ng")
        self.push_start = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_start.setGeometry(QtCore.QRect(10, 10, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.push_start.setFont(font)
        self.push_start.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.push_start.setCheckable(False)
        self.push_start.setObjectName("push_start")
        self.push_stop = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_stop.setGeometry(QtCore.QRect(10, 80, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.push_stop.setFont(font)
        self.push_stop.setStyleSheet("background-color: rgb(255, 0, 0);\n" "border-color: rgb(0, 0, 0);")
        self.push_stop.setObjectName("push_stop")
        self.display_status_ok_ng = QtWidgets.QLabel(parent=self.centralwidget)
        self.display_status_ok_ng.setGeometry(QtCore.QRect(10, 150, 180, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.display_status_ok_ng.setFont(font)
        self.display_status_ok_ng.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.display_status_ok_ng.setAutoFillBackground(False)
        self.display_status_ok_ng.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.display_status_ok_ng.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.display_status_ok_ng.setText("...")
        self.display_status_ok_ng.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.display_status_ok_ng.setScaledContents(False)
        self.display_status_ok_ng.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.display_status_ok_ng.setIndent(-1)
        self.display_status_ok_ng.setObjectName("display_status_ok_ng")
        self.display0 = QtWidgets.QLabel(parent=self.centralwidget)
        self.display0.setEnabled(True)
        self.display0.setGeometry(QtCore.QRect(200, 10, 1000, 720))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.display0.setFont(font)
        self.display0.setAutoFillBackground(False)
        self.display0.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.display0.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.display0.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.display0.setObjectName("display0")
        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1450, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(parent=self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuConfig = QtWidgets.QMenu(parent=self.menubar)
        self.menuConfig.setObjectName("menuConfig")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout = QtWidgets.QMenu(parent=self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(parent=MainWindow1)
        self.action.setCheckable(True)
        self.action.setChecked(True)
        self.action.setVisible(False)
        self.action.setShortcutVisibleInContextMenu(False)
        self.action.setObjectName("action")
        self.actionOpen_Webcam = QtGui.QAction(parent=MainWindow1)
        self.actionOpen_Webcam.setObjectName("actionOpen_Webcam")
        self.actionExit = QtGui.QAction(parent=MainWindow1)
        self.actionExit.setObjectName("actionExit")
        self.actionChoose_AI_Models = QtGui.QAction(parent=MainWindow1)
        self.actionChoose_AI_Models.setCheckable(True)
        self.actionChoose_AI_Models.setObjectName("actionChoose_AI_Models")
        self.actionSetup_Camera = QtGui.QAction(parent=MainWindow1)
        self.actionSetup_Camera.setObjectName("actionSetup_Camera")
        self.actionCOM_port = QtGui.QAction(parent=MainWindow1)
        self.actionCOM_port.setObjectName("actionCOM_port")
        self.actionFormat_SFIS = QtGui.QAction(parent=MainWindow1)
        self.actionFormat_SFIS.setObjectName("actionFormat_SFIS")
        self.actionWelcome = QtGui.QAction(parent=MainWindow1)
        self.actionWelcome.setVisible(False)
        self.actionWelcome.setObjectName("actionWelcome")
        self.actionDocument = QtGui.QAction(parent=MainWindow1)
        self.actionDocument.setObjectName("actionDocument")
        self.actionVersion = QtGui.QAction(parent=MainWindow1)
        self.actionVersion.setObjectName("actionVersion")
        self.actionSuggestions_For_Improvement = QtGui.QAction(parent=MainWindow1)
        self.actionSuggestions_For_Improvement.setObjectName("actionSuggestions_For_Improvement")
        self.actionOpen_Image_Video = QtGui.QAction(parent=MainWindow1)
        self.actionOpen_Image_Video.setObjectName("actionOpen_Image_Video")
        self.actionOpen_Image_Video_2 = QtGui.QAction(parent=MainWindow1)
        self.actionOpen_Image_Video_2.setObjectName("actionOpen_Image_Video_2")
        self.actionOpen_Webcam_2 = QtGui.QAction(parent=MainWindow1)
        self.actionOpen_Webcam_2.setObjectName("actionOpen_Webcam_2")
        self.actionExit_2 = QtGui.QAction(parent=MainWindow1)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionWelcome_2 = QtGui.QAction(parent=MainWindow1)
        self.actionWelcome_2.setObjectName("actionWelcome_2")
        self.actionDocument_2 = QtGui.QAction(parent=MainWindow1)
        self.actionDocument_2.setObjectName("actionDocument_2")
        self.menuFile.addAction(self.actionOpen_Image_Video_2)
        self.menuFile.addAction(self.actionOpen_Webcam_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_2)
        self.menuSettings.addAction(self.actionChoose_AI_Models)
        self.menuSettings.addAction(self.actionSetup_Camera)
        self.menuConfig.addAction(self.actionCOM_port)
        self.menuConfig.addAction(self.actionFormat_SFIS)
        self.menuHelp.addAction(self.actionWelcome)
        self.menuHelp.addAction(self.actionWelcome_2)
        self.menuHelp.addAction(self.actionDocument_2)
        self.menuAbout.addAction(self.actionVersion)
        self.menuAbout.addAction(self.actionSuggestions_For_Improvement)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuConfig.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", TITLE_WINDOW))
        self.label_quality_ok.setText(_translate("MainWindow1", "OK: 0"))
        self.label_quality_ng.setText(_translate("MainWindow1", "NG: 0"))
        self.push_start.setText(_translate("MainWindow1", "START"))
        self.push_stop.setText(_translate("MainWindow1", "STOP"))
        self.display0.setText(_translate("MainWindow1", "NO DATA"))
        self.menuFile.setTitle(_translate("MainWindow1", "File"))
        self.menuSettings.setTitle(_translate("MainWindow1", "Settings"))
        self.menuConfig.setTitle(_translate("MainWindow1", "Config"))
        self.menuHelp.setTitle(_translate("MainWindow1", "Help"))
        self.menuAbout.setTitle(_translate("MainWindow1", "About"))
        self.action.setText(_translate("MainWindow1", "Open Image/Video..."))
        self.actionOpen_Webcam.setText(_translate("MainWindow1", "Open Webcam..."))
        self.actionExit.setText(_translate("MainWindow1", "Exit"))
        self.actionChoose_AI_Models.setText(_translate("MainWindow1", "Choose AI Model..."))
        self.actionSetup_Camera.setText(_translate("MainWindow1", "Setup Camera..."))
        self.actionCOM_port.setText(_translate("MainWindow1", "COM port..."))
        self.actionFormat_SFIS.setText(_translate("MainWindow1", "Format SFIS..."))
        self.actionWelcome.setText(_translate("MainWindow1", "Welcome..."))
        self.actionDocument.setText(_translate("MainWindow1", "Document..."))
        self.actionVersion.setText(_translate("MainWindow1", "Version..."))
        self.actionSuggestions_For_Improvement.setText(_translate("MainWindow1", "Suggestions For Improvement..."))
        self.actionOpen_Image_Video.setText(_translate("MainWindow1", "Open Image/Video..."))
        self.actionOpen_Image_Video_2.setText(_translate("MainWindow1", "Open Image/Video..."))
        self.actionOpen_Webcam_2.setText(_translate("MainWindow1", "Open Webcam..."))
        self.actionExit_2.setText(_translate("MainWindow1", "Exit..."))
        self.actionWelcome_2.setText(_translate("MainWindow1", "Welcome..."))
        self.actionDocument_2.setText(_translate("MainWindow1", "Document..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec())
