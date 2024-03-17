# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hidroPixel_dialog_flow_ttzoPZqR.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qgis.core import (QgsApplication, QgsProject)
from qgis.gui import (QgsMapCanvas, QgsLayerTreeMapCanvasBridge)
from qgis.PyQt.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from qgis.PyQt.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from qgis.PyQt.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QToolButton, QVBoxLayout, QWidget)

import resouces_qrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(751, 642)
        MainWindow.setMinimumSize(QSize(720, 620))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.pg_par_ftt = QWidget()
        self.pg_par_ftt.setObjectName(u"pg_par_ftt")
        self.gridLayout_3 = QGridLayout(self.pg_par_ftt)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_45 = QGridLayout()
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.btn_config = QPushButton(self.pg_par_ftt)
        self.btn_config.setObjectName(u"btn_config")

        self.gridLayout_45.addWidget(self.btn_config, 0, 0, 1, 1)

        self.btn_input_data = QPushButton(self.pg_par_ftt)
        self.btn_input_data.setObjectName(u"btn_input_data")

        self.gridLayout_45.addWidget(self.btn_input_data, 0, 1, 1, 1)

        self.btn_data_va_tool = QPushButton(self.pg_par_ftt)
        self.btn_data_va_tool.setObjectName(u"btn_data_va_tool")

        self.gridLayout_45.addWidget(self.btn_data_va_tool, 0, 2, 1, 1)

        self.btn_run = QPushButton(self.pg_par_ftt)
        self.btn_run.setObjectName(u"btn_run")

        self.gridLayout_45.addWidget(self.btn_run, 0, 3, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_45, 0, 0, 1, 1)

        self.pages_flow_tt = QStackedWidget(self.pg_par_ftt)
        self.pages_flow_tt.setObjectName(u"pages_flow_tt")
        self.pg1_config = QWidget()
        self.pg1_config.setObjectName(u"pg1_config")
        self.gridLayout_4 = QGridLayout(self.pg1_config)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.pg1_config)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.pg1_config)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 689, 473))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_46 = QGridLayout()
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.btn_read_pg1 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_read_pg1.setObjectName(u"btn_read_pg1")

        self.gridLayout_46.addWidget(self.btn_read_pg1, 0, 0, 1, 1)

        self.btn_save_file_pg1 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_save_file_pg1.setObjectName(u"btn_save_file_pg1")

        self.gridLayout_46.addWidget(self.btn_save_file_pg1, 0, 1, 1, 1)

        self.btn_save_pg1 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_save_pg1.setObjectName(u"btn_save_pg1")

        self.gridLayout_46.addWidget(self.btn_save_pg1, 0, 2, 1, 1)

        self.btn_help_pg1 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_help_pg1.setObjectName(u"btn_help_pg1")

        self.gridLayout_46.addWidget(self.btn_help_pg1, 0, 3, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_46, 2, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_9.addWidget(self.label_2, 0, 0, 1, 1)

        self.le_1_pg1 = QLineEdit(self.frame)
        self.le_1_pg1.setObjectName(u"le_1_pg1")
        self.le_1_pg1.setMaximumSize(QSize(80, 24))

        self.gridLayout_9.addWidget(self.le_1_pg1, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_16.addWidget(self.label_3, 0, 0, 1, 1)

        self.le_2_pg1 = QLineEdit(self.frame)
        self.le_2_pg1.setObjectName(u"le_2_pg1")
        self.le_2_pg1.setMinimumSize(QSize(80, 24))
        self.le_2_pg1.setMaximumSize(QSize(80, 24))

        self.gridLayout_16.addWidget(self.le_2_pg1, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_16, 1, 0, 1, 1)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_17.addWidget(self.label_4, 0, 0, 1, 1)

        self.le_3_pg1 = QLineEdit(self.frame)
        self.le_3_pg1.setObjectName(u"le_3_pg1")
        self.le_3_pg1.setMaximumSize(QSize(80, 24))

        self.gridLayout_17.addWidget(self.le_3_pg1, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_17, 2, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_18.addWidget(self.label_5, 0, 0, 1, 1)

        self.le_4_pg1 = QLineEdit(self.frame)
        self.le_4_pg1.setObjectName(u"le_4_pg1")
        self.le_4_pg1.setMaximumSize(QSize(80, 24))

        self.gridLayout_18.addWidget(self.le_4_pg1, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_18, 3, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(50, 0))

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)


        self.gridLayout_7.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(16, 16))
        self.label_13.setMaximumSize(QSize(16, 16))
        self.label_13.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_10.addWidget(self.label_13, 2, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QSize(16, 16))
        self.label_14.setMaximumSize(QSize(16, 16))
        self.label_14.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_10.addWidget(self.label_14, 3, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(16, 16))
        self.label_11.setMaximumSize(QSize(16, 16))
        self.label_11.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_10.addWidget(self.label_11, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(16, 16))
        self.label_12.setMaximumSize(QSize(16, 16))
        self.label_12.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_10.addWidget(self.label_12, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_10, 0, 2, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_7, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)


        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_23 = QLabel(self.frame_2)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_11.addWidget(self.label_23, 0, 0, 1, 1)

        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QSize(16, 16))
        self.label_24.setMaximumSize(QSize(16, 16))
        self.label_24.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_11.addWidget(self.label_24, 0, 3, 1, 1)

        self.label_65 = QLabel(self.frame_2)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setPixmap(QPixmap(u"flowdirs.png"))

        self.gridLayout_11.addWidget(self.label_65, 1, 0, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.le_5_pg1 = QLineEdit(self.frame_2)
        self.le_5_pg1.setObjectName(u"le_5_pg1")
        self.le_5_pg1.setMaximumSize(QSize(60, 24))

        self.horizontalLayout_11.addWidget(self.le_5_pg1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_17.addWidget(self.label_20)

        self.le_6_pg1 = QLineEdit(self.frame_2)
        self.le_6_pg1.setObjectName(u"le_6_pg1")
        self.le_6_pg1.setMaximumSize(QSize(60, 24))

        self.horizontalLayout_17.addWidget(self.le_6_pg1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_18.addWidget(self.label_19)

        self.le_7_pg1 = QLineEdit(self.frame_2)
        self.le_7_pg1.setObjectName(u"le_7_pg1")
        self.le_7_pg1.setMaximumSize(QSize(60, 24))

        self.horizontalLayout_18.addWidget(self.le_7_pg1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_19.addWidget(self.label_16)

        self.le_8_pg1 = QLineEdit(self.frame_2)
        self.le_8_pg1.setObjectName(u"le_8_pg1")
        self.le_8_pg1.setMaximumSize(QSize(60, 24))

        self.horizontalLayout_19.addWidget(self.le_8_pg1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_24.addLayout(self.verticalLayout_3)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_20.addWidget(self.label_21)

        self.le_9_pg1 = QLineEdit(self.frame_2)
        self.le_9_pg1.setObjectName(u"le_9_pg1")
        self.le_9_pg1.setMaximumSize(QSize(60, 24))

        self.horizontalLayout_20.addWidget(self.le_9_pg1)


        self.verticalLayout_9.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_21.addWidget(self.label_15)

        self.le_10_pg1 = QLineEdit(self.frame_2)
        self.le_10_pg1.setObjectName(u"le_10_pg1")
        self.le_10_pg1.setMaximumSize(QSize(60, 24))

        self.horizontalLayout_21.addWidget(self.le_10_pg1)


        self.verticalLayout_9.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_22.addWidget(self.label_17)

        self.le_11_pg1 = QLineEdit(self.frame_2)
        self.le_11_pg1.setObjectName(u"le_11_pg1")
        self.le_11_pg1.setMaximumSize(QSize(60, 24))

        self.horizontalLayout_22.addWidget(self.le_11_pg1)


        self.verticalLayout_9.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_23.addWidget(self.label_18)

        self.le_12_pg1 = QLineEdit(self.frame_2)
        self.le_12_pg1.setObjectName(u"le_12_pg1")
        self.le_12_pg1.setMaximumSize(QSize(60, 24))

        self.horizontalLayout_23.addWidget(self.le_12_pg1)


        self.verticalLayout_9.addLayout(self.horizontalLayout_23)


        self.horizontalLayout_24.addLayout(self.verticalLayout_9)


        self.gridLayout_11.addLayout(self.horizontalLayout_24, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 2, 0, 1, 1)

        self.gridLayout_47 = QGridLayout()
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.tbtn_pg1_1 = QToolButton(self.pg1_config)
        self.tbtn_pg1_1.setObjectName(u"tbtn_pg1_1")
        icon = QIcon()
        icon.addFile(u"folder_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbtn_pg1_1.setIcon(icon)

        self.gridLayout_47.addWidget(self.tbtn_pg1_1, 0, 3, 1, 1)

        self.label_26 = QLabel(self.pg1_config)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_47.addWidget(self.label_26, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_47.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.le_13_pg1 = QLineEdit(self.pg1_config)
        self.le_13_pg1.setObjectName(u"le_13_pg1")

        self.gridLayout_47.addWidget(self.le_13_pg1, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_47, 1, 0, 1, 1)

        self.pages_flow_tt.addWidget(self.pg1_config)
        self.pg2_in_data = QWidget()
        self.pg2_in_data.setObjectName(u"pg2_in_data")
        self.gridLayout_19 = QGridLayout(self.pg2_in_data)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_25 = QLabel(self.pg2_in_data)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_19.addWidget(self.label_25, 0, 0, 1, 1)

        self.scrollArea_2 = QScrollArea(self.pg2_in_data)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -71, 672, 878))
        self.gridLayout_14 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 160))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_3)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_28 = QLabel(self.frame_3)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_21.addWidget(self.label_28, 0, 0, 1, 1)

        self.le_1_pg2 = QLineEdit(self.frame_3)
        self.le_1_pg2.setObjectName(u"le_1_pg2")
        self.le_1_pg2.setMinimumSize(QSize(0, 24))
        self.le_1_pg2.setMaximumSize(QSize(360, 24))

        self.gridLayout_21.addWidget(self.le_1_pg2, 0, 1, 1, 1)

        self.tbtn_pg2_1 = QToolButton(self.frame_3)
        self.tbtn_pg2_1.setObjectName(u"tbtn_pg2_1")

        self.gridLayout_21.addWidget(self.tbtn_pg2_1, 0, 2, 1, 1)

        self.label_27 = QLabel(self.frame_3)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMinimumSize(QSize(16, 16))
        self.label_27.setMaximumSize(QSize(16, 16))
        self.label_27.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_21.addWidget(self.label_27, 0, 3, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_21)

        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_29 = QLabel(self.frame_3)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_22.addWidget(self.label_29, 0, 0, 1, 1)

        self.le_2_pg2 = QLineEdit(self.frame_3)
        self.le_2_pg2.setObjectName(u"le_2_pg2")
        self.le_2_pg2.setMinimumSize(QSize(0, 24))
        self.le_2_pg2.setMaximumSize(QSize(360, 24))

        self.gridLayout_22.addWidget(self.le_2_pg2, 0, 1, 1, 1)

        self.tbtn_pg2_2 = QToolButton(self.frame_3)
        self.tbtn_pg2_2.setObjectName(u"tbtn_pg2_2")

        self.gridLayout_22.addWidget(self.tbtn_pg2_2, 0, 2, 1, 1)

        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setMinimumSize(QSize(16, 16))
        self.label_33.setMaximumSize(QSize(16, 16))
        self.label_33.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_22.addWidget(self.label_33, 0, 3, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_22)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_30 = QLabel(self.frame_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(16777215, 24))

        self.gridLayout_23.addWidget(self.label_30, 0, 0, 1, 1)

        self.te_1_pg2 = QTextEdit(self.frame_3)
        self.te_1_pg2.setObjectName(u"te_1_pg2")
        self.te_1_pg2.setMinimumSize(QSize(0, 24))
        self.te_1_pg2.setMaximumSize(QSize(360, 24))

        self.gridLayout_23.addWidget(self.te_1_pg2, 0, 1, 1, 1)

        self.tbtn_pg2_3 = QToolButton(self.frame_3)
        self.tbtn_pg2_3.setObjectName(u"tbtn_pg2_3")

        self.gridLayout_23.addWidget(self.tbtn_pg2_3, 0, 2, 1, 1)

        self.label_34 = QLabel(self.frame_3)
        self.label_34.setObjectName(u"label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setMinimumSize(QSize(16, 16))
        self.label_34.setMaximumSize(QSize(16, 16))
        self.label_34.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_23.addWidget(self.label_34, 0, 3, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_23)

        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_31 = QLabel(self.frame_3)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_24.addWidget(self.label_31, 0, 0, 1, 1)

        self.le_3_pg2 = QLineEdit(self.frame_3)
        self.le_3_pg2.setObjectName(u"le_3_pg2")
        self.le_3_pg2.setMinimumSize(QSize(0, 24))
        self.le_3_pg2.setMaximumSize(QSize(360, 24))

        self.gridLayout_24.addWidget(self.le_3_pg2, 0, 1, 1, 1)

        self.tbtn_pg2_4 = QToolButton(self.frame_3)
        self.tbtn_pg2_4.setObjectName(u"tbtn_pg2_4")

        self.gridLayout_24.addWidget(self.tbtn_pg2_4, 0, 2, 1, 1)

        self.label_35 = QLabel(self.frame_3)
        self.label_35.setObjectName(u"label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setMinimumSize(QSize(16, 16))
        self.label_35.setMaximumSize(QSize(16, 16))
        self.label_35.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_24.addWidget(self.label_35, 0, 3, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_24)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_32 = QLabel(self.frame_3)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_25.addWidget(self.label_32, 0, 0, 1, 1)

        self.le_4_pg2 = QLineEdit(self.frame_3)
        self.le_4_pg2.setObjectName(u"le_4_pg2")
        self.le_4_pg2.setMinimumSize(QSize(0, 24))
        self.le_4_pg2.setMaximumSize(QSize(360, 24))

        self.gridLayout_25.addWidget(self.le_4_pg2, 0, 1, 1, 1)

        self.tbtn_pg2_5 = QToolButton(self.frame_3)
        self.tbtn_pg2_5.setObjectName(u"tbtn_pg2_5")

        self.gridLayout_25.addWidget(self.tbtn_pg2_5, 0, 2, 1, 1)

        self.label_36 = QLabel(self.frame_3)
        self.label_36.setObjectName(u"label_36")
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setMinimumSize(QSize(16, 16))
        self.label_36.setMaximumSize(QSize(16, 16))
        self.label_36.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_25.addWidget(self.label_36, 0, 3, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_25)


        self.gridLayout_26.addLayout(self.verticalLayout_5, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_4)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_37 = QLabel(self.frame_4)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_8.addWidget(self.label_37)

        self.label_38 = QLabel(self.frame_4)
        self.label_38.setObjectName(u"label_38")
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)
        self.label_38.setMinimumSize(QSize(16, 16))
        self.label_38.setMaximumSize(QSize(16, 16))
        self.label_38.setPixmap(QPixmap(u"tip_icon.png"))

        self.horizontalLayout_8.addWidget(self.label_38)


        self.gridLayout_27.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.gridLayout_38 = QGridLayout()
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_38.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.btn_del_row_1 = QPushButton(self.frame_4)
        self.btn_del_row_1.setObjectName(u"btn_del_row_1")

        self.gridLayout_33.addWidget(self.btn_del_row_1, 1, 0, 1, 1, Qt.AlignTop)

        self.btn_add_row_1 = QPushButton(self.frame_4)
        self.btn_add_row_1.setObjectName(u"btn_add_row_1")

        self.gridLayout_33.addWidget(self.btn_add_row_1, 0, 0, 1, 1, Qt.AlignBottom)


        self.gridLayout_38.addLayout(self.gridLayout_33, 0, 1, 1, 1)

        self.gridLayout_35 = QGridLayout()
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_56 = QGridLayout()
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.label_67 = QLabel(self.frame_4)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_56.addWidget(self.label_67, 0, 0, 1, 1)

        self.le_7_pg2 = QLineEdit(self.frame_4)
        self.le_7_pg2.setObjectName(u"le_7_pg2")
        self.le_7_pg2.setMinimumSize(QSize(220, 24))
        self.le_7_pg2.setMaximumSize(QSize(16777215, 24))

        self.gridLayout_56.addWidget(self.le_7_pg2, 0, 1, 1, 1)


        self.gridLayout_35.addLayout(self.gridLayout_56, 0, 0, 1, 1)

        self.gridLayout_34 = QGridLayout()
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.btn_save_file_t1 = QPushButton(self.frame_4)
        self.btn_save_file_t1.setObjectName(u"btn_save_file_t1")

        self.gridLayout_34.addWidget(self.btn_save_file_t1, 0, 1, 1, 1)

        self.btn_read_t1 = QPushButton(self.frame_4)
        self.btn_read_t1.setObjectName(u"btn_read_t1")

        self.gridLayout_34.addWidget(self.btn_read_t1, 0, 0, 1, 1)

        self.btn_help_t1 = QPushButton(self.frame_4)
        self.btn_help_t1.setObjectName(u"btn_help_t1")

        self.gridLayout_34.addWidget(self.btn_help_t1, 0, 2, 1, 1)


        self.gridLayout_35.addLayout(self.gridLayout_34, 3, 0, 1, 1)

        self.tbw_1_pg2 = QTableWidget(self.frame_4)
        if (self.tbw_1_pg2.columnCount() < 4):
            self.tbw_1_pg2.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbw_1_pg2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbw_1_pg2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbw_1_pg2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbw_1_pg2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tbw_1_pg2.rowCount() < 4):
            self.tbw_1_pg2.setRowCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbw_1_pg2.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbw_1_pg2.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbw_1_pg2.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbw_1_pg2.setVerticalHeaderItem(3, __qtablewidgetitem7)
        self.tbw_1_pg2.setObjectName(u"tbw_1_pg2")
        self.tbw_1_pg2.setMinimumSize(QSize(420, 150))
        self.tbw_1_pg2.setMaximumSize(QSize(420, 150))
        self.tbw_1_pg2.setProperty("showDropIndicator", True)
        self.tbw_1_pg2.setDragDropOverwriteMode(True)
        self.tbw_1_pg2.setAlternatingRowColors(True)
        self.tbw_1_pg2.setTextElideMode(Qt.ElideMiddle)
        self.tbw_1_pg2.setShowGrid(True)
        self.tbw_1_pg2.setGridStyle(Qt.SolidLine)
        self.tbw_1_pg2.setSortingEnabled(False)
        self.tbw_1_pg2.setWordWrap(True)
        self.tbw_1_pg2.horizontalHeader().setVisible(True)
        self.tbw_1_pg2.horizontalHeader().setCascadingSectionResizes(True)
        self.tbw_1_pg2.horizontalHeader().setMinimumSectionSize(24)
        self.tbw_1_pg2.horizontalHeader().setDefaultSectionSize(100)
        self.tbw_1_pg2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tbw_1_pg2.verticalHeader().setDefaultSectionSize(30)

        self.gridLayout_35.addWidget(self.tbw_1_pg2, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_35.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout_38.addLayout(self.gridLayout_35, 0, 2, 1, 1)


        self.gridLayout_27.addLayout(self.gridLayout_38, 1, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_4, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_4, 2, 0, 1, 1)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_7)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_68 = QLabel(self.frame_7)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_25.addWidget(self.label_68)

        self.gridLayout_59 = QGridLayout()
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_59.addItem(self.horizontalSpacer_9, 0, 0, 1, 1)

        self.le_5_pg2 = QLineEdit(self.frame_7)
        self.le_5_pg2.setObjectName(u"le_5_pg2")
        self.le_5_pg2.setMinimumSize(QSize(220, 24))
        self.le_5_pg2.setMaximumSize(QSize(220, 24))

        self.gridLayout_59.addWidget(self.le_5_pg2, 0, 1, 1, 1)

        self.tbtn_pg2_6 = QToolButton(self.frame_7)
        self.tbtn_pg2_6.setObjectName(u"tbtn_pg2_6")

        self.gridLayout_59.addWidget(self.tbtn_pg2_6, 0, 2, 1, 1)

        self.label_69 = QLabel(self.frame_7)
        self.label_69.setObjectName(u"label_69")
        sizePolicy.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy)
        self.label_69.setMinimumSize(QSize(16, 16))
        self.label_69.setMaximumSize(QSize(16, 16))
        self.label_69.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_59.addWidget(self.label_69, 0, 3, 1, 1)


        self.horizontalLayout_25.addLayout(self.gridLayout_59)


        self.gridLayout_12.addLayout(self.horizontalLayout_25, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_7, 3, 0, 1, 1)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_49 = QGridLayout(self.frame_5)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_41 = QLabel(self.frame_5)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_13.addWidget(self.label_41)

        self.label_42 = QLabel(self.frame_5)
        self.label_42.setObjectName(u"label_42")
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)
        self.label_42.setMinimumSize(QSize(16, 16))
        self.label_42.setMaximumSize(QSize(16, 16))
        self.label_42.setPixmap(QPixmap(u"tip_icon.png"))

        self.horizontalLayout_13.addWidget(self.label_42)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_7 = QSpacerItem(182, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)

        self.gridLayout_39 = QGridLayout()
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.btn_del_row_2 = QPushButton(self.frame_5)
        self.btn_del_row_2.setObjectName(u"btn_del_row_2")

        self.gridLayout_39.addWidget(self.btn_del_row_2, 1, 0, 1, 1, Qt.AlignTop)

        self.btn_add_row_2 = QPushButton(self.frame_5)
        self.btn_add_row_2.setObjectName(u"btn_add_row_2")

        self.gridLayout_39.addWidget(self.btn_add_row_2, 0, 0, 1, 1, Qt.AlignBottom)


        self.horizontalLayout_16.addLayout(self.gridLayout_39)

        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_40 = QGridLayout()
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.label_66 = QLabel(self.frame_5)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_40.addWidget(self.label_66, 0, 0, 1, 1)

        self.le_8_pg2 = QLineEdit(self.frame_5)
        self.le_8_pg2.setObjectName(u"le_8_pg2")
        self.le_8_pg2.setMinimumSize(QSize(220, 24))
        self.le_8_pg2.setMaximumSize(QSize(16777215, 24))

        self.gridLayout_40.addWidget(self.le_8_pg2, 0, 1, 1, 1)


        self.gridLayout_37.addLayout(self.gridLayout_40, 0, 0, 1, 1)

        self.tbw_2_pg2 = QTableWidget(self.frame_5)
        if (self.tbw_2_pg2.columnCount() < 3):
            self.tbw_2_pg2.setColumnCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbw_2_pg2.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbw_2_pg2.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbw_2_pg2.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        if (self.tbw_2_pg2.rowCount() < 4):
            self.tbw_2_pg2.setRowCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbw_2_pg2.setVerticalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbw_2_pg2.setVerticalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tbw_2_pg2.setVerticalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tbw_2_pg2.setVerticalHeaderItem(3, __qtablewidgetitem14)
        self.tbw_2_pg2.setObjectName(u"tbw_2_pg2")
        self.tbw_2_pg2.setMinimumSize(QSize(330, 150))
        self.tbw_2_pg2.setMaximumSize(QSize(420, 150))
        self.tbw_2_pg2.setAlternatingRowColors(True)
        self.tbw_2_pg2.setTextElideMode(Qt.ElideMiddle)
        self.tbw_2_pg2.setShowGrid(True)
        self.tbw_2_pg2.setGridStyle(Qt.SolidLine)
        self.tbw_2_pg2.setSortingEnabled(False)
        self.tbw_2_pg2.setWordWrap(True)
        self.tbw_2_pg2.horizontalHeader().setVisible(True)
        self.tbw_2_pg2.horizontalHeader().setCascadingSectionResizes(True)
        self.tbw_2_pg2.horizontalHeader().setMinimumSectionSize(24)
        self.tbw_2_pg2.horizontalHeader().setDefaultSectionSize(100)
        self.tbw_2_pg2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tbw_2_pg2.verticalHeader().setDefaultSectionSize(30)

        self.gridLayout_37.addWidget(self.tbw_2_pg2, 1, 0, 1, 1)


        self.gridLayout_28.addLayout(self.gridLayout_37, 0, 0, 1, 1)

        self.gridLayout_41 = QGridLayout()
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.btn_help_t2 = QPushButton(self.frame_5)
        self.btn_help_t2.setObjectName(u"btn_help_t2")

        self.gridLayout_41.addWidget(self.btn_help_t2, 0, 2, 1, 1)

        self.btn_save_file_t2 = QPushButton(self.frame_5)
        self.btn_save_file_t2.setObjectName(u"btn_save_file_t2")

        self.gridLayout_41.addWidget(self.btn_save_file_t2, 0, 1, 1, 1)

        self.btn_read_t2 = QPushButton(self.frame_5)
        self.btn_read_t2.setObjectName(u"btn_read_t2")

        self.gridLayout_41.addWidget(self.btn_read_t2, 0, 0, 1, 1)


        self.gridLayout_28.addLayout(self.gridLayout_41, 1, 0, 1, 1)


        self.horizontalLayout_16.addLayout(self.gridLayout_28)


        self.verticalLayout_7.addLayout(self.horizontalLayout_16)


        self.gridLayout_49.addLayout(self.verticalLayout_7, 0, 0, 1, 2)


        self.gridLayout_14.addWidget(self.frame_5, 4, 0, 1, 1)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_8)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_43 = QGridLayout()
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.label_43 = QLabel(self.frame_8)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_43.addWidget(self.label_43, 0, 0, 1, 1)

        self.gridLayout_42 = QGridLayout()
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_42.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.le_6_pg2 = QLineEdit(self.frame_8)
        self.le_6_pg2.setObjectName(u"le_6_pg2")
        self.le_6_pg2.setMinimumSize(QSize(80, 24))
        self.le_6_pg2.setMaximumSize(QSize(80, 24))

        self.gridLayout_42.addWidget(self.le_6_pg2, 0, 1, 1, 1)

        self.label_45 = QLabel(self.frame_8)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_42.addWidget(self.label_45, 0, 2, 1, 1)

        self.label_44 = QLabel(self.frame_8)
        self.label_44.setObjectName(u"label_44")
        sizePolicy.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy)
        self.label_44.setMinimumSize(QSize(16, 16))
        self.label_44.setMaximumSize(QSize(16, 16))
        self.label_44.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_42.addWidget(self.label_44, 0, 3, 1, 1)


        self.gridLayout_43.addLayout(self.gridLayout_42, 0, 1, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_43, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_8, 5, 0, 1, 1)

        self.gridLayout_44 = QGridLayout()
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.btn_read_pg2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_read_pg2.setObjectName(u"btn_read_pg2")

        self.gridLayout_44.addWidget(self.btn_read_pg2, 0, 0, 1, 1)

        self.btn_save_file_pg2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_save_file_pg2.setObjectName(u"btn_save_file_pg2")

        self.gridLayout_44.addWidget(self.btn_save_file_pg2, 0, 1, 1, 1)

        self.btn_save_pg2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_save_pg2.setObjectName(u"btn_save_pg2")

        self.gridLayout_44.addWidget(self.btn_save_pg2, 0, 2, 1, 1)

        self.btn_help_pg2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_help_pg2.setObjectName(u"btn_help_pg2")

        self.gridLayout_44.addWidget(self.btn_help_pg2, 0, 3, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_44, 6, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_19.addWidget(self.scrollArea_2, 1, 0, 1, 1)

        self.pages_flow_tt.addWidget(self.pg2_in_data)
        self.pg3_data_val_tool = QWidget()
        self.pg3_data_val_tool.setObjectName(u"pg3_data_val_tool")
        self.gridLayout_29 = QGridLayout(self.pg3_data_val_tool)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.scrollArea_3 = QScrollArea(self.pg3_data_val_tool)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 688, 481))
        self.gridLayout_30 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.frame_6 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_6)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_46 = QLabel(self.frame_6)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_31.addWidget(self.label_46, 0, 0, 1, 1)


        self.gridLayout_30.addWidget(self.frame_6, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_29.addWidget(self.scrollArea_3, 1, 0, 1, 1)

        self.label_47 = QLabel(self.pg3_data_val_tool)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_29.addWidget(self.label_47, 0, 0, 1, 1)

        self.pages_flow_tt.addWidget(self.pg3_data_val_tool)
        self.pg4_run = QWidget()
        self.pg4_run.setObjectName(u"pg4_run")
        self.gridLayout_32 = QGridLayout(self.pg4_run)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.scrollArea_4 = QScrollArea(self.pg4_run)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 688, 481))
        self.gridLayout_48 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_55 = QGridLayout()
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_49 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_49.setObjectName(u"label_49")

        self.verticalLayout_8.addWidget(self.label_49)

        self.line = QFrame(self.scrollAreaWidgetContents_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line)


        self.gridLayout_55.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.label_64 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_4.addWidget(self.label_64)

        self.rb_1_pg4 = QRadioButton(self.scrollAreaWidgetContents_4)
        self.rb_1_pg4.setObjectName(u"rb_1_pg4")

        self.horizontalLayout_4.addWidget(self.rb_1_pg4)


        self.gridLayout_55.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)


        self.gridLayout_48.addLayout(self.gridLayout_55, 0, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ch_1_pg4 = QCheckBox(self.scrollAreaWidgetContents_4)
        self.ch_1_pg4.setObjectName(u"ch_1_pg4")

        self.horizontalLayout_3.addWidget(self.ch_1_pg4)

        self.gridLayout_51 = QGridLayout()
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.label_57 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_51.addWidget(self.label_57, 0, 0, 1, 1)

        self.label_50 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_50.setObjectName(u"label_50")
        sizePolicy.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy)
        self.label_50.setMinimumSize(QSize(16, 16))
        self.label_50.setMaximumSize(QSize(16, 16))
        self.label_50.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_51.addWidget(self.label_50, 0, 3, 1, 1)

        self.le_1_pg4 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.le_1_pg4.setObjectName(u"le_1_pg4")
        self.le_1_pg4.setMaximumSize(QSize(220, 24))

        self.gridLayout_51.addWidget(self.le_1_pg4, 0, 1, 1, 1)

        self.tbtn_pg4_1 = QToolButton(self.scrollAreaWidgetContents_4)
        self.tbtn_pg4_1.setObjectName(u"tbtn_pg4_1")

        self.gridLayout_51.addWidget(self.tbtn_pg4_1, 0, 2, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_51)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ch_2_pg4 = QCheckBox(self.scrollAreaWidgetContents_4)
        self.ch_2_pg4.setObjectName(u"ch_2_pg4")

        self.horizontalLayout_5.addWidget(self.ch_2_pg4)

        self.gridLayout_58 = QGridLayout()
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.label_58 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_58.addWidget(self.label_58, 0, 0, 1, 1)

        self.le_2_pg4 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.le_2_pg4.setObjectName(u"le_2_pg4")
        self.le_2_pg4.setMaximumSize(QSize(220, 24))

        self.gridLayout_58.addWidget(self.le_2_pg4, 0, 1, 1, 1)

        self.label_51 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_51.setObjectName(u"label_51")
        sizePolicy.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy)
        self.label_51.setMinimumSize(QSize(16, 16))
        self.label_51.setMaximumSize(QSize(16, 16))
        self.label_51.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_58.addWidget(self.label_51, 0, 3, 1, 1)

        self.tbtn_pg4_2 = QToolButton(self.scrollAreaWidgetContents_4)
        self.tbtn_pg4_2.setObjectName(u"tbtn_pg4_2")

        self.gridLayout_58.addWidget(self.tbtn_pg4_2, 0, 2, 1, 1)


        self.horizontalLayout_5.addLayout(self.gridLayout_58)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.ch_3_pg4 = QCheckBox(self.scrollAreaWidgetContents_4)
        self.ch_3_pg4.setObjectName(u"ch_3_pg4")

        self.horizontalLayout_6.addWidget(self.ch_3_pg4)

        self.gridLayout_50 = QGridLayout()
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.label_52 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_52.setObjectName(u"label_52")
        sizePolicy.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy)
        self.label_52.setMinimumSize(QSize(16, 16))
        self.label_52.setMaximumSize(QSize(16, 16))
        self.label_52.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_50.addWidget(self.label_52, 0, 3, 1, 1)

        self.label_59 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_50.addWidget(self.label_59, 0, 0, 1, 1)

        self.le_3_pg4 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.le_3_pg4.setObjectName(u"le_3_pg4")
        self.le_3_pg4.setMaximumSize(QSize(220, 24))

        self.gridLayout_50.addWidget(self.le_3_pg4, 0, 1, 1, 1)

        self.tbtn_pg4_3 = QToolButton(self.scrollAreaWidgetContents_4)
        self.tbtn_pg4_3.setObjectName(u"tbtn_pg4_3")

        self.gridLayout_50.addWidget(self.tbtn_pg4_3, 0, 2, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_50)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.ch_4_pg4 = QCheckBox(self.scrollAreaWidgetContents_4)
        self.ch_4_pg4.setObjectName(u"ch_4_pg4")

        self.horizontalLayout_7.addWidget(self.ch_4_pg4)

        self.gridLayout_52 = QGridLayout()
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.label_61 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_52.addWidget(self.label_61, 0, 0, 1, 1)

        self.label_53 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_53.setObjectName(u"label_53")
        sizePolicy.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy)
        self.label_53.setMinimumSize(QSize(16, 16))
        self.label_53.setMaximumSize(QSize(16, 16))
        self.label_53.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_52.addWidget(self.label_53, 0, 3, 1, 1)

        self.le_4_pg4 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.le_4_pg4.setObjectName(u"le_4_pg4")
        self.le_4_pg4.setMaximumSize(QSize(220, 24))

        self.gridLayout_52.addWidget(self.le_4_pg4, 0, 1, 1, 1)

        self.tbtn_pg4_4 = QToolButton(self.scrollAreaWidgetContents_4)
        self.tbtn_pg4_4.setObjectName(u"tbtn_pg4_4")

        self.gridLayout_52.addWidget(self.tbtn_pg4_4, 0, 2, 1, 1)


        self.horizontalLayout_7.addLayout(self.gridLayout_52)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.ch_5_pg4 = QCheckBox(self.scrollAreaWidgetContents_4)
        self.ch_5_pg4.setObjectName(u"ch_5_pg4")

        self.horizontalLayout_9.addWidget(self.ch_5_pg4)

        self.gridLayout_57 = QGridLayout()
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.le_5_pg4 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.le_5_pg4.setObjectName(u"le_5_pg4")
        self.le_5_pg4.setMaximumSize(QSize(220, 24))

        self.gridLayout_57.addWidget(self.le_5_pg4, 0, 1, 1, 1)

        self.label_56 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_56.setObjectName(u"label_56")
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        self.label_56.setMinimumSize(QSize(16, 16))
        self.label_56.setMaximumSize(QSize(16, 16))
        self.label_56.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_57.addWidget(self.label_56, 0, 3, 1, 1)

        self.label_60 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_57.addWidget(self.label_60, 0, 0, 1, 1)

        self.tbtn_pg4_5 = QToolButton(self.scrollAreaWidgetContents_4)
        self.tbtn_pg4_5.setObjectName(u"tbtn_pg4_5")

        self.gridLayout_57.addWidget(self.tbtn_pg4_5, 0, 2, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout_57)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.ch_6_pg4 = QCheckBox(self.scrollAreaWidgetContents_4)
        self.ch_6_pg4.setObjectName(u"ch_6_pg4")

        self.horizontalLayout_12.addWidget(self.ch_6_pg4)

        self.gridLayout_53 = QGridLayout()
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.label_54 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_54.setObjectName(u"label_54")
        sizePolicy.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy)
        self.label_54.setMinimumSize(QSize(16, 16))
        self.label_54.setMaximumSize(QSize(16, 16))
        self.label_54.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_53.addWidget(self.label_54, 0, 3, 1, 1)

        self.label_63 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_53.addWidget(self.label_63, 0, 0, 1, 1)

        self.le_6_pg4 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.le_6_pg4.setObjectName(u"le_6_pg4")
        self.le_6_pg4.setMaximumSize(QSize(220, 24))

        self.gridLayout_53.addWidget(self.le_6_pg4, 0, 1, 1, 1)

        self.tbtn_pg4_6 = QToolButton(self.scrollAreaWidgetContents_4)
        self.tbtn_pg4_6.setObjectName(u"tbtn_pg4_6")

        self.gridLayout_53.addWidget(self.tbtn_pg4_6, 0, 2, 1, 1)


        self.horizontalLayout_12.addLayout(self.gridLayout_53)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.checkBox_7 = QCheckBox(self.scrollAreaWidgetContents_4)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.horizontalLayout_14.addWidget(self.checkBox_7)

        self.gridLayout_54 = QGridLayout()
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.label_62 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_54.addWidget(self.label_62, 0, 0, 1, 1)

        self.le_7_pg4 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.le_7_pg4.setObjectName(u"le_7_pg4")
        self.le_7_pg4.setMaximumSize(QSize(220, 24))

        self.gridLayout_54.addWidget(self.le_7_pg4, 0, 1, 1, 1)

        self.label_55 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_55.setObjectName(u"label_55")
        sizePolicy.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy)
        self.label_55.setMinimumSize(QSize(16, 16))
        self.label_55.setMaximumSize(QSize(16, 16))
        self.label_55.setPixmap(QPixmap(u"tip_icon.png"))

        self.gridLayout_54.addWidget(self.label_55, 0, 3, 1, 1)

        self.tbtn_pg4_7 = QToolButton(self.scrollAreaWidgetContents_4)
        self.tbtn_pg4_7.setObjectName(u"tbtn_pg4_7")

        self.gridLayout_54.addWidget(self.tbtn_pg4_7, 0, 2, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_54)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)


        self.gridLayout_48.addLayout(self.verticalLayout_6, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_48.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_save_pg4 = QPushButton(self.scrollAreaWidgetContents_4)
        self.btn_save_pg4.setObjectName(u"btn_save_pg4")

        self.horizontalLayout_15.addWidget(self.btn_save_pg4)

        self.btn_close_pg4 = QPushButton(self.scrollAreaWidgetContents_4)
        self.btn_close_pg4.setObjectName(u"btn_close_pg4")

        self.horizontalLayout_15.addWidget(self.btn_close_pg4)

        self.btn_run_2 = QPushButton(self.scrollAreaWidgetContents_4)
        self.btn_run_2.setObjectName(u"btn_run_2")
        self.btn_run_2.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"color: rgb(0, 0, 0);\n"
"")

        self.horizontalLayout_15.addWidget(self.btn_run_2)

        self.btn_help_pg4 = QPushButton(self.scrollAreaWidgetContents_4)
        self.btn_help_pg4.setObjectName(u"btn_help_pg4")

        self.horizontalLayout_15.addWidget(self.btn_help_pg4)


        self.gridLayout_48.addLayout(self.horizontalLayout_15, 3, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_32.addWidget(self.scrollArea_4, 1, 0, 1, 1)

        self.label_48 = QLabel(self.pg4_run)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_32.addWidget(self.label_48, 0, 0, 1, 1)

        self.pages_flow_tt.addWidget(self.pg4_run)

        self.gridLayout_3.addWidget(self.pages_flow_tt, 1, 0, 1, 1)

        self.tabWidget.addTab(self.pg_par_ftt, "")
        self.pg_log_ftt = QWidget()
        self.pg_log_ftt.setObjectName(u"pg_log_ftt")
        self.gridLayout_2 = QGridLayout(self.pg_log_ftt)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressBar = QProgressBar(self.pg_log_ftt)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(24)

        self.horizontalLayout.addWidget(self.progressBar)

        self.btn_cancel_log = QPushButton(self.pg_log_ftt)
        self.btn_cancel_log.setObjectName(u"btn_cancel_log")
        self.btn_cancel_log.setMinimumSize(QSize(80, 24))
        self.btn_cancel_log.setMaximumSize(QSize(80, 24))

        self.horizontalLayout.addWidget(self.btn_cancel_log)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_close_log = QPushButton(self.pg_log_ftt)
        self.btn_close_log.setObjectName(u"btn_close_log")

        self.horizontalLayout_2.addWidget(self.btn_close_log, 0, Qt.AlignRight)

        self.btn_help_log = QPushButton(self.pg_log_ftt)
        self.btn_help_log.setObjectName(u"btn_help_log")

        self.horizontalLayout_2.addWidget(self.btn_help_log, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.te_logg = QTextEdit(self.pg_log_ftt)
        self.te_logg.setObjectName(u"te_logg")
        self.te_logg.setEnabled(True)
        self.te_logg.setAcceptDrops(True)
        self.te_logg.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.gridLayout_2.addWidget(self.te_logg, 0, 0, 1, 1)

        self.tabWidget.addTab(self.pg_log_ftt, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.pages_flow_tt.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_config.setText(QCoreApplication.translate("MainWindow", u"CONFIGURATION", None))
        self.btn_input_data.setText(QCoreApplication.translate("MainWindow", u"INPUT DATA", None))
        self.btn_data_va_tool.setText(QCoreApplication.translate("MainWindow", u"DATA VALIDATION TOOL", None))
        self.btn_run.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:9pt; font-weight:700;\">Flow travel time: configuration</span></p></body></html>", None))
        self.btn_read_pg1.setText(QCoreApplication.translate("MainWindow", u"READ FROM FILE", None))
        self.btn_save_file_pg1.setText(QCoreApplication.translate("MainWindow", u"SAVE TO FILE", None))
        self.btn_save_pg1.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.btn_help_pg1.setText(QCoreApplication.translate("MainWindow", u"HELP", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Minimum slope surface travel time determination:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Maximum slope for surface travel time determination:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Orthogonal step for distance computation:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Diagonal step for distance computation:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"m / km", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"m / km", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"dx", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"dx", None))
#if QT_CONFIG(whatsthis)
        self.label_13.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_13.setText("")
#if QT_CONFIG(whatsthis)
        self.label_14.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_14.setText("")
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText("")
#if QT_CONFIG(whatsthis)
        self.label_12.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_12.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Flow direction code:</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.label_24.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_24.setText("")
        self.label_65.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">A</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">B</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">C</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">D</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">E</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">F</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">G</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">H</span></p></body></html>", None))
        self.tbtn_pg1_1.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Select your work folder:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:9pt; font-weight:700;\">Flow travel time: Input Data</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Watershed delineation:</span></p></body></html>", None))
        self.tbtn_pg2_1.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.label_27.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_27.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Digital elevation model:</span></p></body></html>", None))
        self.tbtn_pg2_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.label_33.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_33.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Flow direction:</span></p></body></html>", None))
        self.tbtn_pg2_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.label_34.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_34.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">River drainage network (RDN):</span></p></body></html>", None))
        self.tbtn_pg2_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.label_35.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_35.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">RDN segmentation into classes:</span></p></body></html>", None))
        self.tbtn_pg2_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.label_36.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_36.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Characteristics of RDN classes:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_38.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_38.setText("")
