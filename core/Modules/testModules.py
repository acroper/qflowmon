"""
Test modules

Use this file as example to test the modules compatibles with QFlowMon.
This file is in between the hierarchy, and uses the path to associate the 
modules references the way they will be called from the GUI
"""
import sys
import os


sys.path.insert(0, "../../")   ### Relative folder imports

from core.qflowmon import *

from core.qfoperation import *

from core.Modules.OrcaInputGenerator.qfoperation_module import *



# Orca input module
# Little bit loud but reached to the internal modules

orcainput = OperationType.GetOperation(OperationType.OrcaInput)







