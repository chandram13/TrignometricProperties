# Marvish Chandra

import Math
import Mathplotlib


def basicArc(degrees,radians,r):
    findRadians = 3.14 / 180 * degrees
    print("The radians of the given arc circle is " + findRadians + ".")
    findDegrees = 180 / 3.14 * radians
    print("The degrees of the given arc circle is" + findDegrees + ".")
    sectorArea = 1/2 * (r * r) * radians
    print("The sector area of the given arc circle is" + sectorArea + ".")
    arcLength = r * radians
    print("The arc length of the given arc circle is" + arcLength + ".")

def rightTriangle(opp,adj,hypo):
    findSin = opp /hypo
    findCos = adj / hypo
    findTan = opp / hypo

def nonrightSin(a,b,c,A,B,C):
firstSin = (a / Math.sin(A))
secondSin = (b / Math.sin(B))
thirdSin = (c / Math.sin(C))
assert firstSin = secondSin = thirdSin

def nonrightCos(a,b,c,C):
    assert (c * c) = (a * a) + (b * b) - 2*a*b*Math.cos(C)

def areaTri(a,b,C):
    area = 1/2 * a * b * Math.sin(C)

# r representing radians
def tanIdentity(r):
    assert Math.tan(r) = Math.sin(r) / Math.cos(r)
def sin_cos_relationship(r):
    assert Math.sin(r) ** 2 + Math.cos(r) ** 2 = 1
def secondRelationship(r):
    assert 2*Math.sin(r)*Math.cos(r) = Math.sin(r)
def thirdRelationship(r):
    assert 2 * Math.sin(r) = Math.cos(r) ** 2 - Math.sin(r) ** 2





