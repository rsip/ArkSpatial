# -*- coding: utf-8 -*-
"""
/***************************************************************************
                                      Ark
                                 A QGIS plugin
             QGIS Plugin for ARK, the Archaeological Recording Kit
                              -------------------
        begin                : 2015-03-02
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
from PyQt4.QtGui import QDockWidget, QMenu, QAction, QIcon

from ..libarkqgis.dock import ArkDockWidget
from ..libarkqgis.snapping import *

import plan_dock_base

class PlanDock(ArkDockWidget, plan_dock_base.Ui_PlanDockWidget):

    loadRawFileSelected = pyqtSignal()
    loadGeoFileSelected = pyqtSignal()
    loadContextSelected = pyqtSignal()

    siteChanged = pyqtSignal(str)
    contextNumberChanged = pyqtSignal(int)
    featureIdChanged = pyqtSignal(int)
    featureNameChanged = pyqtSignal(str)
    sourceCodeChanged = pyqtSignal(str)
    sourceClassChanged = pyqtSignal(str)
    sourceIdChanged = pyqtSignal(int)
    sourceFileChanged = pyqtSignal(str)
    commentChanged = pyqtSignal(str)
    createdByChanged = pyqtSignal(str)

    clearSelected = pyqtSignal()
    mergeSelected = pyqtSignal()

    _cgColMax = 3
    _cgCol = 0
    _cgRow = 0
    _fgColMax = 3
    _fgCol = 0
    _fgRow = 0

    def __init__(self, parent=None):
        super(PlanDock, self).__init__(parent)
        self.setupUi(self)

        self.m_loadRawButton.clicked.connect(self.loadRawFileSelected)
        self.m_loadGeoButton.clicked.connect(self.loadGeoFileSelected)
        self.m_loadContextButton.clicked.connect(self.loadContextSelected)

        self.m_siteEdit.textChanged.connect(self.siteChanged)
        self.m_contextNumberSpin.valueChanged.connect(self.contextNumberChanged)
        self.m_featureIdSpin.valueChanged.connect(self.featureIdChanged)
        self.m_featureNameEdit.textChanged.connect(self.featureNameChanged)
        self.m_sourceCodeCombo.currentIndexChanged.connect(self.sourceCodeIndexChanged)
        self.m_sourceClassCombo.currentIndexChanged.connect(self.sourceClassIndexChanged)
        self.m_sourceIdSpin.valueChanged.connect(self.sourceIdChanged)
        self.m_sourceFileEdit.textChanged.connect(self.sourceFileChanged)
        self.m_commentEdit.textChanged.connect(self.commentChanged)
        self.m_createdByEdit.textChanged.connect(self.createdByChanged)

        self.m_clearButton.clicked.connect(self.clearSelected)
        self.m_mergeButton.clicked.connect(self.mergeSelected)

    # Metadata Tools

    def setSite(self, name):
        self.m_siteEdit.setText(name)

    def setContextNumber(self, context):
        self.m_contextNumberSpin.setValue(context)

    def setFeatureId(self, featureId):
        self.m_featureIdSpin.setValue(featureId)

    def setFeatureName(self, name):
        self.m_featureNameEdit.setText(name)

    def addSourceCode(self, name, code):
        self.m_sourceCodeCombo.addItem(name, code)

    def setSourceCode(self, sourceCode):
        self.m_sourceCodeCombo.setCurrentIndex(self.m_sourceCodeCombo.findData(sourceCode))

    def addSourceClass(self, name, code):
        self.m_sourceClassCombo.addItem(name, code)

    def setSourceClass(self, sourceClass):
        self.m_sourceClassCombo.setCurrentIndex(self.m_sourceClassCombo.findData(sourceClass))

    def sourceCodeIndexChanged(self, index):
        self.sourceCodeChanged.emit(self.m_sourceCodeCombo.itemData(index))

    def sourceClassIndexChanged(self, index):
        self.sourceClassChanged.emit(self.m_sourceClassCombo.itemData(index))

    def setSourceId(self, sourceId):
        self.m_sourceIdSpin.setValue(sourceId)

    def setSourceFile(self, sourceFile):
        self.m_sourceFileEdit.setText(sourceFile)

    def setComment(self, comment):
        self.m_commentEdit.setText(comment)

    def setCreatedBy(self, creator):
        self.m_createdByEdit.setText(creator)

    # Drawing Tools

    def addDrawingTool(self, classCode, action):
        toolButton = QToolButton(self)
        toolButton.setFixedWidth(40)
        toolButton.setDefaultAction(action)
        if classCode == 'cxt':
            self.m_contextToolsLayout.addWidget(toolButton, self._cgRow, self._cgCol, Qt.AlignCenter)
            if self._cgCol == self._cgColMax:
                self.newDrawingToolRow(classCode)
            else:
                self._cgCol += 1
        else:
            self.m_featureToolsLayout.addWidget(toolButton, self._fgRow, self._fgCol, Qt.AlignCenter)
            if self._fgCol == self._fgColMax:
                self.newDrawingToolRow(classCode)
            else:
                self._fgCol += 1

    def newDrawingToolRow(self, classCode):
        if classCode == 'cxt':
            self._cgRow += 1
            self._cgCol = 0
        else:
            self._fgRow += 1
            self._fgCol = 0

    # Snapping Tools

    def setLinesBuffer(self, layer):
        self.m_snapLinesBufferTool.setLayer(layer)

    def setPolygonsBuffer(self, layer):
        self.m_snapPolygonsBufferTool.setLayer(layer)

    def setLinesLayer(self, layer):
        self.m_snapLinesLayerTool.setLayer(layer)

    def setPolygonsLayer(self, layer):
        self.m_snapPolygonsLayerTool.setLayer(layer)
