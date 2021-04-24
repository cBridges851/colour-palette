from PySide2 import QtWidgets, QtGui
import sys
from renderer import Renderer

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    """
        The class that is responsible for the application opening from 
        the system tray
    """
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip("Chrispy Colour Palette")
        menu = QtWidgets.QMenu(parent)

        # Context Menu
        open_colour_palette = menu.addAction("Open palette")
        open_colour_palette.triggered.connect(self.open_colour_palette_app)
        
        _exit = menu.addAction("Exit")
        _exit.triggered.connect(sys.exit)

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.double_click_icon)

    def double_click_icon(self, reason):
        """
            The method that is responsible for checking to see if the icon has 
            been double clicked on
            Args:
                reason: QSystemTrayIcon, why the method has been called as a result of the action
                        that has taken place
        """
        if reason == self.DoubleClick:
            self.open_colour_palette_app()

    def open_colour_palette_app(self):
        """
            Opens the colour palette application
        """
        Renderer().render()


def main():
    """
        Entry method for the application and puts the icon in the system tray.
    """
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("favicon.ico"), widget)
    tray_icon.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()