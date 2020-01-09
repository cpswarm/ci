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
	testPackage = findPackage(modelPackage, "t08_Severity_Tag", "t08_02_Default_Severity_Attack")
	assert testPackage is not None, "testPackage is None type"


	tree = testPackage.getOwnedElement().get(0)
	assert tree.getName() == "Tree", "Cannot find a trrr with the name 'Tree', instead we found " + tree.getName()

	diagrams = tree.getDiagramElement()
	diagram = diagrams.get(0)

	attack = tree.getOwnedElement().get(0)

	if(attack.getName() != "Attack"):
		outputError("/errors_output/t08_02_Default_Severity_Attack.err", "Expected to find attack with the name 'Attack', instead we found the name " + attack.getName() + "\n")
	if attack.getTag("AttackTreeDesigner", "Attack", "Severity").getActual().get(0).getValue() != "MEDIUM" :
		outputError("/errors_output/t08_02_Default_Severity_Attack.err", "Expected to find Severity Tag with the value 'MEDIUM', instead we found the value " + attack.getTag("AttackTreeDesigner", "Attack", "Severity").getActual().get(0).getValue() + "\n")



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


