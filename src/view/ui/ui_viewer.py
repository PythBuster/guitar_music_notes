# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewer.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)


class Ui_Viewer(object):
    def setupUi(self, Viewer):
        if not Viewer.objectName():
            Viewer.setObjectName("Viewer")
        Viewer.resize(538, 486)
        Viewer.setStyleSheet("background-color: white;")
        self.verticalLayout = QVBoxLayout(Viewer)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_image = QLabel(Viewer)
        self.label_image.setObjectName("label_image")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_image)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_next = QPushButton(Viewer)
        self.pushButton_next.setObjectName("pushButton_next")

        self.horizontalLayout.addWidget(self.pushButton_next)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Viewer)

        QMetaObject.connectSlotsByName(Viewer)

    # setupUi

    def retranslateUi(self, Viewer):
        Viewer.setWindowTitle(QCoreApplication.translate("Viewer", "Training", None))
        self.label_image.setText("")
        self.pushButton_next.setText(QCoreApplication.translate("Viewer", "Next", None))

    # retranslateUi
