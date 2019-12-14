#main program 
import sys
import gui_design
from PyQt5.QtWidgets import QApplication
def main():
	#Create an instance of QApplication
	app = QApplication(sys.argv)
	#show the calculator's GUI
	view = gui_design.PyCalc()
	view.show()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()