class Solution:
    def generate(self, numRows):      
        a=[[1]] #list of lists
        for i in range(1,numRows):
            a.append([x+y for x,y in zip([0]+a[i-1],a[i-1]+[0])])
        return a[:numRows]
