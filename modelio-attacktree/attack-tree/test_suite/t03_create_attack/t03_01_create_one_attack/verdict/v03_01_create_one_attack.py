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
	testPackage = findPackage(modelPackage, "t03_create_attack", "t03_01_create_one_attack")
	assert testPackage is not None, "testPackage is None type"


	tree = testPackage.getOwnedElement().get(0)
	assert tree.getName() == "Tree", "Cannot find a trrr with the name 'Tree', instead we found " + tree.getName()

	diagrams = tree.getDiagramElement()
	diagram = diagrams.get(0)

	attack = tree.getOwnedElement().get(0)

	if(attack.getName() != "Attack"):
		outputError("/errors_output/t03_01_create_one_attack.err", "Expected to find attack with the name 'Attack', instead we found the name " + attack.getName() + "\n")
	if(attack.getMClass().getName() != "Class"):
		outputError("/errors_output/t03_01_create_one_attack.err", "Expected to find a the meta class Class, instead we found " + attack.getMClass().getName() + "\n")
	if(attack.getExtension().get(0).getName() != "Attack"):
		outputError("/errors_output/t03_01_create_one_attack.err", "Expected to find a stereotype with the name 'Attack', instead we found the name " + attack.getExtension().get(0).getName() + "\n")

	diagramService = Modelio.getInstance().getDiagramService()
	diagramHandle = diagramService.getDiagramHandle(diagram)
	if(diagramHandle.getDiagramGraphics(attack).isEmpty()) :
		outputError("/errors_output/t03_01_create_one_attack.err", "The created attack is not represented in the diagram !\n")


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


