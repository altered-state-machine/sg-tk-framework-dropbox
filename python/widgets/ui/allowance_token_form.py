# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'allowance_token_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from tank.platform.qt import QtCore, QtGui


class Ui_TokenForm(object):
    def setupUi(self, TokenForm):
        if not TokenForm.objectName():
            TokenForm.setObjectName(u"TokenForm")
        TokenForm.resize(345, 131)
        self.verticalLayout = QtGui.QVBoxLayout(TokenForm)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, -1)
        self.details_label = QtGui.QLabel(TokenForm)
        self.details_label.setObjectName(u"details_label")
        self.details_label.setMinimumSize(QtCore.QSize(0, 32))
        self.details_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.details_label)

        self.token_edit = QtGui.QLineEdit(TokenForm)
        self.token_edit.setObjectName(u"token_edit")
        self.token_edit.setMinimumSize(QtCore.QSize(0, 22))
        self.token_edit.setEchoMode(QtGui.QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.token_edit)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.break_line = QtGui.QFrame(TokenForm)
        self.break_line.setObjectName(u"break_line")
        self.break_line.setFrameShape(QtGui.QFrame.HLine)
        self.break_line.setFrameShadow(QtGui.QFrame.Sunken)

        self.verticalLayout.addWidget(self.break_line)

        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, 8, 12, 12)
        self.horizontalSpacer = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.cancel_btn = QtGui.QPushButton(TokenForm)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QtCore.QSize(90, 0))

        self.horizontalLayout_3.addWidget(self.cancel_btn)

        self.ok_btn = QtGui.QPushButton(TokenForm)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setMinimumSize(QtCore.QSize(90, 0))

        self.horizontalLayout_3.addWidget(self.ok_btn)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(TokenForm)

        self.ok_btn.setDefault(True)

        QtCore.QMetaObject.connectSlotsByName(TokenForm)

    # setupUi

    def retranslateUi(self, TokenForm):
        TokenForm.setWindowTitle(QtCore.QCoreApplication.translate("TokenForm", u"Form", None))
        self.details_label.setText(QtCore.QCoreApplication.translate("TokenForm",
                                                              u"<html><head/><body><p>Enter token obtained from the Dropbox Authentication page.</p></body></html>",
                                                              None))
        self.cancel_btn.setText(QtCore.QCoreApplication.translate("TokenForm", u"Cancel", None))
        self.ok_btn.setText(QtCore.QCoreApplication.translate("TokenForm", u"OK", None))
    # retranslateUi
