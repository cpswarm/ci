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
	testPackage = findPackage(modelPackage, "t06_Connection_Dependency", "t06_03_Create_Dep_Root_AND_Attack")
	assert testPackage is not None, "testPackage is None type"


	tree = testPackage.getOwnedElement().get(0)
	assert tree.getName() == "Tree", "Cannot find a trrr with the name 'Tree', instead we found " + tree.getName()

	diagrams = tree.getDiagramElement()
	diagram = diagrams.get(0)


	dependency = tree.getDependsOnDependency().get(0)
	andNode = dependency.getDependsOn()

	if andNode.getDependsOnDependency().size() != 2 :
		outputError("/errors_output/t06_03_Create_Dep_Root_AND_Attack.err", "Expected to find AND node with 2 outggoing dependencies, instead found : " + andNode.getDependsOnDependency().size() +  " \n")

	if tree.getOwnedElement.size() != 1 :
		outputError("/errors_output/t06_03_Create_Dep_Root_AND_Attack.err", "Expected to find Tree node with one node child, instead found : " + tree.getOwnedElement.size() +  " \n")


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


