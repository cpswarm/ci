

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
	assert tree.getName() == "Tree", "Cannot find a tree with the name 'Tree', instead we found " + tree.getName()

	diagrams = tree.getDiagramElement()
	diagram = diagrams.get(0)

	treeOwnedElement = tree.getOwnedElement()
	attackNode = treeOwnedElement.get(0)
	andNode = treeOwnedElement.get(1)

	if attackNode.getName() == "AND" :
		attackNode = treeOwnedElement.get(1)
		andNode = treeOwnedElement.get(0)



	t = session.createTransaction("Create Dependency")

	attackTreePeerModule.createConnection(andNode, attackNode, diagram)

	t.commit()

	coreSession.save(None)



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


