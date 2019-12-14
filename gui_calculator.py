import sys


#import QApplication and other required widgets

from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout,QLineEdit,QPushButton,QVBoxLayout



__version__ = '0.1'
__author__ = 'Ishwor Khanal'

#Create a subclass of QMainWindow to setup the calculator

class PyCalc(QMainWindow):

	def __init__(self):
		super().__init__()
		#Set window properties
		self.setWindowTitle('Calculator')
		self.setFixedSize(235,235)
		#set the central widget and general layout
		self.generalLayout = QVBoxLayout()
		self._centralWidget = QWidget(self)
		self.setCentralWidget(self._centralWidget)
		self._centralWidget.setLayout(self.generalLayout)
		#Create the display and the buttonss
		self._createDisplay()
		self._createButtons()

	def _createDisplay(self):
		#Create the display widget
		self.display = QLineEdit()
		#Set some display's properties
		self.display.setFixedHeight(35)
		self.display.setAlignment(Qt.AlignRight)
		self.display.setReadOnly(True)
		#Add the display to general layout
		self.generalLayout.addWidget(self.display)

	def _createButtons(self):
		self.buttons = {}
		buttonsLayout = QGridLayout()
		#Button text | position on the QGridLayout
		buttons = {'7' : (0,0),
				   '8' : (0,1),
				   '9' : (0,2),
				   '/' : (0,3),
				   'C' : (0,4),
				   '4' : (1,0),
				   '5' : (1,1),
				   '6' : (1,2),
				   '*' : (1,3),
				   '(' : (1,4),
				   '1' : (2,0),
				   '2' : (2,1),
				   '3' : (2,2),
				   '-' : (2,3),
				   ')' : (2,4),
				   '0' : (3,0),
				   '00': (3,1),
				   '.' : (3,2),
				   '+' : (3,3),
				   '=' : (3,4)
				  }
		#Create the buttons and add them to grid layout
		for btnText,pos in buttons.items():
			self.buttons[btnText] = QPushButton(btnText)
			self.buttons[btnText].setFixedSize(40,40)
			buttonsLayout.addWidget(self.buttons[btnText],pos[0],pos[1])
			#Add the buttonsLayout to the general Layout
			self.generalLayout.addLayout(buttonsLayout)
    
    #Set display's text
	def setDisplayText(self,text):
		self.display.setText(text)
		self.display.setFocus()

	#Get display's text
	def displayText(self):
		return self.display.text()

	#Clear the display
	def clearDispaly(self):
		self.setDisplayText('')

#Client Mode
def main():
	#Create an instance of QApplication
	app = QApplication(sys.argv)
	#show the calculator's GUI
	view = PyCalc()
	view.show()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()
