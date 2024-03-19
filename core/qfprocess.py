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
QFLOWMON/QFProcess

Define one process for QFLOWMON.
Each process should have input variables, a defined operation, and an output.

"""

from .qfoperation import *

from enum import Enum

class ProcessStatus(Enum):
    IDLE = 1
    RUNNING = 2
    FINISHED = 3

class QFProcess:
    
    def __init__(self):
        # Define a process
        
        self.Input = None
        self.Operation = None
        self.Output = None
        
        self.ID = -1 # All process ID must be different
        
        self.Status = ProcessStatus.IDLE
        
        
    def SetOperation(self, processType):
        
        self.Operation = OperationType.GetOperation(processType)
        
        
        