#if QT_CONFIG(tooltip)
        self.btn_del_row_1.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Chose one line.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_del_row_1.setText(QCoreApplication.translate("MainWindow", u"Delete row", None))
        self.btn_add_row_1.setText(QCoreApplication.translate("MainWindow", u"Add row", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt;\">File:</span></p></body></html>", None))
        self.btn_save_file_t1.setText(QCoreApplication.translate("MainWindow", u"Save to file", None))
        self.btn_read_t1.setText(QCoreApplication.translate("MainWindow", u"Read from file", None))
        self.btn_help_t1.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        ___qtablewidgetitem = self.tbw_1_pg2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Class ID", None));
        ___qtablewidgetitem1 = self.tbw_1_pg2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Slope (m/m)", None));
        ___qtablewidgetitem2 = self.tbw_1_pg2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Manning Coef", None));
        ___qtablewidgetitem3 = self.tbw_1_pg2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Hydraulic radius", None));
        ___qtablewidgetitem4 = self.tbw_1_pg2.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem5 = self.tbw_1_pg2.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem6 = self.tbw_1_pg2.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem7 = self.tbw_1_pg2.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"4", None));
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Land use /land cover (LULC) map:</span></p></body></html>", None))
        self.tbtn_pg2_6.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.label_69.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_69.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Manning roughness coeficient for each LULC: </span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_42.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_42.setText("")
        self.btn_del_row_2.setText(QCoreApplication.translate("MainWindow", u"Delete row", None))
        self.btn_add_row_2.setText(QCoreApplication.translate("MainWindow", u"Add row", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt;\">File:</span></p></body></html>", None))
        ___qtablewidgetitem8 = self.tbw_2_pg2.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Class ID", None));
        ___qtablewidgetitem9 = self.tbw_2_pg2.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Class Name", None));
        ___qtablewidgetitem10 = self.tbw_2_pg2.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Manning Coef", None));
        ___qtablewidgetitem11 = self.tbw_2_pg2.verticalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem12 = self.tbw_2_pg2.verticalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem13 = self.tbw_2_pg2.verticalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem14 = self.tbw_2_pg2.verticalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"4", None));
        self.btn_help_t2.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.btn_save_file_t2.setText(QCoreApplication.translate("MainWindow", u"Save to file", None))
        self.btn_read_t2.setText(QCoreApplication.translate("MainWindow", u"Read from file", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Rainfall depth for 24-h duration:</span></p></body></html>", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"mm", None))
#if QT_CONFIG(tooltip)
        self.label_44.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_44.setText("")
        self.btn_read_pg2.setText(QCoreApplication.translate("MainWindow", u"READ FROM FILE", None))
        self.btn_save_file_pg2.setText(QCoreApplication.translate("MainWindow", u"SAVE TO FILE", None))
        self.btn_save_pg2.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.btn_help_pg2.setText(QCoreApplication.translate("MainWindow", u"HELP", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">EM DESENVOLVIMENTO</span></p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:9pt; font-weight:700;\">Flow travel time: Data Validation Tool</span></p></body></html>", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Output defination:</span></p></body></html>", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt;\">Open file after executuion:</span></p></body></html>", None))
        self.rb_1_pg4.setText("")
        self.ch_1_pg4.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Numering pixels part of the river drainage network:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_50.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_50.setText("")
        self.tbtn_pg4_1.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ch_2_pg4.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Areas draining directly to each pixel of the RDN:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_51.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_51.setText("")
        self.tbtn_pg4_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ch_3_pg4.setText("")
#if QT_CONFIG(tooltip)
        self.label_52.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_52.setText("")
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Upstream flow path length:</span></p></body></html>", None))
        self.tbtn_pg4_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ch_4_pg4.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Downstream flow path slope (m/m):</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_53.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_53.setText("")
        self.tbtn_pg4_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ch_5_pg4.setText("")
#if QT_CONFIG(tooltip)
        self.label_56.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_56.setText("")
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Downstream flow path length:</span></p></body></html>", None))
        self.tbtn_pg4_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ch_6_pg4.setText("")
#if QT_CONFIG(tooltip)
        self.label_54.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_54.setText("")
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Slope relative to downstream pixel:</span></p></body></html>", None))
        self.tbtn_pg4_6.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBox_7.setText("")
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Flow travel time (min):</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_55.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add the description or function of the object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_55.setText("")
        self.tbtn_pg4_7.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_save_pg4.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.btn_close_pg4.setText(QCoreApplication.translate("MainWindow", u"CLOSE", None))
        self.btn_run_2.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
        self.btn_help_pg4.setText(QCoreApplication.translate("MainWindow", u"HELP", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:9pt; font-weight:700;\">Flow travel time: Run</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pg_par_ftt), QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.btn_cancel_log.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_close_log.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.btn_help_log.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.te_logg.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pg_log_ftt), QCoreApplication.translate("MainWindow", u"Log", None))
    # retranslateUi
    def closeEvent(self, event):
        # Este método será chamado quando a janela estiver sendo fechada
        # Aqui você pode adicionar a lógica que deseja executar antes de fechar a janela
        # Por exemplo, você pode exibir uma mensagem de confirmação antes de fechar a janela
        reply = QMessageBox.question(MainWindow, 'Fechar janela',
                                     "Você tem certeza que deseja fechar a janela?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            # Se o usuário clicar em "Sim", aceita o evento de fechamento e fecha a janela
            event.accept()
        else:
            # Se o usuário clicar em "Não" ou fechar a mensagem de diálogo, ignora o evento de fechamento
            event.ignore()

