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
from core.qfoperation import *


class qfoperation_module(QFOperation):
    
    
    
    def __init__(self):
        print("Starting operation class in Orca Input Generator")
        super().__init__()
        
        self.Load()
        
    
    def test(self):
        print("Testing from Orca Input Module")



