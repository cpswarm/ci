import os
import glob
from java.nio.file import Paths
from org.modelio.gproject.gproject import GProject

#
# MAIN
#
def main():
	root = session.getModel().getModelRoots().get(1)
	gproject =  GProject.getProject(root)

	# Deploy Module (JMDAC File)
	module_jmdac_path = "./module_jmdac_archives"
	moduleArchivePattern = os.path.join(module_jmdac_path, "AttackTreeDesigner_*.jmdac")
	moduleArchives = glob.glob(moduleArchivePattern)
	Modelio.getInstance().getModuleService().installModule(gproject, Paths.get(moduleArchives[0]))
	
	# test if module deployed correctly
	attackTreeDesignerModule =findModule("AttackTreeDesigner")
	if attackTreeDesignerModule is None :
		print("Tested module: not found. ABORT! <br/>")
		return 1
	else:
		print("Module AttackTreeDesigner found")

	
	modelPackage = root.getModel().get(0)





	attackTreePeerModule = Modelio.getInstance().getModuleService().getPeerModule("AttackTreeDesigner")


	attackTreePeerModule.importModel(modelPackage, "./testsuite_XML_trees/test_attacktrees4")

	t = session.createTransaction("transaction 1")
	modelPackage.getOwnedElement().get(0).setName("hihi3")

	t.commit()

	assert modelPackage.getOwnedElement().get(0).getName() == "hihi3", "Error"

	attackTreePeerModule.exportModel(modelPackage, "./generated_trees")




#
# findModule function
#
def findModule(name):
	for module in Modelio.getInstance().getModuleService().getAllPeerModules():
		if (module.getName() == name):
			return module
	return None



######################################################################
main()


