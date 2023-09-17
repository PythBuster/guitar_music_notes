# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewer.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Viewer(object):
    def setupUi(self, Viewer):
        if not Viewer.objectName():
            Viewer.setObjectName(u"Viewer")
        Viewer.resize(428, 447)
        Viewer.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Viewer)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.solution_frame = QFrame(Viewer)
        self.solution_frame.setObjectName(u"solution_frame")
        self.solution_frame.setStyleSheet(u"")
        self.solution_frame.setFrameShape(QFrame.NoFrame)
        self.solution_frame.setFrameShadow(QFrame.Plain)
        self.solution_frame.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.solution_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.label_solution = QLabel(self.solution_frame)
        self.label_solution.setObjectName(u"label_solution")
        font = QFont()
        font.setPointSize(24)
        self.label_solution.setFont(font)

        self.verticalLayout_4.addWidget(self.label_solution)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_note = QLabel(self.solution_frame)
        self.label_note.setObjectName(u"label_note")
        font1 = QFont()
        font1.setPointSize(34)
        self.label_note.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_note)

        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.solution_frame)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.label_image = QLabel(Viewer)
        self.label_image.setObjectName(u"label_image")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_image)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_next = QPushButton(Viewer)
        self.pushButton_next.setObjectName(u"pushButton_next")

        self.horizontalLayout.addWidget(self.pushButton_next)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Viewer)

        QMetaObject.connectSlotsByName(Viewer)
    # setupUi

    def retranslateUi(self, Viewer):
        Viewer.setWindowTitle(QCoreApplication.translate("Viewer", u"Training", None))
        self.label_solution.setText(QCoreApplication.translate("Viewer", u"Solution:", None))
        self.label_note.setText(QCoreApplication.translate("Viewer", u"Note", None))
        self.label_image.setText("")
        self.pushButton_next.setText(QCoreApplication.translate("Viewer", u"Next", None))
    # retranslateUi

