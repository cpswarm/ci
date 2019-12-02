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
	testPackage = findPackage(modelPackage, "t07_Counter_Measure", "t07_02_Delete_CounterMeasure_on_Root")
	assert testPackage is not None, "testPackage is None type"

	tree = testPackage.getOwnedElement().get(0)
	assert tree.getName() == "Tree", "Cannot find a trrr with the name 'Tree', instead we found " + tree.getName()

	diagrams = tree.getDiagramElement()
	diagram = diagrams.get(0)



	# Insert your test here
	
	# Verify if tree has notes
	if not tree.getDescriptor().isEmpty():
		outputError("/errors_output/t07_02_Delete_CounterMeasure_on_Root.err", "Expected to tree with no notes \n")

	# Verify Countered Tag value
	if tree.getTag("AttackTreeDesigner", "Attack", "Countered attack").getActual().get(0).getValue() != "false" :
		outputError("/errors_output/t07_02_Delete_CounterMeasure_on_Root.err", "Expected to find tree with the Countered attack having the value 'false', instead found  " + tree.getTag("AttackTreeDesigner", "Attack", "Countered attack").getActual().get(0).getValue() + "\n")

	# Color of Tree
	diagramService = Modelio.getInstance().getDiagramService()
	diagramHandle = diagramService.getDiagramHandle(diagram)
	treeGraphicNode = diagramHandle.getDiagramGraphics(tree).get(0)
	if treeGraphicNode.getFillColor() != "250,240,210" :
		outputError("/errors_output/t07_02_Delete_CounterMeasure_on_Root.err", "Expected tree to have color 250,240,210 ! Instead we found the color " + treeGraphicNode.getFillColor() + "\n")


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


