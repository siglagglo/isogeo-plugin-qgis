# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\isogeo_dockwidget_base.ui'
#
# Created: Thu Dec 29 18:29:47 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_IsogeoDockWidgetBase(object):
    def setupUi(self, IsogeoDockWidgetBase):
        IsogeoDockWidgetBase.setObjectName(_fromUtf8("IsogeoDockWidgetBase"))
        IsogeoDockWidgetBase.resize(531, 808)
        IsogeoDockWidgetBase.setMinimumSize(QtCore.QSize(531, 523))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        IsogeoDockWidgetBase.setWindowIcon(icon)
        IsogeoDockWidgetBase.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        IsogeoDockWidgetBase.setWindowTitle(_fromUtf8("Isogeo"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.txt_input = QtGui.QLineEdit(self.tab)
        self.txt_input.setInputMask(_fromUtf8(""))
        self.txt_input.setText(_fromUtf8(""))
        self.txt_input.setObjectName(_fromUtf8("txt_input"))
        self.verticalLayout_6.addWidget(self.txt_input)
        self.cbb_saved = QtGui.QComboBox(self.tab)
        self.cbb_saved.setObjectName(_fromUtf8("cbb_saved"))
        self.verticalLayout_6.addWidget(self.cbb_saved)
        self.horizontalLayout_14.addLayout(self.verticalLayout_6)
        self.widget = QtGui.QWidget(self.tab)
        self.widget.setMinimumSize(QtCore.QSize(271, 59))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.layoutWidget = QtGui.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 4, 261, 54))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_11.setMargin(0)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.cbb_keywords = QtGui.QComboBox(self.layoutWidget)
        self.cbb_keywords.setObjectName(_fromUtf8("cbb_keywords"))
        self.verticalLayout_11.addWidget(self.cbb_keywords)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.btn_save = QtGui.QPushButton(self.layoutWidget)
        self.btn_save.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_save.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/save.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon1)
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.horizontalLayout_13.addWidget(self.btn_save)
        self.btn_reinit = QtGui.QPushButton(self.layoutWidget)
        self.btn_reinit.setMinimumSize(QtCore.QSize(81, 0))
        self.btn_reinit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_reinit.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/undo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reinit.setIcon(icon2)
        self.btn_reinit.setObjectName(_fromUtf8("btn_reinit"))
        self.horizontalLayout_13.addWidget(self.btn_reinit)
        self.verticalLayout_11.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14.addWidget(self.widget)
        self.gridLayout_3.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)
        self.grp_filters = QgsCollapsibleGroupBox(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.grp_filters.setFont(font)
        self.grp_filters.setProperty("collapsed", False)
        self.grp_filters.setProperty("scrollOnExpand", True)
        self.grp_filters.setObjectName(_fromUtf8("grp_filters"))
        self.gridLayout_2 = QtGui.QGridLayout(self.grp_filters)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.grp_filters)
        self.label.setMaximumSize(QtCore.QSize(18, 18))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/map.svg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.label_7 = QtGui.QLabel(self.grp_filters)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        spacerItem = QtGui.QSpacerItem(48, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.cbb_geofilter = QtGui.QComboBox(self.grp_filters)
        self.cbb_geofilter.setObjectName(_fromUtf8("cbb_geofilter"))
        self.verticalLayout.addWidget(self.cbb_geofilter)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.grp_filters)
        self.label_2.setMaximumSize(QtCore.QSize(18, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/cube.svg")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_8 = QtGui.QLabel(self.grp_filters)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        spacerItem1 = QtGui.QSpacerItem(138, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.cbb_format = QtGui.QComboBox(self.grp_filters)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbb_format.sizePolicy().hasHeightForWidth())
        self.cbb_format.setSizePolicy(sizePolicy)
        self.cbb_format.setMinimumSize(QtCore.QSize(30, 0))
        self.cbb_format.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cbb_format.setObjectName(_fromUtf8("cbb_format"))
        self.verticalLayout_3.addWidget(self.cbb_format)
        self.verticalLayout_8.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_13 = QtGui.QLabel(self.grp_filters)
        self.label_13.setMaximumSize(QtCore.QSize(18, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setText(_fromUtf8(""))
        self.label_13.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/leaf.svg")))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_4.addWidget(self.label_13)
        self.label_4 = QtGui.QLabel(self.grp_filters)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem2 = QtGui.QSpacerItem(78, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.cbb_inspire = QtGui.QComboBox(self.grp_filters)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbb_inspire.sizePolicy().hasHeightForWidth())
        self.cbb_inspire.setSizePolicy(sizePolicy)
        self.cbb_inspire.setMinimumSize(QtCore.QSize(30, 0))
        self.cbb_inspire.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cbb_inspire.setObjectName(_fromUtf8("cbb_inspire"))
        self.verticalLayout_4.addWidget(self.cbb_inspire)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_10 = QtGui.QLabel(self.grp_filters)
        self.label_10.setMaximumSize(QtCore.QSize(18, 18))
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/asterisk.svg")))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_2.addWidget(self.label_10)
        self.label_11 = QtGui.QLabel(self.grp_filters)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_2.addWidget(self.label_11)
        spacerItem3 = QtGui.QSpacerItem(48, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.cbb_type = QtGui.QComboBox(self.grp_filters)
        self.cbb_type.setObjectName(_fromUtf8("cbb_type"))
        self.verticalLayout_2.addWidget(self.cbb_type)
        self.verticalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_9 = QtGui.QLabel(self.grp_filters)
        self.label_9.setMaximumSize(QtCore.QSize(18, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/users.svg")))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.label_3 = QtGui.QLabel(self.grp_filters)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem4 = QtGui.QSpacerItem(148, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.cbb_owner = QtGui.QComboBox(self.grp_filters)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbb_owner.sizePolicy().hasHeightForWidth())
        self.cbb_owner.setSizePolicy(sizePolicy)
        self.cbb_owner.setMinimumSize(QtCore.QSize(30, 0))
        self.cbb_owner.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cbb_owner.setObjectName(_fromUtf8("cbb_owner"))
        self.verticalLayout_5.addWidget(self.cbb_owner)
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_14 = QtGui.QLabel(self.grp_filters)
        self.label_14.setMaximumSize(QtCore.QSize(18, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setText(_fromUtf8(""))
        self.label_14.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/globe.svg")))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_6.addWidget(self.label_14)
        self.label_5 = QtGui.QLabel(self.grp_filters)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        spacerItem5 = QtGui.QSpacerItem(68, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.cbb_srs = QtGui.QComboBox(self.grp_filters)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbb_srs.sizePolicy().hasHeightForWidth())
        self.cbb_srs.setSizePolicy(sizePolicy)
        self.cbb_srs.setMinimumSize(QtCore.QSize(30, 0))
        self.cbb_srs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cbb_srs.setObjectName(_fromUtf8("cbb_srs"))
        self.verticalLayout_7.addWidget(self.cbb_srs)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_13.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_12 = QtGui.QLabel(self.grp_filters)
        self.label_12.setMaximumSize(QtCore.QSize(18, 18))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/play.svg")))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_7.addWidget(self.label_12)
        self.label_6 = QtGui.QLabel(self.grp_filters)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_7.addWidget(self.label_6)
        spacerItem6 = QtGui.QSpacerItem(18, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.checkBox = QtGui.QCheckBox(self.grp_filters)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_7.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.grp_filters)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.horizontalLayout_7.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(self.grp_filters)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.horizontalLayout_7.addWidget(self.checkBox_3)
        self.checkBox_4 = QtGui.QCheckBox(self.grp_filters)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.horizontalLayout_7.addWidget(self.checkBox_4)
        self.verticalLayout_13.addLayout(self.horizontalLayout_7)
        self.gridLayout_2.addLayout(self.verticalLayout_13, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.grp_filters, 1, 0, 1, 1)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.btn_show = QtGui.QPushButton(self.tab)
        self.btn_show.setMinimumSize(QtCore.QSize(201, 0))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/eye.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_show.setIcon(icon3)
        self.btn_show.setObjectName(_fromUtf8("btn_show"))
        self.horizontalLayout_17.addWidget(self.btn_show)
        self.cbb_ob = QtGui.QComboBox(self.tab)
        self.cbb_ob.setObjectName(_fromUtf8("cbb_ob"))
        self.horizontalLayout_17.addWidget(self.cbb_ob)
        self.cbb_od = QtGui.QComboBox(self.tab)
        self.cbb_od.setMinimumSize(QtCore.QSize(0, 0))
        self.cbb_od.setMaximumSize(QtCore.QSize(111, 16777215))
        self.cbb_od.setObjectName(_fromUtf8("cbb_od"))
        self.horizontalLayout_17.addWidget(self.cbb_od)
        self.gridLayout_3.addLayout(self.horizontalLayout_17, 2, 0, 1, 1)
        self.tbl_result = QtGui.QTableWidget(self.tab)
        self.tbl_result.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tbl_result.setObjectName(_fromUtf8("tbl_result"))
        self.tbl_result.setColumnCount(4)
        self.tbl_result.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tbl_result.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_result.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_result.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_result.setHorizontalHeaderItem(3, item)
        self.tbl_result.horizontalHeader().setVisible(True)
        self.tbl_result.horizontalHeader().setSortIndicatorShown(False)
        self.tbl_result.verticalHeader().setVisible(True)
        self.gridLayout_3.addWidget(self.tbl_result, 3, 0, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        spacerItem7 = QtGui.QSpacerItem(98, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.btn_previous = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_previous.sizePolicy().hasHeightForWidth())
        self.btn_previous.setSizePolicy(sizePolicy)
        self.btn_previous.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/caret-left.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_previous.setIcon(icon4)
        self.btn_previous.setObjectName(_fromUtf8("btn_previous"))
        self.horizontalLayout_12.addWidget(self.btn_previous)
        self.lbl_page = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_page.setFont(font)
        self.lbl_page.setObjectName(_fromUtf8("lbl_page"))
        self.horizontalLayout_12.addWidget(self.lbl_page)
        self.btn_next = QtGui.QPushButton(self.tab)
        self.btn_next.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/caret-right.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next.setIcon(icon5)
        self.btn_next.setObjectName(_fromUtf8("btn_next"))
        self.horizontalLayout_12.addWidget(self.btn_next)
        spacerItem8 = QtGui.QSpacerItem(128, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.gridLayout_3.addLayout(self.horizontalLayout_12, 4, 0, 1, 1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/search.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon6, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 121))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.cbb_modify_sr = QtGui.QComboBox(self.groupBox_2)
        self.cbb_modify_sr.setMinimumSize(QtCore.QSize(221, 20))
        self.cbb_modify_sr.setObjectName(_fromUtf8("cbb_modify_sr"))
        self.horizontalLayout_9.addWidget(self.cbb_modify_sr)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.btn_rename_sr = QtGui.QPushButton(self.groupBox_2)
        self.btn_rename_sr.setMinimumSize(QtCore.QSize(111, 24))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btn_rename_sr.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/pencil.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_rename_sr.setIcon(icon7)
        self.btn_rename_sr.setObjectName(_fromUtf8("btn_rename_sr"))
        self.horizontalLayout_9.addWidget(self.btn_rename_sr)
        self.btn_delete_sr = QtGui.QPushButton(self.groupBox_2)
        self.btn_delete_sr.setMinimumSize(QtCore.QSize(61, 24))
        self.btn_delete_sr.setMaximumSize(QtCore.QSize(61, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btn_delete_sr.setFont(font)
        self.btn_delete_sr.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/trash.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete_sr.setIcon(icon8)
        self.btn_delete_sr.setObjectName(_fromUtf8("btn_delete_sr"))
        self.horizontalLayout_9.addWidget(self.btn_delete_sr)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_20 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_10.addWidget(self.label_20)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        self.btn_default = QtGui.QPushButton(self.groupBox_2)
        self.btn_default.setMinimumSize(QtCore.QSize(111, 24))
        self.btn_default.setText(_fromUtf8(""))
        self.btn_default.setIcon(icon1)
        self.btn_default.setObjectName(_fromUtf8("btn_default"))
        self.horizontalLayout_10.addWidget(self.btn_default)
        self.btn_reset_default = QtGui.QPushButton(self.groupBox_2)
        self.btn_reset_default.setMinimumSize(QtCore.QSize(61, 24))
        self.btn_reset_default.setMaximumSize(QtCore.QSize(61, 16777215))
        self.btn_reset_default.setText(_fromUtf8(""))
        self.btn_reset_default.setIcon(icon2)
        self.btn_reset_default.setObjectName(_fromUtf8("btn_reset_default"))
        self.horizontalLayout_10.addWidget(self.btn_reset_default)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_11.addWidget(self.label_15)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.cbb_geo_op = QtGui.QComboBox(self.groupBox_2)
        self.cbb_geo_op.setMinimumSize(QtCore.QSize(176, 20))
        self.cbb_geo_op.setObjectName(_fromUtf8("cbb_geo_op"))
        self.horizontalLayout_11.addWidget(self.cbb_geo_op)
        self.verticalLayout_10.addLayout(self.horizontalLayout_11)
        self.gridLayout_4.addLayout(self.verticalLayout_10, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.txt_shares = QtGui.QTextBrowser(self.groupBox)
        self.txt_shares.setObjectName(_fromUtf8("txt_shares"))
        self.gridLayout_5.addWidget(self.txt_shares, 1, 0, 1, 1)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.label_16 = QtGui.QLabel(self.groupBox)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_21.addWidget(self.label_16)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem12)
        self.btn_change_user = QtGui.QPushButton(self.groupBox)
        self.btn_change_user.setMinimumSize(QtCore.QSize(91, 0))
        self.btn_change_user.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/user-times.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_change_user.setIcon(icon9)
        self.btn_change_user.setObjectName(_fromUtf8("btn_change_user"))
        self.horizontalLayout_21.addWidget(self.btn_change_user)
        self.gridLayout_5.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.label_17 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_24.addWidget(self.label_17)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem13)
        self.btn_report = QtGui.QPushButton(self.groupBox_4)
        self.btn_report.setMinimumSize(QtCore.QSize(91, 0))
        self.btn_report.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/bullhorn.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_report.setIcon(icon10)
        self.btn_report.setObjectName(_fromUtf8("btn_report"))
        self.horizontalLayout_24.addWidget(self.btn_report)
        self.verticalLayout_12.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.label_18 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_23.addWidget(self.label_18)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem14)
        self.btn_help = QtGui.QPushButton(self.groupBox_4)
        self.btn_help.setMinimumSize(QtCore.QSize(91, 0))
        self.btn_help.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/question.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_help.setIcon(icon11)
        self.btn_help.setObjectName(_fromUtf8("btn_help"))
        self.horizontalLayout_23.addWidget(self.btn_help)
        self.verticalLayout_12.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.label_19 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_22.addWidget(self.label_19)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem15)
        self.btn_credits = QtGui.QPushButton(self.groupBox_4)
        self.btn_credits.setMinimumSize(QtCore.QSize(91, 0))
        self.btn_credits.setText(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/info.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_credits.setIcon(icon12)
        self.btn_credits.setObjectName(_fromUtf8("btn_credits"))
        self.horizontalLayout_22.addWidget(self.btn_credits)
        self.verticalLayout_12.addLayout(self.horizontalLayout_22)
        self.gridLayout_6.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_4, 2, 0, 1, 1)
        spacerItem16 = QtGui.QSpacerItem(20, 105, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem16, 3, 0, 1, 1)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/gear.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon13, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        IsogeoDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(IsogeoDockWidgetBase)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(IsogeoDockWidgetBase)

    def retranslateUi(self, IsogeoDockWidgetBase):
        self.btn_save.setToolTip(_translate("IsogeoDockWidgetBase", "Save research", None))
        self.btn_reinit.setToolTip(_translate("IsogeoDockWidgetBase", "Reset all input fields", None))
        self.grp_filters.setTitle(_translate("IsogeoDockWidgetBase", "Advanced search", None))
        self.label_7.setText(_translate("IsogeoDockWidgetBase", "Geographic filter", None))
        self.label_8.setText(_translate("IsogeoDockWidgetBase", "Format", None))
        self.label_4.setText(_translate("IsogeoDockWidgetBase", "INSPIRE keywords", None))
        self.label_11.setText(_translate("IsogeoDockWidgetBase", "Resource type", None))
        self.label_3.setText(_translate("IsogeoDockWidgetBase", "Owner", None))
        self.label_5.setText(_translate("IsogeoDockWidgetBase", "Coordinate system", None))
        self.label_6.setText(_translate("IsogeoDockWidgetBase", "Associated resources", None))
        self.checkBox.setText(_translate("IsogeoDockWidgetBase", "View", None))
        self.checkBox_2.setText(_translate("IsogeoDockWidgetBase", "Download", None))
        self.checkBox_3.setText(_translate("IsogeoDockWidgetBase", "Other actions", None))
        self.checkBox_4.setText(_translate("IsogeoDockWidgetBase", "None", None))
        self.btn_show.setToolTip(_translate("IsogeoDockWidgetBase", "Display the results list", None))
        self.btn_show.setText(_translate("IsogeoDockWidgetBase", "Show results", None))
        self.cbb_ob.setToolTip(_translate("IsogeoDockWidgetBase", "Sorting method", None))
        self.cbb_od.setToolTip(_translate("IsogeoDockWidgetBase", "Sorting direction", None))
        self.tbl_result.setSortingEnabled(False)
        item = self.tbl_result.horizontalHeaderItem(0)
        item.setText(_translate("IsogeoDockWidgetBase", "Title", None))
        item = self.tbl_result.horizontalHeaderItem(1)
        item.setText(_translate("IsogeoDockWidgetBase", "Modified", None))
        item = self.tbl_result.horizontalHeaderItem(2)
        item.setText(_translate("IsogeoDockWidgetBase", "Type", None))
        item = self.tbl_result.horizontalHeaderItem(3)
        item.setText(_translate("IsogeoDockWidgetBase", "Add", None))
        self.lbl_page.setText(_translate("IsogeoDockWidgetBase", "Page x sur x", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("IsogeoDockWidgetBase", "Search", None))
        self.groupBox_2.setTitle(_translate("IsogeoDockWidgetBase", "Search settings", None))
        self.btn_rename_sr.setText(_translate("IsogeoDockWidgetBase", "Rename", None))
        self.label_20.setText(_translate("IsogeoDockWidgetBase", "Default search", None))
        self.label_15.setText(_translate("IsogeoDockWidgetBase", "Geographical operator applied to the filter", None))
        self.groupBox.setTitle(_translate("IsogeoDockWidgetBase", "Authentication settings", None))
        self.label_16.setText(_translate("IsogeoDockWidgetBase", "Change user id and secret", None))
        self.groupBox_4.setTitle(_translate("IsogeoDockWidgetBase", "Resources", None))
        self.label_17.setText(_translate("IsogeoDockWidgetBase", "Report an issue on the bug tracker", None))
        self.label_18.setText(_translate("IsogeoDockWidgetBase", "Open online plugin help", None))
        self.label_19.setText(_translate("IsogeoDockWidgetBase", "Open plugin credits", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("IsogeoDockWidgetBase", "Settings", None))

from qgis.gui import QgsCollapsibleGroupBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    IsogeoDockWidgetBase = QtGui.QDockWidget()
    ui = Ui_IsogeoDockWidgetBase()
    ui.setupUi(IsogeoDockWidgetBase)
    IsogeoDockWidgetBase.show()
    sys.exit(app.exec_())

