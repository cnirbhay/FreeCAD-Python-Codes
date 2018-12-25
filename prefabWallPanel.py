#importing required modules
import FreeCAD
import PartDesign
import PartDesignGui
import Sketcher

#setting parameters
lengthOfPanel = 6000
heightOfPanel = 3000
sillHeightOfOpening = 1000
heightOfOpening = 500
widthOfOpening = 1000
thicknessOfPanel = 100

#adding body and sketch objects to the active document
App.activeDocument().addObject('PartDesign::Body','prefabWall')
App.activeDocument().prefabWall.newObject('Sketcher::SketchObject','Sketch')
App.activeDocument().Sketch.Support = (App.activeDocument().XZ_Plane, [''])
App.activeDocument().Sketch.MapMode = 'FlatFace'
App.ActiveDocument.recompute()

#adding first list of geometries to the sketch
geoList0 = []
geoList0.append(Part.LineSegment(App.Vector(-14.013569,-0.032741,0),App.Vector(0.130968,4.878557,0)))
geoList0.append(Part.LineSegment(App.Vector(0.000000,4.878557,0),App.Vector(12.549567,-0.063675,0)))
geoList0.append(Part.LineSegment(App.Vector(12.549567,0.000000,0),App.Vector(-13.933221,-0.016098,0)))
App.ActiveDocument.Sketch.addGeometry(geoList0,False)

#adding first list of constraints to the sketch
conList0 = []
conList0.append(Sketcher.Constraint('PointOnObject',0,1,-1)) 
conList0.append(Sketcher.Constraint('PointOnObject',0,2,-2))
conList0.append(Sketcher.Constraint('Coincident',0,2,1,1))
conList0.append(Sketcher.Constraint('Coincident',1,2,2,1)) 
conList0.append(Sketcher.Constraint('Coincident',2,2,0,1))
conList0.append(Sketcher.Constraint('Symmetric',0,1,1,2,-2))
conList0.append(Sketcher.Constraint('DistanceX',0,1,1,2,lengthOfPanel))
conList0.append(Sketcher.Constraint('DistanceY',-1,1,0,2,heightOfPanel))
App.ActiveDocument.Sketch.addConstraint(conList0) 

#adding second list of geometries to the sketch(for opening)
geoList1 = []
geoList1.append(Part.LineSegment(App.Vector(-436.624084,1710.354370,0),App.Vector(413.391266,1710.354370,0)))
geoList1.append(Part.LineSegment(App.Vector(413.391266,1710.354370,0),App.Vector(413.391266,913.465332,0)))
geoList1.append(Part.LineSegment(App.Vector(413.391266,913.465332,0),App.Vector(-436.624084,913.465332,0)))
geoList1.append(Part.LineSegment(App.Vector(-436.624084,913.465332,0),App.Vector(-436.624084,1710.354370,0)))
App.ActiveDocument.Sketch.addGeometry(geoList1,False)

#adding second list of constraints to the sketch(for opening)
conList1 = []
conList1.append(Sketcher.Constraint('Coincident',3,2,4,1))
conList1.append(Sketcher.Constraint('Coincident',4,2,5,1))
conList1.append(Sketcher.Constraint('Coincident',5,2,6,1))
conList1.append(Sketcher.Constraint('Coincident',6,2,3,1))
conList1.append(Sketcher.Constraint('Horizontal',5))
conList1.append(Sketcher.Constraint('Vertical',4))
conList1.append(Sketcher.Constraint('Vertical',6))
conList1.append(Sketcher.Constraint('Symmetric',3,1,3,2,-2)) 
conList1.append(Sketcher.Constraint('DistanceY',-1,1,4,2,sillHeightOfOpening))
conList1.append(Sketcher.Constraint('DistanceY',4,2,4,1,heightOfOpening)) 
conList1.append(Sketcher.Constraint('DistanceX',3,1,3,2,widthOfOpening))
App.ActiveDocument.Sketch.addConstraint(conList1) 

#creating pad from the sketch
App.getDocument('Unnamed').recompute()
App.activeDocument().prefabWall.newObject("PartDesign::Pad","Pad")
App.activeDocument().Pad.Profile = App.activeDocument().Sketch
App.activeDocument().Pad.Length = thicknessOfPanel
App.ActiveDocument.Pad.Length2 = 0
App.ActiveDocument.Pad.Type = 0
App.ActiveDocument.Pad.UpToFace = None
App.ActiveDocument.Pad.Reversed = 0
App.ActiveDocument.Pad.Midplane = 0
App.ActiveDocument.Pad.Offset = 0.000000
App.ActiveDocument.recompute()

#setting the axometric view
App.getDocument('Unnamed').recompute()
Gui.getDocument("Unnamed").getObject("Sketch").Visibility = False
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
