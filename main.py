# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
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
QFLOWMON
Describe the functionality of the software
"""


from PyQt6 import QtWidgets
from gui.mainwindow import *



# Launching GUI
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.aboutToQuit.connect(app.deleteLater)
app.exec()