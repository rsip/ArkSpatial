# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grid/grid_wizard_base.ui'
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

class Ui_GridWizard(object):
    def setupUi(self, GridWizard):
        GridWizard.setObjectName(_fromUtf8("GridWizard"))
        GridWizard.resize(629, 380)
        self.welcomePage = QtGui.QWizardPage()
        self.welcomePage.setObjectName(_fromUtf8("welcomePage"))
        self.gridLayout_2 = QtGui.QGridLayout(self.welcomePage)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        GridWizard.addPage(self.welcomePage)
        self.filesPage = QtGui.QWizardPage()
        self.filesPage.setEnabled(False)
        self.filesPage.setObjectName(_fromUtf8("filesPage"))
        self.gridLayout = QtGui.QGridLayout(self.filesPage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridFolderLabel = QtGui.QLabel(self.filesPage)
        self.gridFolderLabel.setObjectName(_fromUtf8("gridFolderLabel"))
        self.gridLayout.addWidget(self.gridFolderLabel, 0, 0, 1, 1)
        self.gridFolderLayout = QtGui.QHBoxLayout()
        self.gridFolderLayout.setObjectName(_fromUtf8("gridFolderLayout"))
        self.gridFolderEdit = QtGui.QLineEdit(self.filesPage)
        self.gridFolderEdit.setObjectName(_fromUtf8("gridFolderEdit"))
        self.gridFolderLayout.addWidget(self.gridFolderEdit)
        self.gridFolderButton = QtGui.QPushButton(self.filesPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridFolderButton.sizePolicy().hasHeightForWidth())
        self.gridFolderButton.setSizePolicy(sizePolicy)
        self.gridFolderButton.setObjectName(_fromUtf8("gridFolderButton"))
        self.gridFolderLayout.addWidget(self.gridFolderButton)
        self.gridLayout.addLayout(self.gridFolderLayout, 0, 1, 1, 1)
        self.gridGroupNameLabel = QtGui.QLabel(self.filesPage)
        self.gridGroupNameLabel.setObjectName(_fromUtf8("gridGroupNameLabel"))
        self.gridLayout.addWidget(self.gridGroupNameLabel, 1, 0, 1, 1)
        self.gridGroupNameEdit = QtGui.QLineEdit(self.filesPage)
        self.gridGroupNameEdit.setObjectName(_fromUtf8("gridGroupNameEdit"))
        self.gridLayout.addWidget(self.gridGroupNameEdit, 1, 1, 1, 1)
        self.gridPointNameLabel = QtGui.QLabel(self.filesPage)
        self.gridPointNameLabel.setObjectName(_fromUtf8("gridPointNameLabel"))
        self.gridLayout.addWidget(self.gridPointNameLabel, 2, 0, 1, 1)
        self.gridPointsNameEdit = QtGui.QLineEdit(self.filesPage)
        self.gridPointsNameEdit.setObjectName(_fromUtf8("gridPointsNameEdit"))
        self.gridLayout.addWidget(self.gridPointsNameEdit, 2, 1, 1, 1)
        self.gridLinesNameLabel = QtGui.QLabel(self.filesPage)
        self.gridLinesNameLabel.setObjectName(_fromUtf8("gridLinesNameLabel"))
        self.gridLayout.addWidget(self.gridLinesNameLabel, 3, 0, 1, 1)
        self.gridLinesNameEdit = QtGui.QLineEdit(self.filesPage)
        self.gridLinesNameEdit.setObjectName(_fromUtf8("gridLinesNameEdit"))
        self.gridLayout.addWidget(self.gridLinesNameEdit, 3, 1, 1, 1)
        self.gridPolygonsNameLabel = QtGui.QLabel(self.filesPage)
        self.gridPolygonsNameLabel.setObjectName(_fromUtf8("gridPolygonsNameLabel"))
        self.gridLayout.addWidget(self.gridPolygonsNameLabel, 4, 0, 1, 1)
        self.gridPolygonsNameEdit = QtGui.QLineEdit(self.filesPage)
        self.gridPolygonsNameEdit.setObjectName(_fromUtf8("gridPolygonsNameEdit"))
        self.gridLayout.addWidget(self.gridPolygonsNameEdit, 4, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        GridWizard.addPage(self.filesPage)
        self.mapPage = QtGui.QWizardPage()
        self.mapPage.setObjectName(_fromUtf8("mapPage"))
        self.gridLayout_4 = QtGui.QGridLayout(self.mapPage)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.mapEastingLabel = QtGui.QLabel(self.mapPage)
        self.mapEastingLabel.setObjectName(_fromUtf8("mapEastingLabel"))
        self.gridLayout_4.addWidget(self.mapEastingLabel, 3, 1, 1, 1)
        self.localPoint1EastingSpin = QtGui.QDoubleSpinBox(self.mapPage)
        self.localPoint1EastingSpin.setDecimals(3)
        self.localPoint1EastingSpin.setMinimum(-999999.999)
        self.localPoint1EastingSpin.setMaximum(999999.999)
        self.localPoint1EastingSpin.setObjectName(_fromUtf8("localPoint1EastingSpin"))
        self.gridLayout_4.addWidget(self.localPoint1EastingSpin, 5, 1, 1, 1)
        self.mapPoint1Label = QtGui.QLabel(self.mapPage)
        self.mapPoint1Label.setObjectName(_fromUtf8("mapPoint1Label"))
        self.gridLayout_4.addWidget(self.mapPoint1Label, 4, 0, 1, 1)
        self.localPoint1Label = QtGui.QLabel(self.mapPage)
        self.localPoint1Label.setObjectName(_fromUtf8("localPoint1Label"))
        self.gridLayout_4.addWidget(self.localPoint1Label, 5, 0, 1, 1)
        self.mapPoint2Label = QtGui.QLabel(self.mapPage)
        self.mapPoint2Label.setObjectName(_fromUtf8("mapPoint2Label"))
        self.gridLayout_4.addWidget(self.mapPoint2Label, 6, 0, 1, 1)
        self.localPoint2NorthingSpin = QtGui.QDoubleSpinBox(self.mapPage)
        self.localPoint2NorthingSpin.setDecimals(3)
        self.localPoint2NorthingSpin.setMinimum(-999999.999)
        self.localPoint2NorthingSpin.setMaximum(999999.999)
        self.localPoint2NorthingSpin.setObjectName(_fromUtf8("localPoint2NorthingSpin"))
        self.gridLayout_4.addWidget(self.localPoint2NorthingSpin, 7, 2, 1, 1)
        self.mapNorthingLabel = QtGui.QLabel(self.mapPage)
        self.mapNorthingLabel.setObjectName(_fromUtf8("mapNorthingLabel"))
        self.gridLayout_4.addWidget(self.mapNorthingLabel, 3, 2, 1, 1)
        self.localPoint2EastingSpin = QtGui.QDoubleSpinBox(self.mapPage)
        self.localPoint2EastingSpin.setDecimals(3)
        self.localPoint2EastingSpin.setMinimum(-999999.999)
        self.localPoint2EastingSpin.setMaximum(999999.999)
        self.localPoint2EastingSpin.setObjectName(_fromUtf8("localPoint2EastingSpin"))
        self.gridLayout_4.addWidget(self.localPoint2EastingSpin, 7, 1, 1, 1)
        self.localPoint2Label = QtGui.QLabel(self.mapPage)
        self.localPoint2Label.setObjectName(_fromUtf8("localPoint2Label"))
        self.gridLayout_4.addWidget(self.localPoint2Label, 7, 0, 1, 1)
        self.mapPoint1EastingSpin = QtGui.QDoubleSpinBox(self.mapPage)
        self.mapPoint1EastingSpin.setDecimals(3)
        self.mapPoint1EastingSpin.setMinimum(-999999.999)
        self.mapPoint1EastingSpin.setMaximum(999999.999)
        self.mapPoint1EastingSpin.setObjectName(_fromUtf8("mapPoint1EastingSpin"))
        self.gridLayout_4.addWidget(self.mapPoint1EastingSpin, 4, 1, 1, 1)
        self.mapPoint1NorthingSpin = QtGui.QDoubleSpinBox(self.mapPage)
        self.mapPoint1NorthingSpin.setDecimals(3)
        self.mapPoint1NorthingSpin.setMinimum(-999999.999)
        self.mapPoint1NorthingSpin.setMaximum(999999.999)
        self.mapPoint1NorthingSpin.setObjectName(_fromUtf8("mapPoint1NorthingSpin"))
        self.gridLayout_4.addWidget(self.mapPoint1NorthingSpin, 4, 2, 1, 1)
        self.mapPoint1FromMapButton = QtGui.QPushButton(self.mapPage)
        self.mapPoint1FromMapButton.setObjectName(_fromUtf8("mapPoint1FromMapButton"))
        self.gridLayout_4.addWidget(self.mapPoint1FromMapButton, 4, 3, 1, 1)
        self.mapPoint2FromMapButton = QtGui.QPushButton(self.mapPage)
        self.mapPoint2FromMapButton.setObjectName(_fromUtf8("mapPoint2FromMapButton"))
        self.gridLayout_4.addWidget(self.mapPoint2FromMapButton, 6, 3, 1, 1)
        self.mapPoint2EastingSpin = QtGui.QDoubleSpinBox(self.mapPage)
        self.mapPoint2EastingSpin.setDecimals(3)
        self.mapPoint2EastingSpin.setMinimum(-999999.999)
        self.mapPoint2EastingSpin.setMaximum(999999.999)
        self.mapPoint2EastingSpin.setObjectName(_fromUtf8("mapPoint2EastingSpin"))
        self.gridLayout_4.addWidget(self.mapPoint2EastingSpin, 6, 1, 1, 1)
        self.mapPoint2NorthingSpin = QtGui.QDoubleSpinBox(self.mapPage)
        self.mapPoint2NorthingSpin.setDecimals(3)
        self.mapPoint2NorthingSpin.setMinimum(-999999.999)
        self.mapPoint2NorthingSpin.setMaximum(999999.999)
        self.mapPoint2NorthingSpin.setObjectName(_fromUtf8("mapPoint2NorthingSpin"))
        self.gridLayout_4.addWidget(self.mapPoint2NorthingSpin, 6, 2, 1, 1)
        self.localPoint1NorthingSpin = QtGui.QDoubleSpinBox(self.mapPage)
        self.localPoint1NorthingSpin.setDecimals(3)
        self.localPoint1NorthingSpin.setMinimum(-999999.999)
        self.localPoint1NorthingSpin.setMaximum(999999.999)
        self.localPoint1NorthingSpin.setObjectName(_fromUtf8("localPoint1NorthingSpin"))
        self.gridLayout_4.addWidget(self.localPoint1NorthingSpin, 5, 2, 1, 1)
        self.methodLabel = QtGui.QLabel(self.mapPage)
        self.methodLabel.setObjectName(_fromUtf8("methodLabel"))
        self.gridLayout_4.addWidget(self.methodLabel, 1, 0, 1, 1)
        self.methodCombo = QtGui.QComboBox(self.mapPage)
        self.methodCombo.setObjectName(_fromUtf8("methodCombo"))
        self.methodCombo.addItem(_fromUtf8(""))
        self.methodCombo.addItem(_fromUtf8(""))
        self.methodCombo.addItem(_fromUtf8(""))
        self.gridLayout_4.addWidget(self.methodCombo, 1, 1, 1, 3)
        self.label = QtGui.QLabel(self.mapPage)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 1)
        GridWizard.addPage(self.mapPage)
        self.localPage = QtGui.QWizardPage()
        self.localPage.setObjectName(_fromUtf8("localPage"))
        self.gridLayout_5 = QtGui.QGridLayout(self.localPage)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.siteCodeLabel = QtGui.QLabel(self.localPage)
        self.siteCodeLabel.setObjectName(_fromUtf8("siteCodeLabel"))
        self.gridLayout_5.addWidget(self.siteCodeLabel, 0, 0, 1, 1)
        self.gridNameEdit = QtGui.QLineEdit(self.localPage)
        self.gridNameEdit.setObjectName(_fromUtf8("gridNameEdit"))
        self.gridLayout_5.addWidget(self.gridNameEdit, 1, 1, 1, 2)
        self.localNorthingIntervalSpin = QtGui.QSpinBox(self.localPage)
        self.localNorthingIntervalSpin.setMaximum(100)
        self.localNorthingIntervalSpin.setSingleStep(5)
        self.localNorthingIntervalSpin.setProperty("value", 5)
        self.localNorthingIntervalSpin.setObjectName(_fromUtf8("localNorthingIntervalSpin"))
        self.gridLayout_5.addWidget(self.localNorthingIntervalSpin, 6, 2, 1, 1)
        self.localTerminusEastingSpin = QtGui.QSpinBox(self.localPage)
        self.localTerminusEastingSpin.setMaximum(9999)
        self.localTerminusEastingSpin.setSingleStep(5)
        self.localTerminusEastingSpin.setProperty("value", 200)
        self.localTerminusEastingSpin.setObjectName(_fromUtf8("localTerminusEastingSpin"))
        self.gridLayout_5.addWidget(self.localTerminusEastingSpin, 5, 1, 1, 1)
        self.siteCodeEdit = QtGui.QLineEdit(self.localPage)
        self.siteCodeEdit.setObjectName(_fromUtf8("siteCodeEdit"))
        self.gridLayout_5.addWidget(self.siteCodeEdit, 0, 1, 1, 2)
        self.localEastingIntervalSpin = QtGui.QSpinBox(self.localPage)
        self.localEastingIntervalSpin.setMaximum(100)
        self.localEastingIntervalSpin.setSingleStep(5)
        self.localEastingIntervalSpin.setProperty("value", 5)
        self.localEastingIntervalSpin.setObjectName(_fromUtf8("localEastingIntervalSpin"))
        self.gridLayout_5.addWidget(self.localEastingIntervalSpin, 6, 1, 1, 1)
        self.localOriginLabel = QtGui.QLabel(self.localPage)
        self.localOriginLabel.setObjectName(_fromUtf8("localOriginLabel"))
        self.gridLayout_5.addWidget(self.localOriginLabel, 4, 0, 1, 1)
        self.localOriginEastingSpin = QtGui.QSpinBox(self.localPage)
        self.localOriginEastingSpin.setMaximum(9999)
        self.localOriginEastingSpin.setSingleStep(5)
        self.localOriginEastingSpin.setProperty("value", 100)
        self.localOriginEastingSpin.setObjectName(_fromUtf8("localOriginEastingSpin"))
        self.gridLayout_5.addWidget(self.localOriginEastingSpin, 4, 1, 1, 1)
        self.localEastingLabel = QtGui.QLabel(self.localPage)
        self.localEastingLabel.setObjectName(_fromUtf8("localEastingLabel"))
        self.gridLayout_5.addWidget(self.localEastingLabel, 3, 1, 1, 1)
        self.localTerminusNorthingSpin = QtGui.QSpinBox(self.localPage)
        self.localTerminusNorthingSpin.setMaximum(9999)
        self.localTerminusNorthingSpin.setSingleStep(5)
        self.localTerminusNorthingSpin.setProperty("value", 300)
        self.localTerminusNorthingSpin.setObjectName(_fromUtf8("localTerminusNorthingSpin"))
        self.gridLayout_5.addWidget(self.localTerminusNorthingSpin, 5, 2, 1, 1)
        self.localTerminusLabel = QtGui.QLabel(self.localPage)
        self.localTerminusLabel.setObjectName(_fromUtf8("localTerminusLabel"))
        self.gridLayout_5.addWidget(self.localTerminusLabel, 5, 0, 1, 1)
        self.localNorthingLabel = QtGui.QLabel(self.localPage)
        self.localNorthingLabel.setObjectName(_fromUtf8("localNorthingLabel"))
        self.gridLayout_5.addWidget(self.localNorthingLabel, 3, 2, 1, 1)
        self.localOriginNorthingSpin = QtGui.QSpinBox(self.localPage)
        self.localOriginNorthingSpin.setMaximum(9999)
        self.localOriginNorthingSpin.setSingleStep(5)
        self.localOriginNorthingSpin.setProperty("value", 200)
        self.localOriginNorthingSpin.setObjectName(_fromUtf8("localOriginNorthingSpin"))
        self.gridLayout_5.addWidget(self.localOriginNorthingSpin, 4, 2, 1, 1)
        self.gridNameLabel = QtGui.QLabel(self.localPage)
        self.gridNameLabel.setObjectName(_fromUtf8("gridNameLabel"))
        self.gridLayout_5.addWidget(self.gridNameLabel, 1, 0, 1, 1)
        self.localIntervalLabel = QtGui.QLabel(self.localPage)
        self.localIntervalLabel.setObjectName(_fromUtf8("localIntervalLabel"))
        self.gridLayout_5.addWidget(self.localIntervalLabel, 6, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.localPage)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)
        GridWizard.addPage(self.localPage)
        self.gridFolderLabel.setBuddy(self.gridFolderEdit)
        self.gridGroupNameLabel.setBuddy(self.gridGroupNameEdit)
        self.gridPointNameLabel.setBuddy(self.gridPointsNameEdit)
        self.gridLinesNameLabel.setBuddy(self.gridLinesNameEdit)
        self.gridPolygonsNameLabel.setBuddy(self.gridPolygonsNameEdit)
        self.mapPoint1Label.setBuddy(self.mapPoint1EastingSpin)
        self.localPoint1Label.setBuddy(self.localPoint1EastingSpin)
        self.mapPoint2Label.setBuddy(self.mapPoint2EastingSpin)
        self.localPoint2Label.setBuddy(self.localPoint2EastingSpin)
        self.methodLabel.setBuddy(self.methodCombo)
        self.siteCodeLabel.setBuddy(self.siteCodeEdit)
        self.localOriginLabel.setBuddy(self.localOriginEastingSpin)
        self.localTerminusLabel.setBuddy(self.localTerminusEastingSpin)
        self.localIntervalLabel.setBuddy(self.localEastingIntervalSpin)

        self.retranslateUi(GridWizard)
        QtCore.QMetaObject.connectSlotsByName(GridWizard)
        GridWizard.setTabOrder(self.gridFolderEdit, self.gridFolderButton)
        GridWizard.setTabOrder(self.gridFolderButton, self.gridGroupNameEdit)
        GridWizard.setTabOrder(self.gridGroupNameEdit, self.gridPointsNameEdit)
        GridWizard.setTabOrder(self.gridPointsNameEdit, self.gridLinesNameEdit)
        GridWizard.setTabOrder(self.gridLinesNameEdit, self.gridPolygonsNameEdit)
        GridWizard.setTabOrder(self.gridPolygonsNameEdit, self.methodCombo)
        GridWizard.setTabOrder(self.methodCombo, self.mapPoint1EastingSpin)
        GridWizard.setTabOrder(self.mapPoint1EastingSpin, self.mapPoint1NorthingSpin)
        GridWizard.setTabOrder(self.mapPoint1NorthingSpin, self.mapPoint1FromMapButton)
        GridWizard.setTabOrder(self.mapPoint1FromMapButton, self.localPoint1EastingSpin)
        GridWizard.setTabOrder(self.localPoint1EastingSpin, self.localPoint1NorthingSpin)
        GridWizard.setTabOrder(self.localPoint1NorthingSpin, self.mapPoint2EastingSpin)
        GridWizard.setTabOrder(self.mapPoint2EastingSpin, self.mapPoint2NorthingSpin)
        GridWizard.setTabOrder(self.mapPoint2NorthingSpin, self.mapPoint2FromMapButton)
        GridWizard.setTabOrder(self.mapPoint2FromMapButton, self.localPoint2EastingSpin)
        GridWizard.setTabOrder(self.localPoint2EastingSpin, self.localPoint2NorthingSpin)
        GridWizard.setTabOrder(self.localPoint2NorthingSpin, self.siteCodeEdit)
        GridWizard.setTabOrder(self.siteCodeEdit, self.gridNameEdit)
        GridWizard.setTabOrder(self.gridNameEdit, self.localOriginEastingSpin)
        GridWizard.setTabOrder(self.localOriginEastingSpin, self.localOriginNorthingSpin)
        GridWizard.setTabOrder(self.localOriginNorthingSpin, self.localTerminusEastingSpin)
        GridWizard.setTabOrder(self.localTerminusEastingSpin, self.localTerminusNorthingSpin)
        GridWizard.setTabOrder(self.localTerminusNorthingSpin, self.localEastingIntervalSpin)
        GridWizard.setTabOrder(self.localEastingIntervalSpin, self.localNorthingIntervalSpin)

    def retranslateUi(self, GridWizard):
        GridWizard.setWindowTitle(_translate("GridWizard", "Wizard", None))
        self.welcomePage.setTitle(_translate("GridWizard", "Grid Wizard", None))
        self.welcomePage.setSubTitle(_translate("GridWizard", "This wizard will walk you through the steps required to create a new local grid", None))
        self.filesPage.setTitle(_translate("GridWizard", "Choose Files", None))
        self.filesPage.setSubTitle(_translate("GridWizard", "Please select the grid files to use. If you select a folder and files that already exist the new grid will be added to these files. Otherwise the grid files will be created in the selcted folder and the new grid added to the new files. If you leave the Lines or Polygons field empty that file will not be ceated.", None))
        self.gridFolderLabel.setText(_translate("GridWizard", "Folder:", None))
        self.gridFolderButton.setText(_translate("GridWizard", "...", None))
        self.gridGroupNameLabel.setText(_translate("GridWizard", "Group Name:", None))
        self.gridPointNameLabel.setText(_translate("GridWizard", "Points File Name:", None))
        self.gridLinesNameLabel.setText(_translate("GridWizard", "Lines File Name:", None))
        self.gridPolygonsNameLabel.setText(_translate("GridWizard", "Polygons File Name:", None))
        self.mapPage.setTitle(_translate("GridWizard", "Map Coordinates", None))
        self.mapPage.setSubTitle(_translate("GridWizard", "Enter the two map coordinate points to use to calculate your local grid from.", None))
        self.mapEastingLabel.setText(_translate("GridWizard", "Easting", None))
        self.mapPoint1Label.setText(_translate("GridWizard", "Map Point 1:", None))
        self.localPoint1Label.setText(_translate("GridWizard", "Local Point 1:", None))
        self.mapPoint2Label.setText(_translate("GridWizard", "Map Point 2:", None))
        self.mapNorthingLabel.setText(_translate("GridWizard", "Northing", None))
        self.localPoint2Label.setText(_translate("GridWizard", "Local Point 2:", None))
        self.mapPoint1FromMapButton.setText(_translate("GridWizard", "From Map", None))
        self.mapPoint2FromMapButton.setText(_translate("GridWizard", "From Map", None))
        self.methodLabel.setText(_translate("GridWizard", "Method:", None))
        self.methodCombo.setItemText(0, _translate("GridWizard", "Create from two known points", None))
        self.methodCombo.setItemText(1, _translate("GridWizard", "Create from X axis baseline", None))
        self.methodCombo.setItemText(2, _translate("GridWizard", "Create from Y axis baseline", None))
        self.localPage.setTitle(_translate("GridWizard", "Local Grid Extent", None))
        self.localPage.setSubTitle(_translate("GridWizard", "Enter the origin, extent, and interval of the local coordinates.", None))
        self.siteCodeLabel.setText(_translate("GridWizard", "Site Code:", None))
        self.localNorthingIntervalSpin.setSuffix(_translate("GridWizard", " m", None))
        self.localEastingIntervalSpin.setSuffix(_translate("GridWizard", " m", None))
        self.localOriginLabel.setText(_translate("GridWizard", "Local Origin:", None))
        self.localEastingLabel.setText(_translate("GridWizard", "Local Easting", None))
        self.localTerminusLabel.setText(_translate("GridWizard", "Local Terminus:", None))
        self.localNorthingLabel.setText(_translate("GridWizard", "Local Northing", None))
        self.gridNameLabel.setText(_translate("GridWizard", "Grid Name:", None))
        self.localIntervalLabel.setText(_translate("GridWizard", "Grid Interval:", None))

