import sys


#import QApplication and other required widgets

from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget

__version__ = '0.1'
__author__ = 'Ishwor Khanal'

#Create a subclass of QMainWindow to setup the calculator

class PyCalc(QMainWindow):

	def __init__(self):
		super().__init__()
		#Set window properties
		self.setWindowTitle('Calculator')
		self.setFixedSize(235,235)
		#set the central widget
		self._centralWidget = QWidget(self)
		self.setCentralWidget(self._centralWidget)

#Client Mode
def main():
	#Create an instance of QApplication
	pycalc = QApplication(sys.argv)
	#show the calculator's GUI
	view = PyCalc()
	view.show()
	sys.exit(pycalc.exec())


if __name__ == '__main__':
	main()
