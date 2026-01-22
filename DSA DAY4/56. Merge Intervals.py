class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        # ✅ FIX 1: sort first
        intervals.sort(key=lambda x: x[0])
        
        reslt = []
        min_val = intervals[0][0]
        max_val = intervals[0][1]
        
        for i in range(1, len(intervals)):
            
            # overlap case
            if intervals[i][0] <= max_val:
                max_val = max(max_val, intervals[i][1])
            
            # no overlap
            else:
                reslt.append([min_val, max_val])
                min_val = intervals[i][0]
                max_val = intervals[i][1]
        
        # add last interval
        reslt.append([min_val, max_val])
        return reslt
# and self solution is 
    import sys
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        max_val = max(intervals[0][0],intervals[0][1])   # smallest possible integer
        min_val = min(intervals[0][0],intervals[0][1])  
        pre_max = -sys.maxsize - 1   # smallest possible integer
        Pre_min = sys.maxsize 
        reslt=list()
        
        if n==1:
            return intervals

        for i in range(1,n):
            if intervals[i][0]>max_val and intervals[i][1]>max_val :
                temp=[min_val,max_val]
                reslt.append(temp)
                min_val= sys.maxsize 



            if intervals[i][0]<min_val:
                min_val =intervals[i][0]
            if intervals[i][1]<min_val:
                min_val =intervals[i][1]

            if intervals[i][0]>max_val:
                max_val =intervals[i][0]
            if intervals[i][1]>max_val:
                max_val =intervals[i][1]

            
            
            pre_max=max_val
            pre_min=min_val

        temp=[min_val,max_val]
        reslt.append(temp)

        
        return reslt

        # and try to improve 
    
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n=len(intervals)
        max_val = max(intervals[0][0],intervals[0][1])   # smallest possible integer
        min_val = min(intervals[0][0],intervals[0][1])  
        pre_max = -1000 - 1   # smallest possible integer
        pre_min = 1000 
        reslt=list()
        
        if n==1:
            return intervals

        for i in range(1,n):
            
            if intervals[i][0]>max_val and intervals[i][1]>max_val :
                temp=[min_val,max_val]
                reslt.append(temp)
                min_val= 1000 

            if intervals[i][0]<pre_min and intervals[i][1]<pre_min :
                temp=[intervals[i][0],intervals[i][1]]
                
                print('inside if---i =',i)
                reslt.append(temp)
                if(i<n-1):
                    i+=1
                else:
                    break
                



            if intervals[i][0]<min_val:
                min_val =intervals[i][0]
            if intervals[i][1]<min_val:
                min_val =intervals[i][1]

            if intervals[i][0]>max_val:
                max_val =intervals[i][0]
            if intervals[i][1]>max_val:
                max_val =intervals[i][1]

            
            
            pre_max=max_val
            pre_min=min_val
        print(min_val,max_val)
        temp=[min_val,max_val]
        reslt.append(temp)

        
        return reslt

        

        



            


obj=Solution()
print(obj.merge([[3,3],[2,2],[8,10],[15,28],[16,17],[18,19],[12,20],[25,29]]))
print ("execution ended")