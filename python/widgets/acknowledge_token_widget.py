import sgtk
from sgtk.platform.qt import QtCore, QtGui
from .ui.acknowledge_form import Ui_AcknowledgeForm


class AcknowledgeFormWidget(QtGui.QWidget):

    ack_accepted = QtCore.Signal(QtGui.QWidget)

    def __init__(self, setup_proc=None, parent=None):
        """
        Constructor

        :param parent: QT parent object
        """
        QtGui.QWidget.__init__(self, parent)

        # set up the UI
        self.ui = Ui_AcknowledgeForm()
        self.ui.setupUi(self)

        # hook up the UI:
        self.ui.ok_btn.clicked.connect(self._on_ok)
        self.ui.cancel_btn.clicked.connect(self._on_cancel)

        if setup_proc:
            setup_proc(self)

    def _on_ok(self):
        self._exit_code = QtGui.QDialog.Accepted
        self.ack_accepted.emit(self)
        self._exit_code = QtGui.QDialog.Rejected
        self.close()

    def _on_cancel(self):
        """
        Called when the cancel button is clicked
        """
        self._exit_code = QtGui.QDialog.Rejected
        self.close()
