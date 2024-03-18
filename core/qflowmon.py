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

"""
QFLOWMON/CORE

Console project for the QFLOWMON, independent of the GUI.

"""

from .qfvars import QFVars


class QFlowmon:
    
    def __init__(self, Filename=""):
        # Creation of the Qflowmon object
        
        # Attributes
        # filename: external file to read
        # ActiveFile: indicates if the file was properly read
        # Variables: Generic variables generated in the different processes

        
        self.filename = Filename     
        
        self.ActiveFile = False 
        
        self.Variables = [] # List of variables
        
        self.ProcessList = []  # List of processes
        
        self.SelectedProcess = None
        
        
        # If a filename was provided, open it
        if self.filename != "":
            self.parseFile(self.filename)
        
    
    def parseFile(self, Filename):
        # Opens a QFlowmon file and reads its content.
        None
    
    def saveFile(self):
        # Saves a QFlowmon file to disk
        None
        
        
        
        