# approch is just add that interval into the array and thhen sort it so it will be on correct position 
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        final=[]
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

        

        
