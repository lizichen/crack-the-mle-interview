"""
https://leetcode.com/problems/maximum-profit-in-job-scheduling/

You're a dasher, and you want to try planning out your schedule. You can view a list of deliveries along with their associated start time, end time, and dollar amount for completing the order. Assuming dashers can only deliver one order at a time, determine the maximum amount of money you can make from the given deliveries.

The inputs are as follows:

int start_time: when you plan to start your schedule
int end_time: when you plan to end your schedule
int d_starts[n]: the start times of each delivery[i]
int d_ends[n]: the end times of each delivery[i]
int d_pays[n]: the pay for each delivery[i]
The output should be an integer representing the maximum amount of money you can make by forming a schedule with the given deliveries.

Constraints
end_time >= start_time
d_ends[i] >= d_starts[i]
d_pays[i] > 0
len(d_starts) == len(d_ends) == len(d_pays)

"""

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        jobs = [] # startTime, endTime, profit
        for i in range(len(startTime)):
            st = startTime[i]
            et = endTime[i]
            pf = profit[i]
            jobs.append((st, et, pf)) 
            
        # sort by start time:
        jobs.sort(key = lambda x: (x[0], x[1]))
        
        pq = []
        max_profit = 0
        
        for j in jobs:
            
            if len(pq) == 0:
                heapq.heappush(pq, (j[1], j[2]))
            else:
                while len(pq) > 0 and pq[0][0] <= j[0]:
                    max_profit = max(max_profit, heapq.heappop(pq)[1])
                heapq.heappush(pq, (j[1], max_profit + j[2]))
                
        while len(pq) > 0:
            max_profit = max(max_profit, heapq.heappop(pq)[1])
            
        return max_profit
        
        
        
