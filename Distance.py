# make distance matrix
class Distance():

   def __init__(self,s,t):
      self.s = s
      self.t = t
      self.n = len(self.s)
      self.m = len(self.t)

   def Match(self,s,t):
       if (s==t):
           return 0
       else:
           return 1

   def setMatrix(self):
       self.d={}

       # initialize d matrix
       # -GCTGATATAGCT
       # -GGGTGATTAGCT
       # (n+1) by (m+1) matrix. set 0
       for i in range(0,(self.n)+1):
           for j in range(0,(self.m)+1):
               self.d[i,j] = 0

       #set 0,1,2,3,...,n+1
       #set 0,1,2,3,...,m+1
       for i in range((self.n)+1):
           self.d[i,0] = i
       for j in range((self.m)+1):
           self.d[0,j] = i

       #set score matrix
       #min (gap at s, gap at t, mismatch)
       for i in range(1,(self.n)+1):
           for j in range(1,(self.m)+1):
               self.d[i,j] = min(
                   self.d[i-1,j]+1,
                   self.d[i,j-1]+1,
                   self.d[i-1,j-1]+self.Match(self.s[i-1],self.t[j-1])
               )
   def getDistance(self):
      self.setMatrix()
      return self.d[(self.n),(self.m)]
