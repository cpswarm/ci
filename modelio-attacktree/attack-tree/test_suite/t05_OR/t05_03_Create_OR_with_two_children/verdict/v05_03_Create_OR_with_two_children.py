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


	# add your test here in testPackage
	testPackage = findPackage(modelPackage, "t05_OR", "t05_03_Create_OR_with_two_children")
	assert testPackage is not None, "testPackage is None type"


	tree = testPackage.getOwnedElement().get(0)
	assert tree.getName() == "Tree", "Cannot find a tree with the name 'Tree', instead we found " + tree.getName()

	diagrams = tree.getDiagramElement()
	diagram = diagrams.get(0)


	if(tree.getOwnedElement().isEmpty()):
		outputError("/errors_output/t05_03_Create_OR_with_two_children.err", "Expected to find OR node, instead we found only Root \n")
	else: 
		orNode = tree.getOwnedElement().get(0)
		if(orNode.getName() != "OR"):
			outputError("/errors_output/t05_03_Create_OR_with_two_children.err", "Expected to find node with the name 'OR', instead we found the name " + orNode.getName() + "\n")
		if(orNode.getMClass().getName() != "Class"):
			outputError("/errors_output/t05_03_Create_OR_with_two_children.err", "Expected to find a the meta class Class, instead we found " + orNode.getMClass().getName() + "\n")
		if(orNode.getExtension().get(0).getName() != "OR"):
			outputError("/errors_output/t05_03_Create_OR_with_two_children.err", "Expected to find a stereotype with the name 'OR', instead we found the name " + orNode.getExtension().get(0).getName() + "\n")
		diagramService = Modelio.getInstance().getDiagramService()
		diagramHandle = diagramService.getDiagramHandle(diagram)
		if(diagramHandle.getDiagramGraphics(orNode).isEmpty()) :
			outputError("/errors_output/t05_03_Create_OR_with_two_children.err", "The created OR node is not represented in the diagram !\n")
		
		if(orNode.getOwnedElement().isEmpty()):
			outputError("/errors_output/t05_03_Create_OR_with_two_children.err", "Expected to find children of 'OR' node \n")
		else :
			attack1 = orNode.getOwnedElement().get(0)
			attack2 = orNode.getOwnedElement().get(1)
			if(attack1.getExtension().get(0).getName() != "Attack"):
				outputError("/errors_output/t05_03_Create_OR_with_two_children.err", "Expected to find a stereotype with the name 'Attack', instead we found the name " + orNode.getExtension().get(0).getName() + "\n")
			if(attack2.getExtension().get(0).getName() != "Attack"):
				outputError("/errors_output/t05_03_Create_OR_with_two_children.err", "Expected to find a stereotype with the name 'Attack', instead we found the name " + orNode.getExtension().get(0).getName() + "\n")







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


