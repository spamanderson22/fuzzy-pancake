class GenericItem:
	numTotalAffixes = -1
	numTotalGoodAffixes = -1
	numThresholdValue = -1

	itemPos = []

	def __init__(self, xPos, yPos):
		self.itemPos = [xPos,yPos]