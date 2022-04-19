# FreeCAD program to generate a 3D-printable sieve with a certain mesh size.

# All dimensions in mm.

# The size of the holes

holeDiameter = 2.0

# Overall diameter

bigDiameter = 100.0

# Overall depth

depth = 50.0

# Wall thickness

wallThickness = 4.0

# Base thickness

baseThickness = 1.0

#********************************************************************************************************

import Part, FreeCAD, math
from FreeCAD import Base


body = Part.makeCylinder(bigDiameter/2, depth, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1))
body = body.cut(Part.makeCylinder(bigDiameter/2 - wallThickness, depth, Base.Vector(0, 0, baseThickness), Base.Vector(0, 0, 1)))




Part.show(body)
