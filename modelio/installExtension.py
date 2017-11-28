import os
import sys

extensionFolderPath = sys.argv[1]

root = modelingSession.getModel().getModelRoots().get(0)
gproject =  GProject.getProject(root)
moduleArchivePattern = os.path.join(extensionFolderPath, "CPSWarm*")
moduleArchives = glob.glob(moduleArchivePattern)
Modelio.getInstance().getModuleService().installModule(gproject, Paths.get(moduleArchives[0]))