import time
import pyautogui
import pyperclip
from cgenericcraftmat import GenericCraftingMaterial

from cgenericitem import GenericItem
from cchaosmedjewel import ChaosMedJewel

class ChaosCrafting:

	alcOrb = GenericCraftingMaterial("Orb of Alchemy", 1)
	chaosOrb = GenericCraftingMaterial("Chaos Orb", 2)
	exaltOrb = GenericCraftingMaterial("Exalt Orb", 6)
	vaalOrb = GenericCraftingMaterial("Vaal Orb", 1)

	numNeedAffixes = 4
	numMinDesirableAffix = 2

	pGUI = pyautogui

	def __init__(self, itemPassed):
		self.itemToCraft = itemPassed
		self.setCurrencyPositions(itemPassed.getItemLocation())
		self.craftItem()

	def setCurrencyPositions(self, positionalList):
		"""
		Assigns positions of the currencies with reference to the item being crafted
		Assumes item is selected in top-right corner
		"""
		smallGap = 50#50 pixel spacing of boxes
		largeGap = 150#gap between item and 1st crafting column
		self.alcOrb.position = [positionalList[0] + largeGap, positionalList[1]] 
		self.chaosOrb.position = [positionalList[0] + largeGap, positionalList[1] + smallGap]#1 space below alc
		self.exaltOrb.position = [positionalList[0] + largeGap, positionalList[1] + 2*smallGap]#2 spaces below alc
		self.vaalOrb.position = [positionalList[0] + largeGap + smallGap, positionalList[1] + smallGap]#1 space below, 1 space right alc



	def craftItem(self):
		"""
		Performs one iteration of crafting and returns a flag of whether the item is finished or not.
		"""
		normalRarity = "Normal"
		rareRarity = "Rare"
		flagFinished = False
		self.mouseGoto(self.itemToCraft.itemPos)
		itemRarity = self.itemToCraft.getItemRarity()
		#self.pGUI.keyDown('shift')

		for chaosCount in range(self.chaosOrb.totalQuantity):
			print("Crafting!")
			if(self.chaosOrb.quantityUsed == self.chaosOrb.totalQuantity):
				flagFinished = True
			if((itemRarity == rareRarity) & (flagFinished == False)):
				#apply Chaos orb
				self.applyCurrency(self.chaosOrb.getItemLocation(),self.itemToCraft.getItemLocation())
			if((itemRarity == normalRarity) & (flagFinished == False)):
				#apply Alc orb
				self.applyCurrency(self.alcOrb.getItemLocation(),self.itemToCraft.getItemLocation())
			self.copyToClipboard()
			#self.itemToCraft.updateItem(self.readClipboard())

			if(self.itemToCraft.countGoodAffixes() >= self.numMinDesirableAffix):
			#If number of good affixes > (2)
				flagFinished = True
				if(self.itemToCraft.numTotalAffixes < self.numNeedAffixes):
				#Check if open affixes available
				#if so, apply exalt
					self.applyCurrency(self.exaltOrb.getItemLocation(),self.itemToCraft.getItemLocation())

		#self.pGUI.keyUp('shift')

		return flagFinished

	def applyCurrency(self,currencyPositionList, itemPositionList):
		rightButton = "right"
		leftButton = "left"
		self.mouseGoto(currencyPositionList)
		self.pGUI.click(button=rightButton)
		time.sleep(0.01)
		self.pGUI.click(button=rightButton) #need to double-click if holding shift
		self.mouseGoto(itemPositionList)
		self.pGUI.click(button=leftButton)

	def mouseGoto(self, posList):
		"""
		Moves mouse to specified location. Program will halt until move completes.
		"""
		moveTime = 1#time to move, secnds
		self.pGUI.moveTo(posList[0],posList[1], duration=moveTime)

	def copyToClipboard(self):
		pyperclip.copy('')
		while(pyperclip.paste()):
			time.sleep(0.01)
		self.pGUI.hotkey('ctrl','c')

	def readClipboard(self):
		return pyperclip.paste()


#moveTo(x,y,t) tbreleases key
#pyperclip.copy('sumtext')
#pyperclip.paste()


testItemString = """Rarity: Rare
Glyph Spark
Small Cluster Jewel
--------
Requirements:
Level: 54
--------
Item Level: 74
--------
Adds 3 Passive Skills (enchant)
Added Small Passive Skills grant: 4% increased maximum Life (enchant)
--------
Added Small Passive Skills also grant: +4% to Chaos Resistance
1 Added Passive Skill is Unwaveringly Evil 
1 Added Passive Skill is Wicked Pall
--------
Place into an allocated Small, Medium or Large Jewel Socket on the Passive Skill Tree. Added passives do not interact with jewel radiuses. Right click to remove from the Socket.
"""
"""
testItem = ChaosMedJewel()
testItem.setItemLocation(200,200)
testItem.initKeyRing(15)
testClass = ChaosCrafting(testItem)
testItem.updateItem(testItemString)
print(testClass.craftItem())
"""