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

from PyQt4.QtCore import Qt, QObject
from PyQt4.QtGui import QAction, QIcon, QFileDialog

from qgis.core import *
from qgis.gui import QgsExpressionBuilderDialog

from ..core.settings import Settings
from ..core.layers import LayerManager
from ..core.data_model import *

from filter_dock import FilterDock

class Filter(QObject):

    settings = None # Settings()
    layers = None  # LayerManager()
    data = None  # DataManager()

    # Internal variables
    initialised = False

    def __init__(self, settings, layers):
        super(Filter, self).__init__()
        self.settings = settings
        self.layers = layers
        self.data = DataManager(settings)


    # Standard Dock methods

    def initGui(self):
        self.dock = FilterDock()
        self.dock.load(self.settings, Qt.LeftDockWidgetArea, self.tr(u'Filter context layers'), ':/plugins/Ark/filter/view-filter.png')
        self.dock.toggled.connect(self.run)

        self.dock.contextFilterChanged.connect(self.applyContextFilter)
        self.dock.subGroupFilterChanged.connect(self.applySubGroupFilter)
        self.dock.groupFilterChanged.connect(self.applyGroupFilter)
        self.dock.buildFilterSelected.connect(self.buildFilter)
        self.dock.clearFilterSelected.connect(self.clearFilter)
        self.dock.loadDataSelected.connect(self.loadData)
        self.dock.zoomSelected.connect(self.zoomFilter)
        self.dock.showPointsChanged.connect(self.layers.showPoints)
        self.dock.showLinesChanged.connect(self.layers.showLines)
        self.dock.showPolygonsChanged.connect(self.layers.showPolygons)
        self.dock.showSchematicsChanged.connect(self.layers.showSchematics)


    def unload(self):
        self.dock.unload()


    def run(self, checked):
        if checked:
            self.initialise()


    def initialise(self):
        if self.initialised:
            return

        if (not self.settings.isConfigured()):
            self.settings.configure()
        self.layers.initialise()

        self.initialised = True


    # Filter methods

    def applyContextFilter(self, contextList):
        self.layers.applyContextFilter(contextList)
        self.dock.displayFilter(self.layers.filter)


    def applySubGroupFilter(self, subList):
        contextList = []
        for sub in subList:
            contextList.extend(self.data._contextGroupingModel.getContextsForSubGroup(sub))
        self.layers.applyContextFilter(contextList)
        self.dock.displayFilter(self.layers.filter)


    def applyGroupFilter(self, groupList):
        contextList = []
        for group in groupList:
            contextList.extend(self.data._contextGroupingModel.getContextsForGroup(group))
        self.layers.applyContextFilter(contextList)
        self.dock.displayFilter(self.layers.filter)


    def clearFilter(self):
        self.applyFilter('')


    def applyFilter(self, filter):
        self.layers.applyFilter(filter)
        self.dock.displayFilter(self.layers.filter)


    def buildFilter(self):
        dialog = QgsExpressionBuilderDialog(self.layers.linesLayer)
        dialog.setExpressionText(self.layers.filter)
        if (dialog.exec_()):
            self.applyFilter(dialog.expressionText())


    def loadData(self):
        self.data.loadData()
        self.dock.enableGroupFilters(True)


    def zoomFilter(self):
        self.layers.zoomToLayers(False)