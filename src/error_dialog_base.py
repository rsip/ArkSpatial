# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/error_dialog_base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_ErrorDialog(object):
    def setupUi(self, ErrorDialog):
        ErrorDialog.setObjectName(_fromUtf8("ErrorDialog"))
        ErrorDialog.resize(728, 391)
        self.verticalLayout = QtGui.QVBoxLayout(ErrorDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(ErrorDialog)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.errorTable = QtGui.QTableView(ErrorDialog)
        self.errorTable.setObjectName(_fromUtf8("errorTable"))
        self.verticalLayout.addWidget(self.errorTable)
        self.buttonBox = QtGui.QDialogButtonBox(ErrorDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ErrorDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ErrorDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ErrorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ErrorDialog)

    def retranslateUi(self, ErrorDialog):
        ErrorDialog.setWindowTitle(_translate("ErrorDialog", "Validation Errors", None))
        self.label.setText(_translate("ErrorDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Validation Errors:</span></p><p>The following errors were found in the requested data merge. Please correct these errors and try again.<br/></p></body></html>", None))

