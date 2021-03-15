import sys

from cchaosmedjewel import ChaosMedJewel
from cchaoscrafting import ChaosCrafting

#import pygetwindow as gw

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QComboBox

import pyperclip

class Dialog(QDialog):
    """Dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)

        self.itemTypeList = []#List of item types shown in dropdown menu that can be crafted
        self.itemTypeList.append(ChaosMedJewel())

        layout = QFormLayout()
        self.comboBox = self.setupComboBox(self.itemTypeList)

        self.setWindowTitle('QDialog')
        self.dlgLayout = QVBoxLayout()#Defines elements will be stacked vertically
        self.formLayout = QFormLayout()#Defines sub-elements will be 2 wide "forms" (i.e. text - witdget pairs)
        self.buttonLayout = QHBoxLayout()#Defines elements will be stacked horizontally

        
        self.dlgLayout.addWidget(self.comboBox)

        currItem = self.findItemClassByDescription(self.comboBox.currentText())

        self.dlgLayout.addLayout(self.formLayout)
       
        cancelButton = QDialogButtonBox()
        cancelButton.setStandardButtons(QDialogButtonBox.Cancel)
        okButton = QDialogButtonBox()
        okButton.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonLayout.addWidget(cancelButton)
        self.buttonLayout.addWidget(okButton)

        self.dlgLayout.addLayout(self.buttonLayout)

        self.setLayout(self.dlgLayout)

        cancelButton.clicked.connect(self.closeWindow)
        okButton.clicked.connect(self.startCrafting)

    def closeWindow(self):
        self.close()

    def startCrafting(self):
        craftingCode = self.getCraftingCode(self.formLayout)
        itemToCraft = ChaosMedJewel()
        itemToCraft.setItemLocation(580,426) #Approximate location

        itemToCraft.updateItem(pyperclip.paste()) #Requires item copied to clipboard - need to look into changing

        craftingScript = ChaosCrafting(itemToCraft)
        self.close()


    def getCraftingCode(self, layout):
        outputVar = 0
        for rowNum in range(self.formLayout.rowCount()):    #Need to add widget in order to find state?
            if (layout.itemAt(rowNum).widget().isChecked()):
                outputVar = outputVar | 1 << rowNum
        return outputVar
        

    def selectionChanged(self):
    #Updates the list of items when a new selection is made in the comboBox
        #First need to remove old text + checkboxes
        for rowNum in range(self.formLayout.rowCount()):
            self.formLayout.removeRow(0)
        #Now fill in new text + checkboxes
        currentItem = self.findItemClassByDescription(self.comboBox.currentText())
        if(currentItem):#For default case, otherwise brings up an error since it is a string
            affixBoxes = self.setupAffixBoxes(currentItem.getAffixLabels())
            for affixBox in affixBoxes:
                self.formLayout.addRow(affixBoxes[affixBox])

            #setupAffixBoxes(affixList)

    def findItemClassByDescription(self,itemDescription):
    #Searches all classes in drop-down menu for matching description
    #itemDescription - String from class.itemLabel
    #Returns the class with the correct itemLabel
        for itemType in self.itemTypeList:
            if(itemType.itemLabel == itemDescription):
                return itemType

    def setupComboBox(self, craftableItemList):
    #Sets up dropdown list to include various items that can be crafted
    #Returns a combobox with available
        cb = QComboBox()
        cb.addItem("--Select an item--")
        for item in craftableItemList:
            cb.addItem(item.itemLabel)
        cb.currentIndexChanged.connect(self.selectionChanged)
        return cb

    def setupAffixBoxes(self,desirableAffixList):
    #Creates the checkboxes and text for affixes to be selected
    #Returns a dictionary with an affix text-checkbox combination
        textAndBoxDict = {}
        for affix in desirableAffixList:
            textAndBoxDict[affix]=QCheckBox(affix, self)
            #textAndBoxDict[affix].stateChanged.connect() #disabled - not check at time of check but including for reference if needed
        return textAndBoxDict





if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())