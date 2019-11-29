

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
	testPackage = findPackage(modelPackage, "t05_OR", "t05_04_Create_OR_with_three_children")
	assert testPackage is not None, "testPackage is None type"


	tree = testPackage.getOwnedElement().get(0)
	assert tree.getName() == "Tree", "Cannot find a tree with the name 'Tree', instead we found " + tree.getName()

	diagrams = tree.getDiagramElement()
	diagram = diagrams.get(0)

	attack1 = tree.getOwnedElement().get(0)
	attack2 = tree.getOwnedElement().get(1)
	attack3 = tree.getOwnedElement().get(2)

	t = session.createTransaction("create OR")

	orNode = attackTreePeerModule.createORChild(tree,diagram)
	attackTreePeerModule.createConnection(orNode, attack1, diagram)
	attackTreePeerModule.createConnection(orNode, attack2, diagram)
	attackTreePeerModule.createConnection(orNode, attack3, diagram)

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


