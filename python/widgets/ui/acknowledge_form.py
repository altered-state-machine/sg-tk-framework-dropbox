# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acknowledge_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from tank.platform.qt import QtCore, QtGui


class Ui_AcknowledgeForm(object):
    def setupUi(self, TrustForm):
        if not TrustForm.objectName():
            TrustForm.setObjectName(u"TrustForm")
        TrustForm.resize(500, 178)
        self.verticalLayout_3 = QtGui.QVBoxLayout(TrustForm)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, 12, 12, 8)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.warning_label = QtGui.QLabel(TrustForm)
        self.warning_label.setObjectName(u"warning_label")
        self.warning_label.setMinimumSize(QtCore.QSize(0, 0))
        self.warning_label.setMaximumSize(QtCore.QSize(64, 64))

        self.verticalLayout_2.addWidget(self.warning_label)

        self.verticalSpacer = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.msg_label = QtGui.QLabel(TrustForm)
        self.msg_label.setObjectName(u"msg_label")
        self.msg_label.setWordWrap(True)
        self.msg_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.msg_label)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.break_line = QtGui.QFrame(TrustForm)
        self.break_line.setObjectName(u"break_line")
        self.break_line.setFrameShape(QtGui.QFrame.HLine)
        self.break_line.setFrameShadow(QtGui.QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.break_line)

        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, 8, 12, 12)
        self.horizontalSpacer = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.cancel_btn = QtGui.QPushButton(TrustForm)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QtCore.QSize(90, 0))

        self.horizontalLayout_3.addWidget(self.cancel_btn)

        self.ok_btn = QtGui.QPushButton(TrustForm)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setMinimumSize(QtCore.QSize(90, 0))

        self.horizontalLayout_3.addWidget(self.ok_btn)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3.setStretch(1, 1)

        self.retranslateUi(TrustForm)

        self.ok_btn.setDefault(True)

        QtCore.QMetaObject.connectSlotsByName(TrustForm)

    # setupUi

    def retranslateUi(self, TrustForm):
        TrustForm.setWindowTitle(QtCore.QCoreApplication.translate("TrustForm", u"Form", None))
        self.warning_label.setText("")
        self.msg_label.setText(QtCore.QCoreApplication.translate("TrustForm",
                                                                 u"<html><head/><body><p><span style=\" font-weight:600;\">A New Token is required to publish files to cloud storage.</span></p><p>Previously issued access token has expiered or this is the first time request.</p><p>This application requires access to Dropbox on behalf of the <span style=\" font-weight:600;\">&lt;user.name&gt;</span></p><p>When you continue, a new Web Browser window will be open with instructions.</p></body></html>",
                                                                 None))
        self.cancel_btn.setText(QtCore.QCoreApplication.translate("TrustForm", u"Cancel", None))
        self.ok_btn.setText(QtCore.QCoreApplication.translate("TrustForm", u"Continue", None))
    # retranslateUi
