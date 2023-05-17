import sgtk
from sgtk.platform.qt import QtCore, QtGui
from .ui.allowance_token_form import Ui_TokenForm


class AuthCodeFormWidget(QtGui.QWidget):
    auth_code_entered = QtCore.Signal(QtGui.QWidget)

    def __init__(self, setup_proc=None, parent=None):
        """
        Constructor

        :param parent: QT parent object
        """
        QtGui.QWidget.__init__(self, parent)

        # set up the UI
        self.ui = Ui_TokenForm()
        self.ui.setupUi(self)

        # hook up the UI:
        self.ui.ok_btn.clicked.connect(self._on_ok)
        self.ui.cancel_btn.clicked.connect(self._on_cancel)

        if setup_proc:
            setup_proc(self)

    def auth_code(self):
        return str(self.ui.token_edit.text())

    def _on_ok(self):
        self._exit_code = QtGui.QDialog.Accepted
        self.auth_code_entered.emit(self)
        self._exit_code = QtGui.QDialog.Rejected
        self.close()

    def _on_cancel(self):
        """
        Called when the cancel button is clicked
        """
        self._exit_code = QtGui.QDialog.Rejected
        self.close()
