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
	module_jmdac_path = "/module_jmdac_archives"
	moduleArchivePattern = os.path.join(module_jmdac_path, "AttackTreeDesigner_*.jmdac")
	moduleArchives = glob.glob(moduleArchivePattern)
	assert len(moduleArchives) > 0, "No jmdac archive has been found !"
	moduleArchives.sort(reverse=True)
	print("deploying ", Paths.get(moduleArchives[0]))
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


	model = session.getModel()

	t = session.createTransaction("transaction 1")
	modelPackage.setName("Model1")
	p1 = model.createPackage("p1", modelPackage)
	p2 = model.createPackage("p2", modelPackage)
	p3 = model.createPackage("p3", modelPackage)

	p1p1 = model.createPackage("p1_p1", p1)
	p1p2 = model.createPackage("p1_p2", p1)

	p2p1 = model.createPackage("p2_p1", p2)


	t.commit()

	attackTreePeerModule.createNewTree(p1p1)
	attackTreePeerModule.createNewTree(p1p2)
	attackTreePeerModule.createNewTree(p2)
	attackTreePeerModule.createNewTree(p2p1)
	attackTreePeerModule.createNewTree(p3)

	attackTreePeerModule.exportModel(modelPackage, "/attack-tree/generated_trees/test_0_03")




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


