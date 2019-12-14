ERROR_MSG = 'ERROR'
from functools import partial
from gui_design import *
#Controller class to connect the GUI and the model
class PyCalcCtrl:
	
	def __init__(self,model,view):
		#Controller initializer
		self._evaluate = model
		self._view = view
		#Connect the signals and the slots
		self._connectSignals()

	def _calculateResult(self):
		#Evaluate expressions
		result = self._evaluate(expression=self._view.displayText())
		self._view.setDisplayText(result)

	def _buildExpression(self,sub_exp):
		if self._view.displayText() == ERROR_MSG:
			self._view.clearDisplay()

		expression = self._view.displayText() + sub_exp
		self._view.setDisplayText(expression)

	def _connectSignals(self):
		for btnText,btn in self._view.buttons.items():
			if btnText not in {'=','C'}:
				btn.clicked.connect(partial(self._buildExpression,btnText))

		self._view.buttons['='].clicked.connect(self._calculateResult)
		self._view.display.returnPressed.connect(self._calculateResult)
		self._view.buttons['C'].clicked.connect(self._view.clearDisplay)

#Model to handle the calculator's operation
def evaluateExpression(expression):
	try:
		result = str(eval(expression, {}, {}))
	except Exception:
		result = ERROR_MSG
	return result