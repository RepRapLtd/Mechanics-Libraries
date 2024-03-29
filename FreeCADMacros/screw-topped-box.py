#
# FreeCAD Python Macro to generate a screw topped box
#
# Adrian Bowyer
# reprapltd.com
#
# 27 December 2018
#
# Licence: GPL
#

import Part, FreeCAD, math
from FreeCAD import Base

# Parameters

# The box size - the outside dimensions

xBox = 115
yBox = 115
zBox = 70

# Box wall thicknesses

thick = 2.5

# Lid thickness

lid = 4

# Screw self-tapping radius

screwHoleR = 1.3

# Screw clearance radius

screwClearR = 1.8

#Screw length

screwL = 10

# Screw head radius (i.e. outer radius of countersink cone) and height of cone to force 45 degree cone

screwHR = 3

#********************************************************************************

# Make a screw as a cylinder at the origin and at the right height to make
# the correct hole in the lid

def Screw():
 c = Part.makeCylinder(screwClearR, screwL - 0.2)
 d = Part.makeCone(0, screwHR, screwHR)
 d.translate(Base.Vector(0, 0, screwL - screwHR))
 c = c.fuse(d)
 c.translate(Base.Vector(0, 0, lid - screwL))
 return c


# Make the corner into which the screw self-taps.  Again this is with the screw
# hole at the origin and at the right height to union with the rest of the box.

def Corner():
 edge = 3*(screwHR + 2 - thick*0.5)
 c = Part.makeBox(edge, edge, screwL*2)
 c.translate(Base.Vector(-edge*0.5, -edge*0.5, 0))
 e = Part.makeBox(edge*2, edge*2, screwL*3)
 e.translate(Base.Vector(0, -edge,  - thick*0.5))
 e.rotate(Base.Vector(0,0,0),Base.Vector(0,0,1),45)
 c = c.cut(e);
 f = Part.makeBox(edge*2, edge*2, screwL*2)
 f.translate(Base.Vector(0, -edge,  - thick*0.5))
 f.rotate(Base.Vector(0,0,0),Base.Vector(0,0,1),45)
 f.rotate(Base.Vector(0,0,0),Base.Vector(-1,1,0),45)
 f.translate(Base.Vector(-edge*0.5, -edge*0.5, 0))
 c = c.cut(f)
 c.translate(Base.Vector(edge/6, edge/6, 0))
 d = Part.makeCylinder(screwHoleR, screwL*3)
 d.translate(Base.Vector(0, 0, - thick*0.5))
 c = c.cut(d)
 c.translate(Base.Vector(0, 0, zBox - screwL*2 - lid))
 return c

# Transform an object p at the origin to one of the four corners.  Corner i (looking down on top) is:
#
# ^   3    2
# |
# y    0    1
#   x ->

def GoToCorner(p, i):
 xyD = screwHR + 2
 if i == 0:
  p.translate(Base.Vector(xyD, xyD, 0))
 elif i == 1:
  p.rotate(Base.Vector(0,0,0),Base.Vector(0,0,1),90) 
  p.translate(Base.Vector(xBox - xyD, xyD, 0))
 elif i == 2:
  p.rotate(Base.Vector(0,0,0),Base.Vector(0,0,1),180)
  p.translate(Base.Vector(xBox - xyD,yBox - xyD,0))
 elif i == 3:
  p.rotate(Base.Vector(0,0,0),Base.Vector(0,0,1),270)
  p.translate(Base.Vector(xyD,yBox - xyD,0))
 else:
  print("GoToCorner - dud value.")	
 return p


# The box

def BoxBase():
 c = Part.makeBox(xBox, yBox, zBox - lid)
 d = Part.makeBox(xBox-2*thick, yBox-2*thick, zBox)
 d.translate(Base.Vector(thick, thick, thick))
 c = c.cut(d)
 c = c.fuse(GoToCorner(Corner(), 0))
 for i in range(3):
  c = c.fuse(GoToCorner(Corner(), i+1))
 return c


# The lid

def BoxLid():
 c = Part.makeBox(xBox, yBox, lid)
 for i in range(4):
  c = c.cut(GoToCorner(Screw(), i))
 c.translate(Base.Vector(0,0,zBox*1.5))
 return c


# Make one of each

f = BoxBase()
g = BoxLid()
Part.show(f)
Part.show(g)
