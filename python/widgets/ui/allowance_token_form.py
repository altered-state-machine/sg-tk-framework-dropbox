# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'allowance_token_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from  . import resources_rc

class Ui_PasswordForm(object):
    def setupUi(self, PasswordForm):
        if not PasswordForm.objectName():
            PasswordForm.setObjectName(u"PasswordForm")
        PasswordForm.resize(345, 131)
        self.verticalLayout = QVBoxLayout(PasswordForm)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, -1)
        self.details_label = QLabel(PasswordForm)
        self.details_label.setObjectName(u"details_label")
        self.details_label.setMinimumSize(QSize(0, 32))
        self.details_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.details_label)

        self.password_edit = QLineEdit(PasswordForm)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setMinimumSize(QSize(0, 22))
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.password_edit)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.break_line = QFrame(PasswordForm)
        self.break_line.setObjectName(u"break_line")
        self.break_line.setFrameShape(QFrame.HLine)
        self.break_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.break_line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, 8, 12, 12)
        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.cancel_btn = QPushButton(PasswordForm)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_3.addWidget(self.cancel_btn)

        self.ok_btn = QPushButton(PasswordForm)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_3.addWidget(self.ok_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(PasswordForm)

        self.ok_btn.setDefault(True)


        QMetaObject.connectSlotsByName(PasswordForm)
    # setupUi

    def retranslateUi(self, PasswordForm):
        PasswordForm.setWindowTitle(QCoreApplication.translate("PasswordForm", u"Form", None))
        self.details_label.setText(QCoreApplication.translate("PasswordForm", u"<html><head/><body><p>Enter token obtained from the Dropbox Authentication page.</p></body></html>", None))
        self.cancel_btn.setText(QCoreApplication.translate("PasswordForm", u"Cancel", None))
        self.ok_btn.setText(QCoreApplication.translate("PasswordForm", u"OK", None))
    # retranslateUi

