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
from PyQt6.QtGui import QAction

from core.qfoperation import *
from gui.inputconfig import *


class ProcessWidget(QtWidgets.QWidget):
    
    def __init__(self):
        
        super(ProcessWidget, self).__init__()
        
        uic.loadUi('gui/ProcessWidget.ui', self)
        
        self.LoadModules()
              
        self.show()
        
    
    def LoadModules(self):
        
        print("Adding actions")
        
        self.InputConf = InputConfig()
        
        
        toct = QWidgetAction(self)
        
        toct.setDefaultWidget(self.InputConf)
        
        
        self.InputButton.addAction(toct)
        