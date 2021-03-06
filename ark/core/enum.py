# -*- coding: utf-8 -*-
"""
/***************************************************************************
                                ARKspatial
                    A QGIS plugin for Archaeological Recording.
        Part of the Archaeological Recording Kit by L - P : Archaeology
                        http://ark.lparchaeology.com
                              -------------------
        copyright            : 2017 by L - P : Heritage LLP
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


class DrawingAction():
    NoDrawingAction = 0
    LoadDrawings = 1
    AddDrawings = 2


class MapAction():
    NoMapAction = 0
    ZoomMap = 1
    PanMap = 2
    MoveMap = 3


class FilterAction():
    NoFilterAction = 0
    ExcludeFilter = 1
    IncludeFilter = 2
    ExclusiveFilter = 3
    SelectFilter = 4
    ExclusiveSelectFilter = 5
    HighlightFilter = 6
    ExclusiveHighlightFilter = 7


class FilterWidgetAction():
    AddFilter = 0
    RemoveFilter = 1
    LockFilter = 2


class SearchStatus():
    Unknown = 0
    Found = 1
    NotFound = 2
