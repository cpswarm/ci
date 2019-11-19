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
	testPackage = findPackage(modelPackage, "t00_import", "t00_01_import_package")
	assert testPackage is not None, "testPackage is None type"

	package = testPackage.getOwnedElement().get(0)
	if(package.getName() != "package"):
		outputError("/errors_output/t00_01_import_package.err", "Expected to find package with the name 'package', instead we found the name " + package.getName() + "\n")
	tree1 = package.getOwnedElement().get(0)
	if(tree1.getName() != "Tree1"):
		outputError("/errors_output/t00_01_import_package.err", "Expected to find tree with the name 'Tree1', instead we found the name " + tree1.getName() + "\n")
	tree2 = package.getOwnedElement().get(1)
	if(tree2.getName() != "haha2"):
		outputError("/errors_output/t00_01_import_package.err", "Expected to find tree with the name 'haha2', instead we found the name " + tree2.getName() + "\n")


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


