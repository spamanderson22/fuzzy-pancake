class GenericCraftingMaterial:

	def __init__(self, givenName, qty):
		self.name = givenName
		self.position = []
		self.quantityUsed = 0
		self.totalQuantity = qty

	def setItemLocation(self, itemPosList):
		self.position = itemPosList

	def getItemLocation(self):
		return self.position