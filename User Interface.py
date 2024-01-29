import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton,QAction, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


def Button_Create(self, text, a ,b ):
    button = QPushButton(text, self)
    button.resize(200, 100)
    button.move(a, b)
    return button

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 tabs - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 1000
        self.height = 500
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()

class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.Making_Models = QWidget()
        self.Making_test = QWidget()
        self.tabs.resize(900, 400)

        # Add tabs
        self.tabs.addTab(self.Making_Models, "Making_Models")
        self.tabs.addTab(self.Making_test, "Making_Test")

        # Create first tab
        self.Making_Models.layout = QVBoxLayout(self)

        self.Model_button = Button_Create(self, "Create a Model", a=100, b=100)
        self.Model_button.resize(200, 100)
        self.Making_Models.layout.addWidget(self.Model_button)

        self.Model_button.clicked.connect(self.on_click_Model)


        self.Load_button = Button_Create(self, "Load a Model", a=500, b=100)
        self.Making_Models.layout.addWidget(self.Load_button)
        self.Load_button.clicked.connect(self.on_click_Model)

        self.Making_Models.setLayout(self.Making_Models.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    @pyqtSlot()
    def on_click_Model(self):
        print('PyQt5 button click')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())