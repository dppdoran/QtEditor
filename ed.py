import sys
from PySide6 import QtWidgets


class Main(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.text = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text)
        self.toolbar = self.init_toolbar()
        self.addToolBarBreak()
        self.formatbar = self.init_format_bar()
        self.init_menubar()
        self.statusbar = self.statusBar()
        self.setGeometry(100, 100, 1030, 800)
        self.setWindowTitle("Qt Editor")

    def init_toolbar(self):
        toolbar = self.addToolBar("Options")
        return toolbar

    def init_format_bar(self):
        formatbar = self.addToolBar("Format")
        return formatbar

    def init_menubar(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec())