
modelPackage=session.getModel().getModelRoots().get(1).getModel().get(0)

t = session.createTransaction("transaction 1")
modelPackage.getOwnedElement().get(0).setName("haha2")

t.commit()

assert modelPackage.getOwnedElement().get(0).getName() == "haha2", "Error"



attackTreePeerModule = Modelio.getInstance().getModuleService().getPeerModule("AttackTreeDesigner")

attackTreePeerModule.exportModel(modelPackage, "/home/kchaabouni/kais2/p07_cpswarm/CI/testCPSwarmPipelines/simulated_docker_attacktree")
