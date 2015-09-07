# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter/filter_dock_base.ui'
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

class Ui_FilterDock(object):
    def setupUi(self, FilterDock):
        FilterDock.setObjectName(_fromUtf8("FilterDock"))
        FilterDock.resize(306, 324)
        self.FilterDockContents = QtGui.QWidget()
        self.FilterDockContents.setObjectName(_fromUtf8("FilterDockContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.FilterDockContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.zoomFilterTool = QtGui.QToolButton(self.FilterDockContents)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/ArkPlan/mActionZoomToSelected.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomFilterTool.setIcon(icon)
        self.zoomFilterTool.setObjectName(_fromUtf8("zoomFilterTool"))
        self.horizontalLayout.addWidget(self.zoomFilterTool)
        self.buildFilterTool = QtGui.QToolButton(self.FilterDockContents)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/ArkPlan/mIconExpressionEditorOpen.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buildFilterTool.setIcon(icon1)
        self.buildFilterTool.setObjectName(_fromUtf8("buildFilterTool"))
        self.horizontalLayout.addWidget(self.buildFilterTool)
        self.buildSelectionTool = QtGui.QToolButton(self.FilterDockContents)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/ArkPlan/mIconExpressionSelect.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buildSelectionTool.setIcon(icon2)
        self.buildSelectionTool.setObjectName(_fromUtf8("buildSelectionTool"))
        self.horizontalLayout.addWidget(self.buildSelectionTool)
        self.clearFilterTool = QtGui.QToolButton(self.FilterDockContents)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/ArkPlan/mActionRemove.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearFilterTool.setIcon(icon3)
        self.clearFilterTool.setObjectName(_fromUtf8("clearFilterTool"))
        self.horizontalLayout.addWidget(self.clearFilterTool)
        self.loadDataTool = QtGui.QToolButton(self.FilterDockContents)
        self.loadDataTool.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/ArkPlan/mIconDbSchema.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadDataTool.setIcon(icon4)
        self.loadDataTool.setObjectName(_fromUtf8("loadDataTool"))
        self.horizontalLayout.addWidget(self.loadDataTool)
        self.showDataTool = QtGui.QToolButton(self.FilterDockContents)
        self.showDataTool.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/ArkPlan/mActionOpenTable.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.showDataTool.setIcon(icon5)
        self.showDataTool.setObjectName(_fromUtf8("showDataTool"))
        self.horizontalLayout.addWidget(self.showDataTool)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.siteCodeCombo = QtGui.QComboBox(self.FilterDockContents)
        self.siteCodeCombo.setObjectName(_fromUtf8("siteCodeCombo"))
        self.gridLayout.addWidget(self.siteCodeCombo, 0, 1, 1, 2)
        self.siteCodeLabel = QtGui.QLabel(self.FilterDockContents)
        self.siteCodeLabel.setObjectName(_fromUtf8("siteCodeLabel"))
        self.gridLayout.addWidget(self.siteCodeLabel, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.newFilterFrame = QtGui.QFrame(self.FilterDockContents)
        self.newFilterFrame.setObjectName(_fromUtf8("newFilterFrame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.newFilterFrame)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout.addWidget(self.newFilterFrame)
        self.filterListWidget = QtGui.QListWidget(self.FilterDockContents)
        self.filterListWidget.setProperty("showDropIndicator", False)
        self.filterListWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.filterListWidget.setObjectName(_fromUtf8("filterListWidget"))
        self.verticalLayout.addWidget(self.filterListWidget)
        self.filterListWidget.raise_()
        self.newFilterFrame.raise_()
        FilterDock.setWidget(self.FilterDockContents)
        self.zoomFilterAction = QtGui.QAction(FilterDock)
        self.zoomFilterAction.setIcon(icon)
        self.zoomFilterAction.setObjectName(_fromUtf8("zoomFilterAction"))
        self.buildFilterAction = QtGui.QAction(FilterDock)
        self.buildFilterAction.setIcon(icon1)
        self.buildFilterAction.setObjectName(_fromUtf8("buildFilterAction"))
        self.clearFilterAction = QtGui.QAction(FilterDock)
        self.clearFilterAction.setIcon(icon3)
        self.clearFilterAction.setObjectName(_fromUtf8("clearFilterAction"))
        self.loadDataAction = QtGui.QAction(FilterDock)
        self.loadDataAction.setIcon(icon4)
        self.loadDataAction.setObjectName(_fromUtf8("loadDataAction"))
        self.showDataAction = QtGui.QAction(FilterDock)
        self.showDataAction.setIcon(icon5)
        self.showDataAction.setObjectName(_fromUtf8("showDataAction"))
        self.buildSelectionAction = QtGui.QAction(FilterDock)
        self.buildSelectionAction.setIcon(icon2)
        self.buildSelectionAction.setObjectName(_fromUtf8("buildSelectionAction"))

        self.retranslateUi(FilterDock)
        QtCore.QMetaObject.connectSlotsByName(FilterDock)

    def retranslateUi(self, FilterDock):
        FilterDock.setWindowTitle(_translate("FilterDock", "Filter Ark Layers", None))
        self.zoomFilterTool.setText(_translate("FilterDock", "Zoom", None))
        self.buildFilterTool.setText(_translate("FilterDock", "Build", None))
        self.buildSelectionTool.setText(_translate("FilterDock", "...", None))
        self.clearFilterTool.setText(_translate("FilterDock", "Clear", None))
        self.loadDataTool.setText(_translate("FilterDock", "Load", None))
        self.showDataTool.setText(_translate("FilterDock", "Show", None))
        self.siteCodeLabel.setText(_translate("FilterDock", "Site:", None))
        self.zoomFilterAction.setText(_translate("FilterDock", "Zoom To Selection", None))
        self.buildFilterAction.setText(_translate("FilterDock", "Build Filter", None))
        self.clearFilterAction.setText(_translate("FilterDock", "Clear Filter", None))
        self.loadDataAction.setText(_translate("FilterDock", "Load Data", None))
        self.showDataAction.setText(_translate("FilterDock", "Show Data", None))
        self.buildSelectionAction.setText(_translate("FilterDock", "Build Selection", None))
        self.buildSelectionAction.setToolTip(_translate("FilterDock", "Build Selection", None))

from ..libarkqgis.dock import ArkDockWidget
import resources_rc
