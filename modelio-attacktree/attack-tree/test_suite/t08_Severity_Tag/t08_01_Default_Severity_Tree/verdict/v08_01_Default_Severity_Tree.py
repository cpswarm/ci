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
	modelPackage = root.getModel().get(0)


	# add your test here in testPackage
	testPackage = findPackage(modelPackage, "t08_Severity_Tag", "t08_01_Default_Severity_Tree")
	assert testPackage is not None, "testPackage is None type"

	tree = testPackage.getOwnedElement().get(0)
	if(tree.getName() != "Tree"):
		outputError("/errors_output/t08_01_Default_Severity_Tree.err", "Expected to find tree with the name 'Tree', instead we found the name " + tree.getName() + "\n")
	
	if tree.getTag("AttackTreeDesigner", "Attack", "Severity").getActual().get(0).getValue() != "MEDIUM" :
		outputError("/errors_output/t08_01_Default_Severity_Tree.err", "Expected to find Severity Tag with the value 'MEDIUM', instead we found the value " + tree.getTag("AttackTreeDesigner", "Attack", "Severity").getActual().get(0).getValue() + "\n")


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


