from math import *

class vector(object):

    def __init__(self, vXf = 0.0, vYf = 0.0):
        
        self.vX = vXf
        self.vY = vYf
        self.vector = [self.vX, self.vY]

    def __str__(self):

        string = str(self.vector)
        return string

    def changeVdata(self, vXf, vYf):

        self.vX = vXf
        self.vY = vYf
        self.vector = [self.vX, self.vY]

    def copyV2(self):

        return self.vector        

    def __add__(self, rV):
        
        return vector(self.vX + rV.vX, self.vY + rV.vY)
    
    def __sub__(self, rV):
        
        return vector(self.vX - rV.vX, self.vY - rV.vY)
    
    def __mul__(self, rS):
        
        return vector(self.vX * rS, self.vY * rS)

    def __truediv__(self, rS):

        return vector(self.vX / rS, self.vY / rS)
    
    @staticmethod
    def fromPoints(P1, P2):

        return vector(P2[0] - P1[0], P2[1] - P1[1])

    def normalizeV2(self):
        
        mag = self.lengthV2()
        X = self.vX / mag
        Y = self.vY / mag

        return vector(X, Y)
        
    def lengthV2(self):

        LV2 = sqrt((self.vector[0] * self.vector[0])+
                   (self.vector[1] * self.vector[1]))
        return LV2

    def dotProductV2(self, rightV2):

        scalerV2 = ((self.vector[0] * rightV2.vector[0]) + (self.vector[1] * rightV2.vector[1]))

        return scalerV2
        
    def crossProductV2(self, rightV2):

        return (self.vector[0] * rightV2.vector[1] - self.vector[1] * rightV2.vector[0])

    def rotateV2(self, theta):
        rad = radians(theta)
        X = round((self.vX * cos(rad)) - (self.vY * sin(rad)), 3)
        Y = round((self.vX * sin(rad)) + (self.vY * cos(rad)), 3)

        return vector(X, Y)

        

        
