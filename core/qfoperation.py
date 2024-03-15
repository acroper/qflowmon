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
QFLOWMON/QFOPERATION

Defines the base operation class. 
Lists the type of operations.
Each operation/function inherents from this class

"""

from enum import Enum



class OperationType(Enum):
    # List the type of operations
    # Each element is a list: [ Name, Folder location ] 
    OrcaInput = ("Orca Input Generator", "OrcaInputGenerator")
    OrcaOutput = ("Orca Output Generator", "OrcaOutputGenerator")
    
    
    def GetOperation(optype):
        # optype: one operation type elemeent
        # Loads the object type according to the
        # operation type provided
        
        ModuleName = "Modules."+optype.value[1]+".qfoperation_module"
        OperationMod = None
        Operation = None
        Pass = True
        
        try:
            mod = __import__(ModuleName, fromlist=[''])
            OperationMod = mod
        
        except Exception as e:
            Pass = False
            print("Error loading module "+ optype.value[0])
            print(e)
            
        if Pass:
            Operation = OperationMod.qfoperation_module()
            
        return Operation
        
        
        
    
    

class QFOperation:
    
    def __init__(self):
        self.Type = None
    
    def Load(self):
        None


# Test code
# Operation = OperationType.GetOperation(OperationType.OrcaInput)
# if Operation != None:
#     Operation.test()
# else:
#     print("Test failed")