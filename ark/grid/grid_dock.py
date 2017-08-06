# -*- coding: utf-8 -*-
"""
/***************************************************************************
                                ARK Spatial
                    A QGIS plugin for Archaeological Recording.
        Part of the Archaeological Recording Kit by L-P : Archaeology
                        http://ark.lparchaeology.com
                              -------------------
        copyright            : 2017 by L-P : Heritage LLP
        email                : ark@lparchaeology.com
        copyright            : 2017 by John Layt
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

from ark.lib.gui import ToolDockWidget


class GridDock(ToolDockWidget):

    def __init__(self, parent=None):
        super(GridDock, self).__init__(GridWidget(), parent)

        self.setWindowTitle(self.tr(u'ARK Grid'))
        self.setObjectName(u'GridDock')

    def initGui(self, iface, location, menuAction):
        super(GridDock, self).initGui(iface, location, menuAction)
        self.widget.initGui()