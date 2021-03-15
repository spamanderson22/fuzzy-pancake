import re #Imports regular expressions

class GenericItem:

	#affixLabelList = []

	def __init__(self):

		self.itemClipboardString = ""	#Stores clipboard string of item to be referenced
		self.itemPos = []
		self.itemLabel = ""				#Item name/description as displayed in GUI window
		self.numTotalAffixes = -1
		self.numThresholdValue = -1		#Threshold value equal to or above which the affix counts as good
		self.maxAffixes = -1			#Maximum number of available affixes possible on item
		self.DELIMITERTEXT = "\n--------\n"
		self.NEEDLE = "Needle"			#Key for RegEx needle
		self.VALUE = "Value"			#Key for Affix numerical value
		self.THRESHOLD = "Threshold"	#Key for threshold to conside affix "good"
		self.desirableAffixesKeyring = {}#Dictionary containing all desirable affixes which will be used to create keyRing
										#Stored as {"Name":{ENEEDLENAME:"RegEx Needle",VALUENAME:value,THRESHOLDNAME:value}}
		self.keyRing = {}
		"""
		keyName[Needle] - RegEx string to find it
		keyName[1] - value of affix on item (initialized to 0)
		keyName[2] - value of thresold for item to count (initialized to 1)
		self.affixSectionNum = 0#Section in item of affixes, between DELIMITERTEXT
		"""
		#self.affixString = ""#Multi-line string of affixes
		self.affixLabelList = []#List of affixes that are acceptable to craft
		self.affixStringList = []#List of affixes in item

	def getAffixSection(self, itemText, sectionNum):
	#Gets the section of the item text with affixes
		itemText = itemText.split(self.DELIMITERTEXT)
		sectionText = itemText[sectionNum]
		self.affixStringList = sectionText.splitlines()

	def updateItem(self, itemClipboard):
	#Updates the fields from a string passed
		self.itemClipboardString = itemClipboard
		self.getAffixSection(self.itemClipboardString, self.affixSectionNum)
		self.numTotalAffixes = self.countAffixes()


	def checkAffixPresent(self, linesToParse, needleString):
	#Uses RegEx to extract information from a multi-line block of text and returns the total value
		for line in linesToParse:
			outputValue = re.search(needleString, line)
			if(outputValue):
				return True
		return False
	
	def removeKey(self,keyName):
	#Removes key-value pairs from keyRing
		del self.keyRing[keyName]

	def countAffixes(self):
	#counts the number of affixes from 
	#returns number of affixes
		return len(self.affixStringList)

	def countGoodAffixes(self):
	#counts the number of desirable affixes present in the item by looking at a RegEx
	#returns the number of good affixes
		numGoodAfixes = 0
		for lookupKey in self.keyRing:
			if(self.checkAffixPresent(self.affixStringList, self.keyRing[lookupKey][self.NEEDLE])):
				numGoodAfixes += 1
		return numGoodAfixes

	def initKeyRing(self,affixCode):
	#sets up keyRing according to checkboxes when called.
	#returns nothing but modifies keyRing by adding the values
		for loopCounter, possibleAffix in enumerate(self.affixLabelList):
			if(affixCode & (1 << loopCounter)):
				self.keyRing.update({possibleAffix:self.desirableAffixesKeyring[possibleAffix]})

	def setItemLocation(self, xPos, yPos):
		self.itemPos = [xPos,yPos]

	def getItemLocation(self):
		return self.itemPos

	def getModValues(self):
	#gets the values from the item text and fills in the values for the respective mods.
	#returns nothing but modifies keyRing by adding the values
		pass

	def getAffixLabels(self):
	#Gets affix values from keyRing which will be used to display in the GUI
		return self.affixLabelList

	def getItemRarity(self):
	#When given an item's clipboard, will return the rarity as a string
		normalRarity = "Normal"
		magicRarity = "Magic"
		rareRarity = "Rare"
		uniqueRarity = "Unique"
		rarityNeedle = "Rarity: .*"
		rarityText = re.match(rarityNeedle,self.itemClipboardString).group()
		if(normalRarity in rarityText):
			return normalRarity
		elif(magicRarity in rarityText):
			return magicRarity
		elif(rareRarity in rarityText):
			return rareRarity
		elif(uniqueRarity in rarityText):
			return uniqueRarity