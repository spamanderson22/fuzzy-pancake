from cgenericitem import GenericItem

class ChaosMedJewel(GenericItem):
	
	#keyRing for RegEx needle and value for comparison with the threshold. Stores data as {Key:[Needle,Value]} 
	#Key - name of the affix
	#needle - RegEx string
	#Value - The size of the total affix, initialized to 0
	
	def __init__(self):
		GenericItem.__init__(self)

		self.itemLabel = "Chaos Medium Cluster Jewel"
		self.affixSectionNum = 4
		self.maxAffixes = 4
	
		#Notables
		#Wicked Pall
		self.desirableAffixesKeyring = {
			"Wicked Pall": {self.NEEDLE:"Pall",
							self.VALUE:0,
							self.THRESHOLD:1},
			"Exposure Therapy": {self.NEEDLE:"Therapy",
							self.VALUE:0,
							self.THRESHOLD:1},
			"Unwaveringly Evil": {self.NEEDLE:"Evil",
							self.VALUE:0,
							self.THRESHOLD:1},
			"Student of Decay": {self.NEEDLE:"Decay",
							self.VALUE:0,
							self.THRESHOLD:1},
		}
		self.affixLabelList = self.desirableAffixesKeyring.keys()

"""
		if(affixCode & (1 << 0)):
			self.keyRing.update({self.affixLabelList[0]:self.desirableAffixesKeyring[self.affixLabelList[0]]})
		if(affixCode & (1 << 1)):
			self.keyRing.update({self.affixLabelList[1]:self.desirableAffixesKeyring[self.affixLabelList[1]]})
		if(affixCode & (1 << 2)):
			self.keyRing.update({self.affixLabelList[2]:self.desirableAffixesKeyring[self.affixLabelList[2]]})
		if(affixCode & (1 << 3)):
			self.keyRing.update({self.affixLabelList[3]:self.desirableAffixesKeyring[self.affixLabelList[3]]})
"""
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
Added Small Passive Skills also grant: +22 to Evasion
Added Small Passive Skills also grant: +5% to Fire Resistance
1 Added Passive Skill is Wicked Pall
--------
Place into an allocated Small, Medium or Large Jewel Socket on the Passive Skill Tree. Added passives do not interact with jewel radiuses. Right click to remove from the Socket.
"""

"""
testItem = ChaosMedJewel()

testItem.updateItem(testItemString)

testItem.initKeyRing(15)
print(testItem.keyRing)
print(testItem.getItemRarity())
print(testItem.countGoodAffixes())
print(testItem.countAffixes())
testItem.getAffixLabels()
print(testItem.affixLabelList)
print(testItem.keyRing.keys())
"""