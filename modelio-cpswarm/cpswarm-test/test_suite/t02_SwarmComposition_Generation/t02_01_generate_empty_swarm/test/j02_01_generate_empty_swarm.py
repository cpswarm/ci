

#
# MAIN
#
def main():
	root = session.getModel().getModelRoots().get(1)

	#
	cpswarmPeerModule = Modelio.getInstance().getModuleService().getPeerModule("CPSWarm")
	assert cpswarmPeerModule is not None, "CPSWarm is None type"
	modelPackage = root.getModel().get(0)


	# add your test here in testPackage
	testPackage = findPackage(modelPackage, "t02_SwarmComposition_Generation", "t02_01_generate_empty_swarm")
	assert testPackage is not None, "testPackage is None type"

	swarm1 = testPackage.getOwnedElement().get(0)
	assert swarm1.getName() == "Swarm1" , "Expected name Swarm1"
	
	cpswarmPeerModule.generateSwarmComposition(swarm1)




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


