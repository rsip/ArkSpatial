# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plan/plan_dock_base.ui'
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

class Ui_PlanDockWidget(object):
    def setupUi(self, PlanDockWidget):
        PlanDockWidget.setObjectName(_fromUtf8("PlanDockWidget"))
        PlanDockWidget.resize(352, 743)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PlanDockWidget.sizePolicy().hasHeightForWidth())
        PlanDockWidget.setSizePolicy(sizePolicy)
        self.PlanDockContents = QtGui.QWidget()
        self.PlanDockContents.setObjectName(_fromUtf8("PlanDockContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.PlanDockContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.PlanDockContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 328, 651))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.m_metadataGroup = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.m_metadataGroup.setObjectName(_fromUtf8("m_metadataGroup"))
        self.gridLayout = QtGui.QGridLayout(self.m_metadataGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.m_sourceCodeCombo = QtGui.QComboBox(self.m_metadataGroup)
        self.m_sourceCodeCombo.setObjectName(_fromUtf8("m_sourceCodeCombo"))
        self.gridLayout.addWidget(self.m_sourceCodeCombo, 1, 1, 1, 1)
        self.m_sourceIdLabel = QtGui.QLabel(self.m_metadataGroup)
        self.m_sourceIdLabel.setObjectName(_fromUtf8("m_sourceIdLabel"))
        self.gridLayout.addWidget(self.m_sourceIdLabel, 2, 0, 1, 1)
        self.m_siteLabel = QtGui.QLabel(self.m_metadataGroup)
        self.m_siteLabel.setObjectName(_fromUtf8("m_siteLabel"))
        self.gridLayout.addWidget(self.m_siteLabel, 0, 0, 1, 1)
        self.m_siteEdit = QtGui.QLineEdit(self.m_metadataGroup)
        self.m_siteEdit.setReadOnly(False)
        self.m_siteEdit.setObjectName(_fromUtf8("m_siteEdit"))
        self.gridLayout.addWidget(self.m_siteEdit, 0, 1, 1, 1)
        self.m_sourceCodeLabel = QtGui.QLabel(self.m_metadataGroup)
        self.m_sourceCodeLabel.setObjectName(_fromUtf8("m_sourceCodeLabel"))
        self.gridLayout.addWidget(self.m_sourceCodeLabel, 1, 0, 1, 1)
        self.m_sourceFileLabel = QtGui.QLabel(self.m_metadataGroup)
        self.m_sourceFileLabel.setObjectName(_fromUtf8("m_sourceFileLabel"))
        self.gridLayout.addWidget(self.m_sourceFileLabel, 3, 0, 1, 1)
        self.m_sourceFileEdit = QtGui.QLineEdit(self.m_metadataGroup)
        self.m_sourceFileEdit.setObjectName(_fromUtf8("m_sourceFileEdit"))
        self.gridLayout.addWidget(self.m_sourceFileEdit, 3, 1, 1, 1)
        self.m_commentLabel = QtGui.QLabel(self.m_metadataGroup)
        self.m_commentLabel.setObjectName(_fromUtf8("m_commentLabel"))
        self.gridLayout.addWidget(self.m_commentLabel, 4, 0, 1, 1)
        self.m_commentEdit = QtGui.QLineEdit(self.m_metadataGroup)
        self.m_commentEdit.setReadOnly(False)
        self.m_commentEdit.setObjectName(_fromUtf8("m_commentEdit"))
        self.gridLayout.addWidget(self.m_commentEdit, 4, 1, 1, 1)
        self.m_createdByLabel = QtGui.QLabel(self.m_metadataGroup)
        self.m_createdByLabel.setObjectName(_fromUtf8("m_createdByLabel"))
        self.gridLayout.addWidget(self.m_createdByLabel, 5, 0, 1, 1)
        self.m_createdByEdit = QtGui.QLineEdit(self.m_metadataGroup)
        self.m_createdByEdit.setObjectName(_fromUtf8("m_createdByEdit"))
        self.gridLayout.addWidget(self.m_createdByEdit, 5, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.m_sourceClassCombo = QtGui.QComboBox(self.m_metadataGroup)
        self.m_sourceClassCombo.setObjectName(_fromUtf8("m_sourceClassCombo"))
        self.horizontalLayout_2.addWidget(self.m_sourceClassCombo)
        self.m_sourceIdSpin = QtGui.QSpinBox(self.m_metadataGroup)
        self.m_sourceIdSpin.setMaximum(99999)
        self.m_sourceIdSpin.setObjectName(_fromUtf8("m_sourceIdSpin"))
        self.horizontalLayout_2.addWidget(self.m_sourceIdSpin)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.m_metadataGroup)
        self.m_contextDataGroup = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.m_contextDataGroup.setObjectName(_fromUtf8("m_contextDataGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.m_contextDataGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.m_loadContextButton = QtGui.QPushButton(self.m_contextDataGroup)
        self.m_loadContextButton.setObjectName(_fromUtf8("m_loadContextButton"))
        self.gridLayout_2.addWidget(self.m_loadContextButton, 0, 2, 1, 1)
        self.m_loadRawButton = QtGui.QPushButton(self.m_contextDataGroup)
        self.m_loadRawButton.setObjectName(_fromUtf8("m_loadRawButton"))
        self.gridLayout_2.addWidget(self.m_loadRawButton, 0, 0, 1, 1)
        self.m_contextNumberSpin = QtGui.QSpinBox(self.m_contextDataGroup)
        self.m_contextNumberSpin.setMaximum(9999)
        self.m_contextNumberSpin.setObjectName(_fromUtf8("m_contextNumberSpin"))
        self.gridLayout_2.addWidget(self.m_contextNumberSpin, 2, 1, 1, 1)
        self.m_loadGeoButton = QtGui.QPushButton(self.m_contextDataGroup)
        self.m_loadGeoButton.setObjectName(_fromUtf8("m_loadGeoButton"))
        self.gridLayout_2.addWidget(self.m_loadGeoButton, 0, 1, 1, 1)
        self.m_contextNumberLabel = QtGui.QLabel(self.m_contextDataGroup)
        self.m_contextNumberLabel.setObjectName(_fromUtf8("m_contextNumberLabel"))
        self.gridLayout_2.addWidget(self.m_contextNumberLabel, 2, 0, 1, 1)
        self.m_contextToolsLayout = QtGui.QGridLayout()
        self.m_contextToolsLayout.setObjectName(_fromUtf8("m_contextToolsLayout"))
        self.gridLayout_2.addLayout(self.m_contextToolsLayout, 3, 0, 1, 3)
        self.verticalLayout.addWidget(self.m_contextDataGroup)
        self.m_featureDataGroup = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.m_featureDataGroup.setObjectName(_fromUtf8("m_featureDataGroup"))
        self.gridLayout_6 = QtGui.QGridLayout(self.m_featureDataGroup)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.m_featureNameEdit = QtGui.QLineEdit(self.m_featureDataGroup)
        self.m_featureNameEdit.setObjectName(_fromUtf8("m_featureNameEdit"))
        self.gridLayout_6.addWidget(self.m_featureNameEdit, 3, 1, 1, 1)
        self.m_featureToolsLayout = QtGui.QGridLayout()
        self.m_featureToolsLayout.setObjectName(_fromUtf8("m_featureToolsLayout"))
        self.gridLayout_6.addLayout(self.m_featureToolsLayout, 4, 0, 1, 2)
        self.m_featureNameLabel = QtGui.QLabel(self.m_featureDataGroup)
        self.m_featureNameLabel.setObjectName(_fromUtf8("m_featureNameLabel"))
        self.gridLayout_6.addWidget(self.m_featureNameLabel, 3, 0, 1, 1)
        self.m_featureIdLabel = QtGui.QLabel(self.m_featureDataGroup)
        self.m_featureIdLabel.setObjectName(_fromUtf8("m_featureIdLabel"))
        self.gridLayout_6.addWidget(self.m_featureIdLabel, 0, 0, 1, 1)
        self.m_featureIdSpin = QtGui.QSpinBox(self.m_featureDataGroup)
        self.m_featureIdSpin.setObjectName(_fromUtf8("m_featureIdSpin"))
        self.gridLayout_6.addWidget(self.m_featureIdSpin, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.m_featureDataGroup)
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.m_snapPolygonsBufferTool = SnappingToolButton(self.groupBox)
        self.m_snapPolygonsBufferTool.setCheckable(True)
        self.m_snapPolygonsBufferTool.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.m_snapPolygonsBufferTool.setObjectName(_fromUtf8("m_snapPolygonsBufferTool"))
        self.gridLayout_3.addWidget(self.m_snapPolygonsBufferTool, 1, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.m_snapPolygonsLayerTool = SnappingToolButton(self.groupBox)
        self.m_snapPolygonsLayerTool.setCheckable(True)
        self.m_snapPolygonsLayerTool.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.m_snapPolygonsLayerTool.setObjectName(_fromUtf8("m_snapPolygonsLayerTool"))
        self.gridLayout_3.addWidget(self.m_snapPolygonsLayerTool, 2, 2, 1, 1)
        self.m_snapLinesLayerTool = SnappingToolButton(self.groupBox)
        self.m_snapLinesLayerTool.setCheckable(True)
        self.m_snapLinesLayerTool.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.m_snapLinesLayerTool.setObjectName(_fromUtf8("m_snapLinesLayerTool"))
        self.gridLayout_3.addWidget(self.m_snapLinesLayerTool, 2, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 0, 1, 1, 1)
        self.m_snapLinesBufferTool = SnappingToolButton(self.groupBox)
        self.m_snapLinesBufferTool.setCheckable(True)
        self.m_snapLinesBufferTool.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.m_snapLinesBufferTool.setObjectName(_fromUtf8("m_snapLinesBufferTool"))
        self.gridLayout_3.addWidget(self.m_snapLinesBufferTool, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.m_topologicalLabel = QtGui.QLabel(self.groupBox)
        self.m_topologicalLabel.setObjectName(_fromUtf8("m_topologicalLabel"))
        self.horizontalLayout_3.addWidget(self.m_topologicalLabel)
        self.m_topologicalTool = TopoEditToolButton(self.groupBox)
        self.m_topologicalTool.setCheckable(True)
        self.m_topologicalTool.setObjectName(_fromUtf8("m_topologicalTool"))
        self.horizontalLayout_3.addWidget(self.m_topologicalTool)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(17, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.m_contextDataGroup.raise_()
        self.groupBox.raise_()
        self.m_metadataGroup.raise_()
        self.m_featureDataGroup.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.m_clearButton = QtGui.QPushButton(self.PlanDockContents)
        self.m_clearButton.setObjectName(_fromUtf8("m_clearButton"))
        self.horizontalLayout.addWidget(self.m_clearButton)
        self.m_mergeButton = QtGui.QPushButton(self.PlanDockContents)
        self.m_mergeButton.setObjectName(_fromUtf8("m_mergeButton"))
        self.horizontalLayout.addWidget(self.m_mergeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.scrollArea.raise_()
        PlanDockWidget.setWidget(self.PlanDockContents)
        self.m_sourceIdLabel.setBuddy(self.m_sourceClassCombo)
        self.m_siteLabel.setBuddy(self.m_siteEdit)
        self.m_sourceCodeLabel.setBuddy(self.m_sourceCodeCombo)
        self.m_sourceFileLabel.setBuddy(self.m_sourceFileEdit)
        self.m_commentLabel.setBuddy(self.m_commentEdit)
        self.m_createdByLabel.setBuddy(self.m_createdByEdit)
        self.m_contextNumberLabel.setBuddy(self.m_contextNumberSpin)
        self.m_featureNameLabel.setBuddy(self.m_featureNameEdit)
        self.m_featureIdLabel.setBuddy(self.m_featureIdSpin)
        self.label_2.setBuddy(self.m_snapLinesLayerTool)
        self.label.setBuddy(self.m_snapLinesBufferTool)
        self.m_topologicalLabel.setBuddy(self.m_topologicalTool)

        self.retranslateUi(PlanDockWidget)
        QtCore.QMetaObject.connectSlotsByName(PlanDockWidget)
        PlanDockWidget.setTabOrder(self.scrollArea, self.m_siteEdit)
        PlanDockWidget.setTabOrder(self.m_siteEdit, self.m_sourceCodeCombo)
        PlanDockWidget.setTabOrder(self.m_sourceCodeCombo, self.m_sourceClassCombo)
        PlanDockWidget.setTabOrder(self.m_sourceClassCombo, self.m_sourceIdSpin)
        PlanDockWidget.setTabOrder(self.m_sourceIdSpin, self.m_sourceFileEdit)
        PlanDockWidget.setTabOrder(self.m_sourceFileEdit, self.m_commentEdit)
        PlanDockWidget.setTabOrder(self.m_commentEdit, self.m_createdByEdit)
        PlanDockWidget.setTabOrder(self.m_createdByEdit, self.m_loadRawButton)
        PlanDockWidget.setTabOrder(self.m_loadRawButton, self.m_loadGeoButton)
        PlanDockWidget.setTabOrder(self.m_loadGeoButton, self.m_loadContextButton)
        PlanDockWidget.setTabOrder(self.m_loadContextButton, self.m_contextNumberSpin)
        PlanDockWidget.setTabOrder(self.m_contextNumberSpin, self.m_featureIdSpin)
        PlanDockWidget.setTabOrder(self.m_featureIdSpin, self.m_featureNameEdit)
        PlanDockWidget.setTabOrder(self.m_featureNameEdit, self.m_snapLinesBufferTool)
        PlanDockWidget.setTabOrder(self.m_snapLinesBufferTool, self.m_snapPolygonsBufferTool)
        PlanDockWidget.setTabOrder(self.m_snapPolygonsBufferTool, self.m_snapLinesLayerTool)
        PlanDockWidget.setTabOrder(self.m_snapLinesLayerTool, self.m_snapPolygonsLayerTool)
        PlanDockWidget.setTabOrder(self.m_snapPolygonsLayerTool, self.m_topologicalTool)
        PlanDockWidget.setTabOrder(self.m_topologicalTool, self.m_clearButton)
        PlanDockWidget.setTabOrder(self.m_clearButton, self.m_mergeButton)

    def retranslateUi(self, PlanDockWidget):
        PlanDockWidget.setWindowTitle(_translate("PlanDockWidget", "ArkPlan", None))
        self.m_metadataGroup.setTitle(_translate("PlanDockWidget", "Metadata", None))
        self.m_sourceIdLabel.setText(_translate("PlanDockWidget", "Source ID:", None))
        self.m_siteLabel.setText(_translate("PlanDockWidget", "Site Code:", None))
        self.m_sourceCodeLabel.setText(_translate("PlanDockWidget", "Source:", None))
        self.m_sourceFileLabel.setText(_translate("PlanDockWidget", "Source File:", None))
        self.m_commentLabel.setText(_translate("PlanDockWidget", "Comment:", None))
        self.m_createdByLabel.setText(_translate("PlanDockWidget", "Created By:", None))
        self.m_sourceIdSpin.setToolTip(_translate("PlanDockWidget", "Source ID", None))
        self.m_contextDataGroup.setTitle(_translate("PlanDockWidget", "Context Data", None))
        self.m_loadContextButton.setText(_translate("PlanDockWidget", "Context", None))
        self.m_loadRawButton.setText(_translate("PlanDockWidget", "Raw Plan", None))
        self.m_contextNumberSpin.setToolTip(_translate("PlanDockWidget", "Context Number", None))
        self.m_loadGeoButton.setText(_translate("PlanDockWidget", "Geo Plan", None))
        self.m_contextNumberLabel.setText(_translate("PlanDockWidget", "Context:", None))
        self.m_featureDataGroup.setTitle(_translate("PlanDockWidget", "Feature Data", None))
        self.m_featureNameLabel.setText(_translate("PlanDockWidget", "Name:", None))
        self.m_featureIdLabel.setText(_translate("PlanDockWidget", "ID:", None))
        self.groupBox.setTitle(_translate("PlanDockWidget", "Editing:", None))
        self.m_snapPolygonsBufferTool.setText(_translate("PlanDockWidget", "...", None))
        self.label_12.setText(_translate("PlanDockWidget", "Polys", None))
        self.label_2.setText(_translate("PlanDockWidget", "Snap Layers:", None))
        self.m_snapPolygonsLayerTool.setText(_translate("PlanDockWidget", "...", None))
        self.m_snapLinesLayerTool.setText(_translate("PlanDockWidget", "...", None))
        self.label_11.setText(_translate("PlanDockWidget", "Lines", None))
        self.m_snapLinesBufferTool.setText(_translate("PlanDockWidget", "...", None))
        self.label.setText(_translate("PlanDockWidget", "Snap Buffers:", None))
        self.m_topologicalLabel.setText(_translate("PlanDockWidget", "Topological editing:", None))
        self.m_topologicalTool.setText(_translate("PlanDockWidget", "topo", None))
        self.m_clearButton.setToolTip(_translate("PlanDockWidget", "Clear unsaved changes from work layers", None))
        self.m_clearButton.setText(_translate("PlanDockWidget", "Clear", None))
        self.m_mergeButton.setToolTip(_translate("PlanDockWidget", "Move new context to main layers", None))
        self.m_mergeButton.setText(_translate("PlanDockWidget", "Merge", None))

from ..libarkqgis.dock import ArkDockWidget
from ..libarkqgis.snapping import SnappingToolButton, TopoEditToolButton
