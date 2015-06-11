# make distance matrix
class Distance():

    def __init__(self,s,t):
	self.s = s
	self.t = t
	self.n = len(self.s)
	self.m = len(self.t)

    def setMatrix(self):
        self.d={}
