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
	testPackage = findPackage(modelPackage, "t00_import", "t00_02_import_tree")
	assert testPackage is not None, "testPackage is None type"

	tree1 = testPackage.getOwnedElement().get(0)
	if(package.getName() != "Tree1"):
		outputError("/errors_output/t00_02_import_tree.err", "Expected to find tree with the name 'Tree1', instead we found the name " + tree1.getName() + "\n")

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


