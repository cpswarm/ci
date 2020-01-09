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
	testPackage = findPackage(modelPackage, "t09_Probability_Tag", "t09_09_Propagate_Probability_Update_OR_Child")
	assert testPackage is not None, "testPackage is None type"


	tree = testPackage.getOwnedElement().get(0)
	assert tree.getName() == "Tree", "Cannot find a tree with the name 'Tree', instead we found " + tree.getName()


	if(tree.getName() != "Tree"):
		outputError("/errors_output/t09_09_Propagate_Probability_Update_OR_Child.err", "Expected to find tree with the name 'Tree', instead we found the name " + tree.getName() + "\n")
	if tree.getTag("AttackTreeDesigner", "Attack", "Probability").getActual().get(0).getValue() != "HIGH" :
		outputError("/errors_output/t09_09_Propagate_Probability_Update_OR_Child.err", "Expected to find Probability Tag with the value 'HIGH', instead we found the value " + attack.getTag("AttackTreeDesigner", "Attack", "Probability").getActual().get(0).getValue() + "\n")



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


