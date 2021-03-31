import pyqt5_tools
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from data.CharacterSheet import Ui_CreateCharacterWindow
from data.MainWindow import Ui_MainWindow
class CreateC(QMainWindow, Ui_CreateCharacterWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.CharacterNameLineEdit.textChanged.connect(self)

class MainWindow(QMainWindow, Ui_MainWindow):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CreateC()
    ex.show()
    sys.exit(app.exec_())