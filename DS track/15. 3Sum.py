class Solution(object):
    def threeSum(self, nums):
        #method: get the numbers by different situation
        res = set() #use set to avoid duplicate
        
        #store positive, negative and zero nums in different set
        n,p,z = [],[],[]
        for num in nums:
            if num ==0:
                z.append(num)
            elif num <0:
                n.append(num)
            else:
                p.append(num)
        
        ##Create a separate set for negatives and positives for O(1) look-up times
	    N, P = set(n), set(p) #not necessary, but saved time
        
        #1. when there are three zeros in the list
        if len(z)>= 3:
            res.add((0,0,0))
        
        #2. when there are <3 but >0 zeros, find compliment negative and positive numbers
        if len(z)>=1:
            for neg in N:
                pos = -neg
                if pos in P:
                    res.add((neg, 0,pos))
                    
        #3. for all negative pairs , find the compliment positive number
        for i in range(len(n)-1):
            n1 = n[i]
            for j in range(i+1,len(n)):
                n2 = n[j]
                comp = -(n1+n2)
                if comp in P:
                    res.add(tuple(sorted([n1,n2,comp])))
        
        #4. for all positive pairs , find the compliment negative number
        for i in range(len(p)-1):
            n1 = p[i]
            for j in range(i+1,len(p)):
                n2 = p[j]
                comp = -(n1+n2)
                if comp in N:
                    res.add(tuple(sorted([comp,n1,n2])))
        
        return res
        
        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        
   
