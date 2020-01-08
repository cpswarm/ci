

#
# MAIN
#
def main():
	root = session.getModel().getModelRoots().get(1)

	#
	attackTreePeerModule = Modelio.getInstance().getModuleService().getPeerModule("AttackTreeDesigner")
	assert attackTreePeerModule is not None, "attackTreePeerModule is None type"
	modelPackage = root.getModel().get(0)

	# testPackage
	testPackage = findPackage(modelPackage, "t07_Counter_Measure", "t07_23_Update_Undefined_Ref_to_countered_AND_Child")
	assert testPackage is not None, "testPackage is None type"

	testPackageOwnedElements = testPackage.getOwnedElement()
	tree = testPackageOwnedElements.get(0)
	tree1 = testPackageOwnedElements.get(1)

	if tree.getName() == "Tree1" :
		tree = testPackageOwnedElements.get(1)
		tree1 = testPackageOwnedElements.get(0)
	
	assert tree.getName() == "Tree", "Cannot find a tree with the name 'Tree', instead we found " + tree.getName()


	andNode = tree.getOwnedElement().get(0)
	andNodeOwnedElements = andNode.getOwnedElement()
	attack = andNodeOwnedElements.get(0)
	treeReference = andNodeOwnedElements.get(1)

	if treeReference.getName() == "Attack" :
		attack = andNodeOwnedElements.get(1)
		treeReference = andNodeOwnedElements.get(0)

	
	
	# Insert your test here
	t = session.createTransaction("create Counter Measure")

	attackTreePeerModule.updateReference(treeReference, "modelio_test_project/modelio_test_project/t07_Counter_Measure/t07_23_Update_Undefined_Ref_to_countered_AND_Child/Tree1")

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


