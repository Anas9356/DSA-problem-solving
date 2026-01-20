#1st attemp and clared 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm1=dict()
        hm2=dict()
        n1=len(s1)
        n2=len(s2)
        start=0
        end=0
        if n1>n2:
            return False

        #this the lop traversing on s1 and adding it into a map with th freq of ele
        for i in range(n1):
            hm1[s1[i]]=hm1.get(s1[i], 0) + 1
        while end<n1:
            hm2[s2[end]]=hm2.get(s2[end], 0) + 1
            end+=1
        if hm1==hm2:
            return True
        while end<n2:
            ch1=s2[start]
            hm2[ch1] -= 1
            if hm2[ch1] == 0:
                del hm2[ch1]
            hm2[s2[end]]=hm2.get(s2[end], 0) + 1
            if hm1==hm2:
                return True
            end+=1
            start+=1

        return False



        
