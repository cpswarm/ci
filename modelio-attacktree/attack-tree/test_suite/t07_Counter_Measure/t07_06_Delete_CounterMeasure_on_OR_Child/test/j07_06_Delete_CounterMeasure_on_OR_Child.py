

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
	testPackage = findPackage(modelPackage, "t07_Counter_Measure", "t07_06_Delete_CounterMeasure_on_OR_Child")
	assert testPackage is not None, "testPackage is None type"

	tree = testPackage.getOwnedElement().get(0)
	assert tree.getName() == "Tree", "Cannot find a tree with the name 'Tree', instead we found " + tree.getName()

	diagrams = tree.getDiagramElement()
	diagram = diagrams.get(0)


	# Insert your test here
	orNode = tree.getOwnedElement().get(0)

	orNodeOwnedElements = orNode.getOwnedElement()
	
	if orNodeOwnedElements.get(0).getName() == "Attack" :
		attack = orNodeOwnedElements.get(0)
		attack1 = orNodeOwnedElements.get(1)
	else :
		attack1 = orNodeOwnedElements.get(0)
		attack = orNodeOwnedElements.get(1)
		
	t = session.createTransaction("delete Counter Measure")

	attack1Note = attack1.getDescriptor().get(0)
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

