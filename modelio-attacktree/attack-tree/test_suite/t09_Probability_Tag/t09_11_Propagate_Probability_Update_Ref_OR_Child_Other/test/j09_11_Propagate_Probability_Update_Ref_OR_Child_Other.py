

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
	testPackage = findPackage(modelPackage, "t09_Probability_Tag", "t09_11_Propagate_Probability_Update_Ref_OR_Child_Other")
	assert testPackage is not None, "testPackage is None type"


	tree = testPackage.getOwnedElement().get(0)
	assert tree.getName() == "Tree", "Cannot find a tree with the name 'Tree', instead we found " + tree.getName()
	
	andNodeChildren = tree.getOwnedElement().get(0).getOwnedElement()
 	attack =andNodeChildren.get(0)
 	treeRef =andNodeChildren.get(1)

	if attack.getName() != "Attack" :
		attack =andNodeChildren.get(1)
 		treeRef =andNodeChildren.get(0)


	t = session.createTransaction("create an attack")
	attackTreePeerModule.updateReference(treeRef, "modelio_test_project/modelio_test_project/t09_Probability_Tag/t09_11_Propagate_Probability_Update_Ref_OR_Child_Other/Tree2")
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


