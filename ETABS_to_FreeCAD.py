#import the required modules.
import FreeCAD
import Draft
import os
import sys

#install comtypes package before importing.
sys.path.append('C:\Python27\Lib\site-packages')
import comtypes.client

#some imputs
AttachToInstance = True
SpecifyPath = False
ModelPath = 'E:\Etabs_Files\Sample Model'

#code
FreeCAD.newDocument("Test")

myEO = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
myModel = myEO.SapModel

#till here you got full control over the ETABS.
frames = myModel.FrameObj.GetNameList()
frameNames = frames[1]
framePoints = []

for n in frameNames:
	framePoints.append(myModel.FrameObj.GetPoints(n))

sPoints = [i[0] for i in framePoints]
ePoints = [i[1] for i in framePoints]

sCords = []
for p in sPoints:
	sCords.append(myModel.PointObj.GetCoordCartesian(p))

sCordsN = [[a*0.001 for a in b] for b in sCords]

eCords = []
for p in ePoints:
	eCords.append(myModel.PointObj.GetCoordCartesian(p))

eCordsN = [[a*0.001 for a in b] for b in eCords]

lines = []
for n in frameNames:
	lines.append('frame'+n)

wires = []

for i in sCordsN:
	del i[3]

for i in eCordsN:
	del i[3]

allP = zip(sCordsN, eCordsN)
for sc, ec in allP:
	sp = FreeCAD.Vector(sc)
	ep = FreeCAD.Vector(ec)
	Draft.makeWire([sp, ep], placement=pl, False, True, support=None)