# ony passing 72 out of 93 my solution:
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n=len(fruits)
        if n==1:
            return 1
        if n==2:
            return 2
        start=0
        end=1
        tempS=fruits[0]
        tempE=fruits[1]
        Mx=2
        cnt=1
        while  end<n and fruits[end]==fruits[start]:
            cnt+=1           
            temp=fruits[end]
            end+=1
          
        if end>=n :
            if fruits[end-1] !=tempS:
                cnt+=1
            Mx=max(Mx,cnt)
            return Mx
        start=end-1
        tempS=fruits[start]
        tempE=fruits[end]


        while end<n:
            if fruits[end]==tempS or fruits[end]==tempE:                
                cnt+=1
                end+=1
            else:
                
                start=end-1
                tempS=fruits[start]
                tempE=fruits[end]
                Mx=max(Mx,cnt)
                cnt=2
                end+=1
        Mx=max(Mx,cnt)

        return Mx






            

     



            


