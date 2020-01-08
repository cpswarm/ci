import os
import glob
from java.nio.file import Paths
from org.modelio.gproject.gproject import GProject

#
# MAIN
#
def main():
	root = session.getModel().getModelRoots().get(1)

	#
	attackTreePeerModule = Modelio.getInstance().getModuleService().getPeerModule("AttackTreeDesigner")
	assert attackTreePeerModule is not None, "attackTreePeerModule is None type"
	modelPackage = root.getModel().get(0)


	# testPackage
	testPackage = findPackage(modelPackage, "t07_Counter_Measure", "t07_22_Update_Undefined_Ref_to_countered_Root")
	assert testPackage is not None, "testPackage is None type"

	testPackageOwnedElements = testPackage.getOwnedElement()
	tree = testPackageOwnedElements.get(0)
	tree1 = testPackageOwnedElements.get(1)

	if tree.getName() == "Tree1" :
		tree = testPackageOwnedElements.get(1)
		tree1 = testPackageOwnedElements.get(0)
	
	assert tree.getName() == "Tree", "Cannot find a tree with the name 'Tree', instead we found " + tree.getName()

	andNode = tree.getOwnedElement().get(0)
	andNodeOwnedElements = andNode.getOwnedElement()
	attack = andNodeOwnedElements.get(0)
	treeRef = andNodeOwnedElements.get(1)
	if treeRef.getName() == "Attack" :
		attack = andNodeOwnedElements.get(1)
		treeRef = andNodeOwnedElements.get(0)



	diagrams = tree.getDiagramElement()
	diagram = diagrams.get(0)




	# Insert your test here


	# Verify Countered Tag value
	if tree.getTag("AttackTreeDesigner", "Attack", "Countered attack").getActual().get(0).getValue() != "true" :
		outputError("/errors_output/t07_22_Update_Undefined_Ref_to_countered_Root.err", 
		"Expected to find tree with the Countered attack having the value 'false', instead found  " + tree.getTag("AttackTreeDesigner", "Attack", "Countered attack").getActual().get(0).getValue() + "\n")
	if attack.getTag("AttackTreeDesigner", "Attack", "Countered attack").getActual().get(0).getValue() != "false" :
		outputError("/errors_output/t07_22_Update_Undefined_Ref_to_countered_Root.err", 
		"Expected to find attack with the Countered attack having the value 'false', instead found  " + attack.getTag("AttackTreeDesigner", "Attack", "Countered attack").getActual().get(0).getValue() + "\n")

	# Colors
	diagramService = Modelio.getInstance().getDiagramService()

	diagramHandle = diagramService.getDiagramHandle(diagram)
	if diagramHandle.getDiagramGraphics(tree).get(0).getFillColor() != "220,250,210" :
		outputError("/errors_output/t07_22_Update_Undefined_Ref_to_countered_Root.err", 
		"Expected tree to have color 220,250,210 ! Instead we found the color " + diagramHandle.getDiagramGraphics(tree).get(0).getFillColor() + "\n")

	if diagramHandle.getDiagramGraphics(attack).get(0).getFillColor() != "250,240,210" :
		outputError("/errors_output/t07_22_Update_Undefined_Ref_to_countered_Root.err", 
		"Expected attack to have color 250,240,210 ! Instead we found the color " + diagramHandle.getDiagramGraphics(attack).get(0).getFillColor() + "\n")
	
	if diagramHandle.getDiagramGraphics(treeRef).get(0).getFillColor() != "220,250,210" :
		outputError("/errors_output/t07_22_Update_Undefined_Ref_to_countered_Root.err", 
		"Expected treeRef to have color 220,250,210 ! Instead we found the color " + diagramHandle.getDiagramGraphics(treeRef).get(0).getFillColor() + "\n")

#
# findPackage function
#
def findPackage(modelPackage, parent_name, package_name):

	for package_i in modelPackage.getOwnedElement():
		if(package_i.getName()==parent_name):
			for package_j in package_i.getOwnedElement():
				if(package_j.getName()==package_name):
					return package_j
	return None

#
# outputError function
#
def outputError(errorFilePath, errorMessage):
	f= open(errorFilePath,"a+")
	f.write(errorMessage)
	f.close() 

######################################################################
main()


