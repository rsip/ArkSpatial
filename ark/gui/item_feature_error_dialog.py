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

from PyQt4.QtGui import QApplication, QDialog

from ArkSpatial.ark.lib.core import TableModel

from .ui.item_feature_error_dialog_base import Ui_ItemFeatureErrorDialog


class ItemFeatureErrorDialog(QDialog, Ui_ItemFeatureErrorDialog):

    def __init__(self, parent=None):
        super(ItemFeatureErrorDialog, self).__init__(parent)
        self.setupUi(self)

        self._errors = []
        self._model = None  # TableModel()
        self._ignore = False
        self._canIgnore = True

        fields = ['layer', 'row', 'field', 'message']
        nullRecord = {'layer': '', 'row': 0, 'field': '', 'message': ''}
        self._model = TableModel(fields, nullRecord)

        self.okButton.clicked.connect(self.accept)
        self.ignoreButton.clicked.connect(self._ignoreErrors)
        self.copyButton.clicked.connect(self._toText)
        self.csvButton.clicked.connect(self._toCsv)

    def loadErrors(self, errors):
        self._ignore = False
        self._canIgnore = True
        self._errors = errors
        self._model.clear()
        for error in errors:
            self._model.appendRecord(error.toDict())
            if error.ignore == False:
                self._canIgnore = False
        # TODO Temp disable for testing
        # self.ignoreButton.setEnabled(self._canIgnore)
        self.errorTable.setModel(self._model)
        self.errorTable.resizeColumnsToContents()

    def ignoreErrors(self):
        return self._ignore

    def _ignoreErrors(self):
        self._ignore = True
        self.accept()

    def _toText(self):
        txt = ''
        for error in self._errors:
            txt += error.toText() + '\n'
        QApplication.clipboard().setText(txt)
        self.accept()

    def _toCsv(self):
        csv = ''
        for error in self._errors:
            csv += error.toCsv() + '\n'
        QApplication.clipboard().setText(csv)
        self.accept()
