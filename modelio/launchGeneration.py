for root in Modelio.getInstance().getModelingSession().getModel().getModelRoots():
	if isinstance(root, Project):
		for elt in  root.getModel().get(0).getOwnedElement():
			if elt.isStereotyped("CPSWarm", "Problem"):
				cpswarm = Modelio.getInstance().getModuleService().getPeerModule("CPSWarm");
				cpswarm.generateFrevoProject(elt)