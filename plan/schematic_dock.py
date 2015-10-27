# -*- coding: utf-8 -*-
"""
/***************************************************************************
                                      Ark
                                 A QGIS plugin
             QGIS Plugin for ARK, the Archaeological Recording Kit
                              -------------------
        begin                : 2015-10-27
        git sha              : $Format:%H$
        copyright            : (C) 2015 by L - P: Heritage LLP
        copyright            : (C) 2015 by John Layt
        email                : john@layt.net
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import uic
from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4.QtGui import QDockWidget, QPixmap

from ..libarkqgis.dock import ArkDockWidget

import schematic_dock_base
import resources_rc

class SearchStatus():

    Unknown = 0
    Found = 1
    NotFound = 2


class SchematicDock(ArkDockWidget, schematic_dock_base.Ui_SchematicDockWidget):

    findContextSelected = pyqtSignal()
    findSourceSelected = pyqtSignal()
    cloneContextSelected = pyqtSignal()
    clearSelected = pyqtSignal()
    mergeSelected = pyqtSignal()

    _drawColMax = 3
    _drawCol = 0
    _drawRow = 0

    def __init__(self, parent=None):
        super(SchematicDock, self).__init__(parent)
        self.setupUi(self)

        self.findContextButton.clicked.connect(self.findContextSelected)
        self.findSourceButton.clicked.connect(self.findSourceSelected)
        self.cloneSourceButton.clicked.connect(self.cloneContextSelected)
        self.clearButton.clicked.connect(self.clearSelected)
        self.mergeButton.clicked.connect(self.mergeSelected)

    def init(self, project):
        self.metadataWidget.init(project)
        self.setContext(0, SearchStatus.Unknown, SearchStatus.Unknown)

    # Metadata Tools

    def metadata(self):
        return self.metadataWidget.metadata()

    def setMetadata(self, md):
        self.metadataWidget.setMetadata(md)

    # Drawing Tools

    def addDrawingTool(self, classCode, action):
        toolButton = QToolButton(self)
        toolButton.setFixedWidth(40)
        toolButton.setDefaultAction(action)
        self.contextToolsLayout.addWidget(toolButton, self._drawRow, self._drawCol, Qt.AlignCenter)
        if self._cgCol == self._cgColMax:
            self.newDrawingToolRow()
        else:
            self._drawCol += 1

    def newDrawingToolRow(self):
        self._drawRow += 1
        self._drawCol = 0

    # Context Tools

    def setContext(self, context, foundData, foundSchematic):
        self.contextSpin.setValue(context)
        self._setStatus(self.contextDataStatusLabel, foundData)
        self._setStatus(self.contextSchematicStatusLabel, foundSchematic)
        self.setSource(0, SearchStatus.Unknown, SearchStatus.Unknown)
        self._enableSource(foundSchematic == SearchStatus.NotFound)
        self._enableDraw(foundSchematic == SearchStatus.NotFound)

    def setSource(self, context, foundData, foundSchematic):
        self.sourceContextSpin.setValue(context)
        self._setStatus(self.sourceDataStatusLabel, foundData)
        self._setStatus(self.sourceSchematicStatusLabel, foundSchematic)
        self._enableClone(foundSchematic == SearchStatus.Found)

    def _setStatus(self, label, status):
        if status == SearchStatus.Unknown:
            label.setPixmap(QPixmap(':/plugins/ArkPlan/user-offline.png'))
        elif status == SearchStatus.Found:
            label.setPixmap(QPixmap(':/plugins/ArkPlan/user-online.png'))
        elif status == SearchStatus.NotFound:
            label.setPixmap(QPixmap(':/plugins/ArkPlan/user-busy.png'))

    def _enableSource(self, enable):
        self.sourceContextSpin.setEnabled(enable)
        self.findSourceButton.setEnabled(enable)
        self.findSourceButton.setEnabled(enable)
        if not enable:
            self._enableClone(enable)

    def _enableClone(self, enable):
        self.cloneSourceButton.setEnabled(enable)

    def _enableDraw(self, enable):
        self.clearButton.setEnabled(enable)
        self.mergeButton.setEnabled(enable)