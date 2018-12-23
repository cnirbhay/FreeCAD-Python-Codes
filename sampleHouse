#importing some important modules
import FreeCAD
import DraftTools
import Draft
import ArchWall
import Arch
import ArchStructure

#creating parameters
lengthOfRoom = 5000
widthOfRoom = 3000
heightOfWall = 3000
thicknessOfSlab = 200
offset1 = 1000
offset2 = 1500

#creating walls
pl = FreeCAD.Placement()
pl.Base = FreeCAD.Vector(0.0,0.0,0.0)
rec = Draft.makeRectangle(lengthOfRoom,widthOfRoom,pl,False,None)
obj = Arch.makeWall(FreeCAD.ActiveDocument.ActiveObject)
App.ActiveDocument.Wall.Align = 'Right'
Draft.autogroup(obj)

#creating floor slab
rec = Draft.makeRectangle(lengthOfRoom + offset1,widthOfRoom + offset1,pl,False,None)
Draft.move([FreeCAD.ActiveDocument.ActiveObject],FreeCAD.Vector(-offset1/2,-offset1/2.0,0.0),False)
obj = Arch.makeStructure(FreeCAD.ActiveDocument.ActiveObject)
App.ActiveDocument.Structure.Height = thicknessOfSlab
App.ActiveDocument.Structure.Normal.z = -1

#creating roof slab
pl = FreeCAD.Placement()
pl.Base = FreeCAD.Vector(0,0,heightOfWall)
rec = Draft.makeRectangle(lengthOfRoom + offset2,widthOfRoom + offset2,pl,False,None)
Draft.move([FreeCAD.ActiveDocument.ActiveObject],FreeCAD.Vector(-offset2/2,-offset2/2.0,0.0),False)
obj = Arch.makeStructure(FreeCAD.ActiveDocument.ActiveObject)
App.ActiveDocument.ActiveObject.Height = thicknessOfSlab
App.ActiveDocument.ActiveObject.Normal.z = 1
App.ActiveDocument.recompute()
