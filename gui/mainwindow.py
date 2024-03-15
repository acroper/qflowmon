"""
QFLOWMON
Copyright (C) 2024  Mosquera Lab - Montana State University

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import os


from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal, QObject

from gui.processlistwidget import ProcessListWidget


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        
        super(MainWindow, self).__init__()

        uic.loadUi('gui/MainWindow.ui', self)
        
        self.loadPanels()
        
        self.show()
        
        
    def loadPanels(self):
        # Left panel
        None
        
        # Central panel
        
        self.InternalPanel = ProcessListWidget()
        self.CentralPanel.addWidget(self.InternalPanel)
        
        
        # Right panel
        

