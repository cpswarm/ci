

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
	testPackage = findPackage(modelPackage, "t08_Severity_Tag", "t08_14_Propagate_Severity_Delete_Grand_Child")
	assert testPackage is not None, "testPackage is None type"


	tree = testPackage.getOwnedElement().get(0)
	assert tree.getName() == "Tree", "Cannot find a tree with the name 'Tree', instead we found " + tree.getName()
	
	orNodeChildren = tree.getOwnedElement().get(0).getOwnedElement()
	attack1 =orNodeChildren.get(0)
	attack2 =orNodeChildren.get(1)

	orNode2Children = attack2.getOwnedElement().get(0).getOwnedElement()
	
	attack5 = orNode2Children.get(0)
	for child in orNode2Children :
		if child.getName() == "Attack5" :
			attack5 = child
	
	t = session.createTransaction("delete attack")
	attack5.delete()
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


