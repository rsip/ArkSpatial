# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/data_widget_base.ui'
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

class Ui_DataWidget(object):
    def setupUi(self, DataWidget):
        DataWidget.setObjectName(_fromUtf8("DataWidget"))
        DataWidget.resize(278, 332)
        self.gridLayout = QtGui.QGridLayout(DataWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.processEdit = QtGui.QLineEdit(DataWidget)
        self.processEdit.setFrame(True)
        self.processEdit.setReadOnly(True)
        self.processEdit.setObjectName(_fromUtf8("processEdit"))
        self.gridLayout.addWidget(self.processEdit, 6, 2, 1, 3)
        self.siteCodeCombo = QtGui.QComboBox(DataWidget)
        self.siteCodeCombo.setObjectName(_fromUtf8("siteCodeCombo"))
        self.gridLayout.addWidget(self.siteCodeCombo, 0, 2, 1, 3)
        self.subgroupDescriptionEdit = QtGui.QLineEdit(DataWidget)
        self.subgroupDescriptionEdit.setReadOnly(True)
        self.subgroupDescriptionEdit.setObjectName(_fromUtf8("subgroupDescriptionEdit"))
        self.gridLayout.addWidget(self.subgroupDescriptionEdit, 8, 0, 1, 5)
        self.itemRegisterDescriptionEdit = QtGui.QLineEdit(DataWidget)
        self.itemRegisterDescriptionEdit.setReadOnly(True)
        self.itemRegisterDescriptionEdit.setObjectName(_fromUtf8("itemRegisterDescriptionEdit"))
        self.gridLayout.addWidget(self.itemRegisterDescriptionEdit, 3, 0, 1, 5)
        self.itemLabel = QtGui.QLabel(DataWidget)
        self.itemLabel.setObjectName(_fromUtf8("itemLabel"))
        self.gridLayout.addWidget(self.itemLabel, 1, 0, 1, 2)
        self.itemTypeEdit = QtGui.QLineEdit(DataWidget)
        self.itemTypeEdit.setFrame(True)
        self.itemTypeEdit.setReadOnly(True)
        self.itemTypeEdit.setObjectName(_fromUtf8("itemTypeEdit"))
        self.gridLayout.addWidget(self.itemTypeEdit, 2, 2, 1, 3)
        self.itemDescriptionEdit = QtGui.QLineEdit(DataWidget)
        self.itemDescriptionEdit.setReadOnly(True)
        self.itemDescriptionEdit.setObjectName(_fromUtf8("itemDescriptionEdit"))
        self.gridLayout.addWidget(self.itemDescriptionEdit, 4, 0, 1, 5)
        self.siteCodeLabel = QtGui.QLabel(DataWidget)
        self.siteCodeLabel.setObjectName(_fromUtf8("siteCodeLabel"))
        self.gridLayout.addWidget(self.siteCodeLabel, 0, 0, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.classCodeCombo = QtGui.QComboBox(DataWidget)
        self.classCodeCombo.setObjectName(_fromUtf8("classCodeCombo"))
        self.horizontalLayout_3.addWidget(self.classCodeCombo)
        self.itemIdSpin = QtGui.QSpinBox(DataWidget)
        self.itemIdSpin.setMaximum(99999)
        self.itemIdSpin.setObjectName(_fromUtf8("itemIdSpin"))
        self.horizontalLayout_3.addWidget(self.itemIdSpin)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 2, 1, 3)
        self.itemTypeLabel = QtGui.QLabel(DataWidget)
        self.itemTypeLabel.setObjectName(_fromUtf8("itemTypeLabel"))
        self.gridLayout.addWidget(self.itemTypeLabel, 2, 0, 1, 2)
        self.processLabel = QtGui.QLabel(DataWidget)
        self.processLabel.setObjectName(_fromUtf8("processLabel"))
        self.gridLayout.addWidget(self.processLabel, 6, 0, 1, 2)
        self.interpreationLabel = QtGui.QLabel(DataWidget)
        self.interpreationLabel.setObjectName(_fromUtf8("interpreationLabel"))
        self.gridLayout.addWidget(self.interpreationLabel, 5, 0, 1, 2)
        self.subgroupLabel = QtGui.QLabel(DataWidget)
        self.subgroupLabel.setObjectName(_fromUtf8("subgroupLabel"))
        self.gridLayout.addWidget(self.subgroupLabel, 7, 0, 1, 2)
        self.interpretationEdit = QtGui.QLineEdit(DataWidget)
        self.interpretationEdit.setFrame(True)
        self.interpretationEdit.setReadOnly(True)
        self.interpretationEdit.setObjectName(_fromUtf8("interpretationEdit"))
        self.gridLayout.addWidget(self.interpretationEdit, 5, 2, 1, 3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.subgroupSpin = QtGui.QSpinBox(DataWidget)
        self.subgroupSpin.setFrame(True)
        self.subgroupSpin.setReadOnly(True)
        self.subgroupSpin.setMaximum(99999)
        self.subgroupSpin.setObjectName(_fromUtf8("subgroupSpin"))
        self.horizontalLayout.addWidget(self.subgroupSpin)
        self.openSubgroupTool = QtGui.QToolButton(DataWidget)
        self.openSubgroupTool.setEnabled(False)
        self.openSubgroupTool.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/ark/data/openData.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openSubgroupTool.setIcon(icon)
        self.openSubgroupTool.setObjectName(_fromUtf8("openSubgroupTool"))
        self.horizontalLayout.addWidget(self.openSubgroupTool)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 2, 1, 3)
        spacerItem = QtGui.QSpacerItem(20, 243, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 9, 0, 1, 1)
        self.itemLabel.setBuddy(self.classCodeCombo)

        self.retranslateUi(DataWidget)
        QtCore.QMetaObject.connectSlotsByName(DataWidget)

    def retranslateUi(self, DataWidget):
        DataWidget.setWindowTitle(_translate("DataWidget", "Form", None))
        self.itemLabel.setText(_translate("DataWidget", "Item ID:", None))
        self.siteCodeLabel.setText(_translate("DataWidget", "Site Code:", None))
        self.itemIdSpin.setToolTip(_translate("DataWidget", "Source ID", None))
        self.itemTypeLabel.setText(_translate("DataWidget", "Type:", None))
        self.processLabel.setText(_translate("DataWidget", "Process:", None))
        self.interpreationLabel.setText(_translate("DataWidget", "Interpretation:", None))
        self.subgroupLabel.setText(_translate("DataWidget", "Sub-Group:", None))
        self.subgroupSpin.setToolTip(_translate("DataWidget", "Source ID", None))

import resources_rc
