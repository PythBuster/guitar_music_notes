# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
                               QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QMenu, QMenuBar, QPushButton,
                               QRadioButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 595)
        self.action_Close = QAction(MainWindow)
        self.action_Close.setObjectName("action_Close")
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionAbout_Guitar_Music_Notes = QAction(MainWindow)
        self.actionAbout_Guitar_Music_Notes.setObjectName(
            "actionAbout_Guitar_Music_Notes"
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_next_note_settings = QGroupBox(self.centralwidget)
        self.groupBox_next_note_settings.setObjectName("groupBox_next_note_settings")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_next_note_settings)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 6)
        self.groupBox_next_note_raido_buttons = QGroupBox(
            self.groupBox_next_note_settings
        )
        self.groupBox_next_note_raido_buttons.setObjectName(
            "groupBox_next_note_raido_buttons"
        )
        self.groupBox_next_note_raido_buttons.setStyleSheet("QGroupBox {border:0;}")
        self.groupBox_next_note_raido_buttons.setFlat(False)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_next_note_raido_buttons)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.radioButton_timer = QRadioButton(self.groupBox_next_note_raido_buttons)
        self.radioButton_timer.setObjectName("radioButton_timer")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.radioButton_timer.sizePolicy().hasHeightForWidth()
        )
        self.radioButton_timer.setSizePolicy(sizePolicy)
        self.radioButton_timer.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton_timer)

        self.radioButton_manually = QRadioButton(self.groupBox_next_note_raido_buttons)
        self.radioButton_manually.setObjectName("radioButton_manually")
        sizePolicy.setHeightForWidth(
            self.radioButton_manually.sizePolicy().hasHeightForWidth()
        )
        self.radioButton_manually.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.radioButton_manually)

        self.horizontalLayout.addWidget(self.groupBox_next_note_raido_buttons)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.groupBox_timer_settings = QGroupBox(self.groupBox_next_note_settings)
        self.groupBox_timer_settings.setObjectName("groupBox_timer_settings")
        font = QFont()
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.groupBox_timer_settings.setFont(font)
        self.groupBox_timer_settings.setStyleSheet("QGroupBox {border:0;}")
        self.groupBox_timer_settings.setFlat(True)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_timer_settings)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.lineEdit_timer_seconds = QLineEdit(self.groupBox_timer_settings)
        self.lineEdit_timer_seconds.setObjectName("lineEdit_timer_seconds")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.lineEdit_timer_seconds.sizePolicy().hasHeightForWidth()
        )
        self.lineEdit_timer_seconds.setSizePolicy(sizePolicy1)
        self.lineEdit_timer_seconds.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_timer_seconds.setStyleSheet("")
        self.lineEdit_timer_seconds.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit_timer_seconds.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_timer_seconds)

        self.label_timer_seconds = QLabel(self.groupBox_timer_settings)
        self.label_timer_seconds.setObjectName("label_timer_seconds")

        self.horizontalLayout_2.addWidget(self.label_timer_seconds)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2.addWidget(self.groupBox_timer_settings)

        self.verticalLayout.addWidget(self.groupBox_next_note_settings)

        self.verticalSpacer_2 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_selection_hint = QLabel(self.centralwidget)
        self.label_selection_hint.setObjectName("label_selection_hint")
        font1 = QFont()
        font1.setBold(True)
        self.label_selection_hint.setFont(font1)
        self.label_selection_hint.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.label_selection_hint)

        self.groupBox_select_notes = QGroupBox(self.centralwidget)
        self.groupBox_select_notes.setObjectName("groupBox_select_notes")
        self.gridLayout = QGridLayout(self.groupBox_select_notes)
        self.gridLayout.setObjectName("gridLayout")
        self.note_c = QCheckBox(self.groupBox_select_notes)
        self.note_c.setObjectName("note_c")

        self.gridLayout.addWidget(self.note_c, 13, 0, 1, 1)

        self.note__g = QCheckBox(self.groupBox_select_notes)
        self.note__g.setObjectName("note__g")

        self.gridLayout.addWidget(self.note__g, 6, 0, 1, 1)

        self.note_b__ = QCheckBox(self.groupBox_select_notes)
        self.note_b__.setObjectName("note_b__")

        self.gridLayout.addWidget(self.note_b__, 14, 4, 1, 1)

        self.note_dis = QCheckBox(self.groupBox_select_notes)
        self.note_dis.setObjectName("note_dis")

        self.gridLayout.addWidget(self.note_dis, 17, 0, 1, 1)

        self.note_c___ = QCheckBox(self.groupBox_select_notes)
        self.note_c___.setObjectName("note_c___")

        self.gridLayout.addWidget(self.note_c___, 16, 4, 1, 1)

        self.note_cis = QCheckBox(self.groupBox_select_notes)
        self.note_cis.setObjectName("note_cis")

        self.gridLayout.addWidget(self.note_cis, 14, 0, 1, 1)

        self.note__fis = QCheckBox(self.groupBox_select_notes)
        self.note__fis.setObjectName("note__fis")

        self.gridLayout.addWidget(self.note__fis, 4, 0, 1, 1)

        self.note___ais = QCheckBox(self.groupBox_select_notes)
        self.note___ais.setObjectName("note___ais")

        self.gridLayout.addWidget(self.note___ais, 10, 0, 1, 1)

        self.note__as = QCheckBox(self.groupBox_select_notes)
        self.note__as.setObjectName("note__as")

        self.gridLayout.addWidget(self.note__as, 8, 0, 1, 1)

        self.note_d = QCheckBox(self.groupBox_select_notes)
        self.note_d.setObjectName("note_d")

        self.gridLayout.addWidget(self.note_d, 16, 0, 1, 1)

        self.note__gis = QCheckBox(self.groupBox_select_notes)
        self.note__gis.setObjectName("note__gis")

        self.gridLayout.addWidget(self.note__gis, 7, 0, 1, 1)

        self.note_ais_ = QCheckBox(self.groupBox_select_notes)
        self.note_ais_.setObjectName("note_ais_")

        self.gridLayout.addWidget(self.note_ais_, 12, 3, 1, 1)

        self.note_h_ = QCheckBox(self.groupBox_select_notes)
        self.note_h_.setObjectName("note_h_")

        self.gridLayout.addWidget(self.note_h_, 14, 3, 1, 1)

        self.note__h = QCheckBox(self.groupBox_select_notes)
        self.note__h.setObjectName("note__h")

        self.gridLayout.addWidget(self.note__h, 12, 0, 1, 1)

        self.note_b_ = QCheckBox(self.groupBox_select_notes)
        self.note_b_.setObjectName("note_b_")

        self.gridLayout.addWidget(self.note_b_, 13, 3, 1, 1)

        self.note__a = QCheckBox(self.groupBox_select_notes)
        self.note__a.setObjectName("note__a")

        self.gridLayout.addWidget(self.note__a, 9, 0, 1, 1)

        self.note_c__ = QCheckBox(self.groupBox_select_notes)
        self.note_c__.setObjectName("note_c__")

        self.gridLayout.addWidget(self.note_c__, 15, 3, 1, 1)

        self.note__e = QCheckBox(self.groupBox_select_notes)
        self.note__e.setObjectName("note__e")

        self.gridLayout.addWidget(self.note__e, 2, 0, 1, 1)

        self.note_gis__ = QCheckBox(self.groupBox_select_notes)
        self.note_gis__.setObjectName("note_gis__")

        self.gridLayout.addWidget(self.note_gis__, 10, 4, 1, 1)

        self.note_h__ = QCheckBox(self.groupBox_select_notes)
        self.note_h__.setObjectName("note_h__")

        self.gridLayout.addWidget(self.note_h__, 15, 4, 1, 1)

        self.note_as__ = QCheckBox(self.groupBox_select_notes)
        self.note_as__.setObjectName("note_as__")

        self.gridLayout.addWidget(self.note_as__, 11, 4, 1, 1)

        self.note_a__ = QCheckBox(self.groupBox_select_notes)
        self.note_a__.setObjectName("note_a__")

        self.gridLayout.addWidget(self.note_a__, 12, 4, 1, 1)

        self.note_ais__ = QCheckBox(self.groupBox_select_notes)
        self.note_ais__.setObjectName("note_ais__")

        self.gridLayout.addWidget(self.note_ais__, 13, 4, 1, 1)

        self.note__ges = QCheckBox(self.groupBox_select_notes)
        self.note__ges.setObjectName("note__ges")

        self.gridLayout.addWidget(self.note__ges, 5, 0, 1, 1)

        self.note__f = QCheckBox(self.groupBox_select_notes)
        self.note__f.setObjectName("note__f")

        self.gridLayout.addWidget(self.note__f, 3, 0, 1, 1)

        self.note__b = QCheckBox(self.groupBox_select_notes)
        self.note__b.setObjectName("note__b")

        self.gridLayout.addWidget(self.note__b, 11, 0, 1, 1)

        self.note_des = QCheckBox(self.groupBox_select_notes)
        self.note_des.setObjectName("note_des")

        self.gridLayout.addWidget(self.note_des, 15, 0, 1, 1)

        self.note_fis__ = QCheckBox(self.groupBox_select_notes)
        self.note_fis__.setObjectName("note_fis__")

        self.gridLayout.addWidget(self.note_fis__, 7, 4, 1, 1)

        self.note_f__ = QCheckBox(self.groupBox_select_notes)
        self.note_f__.setObjectName("note_f__")

        self.gridLayout.addWidget(self.note_f__, 6, 4, 1, 1)

        self.note_ges__ = QCheckBox(self.groupBox_select_notes)
        self.note_ges__.setObjectName("note_ges__")

        self.gridLayout.addWidget(self.note_ges__, 8, 4, 1, 1)

        self.note_es__ = QCheckBox(self.groupBox_select_notes)
        self.note_es__.setObjectName("note_es__")

        self.gridLayout.addWidget(self.note_es__, 4, 4, 1, 1)

        self.note_g__ = QCheckBox(self.groupBox_select_notes)
        self.note_g__.setObjectName("note_g__")

        self.gridLayout.addWidget(self.note_g__, 9, 4, 1, 1)

        self.note_e__ = QCheckBox(self.groupBox_select_notes)
        self.note_e__.setObjectName("note_e__")

        self.gridLayout.addWidget(self.note_e__, 5, 4, 1, 1)

        self.note_dis__ = QCheckBox(self.groupBox_select_notes)
        self.note_dis__.setObjectName("note_dis__")

        self.gridLayout.addWidget(self.note_dis__, 3, 4, 1, 1)

        self.note_d__ = QCheckBox(self.groupBox_select_notes)
        self.note_d__.setObjectName("note_d__")

        self.gridLayout.addWidget(self.note_d__, 2, 4, 1, 1)

        self.note_a_ = QCheckBox(self.groupBox_select_notes)
        self.note_a_.setObjectName("note_a_")

        self.gridLayout.addWidget(self.note_a_, 11, 3, 1, 1)

        self.note_cis__ = QCheckBox(self.groupBox_select_notes)
        self.note_cis__.setObjectName("note_cis__")

        self.gridLayout.addWidget(self.note_cis__, 16, 3, 1, 1)

        self.note_f = QCheckBox(self.groupBox_select_notes)
        self.note_f.setObjectName("note_f")

        self.gridLayout.addWidget(self.note_f, 4, 2, 1, 1)

        self.note_gis = QCheckBox(self.groupBox_select_notes)
        self.note_gis.setObjectName("note_gis")

        self.gridLayout.addWidget(self.note_gis, 8, 2, 1, 1)

        self.note_fis = QCheckBox(self.groupBox_select_notes)
        self.note_fis.setObjectName("note_fis")

        self.gridLayout.addWidget(self.note_fis, 5, 2, 1, 1)

        self.note_g = QCheckBox(self.groupBox_select_notes)
        self.note_g.setObjectName("note_g")

        self.gridLayout.addWidget(self.note_g, 7, 2, 1, 1)

        self.note_as = QCheckBox(self.groupBox_select_notes)
        self.note_as.setObjectName("note_as")

        self.gridLayout.addWidget(self.note_as, 9, 2, 1, 1)

        self.note_ges = QCheckBox(self.groupBox_select_notes)
        self.note_ges.setObjectName("note_ges")

        self.gridLayout.addWidget(self.note_ges, 6, 2, 1, 1)

        self.note_e = QCheckBox(self.groupBox_select_notes)
        self.note_e.setObjectName("note_e")

        self.gridLayout.addWidget(self.note_e, 3, 2, 1, 1)

        self.note_ais = QCheckBox(self.groupBox_select_notes)
        self.note_ais.setObjectName("note_ais")

        self.gridLayout.addWidget(self.note_ais, 11, 2, 1, 1)

        self.note_a = QCheckBox(self.groupBox_select_notes)
        self.note_a.setObjectName("note_a")

        self.gridLayout.addWidget(self.note_a, 10, 2, 1, 1)

        self.note_b = QCheckBox(self.groupBox_select_notes)
        self.note_b.setObjectName("note_b")

        self.gridLayout.addWidget(self.note_b, 12, 2, 1, 1)

        self.note_es = QCheckBox(self.groupBox_select_notes)
        self.note_es.setObjectName("note_es")

        self.gridLayout.addWidget(self.note_es, 2, 2, 1, 1)

        self.note_e_ = QCheckBox(self.groupBox_select_notes)
        self.note_e_.setObjectName("note_e_")

        self.gridLayout.addWidget(self.note_e_, 4, 3, 1, 1)

        self.note_des_ = QCheckBox(self.groupBox_select_notes)
        self.note_des_.setObjectName("note_des_")

        self.gridLayout.addWidget(self.note_des_, 16, 2, 1, 1)

        self.note_des__ = QCheckBox(self.groupBox_select_notes)
        self.note_des__.setObjectName("note_des__")

        self.gridLayout.addWidget(self.note_des__, 17, 3, 1, 1)

        self.note_f_ = QCheckBox(self.groupBox_select_notes)
        self.note_f_.setObjectName("note_f_")

        self.gridLayout.addWidget(self.note_f_, 5, 3, 1, 1)

        self.note_fis_ = QCheckBox(self.groupBox_select_notes)
        self.note_fis_.setObjectName("note_fis_")

        self.gridLayout.addWidget(self.note_fis_, 6, 3, 1, 1)

        self.note_c_ = QCheckBox(self.groupBox_select_notes)
        self.note_c_.setObjectName("note_c_")

        self.gridLayout.addWidget(self.note_c_, 14, 2, 1, 1)

        self.note_dis_ = QCheckBox(self.groupBox_select_notes)
        self.note_dis_.setObjectName("note_dis_")

        self.gridLayout.addWidget(self.note_dis_, 2, 3, 1, 1)

        self.note_cis_ = QCheckBox(self.groupBox_select_notes)
        self.note_cis_.setObjectName("note_cis_")

        self.gridLayout.addWidget(self.note_cis_, 15, 2, 1, 1)

        self.note_d_ = QCheckBox(self.groupBox_select_notes)
        self.note_d_.setObjectName("note_d_")

        self.gridLayout.addWidget(self.note_d_, 17, 2, 1, 1)

        self.note_h = QCheckBox(self.groupBox_select_notes)
        self.note_h.setObjectName("note_h")

        self.gridLayout.addWidget(self.note_h, 13, 2, 1, 1)

        self.note_es_ = QCheckBox(self.groupBox_select_notes)
        self.note_es_.setObjectName("note_es_")

        self.gridLayout.addWidget(self.note_es_, 3, 3, 1, 1)

        self.note_ges_ = QCheckBox(self.groupBox_select_notes)
        self.note_ges_.setObjectName("note_ges_")

        self.gridLayout.addWidget(self.note_ges_, 7, 3, 1, 1)

        self.note_as_ = QCheckBox(self.groupBox_select_notes)
        self.note_as_.setObjectName("note_as_")

        self.gridLayout.addWidget(self.note_as_, 10, 3, 1, 1)

        self.note_g_ = QCheckBox(self.groupBox_select_notes)
        self.note_g_.setObjectName("note_g_")

        self.gridLayout.addWidget(self.note_g_, 8, 3, 1, 1)

        self.note_gis_ = QCheckBox(self.groupBox_select_notes)
        self.note_gis_.setObjectName("note_gis_")

        self.gridLayout.addWidget(self.note_gis_, 9, 3, 1, 1)

        self.verticalLayout.addWidget(self.groupBox_select_notes)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(
            250, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushButton_start_training = QPushButton(self.centralwidget)
        self.pushButton_start_training.setObjectName("pushButton_start_training")

        self.horizontalLayout_4.addWidget(self.pushButton_start_training)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 351, 21))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuAbout_Qt = QMenu(self.menubar)
        self.menuAbout_Qt.setObjectName("menuAbout_Qt")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuAbout_Qt.menuAction())
        self.menu_File.addAction(self.action_Close)
        self.menuAbout_Qt.addAction(self.actionAbout_Qt)
        self.menuAbout_Qt.addAction(self.actionAbout_Guitar_Music_Notes)

        self.retranslateUi(MainWindow)
        self.action_Close.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Guitar Music Notes", None)
        )
        self.action_Close.setText(
            QCoreApplication.translate("MainWindow", "&Close", None)
        )
        self.actionAbout_Qt.setText(
            QCoreApplication.translate("MainWindow", "About &Qt", None)
        )
        self.actionAbout_Guitar_Music_Notes.setText(
            QCoreApplication.translate("MainWindow", "About &Guitar Music Notes", None)
        )
        self.groupBox_next_note_settings.setTitle(
            QCoreApplication.translate("MainWindow", "Next Note Seelction", None)
        )
        self.groupBox_next_note_raido_buttons.setTitle("")
        self.radioButton_timer.setText(
            QCoreApplication.translate("MainWindow", "Timer", None)
        )
        self.radioButton_manually.setText(
            QCoreApplication.translate("MainWindow", "Next Note manually", None)
        )
        self.groupBox_timer_settings.setTitle("")
        self.lineEdit_timer_seconds.setText(
            QCoreApplication.translate("MainWindow", "4", None)
        )
        self.label_timer_seconds.setText(
            QCoreApplication.translate("MainWindow", "seconds", None)
        )
        self.label_selection_hint.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Note: If no note is selected, all notes will be trained!",
                None,
            )
        )
        self.groupBox_select_notes.setTitle(
            QCoreApplication.translate("MainWindow", "Select Notes", None)
        )
        self.note_c.setText(QCoreApplication.translate("MainWindow", "c", None))
        self.note__g.setText(QCoreApplication.translate("MainWindow", "G", None))
        self.note_b__.setText(QCoreApplication.translate("MainWindow", "b ' '", None))
        self.note_dis.setText(QCoreApplication.translate("MainWindow", "# d", None))
        self.note_c___.setText(
            QCoreApplication.translate("MainWindow", "c ' ' '", None)
        )
        self.note_cis.setText(QCoreApplication.translate("MainWindow", "# c", None))
        self.note__fis.setText(QCoreApplication.translate("MainWindow", "# F", None))
        self.note___ais.setText(QCoreApplication.translate("MainWindow", "# A", None))
        self.note__as.setText(QCoreApplication.translate("MainWindow", "\u266dA", None))
        self.note_d.setText(QCoreApplication.translate("MainWindow", "d", None))
        self.note__gis.setText(QCoreApplication.translate("MainWindow", "# G", None))
        self.note_ais_.setText(QCoreApplication.translate("MainWindow", "# a '", None))
        self.note_h_.setText(QCoreApplication.translate("MainWindow", "h '", None))
        self.note__h.setText(QCoreApplication.translate("MainWindow", "H", None))
        self.note_b_.setText(QCoreApplication.translate("MainWindow", "b '", None))
        self.note__a.setText(QCoreApplication.translate("MainWindow", "A", None))
        self.note_c__.setText(QCoreApplication.translate("MainWindow", "c ' '", None))
        self.note__e.setText(QCoreApplication.translate("MainWindow", "E", None))
        self.note_gis__.setText(
            QCoreApplication.translate("MainWindow", "# g ' '", None)
        )
        self.note_h__.setText(QCoreApplication.translate("MainWindow", "h ' '", None))
        self.note_as__.setText(
            QCoreApplication.translate("MainWindow", "\u266da ' '", None)
        )
        self.note_a__.setText(QCoreApplication.translate("MainWindow", "a ' '", None))
        self.note_ais__.setText(
            QCoreApplication.translate("MainWindow", "# a ' '", None)
        )
        self.note__ges.setText(
            QCoreApplication.translate("MainWindow", "\u266dG", None)
        )
        self.note__f.setText(QCoreApplication.translate("MainWindow", "F", None))
        self.note__b.setText(QCoreApplication.translate("MainWindow", "B", None))
        self.note_des.setText(QCoreApplication.translate("MainWindow", "\u266dd", None))
        self.note_fis__.setText(
            QCoreApplication.translate("MainWindow", "# f ' '", None)
        )
        self.note_f__.setText(QCoreApplication.translate("MainWindow", "f ' '", None))
        self.note_ges__.setText(
            QCoreApplication.translate("MainWindow", "\u266dg ' '", None)
        )
        self.note_es__.setText(
            QCoreApplication.translate("MainWindow", "\u266de ' '", None)
        )
        self.note_g__.setText(QCoreApplication.translate("MainWindow", "g ' '", None))
        self.note_e__.setText(QCoreApplication.translate("MainWindow", "e ' '", None))
        self.note_dis__.setText(
            QCoreApplication.translate("MainWindow", "# d ' '", None)
        )
        self.note_d__.setText(QCoreApplication.translate("MainWindow", "d ' '", None))
        self.note_a_.setText(QCoreApplication.translate("MainWindow", "a '", None))
        self.note_cis__.setText(
            QCoreApplication.translate("MainWindow", "# c ' '", None)
        )
        self.note_f.setText(QCoreApplication.translate("MainWindow", "f", None))
        self.note_gis.setText(QCoreApplication.translate("MainWindow", "# g", None))
        self.note_fis.setText(QCoreApplication.translate("MainWindow", "# f", None))
        self.note_g.setText(QCoreApplication.translate("MainWindow", "g", None))
        self.note_as.setText(QCoreApplication.translate("MainWindow", "\u266da", None))
        self.note_ges.setText(QCoreApplication.translate("MainWindow", "\u266dg", None))
        self.note_e.setText(QCoreApplication.translate("MainWindow", "e", None))
        self.note_ais.setText(QCoreApplication.translate("MainWindow", "# a", None))
        self.note_a.setText(QCoreApplication.translate("MainWindow", "a", None))
        self.note_b.setText(QCoreApplication.translate("MainWindow", "b", None))
        self.note_es.setText(QCoreApplication.translate("MainWindow", "\u266de", None))
        self.note_e_.setText(QCoreApplication.translate("MainWindow", "e '", None))
        self.note_des_.setText(
            QCoreApplication.translate("MainWindow", "\u266dd '", None)
        )
        self.note_des__.setText(
            QCoreApplication.translate("MainWindow", "\u266dd ' '", None)
        )
        self.note_f_.setText(QCoreApplication.translate("MainWindow", "f '", None))
        self.note_fis_.setText(QCoreApplication.translate("MainWindow", "# f '", None))
        self.note_c_.setText(QCoreApplication.translate("MainWindow", "c '", None))
        self.note_dis_.setText(QCoreApplication.translate("MainWindow", "# d '", None))
        self.note_cis_.setText(QCoreApplication.translate("MainWindow", "# c '", None))
        self.note_d_.setText(QCoreApplication.translate("MainWindow", "d '", None))
        self.note_h.setText(QCoreApplication.translate("MainWindow", "h", None))
        self.note_es_.setText(
            QCoreApplication.translate("MainWindow", "\u266de '", None)
        )
        self.note_ges_.setText(
            QCoreApplication.translate("MainWindow", "\u266dg '", None)
        )
        self.note_as_.setText(
            QCoreApplication.translate("MainWindow", "\u266da '", None)
        )
        self.note_g_.setText(QCoreApplication.translate("MainWindow", "g '", None))
        self.note_gis_.setText(QCoreApplication.translate("MainWindow", "# g '", None))
        self.pushButton_start_training.setText(
            QCoreApplication.translate("MainWindow", "Start Training", None)
        )
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", "&File", None))
        self.menuAbout_Qt.setTitle(
            QCoreApplication.translate("MainWindow", "&Help", None)
        )

    # retranslateUi
