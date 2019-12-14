#Controller class to connect the GUI and the model
from functools import partial
from gui_design import *
class PyCalcCtrl:
	
	def __init__(self,view):
		#Controller initializer
		self._view = view
		#Connect the signals and the slots
		self._connectSignals()

	def _buildExpression(self,sub_exp):
		expression = self._view.displayText() + sub_exp
		self._view.setDisplayText(expression)

	def _connectSignals(self):
		for btnText,btn in self._view.buttons.items():
			if btnText not in {'=','C'}:
				btn.clicked.connect(partial(self._buildExpression,btnText))

		self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
	 