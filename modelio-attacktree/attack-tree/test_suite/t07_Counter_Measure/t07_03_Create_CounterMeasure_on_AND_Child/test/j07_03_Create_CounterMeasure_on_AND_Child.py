

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
	testPackage = findPackage(modelPackage, "t07_Counter_Measure", "t07_03_Create_CounterMeasure_on_AND_Child")
	assert testPackage is not None, "testPackage is None type"

	tree = testPackage.getOwnedElement().get(0)
	assert tree.getName() == "Tree", "Cannot find a tree with the name 'Tree', instead we found " + tree.getName()

	diagrams = tree.getDiagramElement()
	diagram = diagrams.get(0)


	# Insert your test here
	andNode = tree.getOwnedElement().get(0)

	andNodeOwnedElements = andNode.getOwnedElement()
	
	if andNodeOwnedElements.get(0).getName() == "Attack" :
		attack = andNodeOwnedElements.get(0)
		attack1 = andNodeOwnedElements.get(1)
	else :
		attack1 = andNodeOwnedElements.get(0)
		attack = andNodeOwnedElements.get(1)

	t = session.createTransaction("create Counter Measure")

	attackTreePeerModule.createCounterMeasure(attack, diagram)

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


