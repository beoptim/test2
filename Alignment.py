from Distance import Distance

class Alignment(Distance):

    def setBacktrackingMatrix(self):
        self.bm={}
        for i in range((self.n)+1):
            for j in range((self.m)+1):
                self.bm[i,j]= 0
        for i in range((self.n)+1):
            self.bm[i,0] = 2
        for j in range((self.m)+1):
            self.bm[0,j] = 4

		for i in range(1,(self.n)+1):
            for j in range(1,(self.m)+1):
                if (self.d[i,j]==self.d[i-1,j-1]+self.Match(self.s[i-1],self.t[j-1])):
                    self.bm[i,j] += 1
                if (self.d[i,j]== self.d[i-1,j]+1):
                    self.bm[i,j] += 2
                if (self.d[i,j]==self.d[i,j-1]+1):
                    self.bm[i,j] += 4

    #recurssive function
    #printalignment(n,m,'','')
    def printalignment(self,i,j,new_s,new_t):
        if ((i==0) and (j==0)):
            print new_s
            print new_t
            print "\n"
        else:
            if (self.bm[i,j] & 1 ) == 1 :
                self.printalignment(i-1,j-1,self.s[i-1]+new_s,self.t[j-1]+new_t)
            if (self.bm[i,j] & 2 ) == 2 :
                self.printalignment(i-1,j,self.s[i-1]+new_s,"-"+new_t)
            if (self.bm[i,j] & 4 ) == 4 :
                self.printalignment(i,j-1,"-"+new_s,self.t[j-1]+new_t)

    def __str__(self):
        self.setMatrix()
        self.setBacktrackingMatrix()
        self.printalignment(self.n,self.m,'','')
        return ""
