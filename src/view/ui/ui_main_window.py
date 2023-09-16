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
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(351, 595)
        self.action_Close = QAction(MainWindow)
        self.action_Close.setObjectName(u"action_Close")
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.actionAbout_Guitar_Music_Notes = QAction(MainWindow)
        self.actionAbout_Guitar_Music_Notes.setObjectName(u"actionAbout_Guitar_Music_Notes")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_next_note_settings = QGroupBox(self.centralwidget)
        self.groupBox_next_note_settings.setObjectName(u"groupBox_next_note_settings")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_next_note_settings)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 6)
        self.groupBox_next_note_raido_buttons = QGroupBox(self.groupBox_next_note_settings)
        self.groupBox_next_note_raido_buttons.setObjectName(u"groupBox_next_note_raido_buttons")
        self.groupBox_next_note_raido_buttons.setStyleSheet(u"QGroupBox {border:0;}")
        self.groupBox_next_note_raido_buttons.setFlat(False)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_next_note_raido_buttons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.radioButton_timer = QRadioButton(self.groupBox_next_note_raido_buttons)
        self.radioButton_timer.setObjectName(u"radioButton_timer")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_timer.sizePolicy().hasHeightForWidth())
        self.radioButton_timer.setSizePolicy(sizePolicy)
        self.radioButton_timer.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton_timer)

        self.radioButton_manually = QRadioButton(self.groupBox_next_note_raido_buttons)
        self.radioButton_manually.setObjectName(u"radioButton_manually")
        sizePolicy.setHeightForWidth(self.radioButton_manually.sizePolicy().hasHeightForWidth())
        self.radioButton_manually.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.radioButton_manually)


        self.horizontalLayout.addWidget(self.groupBox_next_note_raido_buttons)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.groupBox_timer_settings = QGroupBox(self.groupBox_next_note_settings)
        self.groupBox_timer_settings.setObjectName(u"groupBox_timer_settings")
        font = QFont()
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.groupBox_timer_settings.setFont(font)
        self.groupBox_timer_settings.setStyleSheet(u"QGroupBox {border:0;}")
        self.groupBox_timer_settings.setFlat(True)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_timer_settings)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.lineEdit_timer_seconds = QLineEdit(self.groupBox_timer_settings)
        self.lineEdit_timer_seconds.setObjectName(u"lineEdit_timer_seconds")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_timer_seconds.sizePolicy().hasHeightForWidth())
        self.lineEdit_timer_seconds.setSizePolicy(sizePolicy1)
        self.lineEdit_timer_seconds.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_timer_seconds.setStyleSheet(u"")
        self.lineEdit_timer_seconds.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit_timer_seconds.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_timer_seconds)

        self.label_timer_seconds = QLabel(self.groupBox_timer_settings)
        self.label_timer_seconds.setObjectName(u"label_timer_seconds")

        self.horizontalLayout_2.addWidget(self.label_timer_seconds)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.groupBox_timer_settings)

        self.checkBox_follow_with_solution = QCheckBox(self.groupBox_next_note_settings)
        self.checkBox_follow_with_solution.setObjectName(u"checkBox_follow_with_solution")

        self.verticalLayout_2.addWidget(self.checkBox_follow_with_solution)


        self.verticalLayout.addWidget(self.groupBox_next_note_settings)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_selection_hint = QLabel(self.centralwidget)
        self.label_selection_hint.setObjectName(u"label_selection_hint")
        font1 = QFont()
        font1.setBold(True)
        self.label_selection_hint.setFont(font1)
        self.label_selection_hint.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.label_selection_hint)

        self.groupBox_select_notes = QGroupBox(self.centralwidget)
        self.groupBox_select_notes.setObjectName(u"groupBox_select_notes")
        self.gridLayout = QGridLayout(self.groupBox_select_notes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.note_c = QCheckBox(self.groupBox_select_notes)
        self.note_c.setObjectName(u"note_c")

        self.gridLayout.addWidget(self.note_c, 13, 0, 1, 1)

        self.note__g = QCheckBox(self.groupBox_select_notes)
        self.note__g.setObjectName(u"note__g")

        self.gridLayout.addWidget(self.note__g, 6, 0, 1, 1)

        self.note_b__ = QCheckBox(self.groupBox_select_notes)
        self.note_b__.setObjectName(u"note_b__")

        self.gridLayout.addWidget(self.note_b__, 14, 4, 1, 1)

        self.note_dis = QCheckBox(self.groupBox_select_notes)
        self.note_dis.setObjectName(u"note_dis")

        self.gridLayout.addWidget(self.note_dis, 17, 0, 1, 1)

        self.note_c___ = QCheckBox(self.groupBox_select_notes)
        self.note_c___.setObjectName(u"note_c___")

        self.gridLayout.addWidget(self.note_c___, 16, 4, 1, 1)

        self.note_cis = QCheckBox(self.groupBox_select_notes)
        self.note_cis.setObjectName(u"note_cis")

        self.gridLayout.addWidget(self.note_cis, 14, 0, 1, 1)

        self.note__fis = QCheckBox(self.groupBox_select_notes)
        self.note__fis.setObjectName(u"note__fis")

        self.gridLayout.addWidget(self.note__fis, 4, 0, 1, 1)

        self.note__ais = QCheckBox(self.groupBox_select_notes)
        self.note__ais.setObjectName(u"note__ais")

        self.gridLayout.addWidget(self.note__ais, 10, 0, 1, 1)

        self.note__as = QCheckBox(self.groupBox_select_notes)
        self.note__as.setObjectName(u"note__as")

        self.gridLayout.addWidget(self.note__as, 8, 0, 1, 1)

        self.note_d = QCheckBox(self.groupBox_select_notes)
        self.note_d.setObjectName(u"note_d")

        self.gridLayout.addWidget(self.note_d, 16, 0, 1, 1)

        self.note__gis = QCheckBox(self.groupBox_select_notes)
        self.note__gis.setObjectName(u"note__gis")

        self.gridLayout.addWidget(self.note__gis, 7, 0, 1, 1)

        self.note_ais_ = QCheckBox(self.groupBox_select_notes)
        self.note_ais_.setObjectName(u"note_ais_")

        self.gridLayout.addWidget(self.note_ais_, 12, 3, 1, 1)

        self.note_h_ = QCheckBox(self.groupBox_select_notes)
        self.note_h_.setObjectName(u"note_h_")

        self.gridLayout.addWidget(self.note_h_, 14, 3, 1, 1)

        self.note__h = QCheckBox(self.groupBox_select_notes)
        self.note__h.setObjectName(u"note__h")

        self.gridLayout.addWidget(self.note__h, 12, 0, 1, 1)

        self.note_b_ = QCheckBox(self.groupBox_select_notes)
        self.note_b_.setObjectName(u"note_b_")

        self.gridLayout.addWidget(self.note_b_, 13, 3, 1, 1)

        self.note__a = QCheckBox(self.groupBox_select_notes)
        self.note__a.setObjectName(u"note__a")

        self.gridLayout.addWidget(self.note__a, 9, 0, 1, 1)

        self.note_c__ = QCheckBox(self.groupBox_select_notes)
        self.note_c__.setObjectName(u"note_c__")

        self.gridLayout.addWidget(self.note_c__, 15, 3, 1, 1)

        self.note__e = QCheckBox(self.groupBox_select_notes)
        self.note__e.setObjectName(u"note__e")

        self.gridLayout.addWidget(self.note__e, 2, 0, 1, 1)

        self.note_gis__ = QCheckBox(self.groupBox_select_notes)
        self.note_gis__.setObjectName(u"note_gis__")

        self.gridLayout.addWidget(self.note_gis__, 10, 4, 1, 1)

        self.note_h__ = QCheckBox(self.groupBox_select_notes)
        self.note_h__.setObjectName(u"note_h__")

        self.gridLayout.addWidget(self.note_h__, 15, 4, 1, 1)

        self.note_as__ = QCheckBox(self.groupBox_select_notes)
        self.note_as__.setObjectName(u"note_as__")

        self.gridLayout.addWidget(self.note_as__, 11, 4, 1, 1)

        self.note_a__ = QCheckBox(self.groupBox_select_notes)
        self.note_a__.setObjectName(u"note_a__")

        self.gridLayout.addWidget(self.note_a__, 12, 4, 1, 1)

        self.note_ais__ = QCheckBox(self.groupBox_select_notes)
        self.note_ais__.setObjectName(u"note_ais__")

        self.gridLayout.addWidget(self.note_ais__, 13, 4, 1, 1)

        self.note__ges = QCheckBox(self.groupBox_select_notes)
        self.note__ges.setObjectName(u"note__ges")

        self.gridLayout.addWidget(self.note__ges, 5, 0, 1, 1)

        self.note__f = QCheckBox(self.groupBox_select_notes)
        self.note__f.setObjectName(u"note__f")

        self.gridLayout.addWidget(self.note__f, 3, 0, 1, 1)

        self.note__b = QCheckBox(self.groupBox_select_notes)
        self.note__b.setObjectName(u"note__b")

        self.gridLayout.addWidget(self.note__b, 11, 0, 1, 1)

        self.note_des = QCheckBox(self.groupBox_select_notes)
        self.note_des.setObjectName(u"note_des")

        self.gridLayout.addWidget(self.note_des, 15, 0, 1, 1)

        self.note_fis__ = QCheckBox(self.groupBox_select_notes)
        self.note_fis__.setObjectName(u"note_fis__")

        self.gridLayout.addWidget(self.note_fis__, 7, 4, 1, 1)

        self.note_f__ = QCheckBox(self.groupBox_select_notes)
        self.note_f__.setObjectName(u"note_f__")

        self.gridLayout.addWidget(self.note_f__, 6, 4, 1, 1)

        self.note_ges__ = QCheckBox(self.groupBox_select_notes)
        self.note_ges__.setObjectName(u"note_ges__")

        self.gridLayout.addWidget(self.note_ges__, 8, 4, 1, 1)

        self.note_es__ = QCheckBox(self.groupBox_select_notes)
        self.note_es__.setObjectName(u"note_es__")

        self.gridLayout.addWidget(self.note_es__, 4, 4, 1, 1)

        self.note_g__ = QCheckBox(self.groupBox_select_notes)
        self.note_g__.setObjectName(u"note_g__")

        self.gridLayout.addWidget(self.note_g__, 9, 4, 1, 1)

        self.note_e__ = QCheckBox(self.groupBox_select_notes)
        self.note_e__.setObjectName(u"note_e__")

        self.gridLayout.addWidget(self.note_e__, 5, 4, 1, 1)

        self.note_dis__ = QCheckBox(self.groupBox_select_notes)
        self.note_dis__.setObjectName(u"note_dis__")

        self.gridLayout.addWidget(self.note_dis__, 3, 4, 1, 1)

        self.note_d__ = QCheckBox(self.groupBox_select_notes)
        self.note_d__.setObjectName(u"note_d__")

        self.gridLayout.addWidget(self.note_d__, 2, 4, 1, 1)

        self.note_a_ = QCheckBox(self.groupBox_select_notes)
        self.note_a_.setObjectName(u"note_a_")

        self.gridLayout.addWidget(self.note_a_, 11, 3, 1, 1)

        self.note_cis__ = QCheckBox(self.groupBox_select_notes)
        self.note_cis__.setObjectName(u"note_cis__")

        self.gridLayout.addWidget(self.note_cis__, 16, 3, 1, 1)

        self.note_f = QCheckBox(self.groupBox_select_notes)
        self.note_f.setObjectName(u"note_f")

        self.gridLayout.addWidget(self.note_f, 4, 2, 1, 1)

        self.note_gis = QCheckBox(self.groupBox_select_notes)
        self.note_gis.setObjectName(u"note_gis")

        self.gridLayout.addWidget(self.note_gis, 8, 2, 1, 1)

        self.note_fis = QCheckBox(self.groupBox_select_notes)
        self.note_fis.setObjectName(u"note_fis")

        self.gridLayout.addWidget(self.note_fis, 5, 2, 1, 1)

        self.note_g = QCheckBox(self.groupBox_select_notes)
        self.note_g.setObjectName(u"note_g")

        self.gridLayout.addWidget(self.note_g, 7, 2, 1, 1)

        self.note_as = QCheckBox(self.groupBox_select_notes)
        self.note_as.setObjectName(u"note_as")

        self.gridLayout.addWidget(self.note_as, 9, 2, 1, 1)

        self.note_ges = QCheckBox(self.groupBox_select_notes)
        self.note_ges.setObjectName(u"note_ges")

        self.gridLayout.addWidget(self.note_ges, 6, 2, 1, 1)

        self.note_e = QCheckBox(self.groupBox_select_notes)
        self.note_e.setObjectName(u"note_e")

        self.gridLayout.addWidget(self.note_e, 3, 2, 1, 1)

        self.note_ais = QCheckBox(self.groupBox_select_notes)
        self.note_ais.setObjectName(u"note_ais")

        self.gridLayout.addWidget(self.note_ais, 11, 2, 1, 1)

        self.note_a = QCheckBox(self.groupBox_select_notes)
        self.note_a.setObjectName(u"note_a")

        self.gridLayout.addWidget(self.note_a, 10, 2, 1, 1)

        self.note_b = QCheckBox(self.groupBox_select_notes)
        self.note_b.setObjectName(u"note_b")

        self.gridLayout.addWidget(self.note_b, 12, 2, 1, 1)

        self.note_es = QCheckBox(self.groupBox_select_notes)
        self.note_es.setObjectName(u"note_es")

        self.gridLayout.addWidget(self.note_es, 2, 2, 1, 1)

        self.note_e_ = QCheckBox(self.groupBox_select_notes)
        self.note_e_.setObjectName(u"note_e_")

        self.gridLayout.addWidget(self.note_e_, 4, 3, 1, 1)

        self.note_des_ = QCheckBox(self.groupBox_select_notes)
        self.note_des_.setObjectName(u"note_des_")

        self.gridLayout.addWidget(self.note_des_, 16, 2, 1, 1)

        self.note_des__ = QCheckBox(self.groupBox_select_notes)
        self.note_des__.setObjectName(u"note_des__")

        self.gridLayout.addWidget(self.note_des__, 17, 3, 1, 1)

        self.note_f_ = QCheckBox(self.groupBox_select_notes)
        self.note_f_.setObjectName(u"note_f_")

        self.gridLayout.addWidget(self.note_f_, 5, 3, 1, 1)

        self.note_fis_ = QCheckBox(self.groupBox_select_notes)
        self.note_fis_.setObjectName(u"note_fis_")

        self.gridLayout.addWidget(self.note_fis_, 6, 3, 1, 1)

        self.note_c_ = QCheckBox(self.groupBox_select_notes)
        self.note_c_.setObjectName(u"note_c_")

        self.gridLayout.addWidget(self.note_c_, 14, 2, 1, 1)

        self.note_dis_ = QCheckBox(self.groupBox_select_notes)
        self.note_dis_.setObjectName(u"note_dis_")

        self.gridLayout.addWidget(self.note_dis_, 2, 3, 1, 1)

        self.note_cis_ = QCheckBox(self.groupBox_select_notes)
        self.note_cis_.setObjectName(u"note_cis_")

        self.gridLayout.addWidget(self.note_cis_, 15, 2, 1, 1)

        self.note_d_ = QCheckBox(self.groupBox_select_notes)
        self.note_d_.setObjectName(u"note_d_")

        self.gridLayout.addWidget(self.note_d_, 17, 2, 1, 1)

        self.note_h = QCheckBox(self.groupBox_select_notes)
        self.note_h.setObjectName(u"note_h")

        self.gridLayout.addWidget(self.note_h, 13, 2, 1, 1)

        self.note_es_ = QCheckBox(self.groupBox_select_notes)
        self.note_es_.setObjectName(u"note_es_")

        self.gridLayout.addWidget(self.note_es_, 3, 3, 1, 1)

        self.note_ges_ = QCheckBox(self.groupBox_select_notes)
        self.note_ges_.setObjectName(u"note_ges_")

        self.gridLayout.addWidget(self.note_ges_, 7, 3, 1, 1)

        self.note_as_ = QCheckBox(self.groupBox_select_notes)
        self.note_as_.setObjectName(u"note_as_")

        self.gridLayout.addWidget(self.note_as_, 10, 3, 1, 1)

        self.note_g_ = QCheckBox(self.groupBox_select_notes)
        self.note_g_.setObjectName(u"note_g_")

        self.gridLayout.addWidget(self.note_g_, 8, 3, 1, 1)

        self.note_gis_ = QCheckBox(self.groupBox_select_notes)
        self.note_gis_.setObjectName(u"note_gis_")

        self.gridLayout.addWidget(self.note_gis_, 9, 3, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_select_notes)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(250, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushButton_start_training = QPushButton(self.centralwidget)
        self.pushButton_start_training.setObjectName(u"pushButton_start_training")

        self.horizontalLayout_4.addWidget(self.pushButton_start_training)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 351, 21))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menuAbout_Qt = QMenu(self.menubar)
        self.menuAbout_Qt.setObjectName(u"menuAbout_Qt")
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.radioButton_timer, self.radioButton_manually)
        QWidget.setTabOrder(self.radioButton_manually, self.lineEdit_timer_seconds)
        QWidget.setTabOrder(self.lineEdit_timer_seconds, self.note__e)
        QWidget.setTabOrder(self.note__e, self.note__f)
        QWidget.setTabOrder(self.note__f, self.note__fis)
        QWidget.setTabOrder(self.note__fis, self.note__ges)
        QWidget.setTabOrder(self.note__ges, self.note__g)
        QWidget.setTabOrder(self.note__g, self.note__gis)
        QWidget.setTabOrder(self.note__gis, self.note__as)
        QWidget.setTabOrder(self.note__as, self.note__a)
        QWidget.setTabOrder(self.note__a, self.note__ais)
        QWidget.setTabOrder(self.note__ais, self.note__b)
        QWidget.setTabOrder(self.note__b, self.note__h)
        QWidget.setTabOrder(self.note__h, self.note_c)
        QWidget.setTabOrder(self.note_c, self.note_cis)
        QWidget.setTabOrder(self.note_cis, self.note_des)
        QWidget.setTabOrder(self.note_des, self.note_d)
        QWidget.setTabOrder(self.note_d, self.note_dis)
        QWidget.setTabOrder(self.note_dis, self.note_es)
        QWidget.setTabOrder(self.note_es, self.note_e)
        QWidget.setTabOrder(self.note_e, self.note_f)
        QWidget.setTabOrder(self.note_f, self.note_fis)
        QWidget.setTabOrder(self.note_fis, self.note_ges)
        QWidget.setTabOrder(self.note_ges, self.note_g)
        QWidget.setTabOrder(self.note_g, self.note_gis)
        QWidget.setTabOrder(self.note_gis, self.note_as)
        QWidget.setTabOrder(self.note_as, self.note_a)
        QWidget.setTabOrder(self.note_a, self.note_ais)
        QWidget.setTabOrder(self.note_ais, self.note_b)
        QWidget.setTabOrder(self.note_b, self.note_h)
        QWidget.setTabOrder(self.note_h, self.note_c_)
        QWidget.setTabOrder(self.note_c_, self.note_cis_)
        QWidget.setTabOrder(self.note_cis_, self.note_des_)
        QWidget.setTabOrder(self.note_des_, self.note_d_)
        QWidget.setTabOrder(self.note_d_, self.note_dis_)
        QWidget.setTabOrder(self.note_dis_, self.note_es_)
        QWidget.setTabOrder(self.note_es_, self.note_e_)
        QWidget.setTabOrder(self.note_e_, self.note_f_)
        QWidget.setTabOrder(self.note_f_, self.note_fis_)
        QWidget.setTabOrder(self.note_fis_, self.note_ges_)
        QWidget.setTabOrder(self.note_ges_, self.note_g_)
        QWidget.setTabOrder(self.note_g_, self.note_gis_)
        QWidget.setTabOrder(self.note_gis_, self.note_as_)
        QWidget.setTabOrder(self.note_as_, self.note_a_)
        QWidget.setTabOrder(self.note_a_, self.note_ais_)
        QWidget.setTabOrder(self.note_ais_, self.note_b_)
        QWidget.setTabOrder(self.note_b_, self.note_h_)
        QWidget.setTabOrder(self.note_h_, self.note_c__)
        QWidget.setTabOrder(self.note_c__, self.note_cis__)
        QWidget.setTabOrder(self.note_cis__, self.note_des__)
        QWidget.setTabOrder(self.note_des__, self.note_d__)
        QWidget.setTabOrder(self.note_d__, self.note_dis__)
        QWidget.setTabOrder(self.note_dis__, self.note_es__)
        QWidget.setTabOrder(self.note_es__, self.note_e__)
        QWidget.setTabOrder(self.note_e__, self.note_f__)
        QWidget.setTabOrder(self.note_f__, self.note_fis__)
        QWidget.setTabOrder(self.note_fis__, self.note_ges__)
        QWidget.setTabOrder(self.note_ges__, self.note_g__)
        QWidget.setTabOrder(self.note_g__, self.note_gis__)
        QWidget.setTabOrder(self.note_gis__, self.note_as__)
        QWidget.setTabOrder(self.note_as__, self.note_a__)
        QWidget.setTabOrder(self.note_a__, self.note_ais__)
        QWidget.setTabOrder(self.note_ais__, self.note_b__)
        QWidget.setTabOrder(self.note_b__, self.note_h__)
        QWidget.setTabOrder(self.note_h__, self.note_c___)
        QWidget.setTabOrder(self.note_c___, self.pushButton_start_training)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Guitar Music Notes", None))
        self.action_Close.setText(QCoreApplication.translate("MainWindow", u"&Close", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About &Qt", None))
        self.actionAbout_Guitar_Music_Notes.setText(QCoreApplication.translate("MainWindow", u"About &Guitar Music Notes", None))
        self.groupBox_next_note_settings.setTitle(QCoreApplication.translate("MainWindow", u"Next Note Selection", None))
        self.groupBox_next_note_raido_buttons.setTitle("")
        self.radioButton_timer.setText(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.radioButton_manually.setText(QCoreApplication.translate("MainWindow", u"Next Note manually", None))
        self.groupBox_timer_settings.setTitle("")
        self.lineEdit_timer_seconds.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_timer_seconds.setText(QCoreApplication.translate("MainWindow", u"seconds", None))
        self.checkBox_follow_with_solution.setText(QCoreApplication.translate("MainWindow", u"Show Solution", None))
        self.label_selection_hint.setText(QCoreApplication.translate("MainWindow", u"Note: If no note is selected, all notes will be trained!", None))
        self.groupBox_select_notes.setTitle(QCoreApplication.translate("MainWindow", u"Select Notes", None))
        self.note_c.setText(QCoreApplication.translate("MainWindow", u"c", None))
        self.note__g.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.note_b__.setText(QCoreApplication.translate("MainWindow", u"b ' '", None))
        self.note_dis.setText(QCoreApplication.translate("MainWindow", u"# d", None))
        self.note_c___.setText(QCoreApplication.translate("MainWindow", u"c ' ' '", None))
        self.note_cis.setText(QCoreApplication.translate("MainWindow", u"# c", None))
        self.note__fis.setText(QCoreApplication.translate("MainWindow", u"# F", None))
        self.note__ais.setText(QCoreApplication.translate("MainWindow", u"# A", None))
        self.note__as.setText(QCoreApplication.translate("MainWindow", u"\u266dA", None))
        self.note_d.setText(QCoreApplication.translate("MainWindow", u"d", None))
        self.note__gis.setText(QCoreApplication.translate("MainWindow", u"# G", None))
        self.note_ais_.setText(QCoreApplication.translate("MainWindow", u"# a '", None))
        self.note_h_.setText(QCoreApplication.translate("MainWindow", u"h '", None))
        self.note__h.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.note_b_.setText(QCoreApplication.translate("MainWindow", u"b '", None))
        self.note__a.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.note_c__.setText(QCoreApplication.translate("MainWindow", u"c ' '", None))
        self.note__e.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.note_gis__.setText(QCoreApplication.translate("MainWindow", u"# g ' '", None))
        self.note_h__.setText(QCoreApplication.translate("MainWindow", u"h ' '", None))
        self.note_as__.setText(QCoreApplication.translate("MainWindow", u"\u266da ' '", None))
        self.note_a__.setText(QCoreApplication.translate("MainWindow", u"a ' '", None))
        self.note_ais__.setText(QCoreApplication.translate("MainWindow", u"# a ' '", None))
        self.note__ges.setText(QCoreApplication.translate("MainWindow", u"\u266dG", None))
        self.note__f.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.note__b.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.note_des.setText(QCoreApplication.translate("MainWindow", u"\u266dd", None))
        self.note_fis__.setText(QCoreApplication.translate("MainWindow", u"# f ' '", None))
        self.note_f__.setText(QCoreApplication.translate("MainWindow", u"f ' '", None))
        self.note_ges__.setText(QCoreApplication.translate("MainWindow", u"\u266dg ' '", None))
        self.note_es__.setText(QCoreApplication.translate("MainWindow", u"\u266de ' '", None))
        self.note_g__.setText(QCoreApplication.translate("MainWindow", u"g ' '", None))
        self.note_e__.setText(QCoreApplication.translate("MainWindow", u"e ' '", None))
        self.note_dis__.setText(QCoreApplication.translate("MainWindow", u"# d ' '", None))
        self.note_d__.setText(QCoreApplication.translate("MainWindow", u"d ' '", None))
        self.note_a_.setText(QCoreApplication.translate("MainWindow", u"a '", None))
        self.note_cis__.setText(QCoreApplication.translate("MainWindow", u"# c ' '", None))
        self.note_f.setText(QCoreApplication.translate("MainWindow", u"f", None))
        self.note_gis.setText(QCoreApplication.translate("MainWindow", u"# g", None))
        self.note_fis.setText(QCoreApplication.translate("MainWindow", u"# f", None))
        self.note_g.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.note_as.setText(QCoreApplication.translate("MainWindow", u"\u266da", None))
        self.note_ges.setText(QCoreApplication.translate("MainWindow", u"\u266dg", None))
        self.note_e.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.note_ais.setText(QCoreApplication.translate("MainWindow", u"# a", None))
        self.note_a.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.note_b.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.note_es.setText(QCoreApplication.translate("MainWindow", u"\u266de", None))
        self.note_e_.setText(QCoreApplication.translate("MainWindow", u"e '", None))
        self.note_des_.setText(QCoreApplication.translate("MainWindow", u"\u266dd '", None))
        self.note_des__.setText(QCoreApplication.translate("MainWindow", u"\u266dd ' '", None))
        self.note_f_.setText(QCoreApplication.translate("MainWindow", u"f '", None))
        self.note_fis_.setText(QCoreApplication.translate("MainWindow", u"# f '", None))
        self.note_c_.setText(QCoreApplication.translate("MainWindow", u"c '", None))
        self.note_dis_.setText(QCoreApplication.translate("MainWindow", u"# d '", None))
        self.note_cis_.setText(QCoreApplication.translate("MainWindow", u"# c '", None))
        self.note_d_.setText(QCoreApplication.translate("MainWindow", u"d '", None))
        self.note_h.setText(QCoreApplication.translate("MainWindow", u"h", None))
        self.note_es_.setText(QCoreApplication.translate("MainWindow", u"\u266de '", None))
        self.note_ges_.setText(QCoreApplication.translate("MainWindow", u"\u266dg '", None))
        self.note_as_.setText(QCoreApplication.translate("MainWindow", u"\u266da '", None))
        self.note_g_.setText(QCoreApplication.translate("MainWindow", u"g '", None))
        self.note_gis_.setText(QCoreApplication.translate("MainWindow", u"# g '", None))
        self.pushButton_start_training.setText(QCoreApplication.translate("MainWindow", u"Start Training", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuAbout_Qt.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
    # retranslateUi

