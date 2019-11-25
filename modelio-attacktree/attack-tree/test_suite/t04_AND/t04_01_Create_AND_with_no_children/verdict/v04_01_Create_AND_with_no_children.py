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
	testPackage = findPackage(modelPackage, "t04_AND", "t04_01_Create_AND_with_no_children")
	assert testPackage is not None, "testPackage is None type"


	tree = testPackage.getOwnedElement().get(0)
	assert tree.getName() == "Tree", "Cannot find a trrr with the name 'Tree', instead we found " + tree.getName()

	diagrams = tree.getDiagramElement()
	diagram = diagrams.get(0)


	if(tree.getOwnedElement().isEmpty()):
		outputError("/errors_output/t04_01_Create_AND_with_no_children.err", "Expected to find AND node, instead we found only Root \n")
	else: 
		andNode = tree.getOwnedElement().get(0)
		if(andNode.getName() != "AND"):
			outputError("/errors_output/t04_01_Create_AND_with_no_children.err", "Expected to find node with the name 'AND', instead we found the name " + andNode.getName() + "\n")
		if(andNode.getMClass().getName() != "Class"):
			outputError("/errors_output/t04_01_Create_AND_with_no_children.err", "Expected to find a the meta class Class, instead we found " + andNode.getMClass().getName() + "\n")
		if(andNode.getExtension().get(0).getName() != "AND"):
			outputError("/errors_output/t04_01_Create_AND_with_no_children.err", "Expected to find a stereotype with the name 'AND', instead we found the name " + andNode.getExtension().get(0).getName() + "\n")
		diagramService = Modelio.getInstance().getDiagramService()
		diagramHandle = diagramService.getDiagramHandle(diagram)
		if(diagramHandle.getDiagramGraphics(andNode).isEmpty()) :
			outputError("/errors_output/t04_01_Create_AND_with_no_children.err", "The created AND node is not represented in the diagram !\n")




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


