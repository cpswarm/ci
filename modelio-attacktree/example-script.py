root = session.getModel().getModelRoots().get(1)
modelPackage = root.getModel().get(0)

attackTreePeerModule = Modelio.getInstance().getModuleService().getPeerModule("AttackTreeDesigner")

tree1 = attackTreePeerModule.createNewTree(modelPackage)
tree2 = attackTreePeerModule.createNewTree(modelPackage)

diagrams = tree1.getDiagramElement()
diagram = diagrams[0]

and1 = attackTreePeerModule.createANDChild(tree1,diagram)
attack1 = attackTreePeerModule.createAttack(diagram)
or1 = attackTreePeerModule.createORChild(attack1,diagram)
attackTreePeerModule.createConnection(and1, attack1, diagram)

ref1 =  attackTreePeerModule.createReference(diagram)
attackTreePeerModule.createConnection(and1, ref1, diagram)


pathtree2 = attackTreePeerModule.getElementFullPath(tree2)

attackTreePeerModule.updateReference(ref1,pathtree2)

counter = attackTreePeerModule.createCounterMeasure(attack1, diagram)

attackTreePeerModule.updateTag(attack1, "Severity", "LOW")

