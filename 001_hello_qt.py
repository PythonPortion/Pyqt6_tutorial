# -*- coding: utf-8 -*-
"""
@Project : Pyqt6_tutorial
@File    : 001_hello_qt
@Author  : lingxiao
@Date    : 2026-05-06 13:05
@License : (C) Copyright 2026 Ling Xiao. All Rights Reserved.
"""

# ... existing code ...
'''
- What is Qt?
    Qt is a framework coded in C++ that is used for developing GUI application.
    It allows developers to write code once and deploy it across multiple platforms.
    
- What is PyQt?
    PyQt is a bridge between Python and Qt. Generally, we can regard it as a binding module/
'''

import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

if __name__ == '__main__':
    # 1 - It is the entry point of the application.
    app = QApplication([])

    # 2 - Create a window

    # act as window of the app
    window = QWidget()

    # set window title
    window.setWindowTitle('Hello Qt')

    # set geometry location on the screen
    window.setGeometry(100, 100, 300, 200)

    # create a label
    label = QLabel('Hello, Qt!', parent=window)
    label.move(10, 10)

    # 3 - Show the window
    window.show()

    # 4 - Run the application: Run the event loop
    sys.exit(app.exec())



"""
From the above code, we can see the app and the window do not linked directly via explict code.
Instead, they work together through PyQt6's internal architecture:

1. QApplication as the foundation.
    - QApplication manages the application-wide resources and settings
        - it controls the event loop(the main loop that handles user interactions)
        - There should be only one QApplication instance per application.

2. QWidget as a Managed Widget
    - When you call `window.show()`, PyQt6 automatically registers this widget with the QApplication
    - The QApplication
"""

