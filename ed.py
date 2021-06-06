import sys
from PySide6 import QtWidgets, QtGui


class Main(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.filename = ""
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
        self.new_action = QtGui.QAction(QtGui.QIcon("icons/new.png"), "New", self)
        self.new_action.setStatusTip("Create a new document from scratch")
        self.new_action.setShortcut(("Ctrl+N"))
        self.new_action.triggered.connect(self.new_file)

        self.open_action = QtGui.QAction(QtGui.QIcon("icons/open.png"), "Open file", self)
        self.open_action.setStatusTip("Open existing document")
        self.open_action.setShortcut(("Ctrl+O"))
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QtGui.QAction(QtGui.QIcon("icons/save.png"), "Save", self)
        self.save_action.setStatusTip("Save document")
        self.save_action.setShortcut(("Ctrl+S"))
        self.save_action.triggered.connect(self.save_file)

        toolbar = self.addToolBar("Options")
        toolbar.addAction(self.new_action)
        toolbar.addAction(self.open_action)
        toolbar.addAction(self.save_action)
        toolbar.addSeparator()
        return toolbar

    def init_format_bar(self):
        formatbar = self.addToolBar("Format")
        return formatbar

    def init_menubar(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")

    def new_file(self):
        spawn = Main(self)
        spawn.show()

    def save_file(self):
        print("Saving")

    def open_file(self):
        print("Opening")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec())