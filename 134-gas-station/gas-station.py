class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start=0
        current_tank=0
        if sum(gas)<sum(cost):
            return -1
        for i in range(len(gas)):
            current_tank+=gas[i]-cost[i]
            if current_tank<0:
                start=i+1
                current_tank=0
        return start