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
from gui.processwidget import *


class ProcessListWidget(QtWidgets.QWidget):
    
    def __init__(self):
        
        super(ProcessListWidget, self).__init__()
        
        uic.loadUi('gui/ProcessListWidget.ui', self)
        
        self.LoadProcessTypes()
        
        self.show()
        
        
        
        
    def LoadProcessTypes(self):
        
        
        
        ListOp = list(OperationType)
        
        # Adding the types of operations to the dropdown button list
        
        for Op in ListOp:
            tmpAction = QAction( Op.value[0], self )
            self.AddProcButton.addAction(tmpAction)
            tmpAction.ProcessType = Op
            tmpAction.triggered.connect(self.AddProcess)
            
    
    def AddProcess(self):
        
        self.ProcessList.removeWidget(self.Spacing)
        
        print(self.sender().ProcessType)
        
        pw = ProcessWidget()
        
        self.ProcessList.addWidget(pw)
        
        self.ProcessList.addWidget(self.Spacing)
        
            
            
        
        