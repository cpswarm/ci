

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
	testPackage = findPackage(modelPackage, "t07_Counter_Measure", "t07_08_Delete_CM_Ref_Root_with_no_children")
	assert testPackage is not None, "testPackage is None type"

	testPackageOwnedElements = testPackage.getOwnedElement()
	tree = testPackageOwnedElements.get(0)
	tree1 = testPackageOwnedElements.get(1)

	if tree.getName() == "Tree1" :
		tree = testPackageOwnedElements.get(1)
		tree1 = testPackageOwnedElements.get(0)
	
	assert tree1.getName() == "Tree1", "Cannot find a tree with the name 'Tree1', instead we found " + tree1.getName()

	# Insert your test here
	t = session.createTransaction("create Counter Measure")

	attack1Note = tree1.getDescriptor().get(0)
	attack1Note.delete()

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


