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

from gui.guidialogs import *

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, MainProject):
        
        super(MainWindow, self).__init__()

        uic.loadUi('gui/MainWindow.ui', self)
        
        self.MainProject = MainProject
        
        self.setMenuActions()
        
        self.loadPanels()
        
        self.show()
        
    
    def setMenuActions(self):
        # Assign actions for the GUI menu
        
        
        
        # close
        self.actionQuit.triggered.connect(self.closing)
        self.actionOpen_Project.triggered.connect(self.showOpenProject)
        
       
    
    
    def loadPanels(self):
        # Left panel
        None
        
        # Central panel
        
        self.InternalPanel = ProcessListWidget()
        self.CentralPanel.addWidget(self.InternalPanel)
        
        # Assign mainproject
        self.InternalPanel.MainProject = self.MainProject
        
        # Right panel
        
        
    def showOpenProject(self):
        
        filename = openFileNameDialog(self, "", "Project files | *.txt (*.txt)")
        
        if filename != "":
            self.openProject(filename)
            
        
    
        
    
    def openProject(self, filename):
        ### Restart the GUI and loads the new project
        
        # Opens the project file
        
        self.MainProject.readFile(filename)
        self.InternalPanel.LoadProject()
    
    
    ### Check how to improve to ask to save the file
    def closeEvent(self, event):
        print("Closing")
        QApplication.instance().quit()
        
    def closing(self):
        # First ask about to quit
        print("Quitting...")
        QApplication.instance().quit()
        
        

