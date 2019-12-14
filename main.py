#main program 
import sys
import gui_design
import controller
from PyQt5.QtWidgets import QApplication
def main():
	#Create an instance of QApplication
	app = QApplication(sys.argv)
	#show the calculator's GUI
	view = gui_design.PyCalc()
	view.show()
	#Create the instance of the model and the controller
	model = controller.evaluateExpression
	controller.PyCalcCtrl(model=model,view=view)
	sys.exit(app.exec())


if __name__ == '__main__':
	main()