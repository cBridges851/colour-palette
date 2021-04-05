from PySide2 import QtWidgets, QtGui
import os
import sys
from renderer import Renderer

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip("Chrispy Colour Palette")
        menu = QtWidgets.QMenu(parent)

        # Context Menu
        open_colour_palette = menu.addAction("Open palette")
        open_colour_palette.triggered.connect(self.open_colour_palette_app)
        
        _exit = menu.addAction("Exit")
        _exit.triggered.connect(lambda: sys.exit())

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.double_click_icon)

    def double_click_icon(self, reason):
        if reason == self.DoubleClick:
            self.open_colour_palette_app()

    def open_colour_palette_app(self):
        Renderer().render()


def main():
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("favicon.ico"), widget)
    tray_icon.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()