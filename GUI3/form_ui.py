# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QRadioButton, QScrollBar, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 550)
        MainWindow.setMinimumSize(QSize(800, 550))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 55))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toodle = QFrame(self.frame_top)
        self.frame_toodle.setObjectName(u"frame_toodle")
        self.frame_toodle.setMinimumSize(QSize(80, 55))
        self.frame_toodle.setMaximumSize(QSize(80, 55))
        self.frame_toodle.setStyleSheet(u"background:rgb(0,143,150);")
        self.frame_toodle.setFrameShape(QFrame.NoFrame)
        self.frame_toodle.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_toodle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toodle = QPushButton(self.frame_toodle)
        self.toodle.setObjectName(u"toodle")
        self.toodle.setMinimumSize(QSize(80, 55))
        self.toodle.setMaximumSize(QSize(80, 55))
        self.toodle.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(8, 62, 33);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(12, 100, 53);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(21, 176, 93);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/1x/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toodle.setIcon(icon)
        self.toodle.setIconSize(QSize(22, 12))
        self.toodle.setFlat(True)

        self.horizontalLayout_3.addWidget(self.toodle)


        self.horizontalLayout.addWidget(self.frame_toodle)

        self.frame_top_east = QFrame(self.frame_top)
        self.frame_top_east.setObjectName(u"frame_top_east")
        self.frame_top_east.setMaximumSize(QSize(16777215, 55))
        self.frame_top_east.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_top_east.setFrameShape(QFrame.NoFrame)
        self.frame_top_east.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_appname = QFrame(self.frame_top_east)
        self.frame_appname.setObjectName(u"frame_appname")
        self.frame_appname.setFrameShape(QFrame.NoFrame)
        self.frame_appname.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_appname)
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lab_appname = QLabel(self.frame_appname)
        self.lab_appname.setObjectName(u"lab_appname")
        font = QFont()
        font.setFamilies([u"Segoe UI Light"])
        font.setPointSize(24)
        self.lab_appname.setFont(font)
        self.lab_appname.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_10.addWidget(self.lab_appname)


        self.horizontalLayout_4.addWidget(self.frame_appname)

        self.frame_user = QFrame(self.frame_top_east)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setFrameShape(QFrame.NoFrame)
        self.frame_user.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_user)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lab_user = QLabel(self.frame_user)
        self.lab_user.setObjectName(u"lab_user")
        self.lab_user.setFont(font)
        self.lab_user.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_user.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lab_user)


        self.horizontalLayout_4.addWidget(self.frame_user)

        self.frame_person = QFrame(self.frame_top_east)
        self.frame_person.setObjectName(u"frame_person")
        self.frame_person.setMinimumSize(QSize(55, 55))
        self.frame_person.setMaximumSize(QSize(55, 55))
        self.frame_person.setFrameShape(QFrame.NoFrame)
        self.frame_person.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_person)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lab_person = QLabel(self.frame_person)
        self.lab_person.setObjectName(u"lab_person")
        self.lab_person.setMaximumSize(QSize(55, 55))
        self.lab_person.setPixmap(QPixmap(u"icons/1x/rc_logo.png"))
        self.lab_person.setScaledContents(True)
        self.lab_person.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lab_person)


        self.horizontalLayout_4.addWidget(self.frame_person)

        self.frame_min = QFrame(self.frame_top_east)
        self.frame_min.setObjectName(u"frame_min")
        self.frame_min.setMinimumSize(QSize(55, 55))
        self.frame_min.setMaximumSize(QSize(55, 55))
        self.frame_min.setFrameShape(QFrame.NoFrame)
        self.frame_min.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_min)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bn_min = QPushButton(self.frame_min)
        self.bn_min.setObjectName(u"bn_min")
        self.bn_min.setMaximumSize(QSize(55, 55))
        self.bn_min.setAutoFillBackground(False)
        self.bn_min.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(8, 62, 33);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(21, 176, 93);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/1x/minimize-8-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_min.setIcon(icon1)
        self.bn_min.setIconSize(QSize(22, 22))
        self.bn_min.setFlat(True)

        self.horizontalLayout_7.addWidget(self.bn_min)


        self.horizontalLayout_4.addWidget(self.frame_min)

        self.frame_max = QFrame(self.frame_top_east)
        self.frame_max.setObjectName(u"frame_max")
        self.frame_max.setMinimumSize(QSize(55, 55))
        self.frame_max.setMaximumSize(QSize(55, 55))
        self.frame_max.setFrameShape(QFrame.NoFrame)
        self.frame_max.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_max)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bn_max = QPushButton(self.frame_max)
        self.bn_max.setObjectName(u"bn_max")
        self.bn_max.setMaximumSize(QSize(55, 55))
        self.bn_max.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(8, 62, 33);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(21, 176, 93);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/1x/maximize-size.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_max.setIcon(icon2)
        self.bn_max.setIconSize(QSize(22, 22))
        self.bn_max.setFlat(True)

        self.horizontalLayout_6.addWidget(self.bn_max)


        self.horizontalLayout_4.addWidget(self.frame_max)

        self.frame_close = QFrame(self.frame_top_east)
        self.frame_close.setObjectName(u"frame_close")
        self.frame_close.setMinimumSize(QSize(55, 55))
        self.frame_close.setMaximumSize(QSize(55, 55))
        self.frame_close.setFrameShape(QFrame.NoFrame)
        self.frame_close.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_close)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bn_close = QPushButton(self.frame_close)
        self.bn_close.setObjectName(u"bn_close")
        self.bn_close.setMaximumSize(QSize(55, 55))
        self.bn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(8, 62, 33);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(21, 176, 93);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/1x/close_17.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_close.setIcon(icon3)
        self.bn_close.setIconSize(QSize(22, 22))
        self.bn_close.setFlat(True)

        self.horizontalLayout_5.addWidget(self.bn_close)


        self.horizontalLayout_4.addWidget(self.frame_close)


        self.horizontalLayout.addWidget(self.frame_top_east)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom_west = QFrame(self.frame_bottom)
        self.frame_bottom_west.setObjectName(u"frame_bottom_west")
        self.frame_bottom_west.setMinimumSize(QSize(80, 0))
        self.frame_bottom_west.setMaximumSize(QSize(80, 16777215))
        self.frame_bottom_west.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_bottom_west.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_west.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_home = QFrame(self.frame_bottom_west)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setMinimumSize(QSize(80, 55))
        self.frame_home.setMaximumSize(QSize(160, 55))
        self.frame_home.setFrameShape(QFrame.NoFrame)
        self.frame_home.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_home)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bn_home = QPushButton(self.frame_home)
        self.bn_home.setObjectName(u"bn_home")
        self.bn_home.setMinimumSize(QSize(80, 55))
        self.bn_home.setMaximumSize(QSize(160, 55))
        self.bn_home.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/1x/pngwing.com.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_home.setIcon(icon4)
        self.bn_home.setIconSize(QSize(22, 22))
        self.bn_home.setFlat(True)

        self.horizontalLayout_15.addWidget(self.bn_home)


        self.verticalLayout_3.addWidget(self.frame_home)

        self.frame_audit = QFrame(self.frame_bottom_west)
        self.frame_audit.setObjectName(u"frame_audit")
        self.frame_audit.setMinimumSize(QSize(80, 55))
        self.frame_audit.setMaximumSize(QSize(160, 55))
        self.frame_audit.setFrameShape(QFrame.NoFrame)
        self.frame_audit.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_audit)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.bn_audit = QPushButton(self.frame_audit)
        self.bn_audit.setObjectName(u"bn_audit")
        self.bn_audit.setMinimumSize(QSize(80, 55))
        self.bn_audit.setMaximumSize(QSize(160, 55))
        self.bn_audit.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/1x/kindpng_720992.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_audit.setIcon(icon5)
        self.bn_audit.setIconSize(QSize(22, 22))
        self.bn_audit.setFlat(True)

        self.horizontalLayout_16.addWidget(self.bn_audit)


        self.verticalLayout_3.addWidget(self.frame_audit)

        self.frame_settings = QFrame(self.frame_bottom_west)
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setMinimumSize(QSize(80, 55))
        self.frame_settings.setMaximumSize(QSize(160, 55))
        self.frame_settings.setFrameShape(QFrame.NoFrame)
        self.frame_settings.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_settings)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.bn_settings = QPushButton(self.frame_settings)
        self.bn_settings.setObjectName(u"bn_settings")
        self.bn_settings.setMinimumSize(QSize(80, 55))
        self.bn_settings.setMaximumSize(QSize(160, 55))
        self.bn_settings.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/1x/pngwing.com (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_settings.setIcon(icon6)
        self.bn_settings.setIconSize(QSize(20, 22))
        self.bn_settings.setFlat(True)

        self.horizontalLayout_18.addWidget(self.bn_settings)


        self.verticalLayout_3.addWidget(self.frame_settings)

        self.frame_8 = QFrame(self.frame_bottom_west)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_8)


        self.horizontalLayout_2.addWidget(self.frame_bottom_west)

        self.frame_bottom_east = QFrame(self.frame_bottom)
        self.frame_bottom_east.setObjectName(u"frame_bottom_east")
        self.frame_bottom_east.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_east.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_bottom_east)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 55))
        self.stackedWidget.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_19 = QHBoxLayout(self.page_home)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 5, 0, 5)
        self.frame_home_main = QFrame(self.page_home)
        self.frame_home_main.setObjectName(u"frame_home_main")
        self.frame_home_main.setFrameShape(QFrame.NoFrame)
        self.frame_home_main.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frame_home_main)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.lab_home_main_hed = QLabel(self.frame_home_main)
        self.lab_home_main_hed.setObjectName(u"lab_home_main_hed")
        self.lab_home_main_hed.setMinimumSize(QSize(0, 55))
        self.lab_home_main_hed.setMaximumSize(QSize(16777215, 55))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semilight"])
        font1.setPointSize(24)
        self.lab_home_main_hed.setFont(font1)
        self.lab_home_main_hed.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.lab_home_main_hed.setTextFormat(Qt.RichText)

        self.verticalLayout_5.addWidget(self.lab_home_main_hed)

        self.lab_home_main_disc = QLabel(self.frame_home_main)
        self.lab_home_main_disc.setObjectName(u"lab_home_main_disc")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        self.lab_home_main_disc.setFont(font2)
        self.lab_home_main_disc.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_home_main_disc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lab_home_main_disc.setWordWrap(True)
        self.lab_home_main_disc.setMargin(5)

        self.verticalLayout_5.addWidget(self.lab_home_main_disc)


        self.horizontalLayout_19.addWidget(self.frame_home_main)

        self.vert_divide = QFrame(self.page_home)
        self.vert_divide.setObjectName(u"vert_divide")
        self.vert_divide.setFrameShape(QFrame.VLine)
        self.vert_divide.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.vert_divide)

        self.frame_home_stat = QFrame(self.page_home)
        self.frame_home_stat.setObjectName(u"frame_home_stat")
        self.frame_home_stat.setMinimumSize(QSize(220, 0))
        self.frame_home_stat.setMaximumSize(QSize(220, 16777215))
        self.frame_home_stat.setFrameShape(QFrame.NoFrame)
        self.frame_home_stat.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame_home_stat)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.lab_home_stat_hed = QLabel(self.frame_home_stat)
        self.lab_home_stat_hed.setObjectName(u"lab_home_stat_hed")
        self.lab_home_stat_hed.setMinimumSize(QSize(0, 55))
        self.lab_home_stat_hed.setMaximumSize(QSize(16777215, 55))
        self.lab_home_stat_hed.setFont(font1)
        self.lab_home_stat_hed.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.lab_home_stat_hed.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lab_home_stat_hed)

        self.lab_home_stat_disc = QLabel(self.frame_home_stat)
        self.lab_home_stat_disc.setObjectName(u"lab_home_stat_disc")
        self.lab_home_stat_disc.setFont(font2)
        self.lab_home_stat_disc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.lab_home_stat_disc)


        self.horizontalLayout_19.addWidget(self.frame_home_stat)

        self.stackedWidget.addWidget(self.page_home)
        self.page_about_home = QWidget()
        self.page_about_home.setObjectName(u"page_about_home")
        self.page_about_home.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_13 = QVBoxLayout(self.page_about_home)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.lab_about_home = QLabel(self.page_about_home)
        self.lab_about_home.setObjectName(u"lab_about_home")
        self.lab_about_home.setMinimumSize(QSize(0, 55))
        self.lab_about_home.setMaximumSize(QSize(16777215, 55))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(24)
        self.lab_about_home.setFont(font3)
        self.lab_about_home.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_13.addWidget(self.lab_about_home)

        self.frame_about_home = QFrame(self.page_about_home)
        self.frame_about_home.setObjectName(u"frame_about_home")
        self.frame_about_home.setFrameShape(QFrame.StyledPanel)
        self.frame_about_home.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_about_home)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(5, 5, 0, 5)
        self.text_about_home = QTextEdit(self.frame_about_home)
        self.text_about_home.setObjectName(u"text_about_home")
        self.text_about_home.setEnabled(True)
        self.text_about_home.setFont(font2)
        self.text_about_home.setStyleSheet(u"color:rgb(255,255,255);")
        self.text_about_home.setFrameShape(QFrame.NoFrame)
        self.text_about_home.setFrameShadow(QFrame.Plain)
        self.text_about_home.setReadOnly(True)
        self.text_about_home.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.horizontalLayout_28.addWidget(self.text_about_home)

        self.vsb_about_home = QScrollBar(self.frame_about_home)
        self.vsb_about_home.setObjectName(u"vsb_about_home")
        self.vsb_about_home.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.vsb_about_home.setOrientation(Qt.Vertical)

        self.horizontalLayout_28.addWidget(self.vsb_about_home)


        self.verticalLayout_13.addWidget(self.frame_about_home)

        self.stackedWidget.addWidget(self.page_about_home)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_29 = QHBoxLayout(self.widget)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(30)
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color:rgb(255,255,255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_10)

        self.stackedWidget.addWidget(self.widget)
        self.page_about_settings = QWidget()
        self.page_about_settings.setObjectName(u"page_about_settings")
        self.page_about_settings.setStyleSheet(u"background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_settings)
        self.page_about_audit = QWidget()
        self.page_about_audit.setObjectName(u"page_about_audit")
        self.page_about_audit.setStyleSheet(u"background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_audit)
        self.page_audit = QWidget()
        self.page_audit.setObjectName(u"page_audit")
        self.page_audit.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_7 = QVBoxLayout(self.page_audit)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.lab_audit = QLabel(self.page_audit)
        self.lab_audit.setObjectName(u"lab_audit")
        self.lab_audit.setMinimumSize(QSize(0, 55))
        self.lab_audit.setMaximumSize(QSize(16777215, 55))
        self.lab_audit.setFont(font1)
        self.lab_audit.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_audit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lab_audit)

        self.frame_audit_main = QFrame(self.page_audit)
        self.frame_audit_main.setObjectName(u"frame_audit_main")
        self.frame_audit_main.setMinimumSize(QSize(0, 200))
        self.frame_audit_main.setMaximumSize(QSize(16777215, 200))
        self.frame_audit_main.setFrameShape(QFrame.NoFrame)
        self.frame_audit_main.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame_audit_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lab_bullet2 = QLabel(self.frame_audit_main)
        self.lab_bullet2.setObjectName(u"lab_bullet2")
        self.lab_bullet2.setMaximumSize(QSize(5, 16777215))
        self.lab_bullet2.setPixmap(QPixmap(u"icons/1x/bulletAsset 54.png"))

        self.gridLayout.addWidget(self.lab_bullet2, 1, 0, 1, 1)

        self.lab_audit2 = QLabel(self.frame_audit_main)
        self.lab_audit2.setObjectName(u"lab_audit2")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(14)
        self.lab_audit2.setFont(font5)
        self.lab_audit2.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout.addWidget(self.lab_audit2, 1, 1, 1, 1)

        self.lab_bullet = QLabel(self.frame_audit_main)
        self.lab_bullet.setObjectName(u"lab_bullet")
        self.lab_bullet.setMaximumSize(QSize(5, 16777215))
        self.lab_bullet.setPixmap(QPixmap(u"icons/1x/bulletAsset 54.png"))
        self.lab_bullet.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lab_bullet, 0, 0, 1, 1)

        self.export_path = QLineEdit(self.frame_audit_main)
        self.export_path.setObjectName(u"export_path")

        self.gridLayout.addWidget(self.export_path, 4, 1, 1, 1)

        self.lab_audit_action = QLabel(self.frame_audit_main)
        self.lab_audit_action.setObjectName(u"lab_audit_action")
        self.lab_audit_action.setMinimumSize(QSize(0, 20))
        self.lab_audit_action.setMaximumSize(QSize(16777215, 30))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(16)
        self.lab_audit_action.setFont(font6)
        self.lab_audit_action.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_audit_action.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.lab_audit_action, 3, 5, 1, 2)

        self.lab_audit3 = QLabel(self.frame_audit_main)
        self.lab_audit3.setObjectName(u"lab_audit3")
        self.lab_audit3.setFont(font5)

        self.gridLayout.addWidget(self.lab_audit3, 2, 1, 1, 4)

        self.browseButton = QPushButton(self.frame_audit_main)
        self.browseButton.setObjectName(u"browseButton")

        self.gridLayout.addWidget(self.browseButton, 4, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(421, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 5, 1, 3)

        self.lab_bullet3 = QLabel(self.frame_audit_main)
        self.lab_bullet3.setObjectName(u"lab_bullet3")
        self.lab_bullet3.setMaximumSize(QSize(5, 16777215))
        self.lab_bullet3.setPixmap(QPixmap(u"icons/1x/bulletAsset 54.png"))

        self.gridLayout.addWidget(self.lab_bullet3, 2, 0, 1, 1)

        self.lab_audit1 = QLabel(self.frame_audit_main)
        self.lab_audit1.setObjectName(u"lab_audit1")
        self.lab_audit1.setMinimumSize(QSize(0, 0))
        self.lab_audit1.setMaximumSize(QSize(16777215, 16777215))
        self.lab_audit1.setFont(font5)
        self.lab_audit1.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_audit1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.lab_audit1, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 5, 1, 1, 1)

        self.bn_audit_start = QPushButton(self.frame_audit_main)
        self.bn_audit_start.setObjectName(u"bn_audit_start")
        self.bn_audit_start.setMinimumSize(QSize(69, 25))
        self.bn_audit_start.setMaximumSize(QSize(69, 25))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(12)
        self.bn_audit_start.setFont(font7)
        self.bn_audit_start.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(8, 62, 33);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(17, 138, 73);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.bn_audit_start.setCheckable(False)
        self.bn_audit_start.setFlat(True)

        self.gridLayout.addWidget(self.bn_audit_start, 3, 7, 1, 1)

        self.progressBar_audit = QProgressBar(self.frame_audit_main)
        self.progressBar_audit.setObjectName(u"progressBar_audit")
        self.progressBar_audit.setEnabled(True)
        self.progressBar_audit.setStyleSheet(u"QProgressBar\n"
"{\n"
"	color:rgb(255,255,255);\n"
"	background-color :rgb(51,51,51);\n"
"	border : 2px;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border : 2px;\n"
"	border-radius:4px;\n"
"	background-color:rgb(213, 224, 78);\n"
"}")
        self.progressBar_audit.setValue(0)
        self.progressBar_audit.setAlignment(Qt.AlignCenter)
        self.progressBar_audit.setTextVisible(True)
        self.progressBar_audit.setOrientation(Qt.Horizontal)
        self.progressBar_audit.setInvertedAppearance(False)
        self.progressBar_audit.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout.addWidget(self.progressBar_audit, 4, 5, 1, 3)


        self.verticalLayout_7.addWidget(self.frame_audit_main)

        self.stackedWidget.addWidget(self.page_audit)
        self.widget_2 = QWidget()
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.lab_cloud_main = QLabel(self.widget_2)
        self.lab_cloud_main.setObjectName(u"lab_cloud_main")
        self.lab_cloud_main.setMinimumSize(QSize(0, 55))
        self.lab_cloud_main.setMaximumSize(QSize(16777215, 55))
        self.lab_cloud_main.setFont(font3)
        self.lab_cloud_main.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout_8.addWidget(self.lab_cloud_main)

        self.verticalSpacer_2 = QSpacerItem(20, 162, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.widget_2)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.page_settings.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_9 = QVBoxLayout(self.page_settings)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_settings_menu = QFrame(self.page_settings)
        self.frame_settings_menu.setObjectName(u"frame_settings_menu")
        self.frame_settings_menu.setMinimumSize(QSize(0, 30))
        self.frame_settings_menu.setMaximumSize(QSize(16777215, 30))
        self.frame_settings_menu.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_settings_menu.setFrameShape(QFrame.NoFrame)
        self.frame_settings_menu.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_settings_menu)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_settings_clean = QFrame(self.frame_settings_menu)
        self.frame_settings_clean.setObjectName(u"frame_settings_clean")
        self.frame_settings_clean.setMinimumSize(QSize(80, 30))
        self.frame_settings_clean.setMaximumSize(QSize(80, 30))
        self.frame_settings_clean.setFrameShape(QFrame.NoFrame)
        self.frame_settings_clean.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_settings_clean)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.bn_settings_clean = QPushButton(self.frame_settings_clean)
        self.bn_settings_clean.setObjectName(u"bn_settings_clean")
        self.bn_settings_clean.setMinimumSize(QSize(80, 30))
        self.bn_settings_clean.setMaximumSize(QSize(80, 30))
        self.bn_settings_clean.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/1x/bulletAsset 54.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_settings_clean.setIcon(icon7)
        self.bn_settings_clean.setFlat(True)

        self.horizontalLayout_23.addWidget(self.bn_settings_clean)


        self.horizontalLayout_20.addWidget(self.frame_settings_clean)

        self.frame_settings_world = QFrame(self.frame_settings_menu)
        self.frame_settings_world.setObjectName(u"frame_settings_world")
        self.frame_settings_world.setMinimumSize(QSize(80, 30))
        self.frame_settings_world.setMaximumSize(QSize(80, 30))
        self.frame_settings_world.setFrameShape(QFrame.NoFrame)
        self.frame_settings_world.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_settings_world)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.bn_settings_world = QPushButton(self.frame_settings_world)
        self.bn_settings_world.setObjectName(u"bn_settings_world")
        self.bn_settings_world.setMinimumSize(QSize(80, 30))
        self.bn_settings_world.setMaximumSize(QSize(80, 30))
        self.bn_settings_world.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_settings_world.setIcon(icon7)
        self.bn_settings_world.setFlat(True)

        self.horizontalLayout_24.addWidget(self.bn_settings_world)


        self.horizontalLayout_20.addWidget(self.frame_settings_world)

        self.horizontalSpacer_4 = QSpacerItem(397, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addWidget(self.frame_settings_menu)

        self.stackedWidget_settings = QStackedWidget(self.page_settings)
        self.stackedWidget_settings.setObjectName(u"stackedWidget_settings")
        self.stackedWidget_settings.setStyleSheet(u"background:rgb(91,90,90);")
        self.page_android_contact = QWidget()
        self.page_android_contact.setObjectName(u"page_android_contact")
        self.page_android_contact.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_10 = QVBoxLayout(self.page_android_contact)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.lab_android_contact = QLabel(self.page_android_contact)
        self.lab_android_contact.setObjectName(u"lab_android_contact")
        self.lab_android_contact.setMinimumSize(QSize(0, 55))
        self.lab_android_contact.setMaximumSize(QSize(16777215, 55))
        self.lab_android_contact.setFont(font3)
        self.lab_android_contact.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_10.addWidget(self.lab_android_contact)

        self.frame_android_bottom = QFrame(self.page_android_contact)
        self.frame_android_bottom.setObjectName(u"frame_android_bottom")
        self.frame_android_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_android_bottom.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_android_bottom)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.lab_person_icon = QLabel(self.frame_android_bottom)
        self.lab_person_icon.setObjectName(u"lab_person_icon")
        self.lab_person_icon.setMinimumSize(QSize(200, 160))
        self.lab_person_icon.setMaximumSize(QSize(200, 160))
        self.lab_person_icon.setPixmap(QPixmap(u"icons/1x/peopleAsset 62.png"))

        self.gridLayout_3.addWidget(self.lab_person_icon, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.frame_android_field = QFrame(self.frame_android_bottom)
        self.frame_android_field.setObjectName(u"frame_android_field")
        self.frame_android_field.setFrameShape(QFrame.NoFrame)
        self.frame_android_field.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frame_android_field)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_8 = QLabel(self.frame_android_field)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_8, 7, 0, 1, 1)

        self.label_6 = QLabel(self.frame_android_field)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_7 = QLabel(self.frame_android_field)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_7, 5, 0, 1, 1)

        self.label = QLabel(self.frame_android_field)
        self.label.setObjectName(u"label")
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 3)

        self.line_android_name = QLineEdit(self.frame_android_field)
        self.line_android_name.setObjectName(u"line_android_name")
        self.line_android_name.setEnabled(False)
        self.line_android_name.setMinimumSize(QSize(300, 25))
        self.line_android_name.setMaximumSize(QSize(400, 25))
        self.line_android_name.setFont(font7)
        self.line_android_name.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.line_android_name, 1, 3, 1, 1)

        self.label_5 = QLabel(self.frame_android_field)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 3)

        self.line_android_org = QLineEdit(self.frame_android_field)
        self.line_android_org.setObjectName(u"line_android_org")
        self.line_android_org.setEnabled(False)
        self.line_android_org.setMinimumSize(QSize(300, 25))
        self.line_android_org.setMaximumSize(QSize(400, 25))
        self.line_android_org.setFont(font7)
        self.line_android_org.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.line_android_org, 4, 3, 1, 1)

        self.line_android_adress = QLineEdit(self.frame_android_field)
        self.line_android_adress.setObjectName(u"line_android_adress")
        self.line_android_adress.setEnabled(False)
        self.line_android_adress.setMinimumSize(QSize(300, 25))
        self.line_android_adress.setMaximumSize(QSize(400, 25))
        self.line_android_adress.setFont(font7)
        self.line_android_adress.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.line_android_adress, 3, 3, 1, 1)

        self.line_android_ph = QLineEdit(self.frame_android_field)
        self.line_android_ph.setObjectName(u"line_android_ph")
        self.line_android_ph.setEnabled(False)
        self.line_android_ph.setMinimumSize(QSize(300, 25))
        self.line_android_ph.setMaximumSize(QSize(400, 25))
        self.line_android_ph.setFont(font7)
        self.line_android_ph.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.line_android_ph, 7, 3, 1, 1)

        self.line_android_email = QLineEdit(self.frame_android_field)
        self.line_android_email.setObjectName(u"line_android_email")
        self.line_android_email.setEnabled(False)
        self.line_android_email.setMinimumSize(QSize(300, 25))
        self.line_android_email.setMaximumSize(QSize(400, 25))
        self.line_android_email.setFont(font7)
        self.line_android_email.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.line_android_email, 5, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 8, 8, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 4, 8, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 9, 3, 1, 1)

        self.frame_3 = QFrame(self.frame_android_field)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(100, 0, 0, 0)
        self.bn_android_contact_edit = QPushButton(self.frame_3)
        self.bn_android_contact_edit.setObjectName(u"bn_android_contact_edit")
        self.bn_android_contact_edit.setMinimumSize(QSize(69, 25))
        self.bn_android_contact_edit.setMaximumSize(QSize(69, 25))
        self.bn_android_contact_edit.setFont(font7)
        self.bn_android_contact_edit.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_25.addWidget(self.bn_android_contact_edit)

        self.bn_android_contact_share = QPushButton(self.frame_3)
        self.bn_android_contact_share.setObjectName(u"bn_android_contact_share")
        self.bn_android_contact_share.setMinimumSize(QSize(69, 25))
        self.bn_android_contact_share.setMaximumSize(QSize(69, 25))
        self.bn_android_contact_share.setFont(font7)
        self.bn_android_contact_share.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_25.addWidget(self.bn_android_contact_share)

        self.bn_android_contact_delete = QPushButton(self.frame_3)
        self.bn_android_contact_delete.setObjectName(u"bn_android_contact_delete")
        self.bn_android_contact_delete.setMinimumSize(QSize(69, 25))
        self.bn_android_contact_delete.setMaximumSize(QSize(69, 25))
        self.bn_android_contact_delete.setFont(font7)
        self.bn_android_contact_delete.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(112,0,0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_25.addWidget(self.bn_android_contact_delete)

        self.bn_android_contact_save = QPushButton(self.frame_3)
        self.bn_android_contact_save.setObjectName(u"bn_android_contact_save")
        self.bn_android_contact_save.setEnabled(False)
        self.bn_android_contact_save.setMinimumSize(QSize(69, 25))
        self.bn_android_contact_save.setMaximumSize(QSize(69, 25))
        self.bn_android_contact_save.setFont(font7)
        self.bn_android_contact_save.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_25.addWidget(self.bn_android_contact_save)


        self.gridLayout_4.addWidget(self.frame_3, 8, 0, 1, 7)


        self.gridLayout_3.addWidget(self.frame_android_field, 0, 1, 2, 1)


        self.verticalLayout_10.addWidget(self.frame_android_bottom)

        self.stackedWidget_settings.addWidget(self.page_android_contact)
        self.page_android_game = QWidget()
        self.page_android_game.setObjectName(u"page_android_game")
        self.page_android_game.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_11 = QVBoxLayout(self.page_android_game)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.lab_gamepad = QLabel(self.page_android_game)
        self.lab_gamepad.setObjectName(u"lab_gamepad")
        self.lab_gamepad.setMinimumSize(QSize(0, 55))
        self.lab_gamepad.setMaximumSize(QSize(16777215, 55))
        self.lab_gamepad.setFont(font3)
        self.lab_gamepad.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_11.addWidget(self.lab_gamepad)

        self.frame_textbar = QFrame(self.page_android_game)
        self.frame_textbar.setObjectName(u"frame_textbar")
        self.frame_textbar.setStyleSheet(u"background:rgb(91,90,90);")
        self.frame_textbar.setFrameShape(QFrame.StyledPanel)
        self.frame_textbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_textbar)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(5, 0, 0, 0)
        self.textEdit_gamepad = QTextEdit(self.frame_textbar)
        self.textEdit_gamepad.setObjectName(u"textEdit_gamepad")
        self.textEdit_gamepad.setFont(font7)
        self.textEdit_gamepad.setStyleSheet(u"color:rgb(255,255,255);")
        self.textEdit_gamepad.setFrameShape(QFrame.NoFrame)
        self.textEdit_gamepad.setFrameShadow(QFrame.Plain)
        self.textEdit_gamepad.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textEdit_gamepad.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_26.addWidget(self.textEdit_gamepad)

        self.vsb_gamepad = QScrollBar(self.frame_textbar)
        self.vsb_gamepad.setObjectName(u"vsb_gamepad")
        self.vsb_gamepad.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.vsb_gamepad.setOrientation(Qt.Vertical)
        self.vsb_gamepad.setInvertedControls(True)

        self.horizontalLayout_26.addWidget(self.vsb_gamepad)


        self.verticalLayout_11.addWidget(self.frame_textbar)

        self.stackedWidget_settings.addWidget(self.page_android_game)
        self.page_settings_clean = QWidget()
        self.page_settings_clean.setObjectName(u"page_settings_clean")
        self.page_settings_clean.setStyleSheet(u"background:rgb(91,90,90);")
        self.gridLayout_5 = QGridLayout(self.page_settings_clean)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.groupBox_passes = QGroupBox(self.page_settings_clean)
        self.groupBox_passes.setObjectName(u"groupBox_passes")
        self.onlysec_audit = QRadioButton(self.groupBox_passes)
        self.onlysec_audit.setObjectName(u"onlysec_audit")
        self.onlysec_audit.setGeometry(QRect(10, 60, 211, 22))
        self.line_2 = QFrame(self.groupBox_passes)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 180, 211, 21))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_spsettings = QLabel(self.groupBox_passes)
        self.label_spsettings.setObjectName(u"label_spsettings")
        self.label_spsettings.setGeometry(QRect(8, 29, 221, 21))
        font8 = QFont()
        font8.setBold(True)
        self.label_spsettings.setFont(font8)
        self.label_spsettings.setFrameShape(QFrame.Box)
        self.label_spsettings.setAlignment(Qt.AlignCenter)
        self.secweek_audit = QRadioButton(self.groupBox_passes)
        self.secweek_audit.setObjectName(u"secweek_audit")
        self.secweek_audit.setGeometry(QRect(10, 90, 221, 22))
        self.secweek_audit.setAutoExclusive(True)
        self.radioButton_clearselec = QRadioButton(self.groupBox_passes)
        self.radioButton_clearselec.setObjectName(u"radioButton_clearselec")
        self.radioButton_clearselec.setGeometry(QRect(10, 120, 221, 22))
        self.label_3 = QLabel(self.groupBox_passes)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(8, 150, 211, 20))
        self.lineEdit_sptripid = QLineEdit(self.groupBox_passes)
        self.lineEdit_sptripid.setObjectName(u"lineEdit_sptripid")
        self.lineEdit_sptripid.setGeometry(QRect(10, 150, 211, 24))
        self.output_label = QLabel(self.groupBox_passes)
        self.output_label.setObjectName(u"output_label")
        self.output_label.setGeometry(QRect(8, 200, 211, 20))
        self.output_label.setFont(font8)
        self.output_label.setFrameShape(QFrame.Box)
        self.output_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.checkBox_alloutputs = QCheckBox(self.groupBox_passes)
        self.checkBox_alloutputs.setObjectName(u"checkBox_alloutputs")
        self.checkBox_alloutputs.setGeometry(QRect(10, 220, 211, 22))
        self.checkBox_alloutputs.setChecked(True)
        self.checkBox_payableout = QCheckBox(self.groupBox_passes)
        self.checkBox_payableout.setObjectName(u"checkBox_payableout")
        self.checkBox_payableout.setGeometry(QRect(10, 240, 211, 22))
        self.checkBox_payableout.setChecked(True)
        self.checkBox_flagout = QCheckBox(self.groupBox_passes)
        self.checkBox_flagout.setObjectName(u"checkBox_flagout")
        self.checkBox_flagout.setGeometry(QRect(10, 260, 211, 22))
        self.checkBox_flagout.setChecked(True)
        self.checkBox_taxiout = QCheckBox(self.groupBox_passes)
        self.checkBox_taxiout.setObjectName(u"checkBox_taxiout")
        self.checkBox_taxiout.setGeometry(QRect(10, 280, 211, 22))
        self.checkBox_taxiout.setChecked(True)

        self.gridLayout_5.addWidget(self.groupBox_passes, 5, 4, 2, 1)

        self.groupBox_flags = QGroupBox(self.page_settings_clean)
        self.groupBox_flags.setObjectName(u"groupBox_flags")
        self.checkBox_selectall = QCheckBox(self.groupBox_flags)
        self.checkBox_selectall.setObjectName(u"checkBox_selectall")
        self.checkBox_selectall.setGeometry(QRect(10, 30, 211, 22))
        self.checkBox_selectall.setChecked(True)
        self.checkBox_bprovider = QCheckBox(self.groupBox_flags)
        self.checkBox_bprovider.setObjectName(u"checkBox_bprovider")
        self.checkBox_bprovider.setGeometry(QRect(10, 60, 201, 22))
        self.checkBox_bprovider.setChecked(True)
        self.checkBox_candd = QCheckBox(self.groupBox_flags)
        self.checkBox_candd.setObjectName(u"checkBox_candd")
        self.checkBox_candd.setGeometry(QRect(10, 80, 211, 22))
        self.checkBox_candd.setChecked(True)
        self.checkBox_tddate = QCheckBox(self.groupBox_flags)
        self.checkBox_tddate.setObjectName(u"checkBox_tddate")
        self.checkBox_tddate.setGeometry(QRect(10, 100, 211, 22))
        self.checkBox_tddate.setChecked(True)
        self.checkBox_duptrip = QCheckBox(self.groupBox_flags)
        self.checkBox_duptrip.setObjectName(u"checkBox_duptrip")
        self.checkBox_duptrip.setGeometry(QRect(10, 120, 211, 22))
        self.checkBox_duptrip.setChecked(True)
        self.checkBox_1leg = QCheckBox(self.groupBox_flags)
        self.checkBox_1leg.setObjectName(u"checkBox_1leg")
        self.checkBox_1leg.setGeometry(QRect(10, 140, 211, 22))
        self.checkBox_1leg.setChecked(True)
        self.checkBox_ooa = QCheckBox(self.groupBox_flags)
        self.checkBox_ooa.setObjectName(u"checkBox_ooa")
        self.checkBox_ooa.setGeometry(QRect(10, 160, 191, 22))
        self.checkBox_ooa.setChecked(True)
        self.checkBox_trippurp = QCheckBox(self.groupBox_flags)
        self.checkBox_trippurp.setObjectName(u"checkBox_trippurp")
        self.checkBox_trippurp.setGeometry(QRect(10, 180, 211, 22))
        self.checkBox_trippurp.setChecked(True)
        self.checkBox_compwcan = QCheckBox(self.groupBox_flags)
        self.checkBox_compwcan.setObjectName(u"checkBox_compwcan")
        self.checkBox_compwcan.setGeometry(QRect(10, 200, 201, 22))
        self.checkBox_compwcan.setChecked(True)
        self.checkBox_excapps = QCheckBox(self.groupBox_flags)
        self.checkBox_excapps.setObjectName(u"checkBox_excapps")
        self.checkBox_excapps.setGeometry(QRect(10, 220, 211, 22))
        self.checkBox_excapps.setChecked(True)
        self.checkBox_paiddups = QCheckBox(self.groupBox_flags)
        self.checkBox_paiddups.setObjectName(u"checkBox_paiddups")
        self.checkBox_paiddups.setGeometry(QRect(10, 240, 221, 22))
        self.checkBox_paiddups.setChecked(True)
        self.line_3 = QFrame(self.groupBox_flags)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 39, 221, 31))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.raise_()
        self.checkBox_selectall.raise_()
        self.checkBox_bprovider.raise_()
        self.checkBox_candd.raise_()
        self.checkBox_tddate.raise_()
        self.checkBox_duptrip.raise_()
        self.checkBox_1leg.raise_()
        self.checkBox_ooa.raise_()
        self.checkBox_trippurp.raise_()
        self.checkBox_compwcan.raise_()
        self.checkBox_excapps.raise_()
        self.checkBox_paiddups.raise_()

        self.gridLayout_5.addWidget(self.groupBox_flags, 5, 0, 2, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 7, 4, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_6, 0, 4, 1, 1)

        self.groupBox_output = QGroupBox(self.page_settings_clean)
        self.groupBox_output.setObjectName(u"groupBox_output")
        self.lineEdit_resultOutput_path = QLineEdit(self.groupBox_output)
        self.lineEdit_resultOutput_path.setObjectName(u"lineEdit_resultOutput_path")
        self.lineEdit_resultOutput_path.setGeometry(QRect(10, 100, 211, 24))
        self.label_4 = QLabel(self.groupBox_output)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 30, 211, 61))
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.browseButton_output = QPushButton(self.groupBox_output)
        self.browseButton_output.setObjectName(u"browseButton_output")
        self.browseButton_output.setGeometry(QRect(169, 130, 51, 24))

        self.gridLayout_5.addWidget(self.groupBox_output, 5, 6, 2, 1)

        self.stackedWidget_settings.addWidget(self.page_settings_clean)
        self.page_android_world = QWidget()
        self.page_android_world.setObjectName(u"page_android_world")
        self.page_android_world.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_27 = QHBoxLayout(self.page_android_world)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_9 = QLabel(self.page_android_world)
        self.label_9.setObjectName(u"label_9")
        font9 = QFont()
        font9.setFamilies([u"Segoe UI Light"])
        font9.setPointSize(30)
        self.label_9.setFont(font9)
        self.label_9.setStyleSheet(u"color:rgb(255,255,255);")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)

        self.horizontalLayout_27.addWidget(self.label_9)

        self.stackedWidget_settings.addWidget(self.page_android_world)

        self.verticalLayout_9.addWidget(self.stackedWidget_settings)

        self.stackedWidget.addWidget(self.page_settings)

        self.horizontalLayout_14.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_low = QFrame(self.frame_bottom_east)
        self.frame_low.setObjectName(u"frame_low")
        self.frame_low.setMinimumSize(QSize(0, 20))
        self.frame_low.setMaximumSize(QSize(16777215, 20))
        self.frame_low.setStyleSheet(u"")
        self.frame_low.setFrameShape(QFrame.NoFrame)
        self.frame_low.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_low)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_tab = QFrame(self.frame_low)
        self.frame_tab.setObjectName(u"frame_tab")
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        self.frame_tab.setFont(font10)
        self.frame_tab.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_tab.setFrameShape(QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lab_tab = QLabel(self.frame_tab)
        self.lab_tab.setObjectName(u"lab_tab")
        font11 = QFont()
        font11.setFamilies([u"Segoe UI Light"])
        font11.setPointSize(10)
        self.lab_tab.setFont(font11)
        self.lab_tab.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_12.addWidget(self.lab_tab)


        self.horizontalLayout_11.addWidget(self.frame_tab)

        self.frame_drag = QFrame(self.frame_low)
        self.frame_drag.setObjectName(u"frame_drag")
        self.frame_drag.setMinimumSize(QSize(20, 20))
        self.frame_drag.setMaximumSize(QSize(20, 20))
        self.frame_drag.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_drag.setFrameShape(QFrame.NoFrame)
        self.frame_drag.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_drag)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.frame_drag)


        self.verticalLayout_2.addWidget(self.frame_low)


        self.horizontalLayout_2.addWidget(self.frame_bottom_east)


        self.verticalLayout.addWidget(self.frame_bottom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.onlysec_audit.toggled.connect(self.secweek_audit.setDisabled)
        self.secweek_audit.toggled.connect(self.onlysec_audit.setDisabled)
        self.radioButton_clearselec.toggled.connect(self.secweek_audit.setEnabled)
        self.radioButton_clearselec.toggled.connect(self.onlysec_audit.setEnabled)
        self.checkBox_selectall.toggled.connect(self.checkBox_bprovider.setChecked)
        self.checkBox_selectall.toggled.connect(self.checkBox_candd.setChecked)
        self.checkBox_selectall.toggled.connect(self.checkBox_tddate.setChecked)
        self.checkBox_selectall.toggled.connect(self.checkBox_duptrip.setChecked)
        self.checkBox_selectall.toggled.connect(self.checkBox_1leg.setChecked)
        self.checkBox_selectall.toggled.connect(self.checkBox_ooa.setChecked)
        self.checkBox_selectall.toggled.connect(self.checkBox_trippurp.setChecked)
        self.checkBox_selectall.toggled.connect(self.checkBox_compwcan.setChecked)
        self.checkBox_selectall.toggled.connect(self.checkBox_excapps.setChecked)
        self.checkBox_selectall.toggled.connect(self.checkBox_paiddups.setChecked)
        self.browseButton_output.clicked.connect(self.lineEdit_resultOutput_path.clear)
        self.browseButton_output.clicked.connect(self.lineEdit_resultOutput_path.paste)
        self.browseButton.clicked.connect(self.export_path.clear)
        self.browseButton.released.connect(self.export_path.paste)
        self.checkBox_alloutputs.toggled.connect(self.checkBox_payableout.setChecked)
        self.checkBox_alloutputs.toggled.connect(self.checkBox_flagout.setChecked)
        self.checkBox_alloutputs.toggled.connect(self.checkBox_taxiout.setChecked)
        self.lineEdit_sptripid.textEdited.connect(self.lineEdit_sptripid.clear)

        self.stackedWidget.setCurrentIndex(7)
        self.stackedWidget_settings.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toodle.setText("")
        self.lab_appname.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lab_user.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lab_person.setText("")
#if QT_CONFIG(tooltip)
        self.bn_min.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_min.setText("")
#if QT_CONFIG(tooltip)
        self.bn_max.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_max.setText("")
#if QT_CONFIG(tooltip)
        self.bn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.bn_close.setText("")
#if QT_CONFIG(tooltip)
        self.bn_home.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.bn_home.setText("")
#if QT_CONFIG(tooltip)
        self.bn_audit.setToolTip(QCoreApplication.translate("MainWindow", u"Run Audit Here", None))
#endif // QT_CONFIG(tooltip)
        self.bn_audit.setText("")
#if QT_CONFIG(tooltip)
        self.bn_settings.setToolTip(QCoreApplication.translate("MainWindow", u"Audit Settings", None))
#endif // QT_CONFIG(tooltip)
        self.bn_settings.setText("")
        self.lab_home_main_hed.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Instructions</span></p><p><br/></p></body></html>", None))
        self.lab_home_main_disc.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Will put instructions</p></body></html>", None))
        self.lab_home_stat_hed.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Extra Info</span></p><p><br/></p></body></html>", None))
        self.lab_home_stat_disc.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Boop bop do do do </span></p></body></html>", None))
        self.lab_about_home.setText(QCoreApplication.translate("MainWindow", u"About: Home", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Empty", None))
        self.lab_audit.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Run Audit</span></p></body></html>", None))
        self.lab_bullet2.setText("")
        self.lab_audit2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Make sure appropriate settings are set</span></p></body></html>", None))
        self.lab_bullet.setText("")
        self.export_path.setText(QCoreApplication.translate("MainWindow", u"Input Ecolane Export Path", None))
        self.lab_audit_action.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Push to Perform Audit:</span></p></body></html>", None))
        self.lab_audit3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Make sure the file is a .csv or .xlsx </span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>", None))
        self.browseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.lab_bullet3.setText("")
        self.lab_audit1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Select Ecolane Export Path</span></p></body></html>", None))
        self.bn_audit_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.lab_cloud_main.setText(QCoreApplication.translate("MainWindow", u"Cloud Connect", None))
#if QT_CONFIG(tooltip)
        self.bn_settings_clean.setToolTip(QCoreApplication.translate("MainWindow", u"Clean", None))
#endif // QT_CONFIG(tooltip)
        self.bn_settings_clean.setText("")
#if QT_CONFIG(tooltip)
        self.bn_settings_world.setToolTip(QCoreApplication.translate("MainWindow", u"World", None))
#endif // QT_CONFIG(tooltip)
        self.bn_settings_world.setText("")
        self.lab_android_contact.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.lab_person_icon.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ph:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Organisation:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.line_android_name.setText(QCoreApplication.translate("MainWindow", u"ALBERT EINSTEIN", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Adress: ", None))
        self.line_android_org.setText(QCoreApplication.translate("MainWindow", u"Physist", None))
        self.line_android_adress.setText(QCoreApplication.translate("MainWindow", u"112 Mercer Street", None))
        self.line_android_email.setText(QCoreApplication.translate("MainWindow", u"einstein@gmail.com", None))
        self.bn_android_contact_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.bn_android_contact_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.bn_android_contact_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bn_android_contact_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.lab_gamepad.setText(QCoreApplication.translate("MainWindow", u"GamePad", None))
        self.groupBox_passes.setTitle(QCoreApplication.translate("MainWindow", u"Audit Settings", None))
        self.onlysec_audit.setText(QCoreApplication.translate("MainWindow", u"Secondary Audit Only", None))
        self.label_spsettings.setText(QCoreApplication.translate("MainWindow", u"Check To Include Secondary Payments", None))
        self.secweek_audit.setText(QCoreApplication.translate("MainWindow", u"Include Secondary Audit With Weekly", None))
        self.radioButton_clearselec.setText(QCoreApplication.translate("MainWindow", u"Clear Selection", None))
        self.label_3.setText("")
        self.lineEdit_sptripid.setText(QCoreApplication.translate("MainWindow", u"Paste Secondary Payment Trip IDs", None))
        self.output_label.setText(QCoreApplication.translate("MainWindow", u"Choose What Folders To Output", None))
        self.checkBox_alloutputs.setText(QCoreApplication.translate("MainWindow", u"All Outputs", None))
        self.checkBox_payableout.setText(QCoreApplication.translate("MainWindow", u"Payable Trips", None))
        self.checkBox_flagout.setText(QCoreApplication.translate("MainWindow", u"Flagged Trips", None))
        self.checkBox_taxiout.setText(QCoreApplication.translate("MainWindow", u"Taxi Trips", None))
        self.groupBox_flags.setTitle(QCoreApplication.translate("MainWindow", u"Audit Flags", None))
        self.checkBox_selectall.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
        self.checkBox_bprovider.setText(QCoreApplication.translate("MainWindow", u"Blank Provider", None))
        self.checkBox_candd.setText(QCoreApplication.translate("MainWindow", u"Cancel with Distribution Date", None))
        self.checkBox_tddate.setText(QCoreApplication.translate("MainWindow", u"Incorrect TD Date", None))
        self.checkBox_duptrip.setText(QCoreApplication.translate("MainWindow", u"Duplicate Trip", None))
        self.checkBox_1leg.setText(QCoreApplication.translate("MainWindow", u"Single Leg Trip", None))
        self.checkBox_ooa.setText(QCoreApplication.translate("MainWindow", u"OOA", None))
        self.checkBox_trippurp.setText(QCoreApplication.translate("MainWindow", u"Trip Purpose Error", None))
        self.checkBox_compwcan.setText(QCoreApplication.translate("MainWindow", u"Comp with Cancel", None))
        self.checkBox_excapps.setText(QCoreApplication.translate("MainWindow", u"Excess Appointments", None))
        self.checkBox_paiddups.setText(QCoreApplication.translate("MainWindow", u"Duplicate Trips (only within mileage)", None))
        self.groupBox_output.setTitle(QCoreApplication.translate("MainWindow", u"Audit Output", None))
        self.lineEdit_resultOutput_path.setText(QCoreApplication.translate("MainWindow", u"Audit Output Path", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Choose directory to output audit results. The default is the desktop.", None))
        self.browseButton_output.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"VACANT? TRY YOUR IMAGINATION", None))
        self.lab_tab.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.frame_drag.setToolTip(QCoreApplication.translate("MainWindow", u"Drag", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

