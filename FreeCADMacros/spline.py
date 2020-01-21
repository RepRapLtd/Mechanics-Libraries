import Part
c=Part.BSplineCurve()
from FreeCAD import Base
scale = (1500/(275.5+4.4))*(44/(275.5+4.4))
pts1=[
 Base.Vector(0, 0, 0).multiply(scale),
 Base.Vector(5.5, 6.4, 0).multiply(scale),
 Base.Vector(15.5, 12.5, 0).multiply(scale),
 Base.Vector(25.5, 16.2, 0).multiply(scale),
 Base.Vector(35.5, 18.75, 0).multiply(scale),
 Base.Vector(45.5, 20.33, 0).multiply(scale),
 Base.Vector(55.5, 21.3, 0).multiply(scale),
 Base.Vector(65.5, 22.1, 0).multiply(scale),
 Base.Vector(75.5, 22.73, 0).multiply(scale),
 Base.Vector(85.5, 23, 0).multiply(scale),
 Base.Vector(95.5, 23.53, 0).multiply(scale),
 Base.Vector(105.5, 23.53, 0).multiply(scale),
 Base.Vector(115.5, 23.53, 0).multiply(scale),
 Base.Vector(125.5, 23.68, 0).multiply(scale),
 Base.Vector(135.5, 23.49, 0).multiply(scale),
 Base.Vector(145.5, 23.1, 0).multiply(scale),
 Base.Vector(155.5, 23.08, 0).multiply(scale),
 Base.Vector(165.5, 22.42, 0).multiply(scale),
 Base.Vector(175.5, 21.81, 0).multiply(scale),
 Base.Vector(185.5, 20.91, 0).multiply(scale),
 Base.Vector(195.5, 20.37, 0).multiply(scale),
 Base.Vector(205.5, 19.37, 0).multiply(scale),
 Base.Vector(215.5, 18.13, 0).multiply(scale),
 Base.Vector(225.5, 16.28, 0).multiply(scale),
 Base.Vector(235.5, 14.64, 0).multiply(scale),
 Base.Vector(245.5, 12.38, 0).multiply(scale),
 Base.Vector(255.5, 10.2, 0).multiply(scale),
 Base.Vector(265.5, 7.38, 0).multiply(scale),
 Base.Vector(275.5+4.4-0.95, 1, 0).multiply(scale),
 Base.Vector(275.5+4.4, 0, 0).multiply(scale)
 ]
pts1
c.interpolate(pts1)
s=c.toShape()
Part.show(s)

d=Part.BSplineCurve()
pts2=[
 Base.Vector(0, 0, 0).multiply(scale),
 Base.Vector(275.5+4.4, 0, 0).multiply(scale)
 ]
pts2
d.interpolate(pts2)
t=d.toShape()
Part.show(t)
