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
	testPackage = findPackage(modelPackage, "t02_create_diagram", "t02_01_create_diagram")
	assert testPackage is not None, "testPackage is None type"

	tree = testPackage.getOwnedElement().get(0)
	if(tree.getName() != "Tree"):
		outputError("/errors_output/t02_01_create_diagram.err", "Expected to find tree with the name 'Tree', instead we found the name " + tree.getName() + "\n")

	diagram = tree.getOwnedElement().get(0)
	if(diagram.getName() != "Tree Diagram"):
		outputError("/errors_output/t02_01_create_diagram.err", "Expected to find diagram with the name 'Tree', instead we found the name " + diagram.getName() + "\n")

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


