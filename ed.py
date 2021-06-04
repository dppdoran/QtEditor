import sys
from PySide6 import QtWidgets

class Main(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 1030, 800)
        self.setWindowTitle("Qt Editor")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec())