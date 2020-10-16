class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        relations = [0 for i in range(N)]
        
        for t in trust:
            #incoming edge increment by 1, outgoing edge decrement by 1
            relation = t
            incoming  = relation[1] 
            outgoing = relation[0]
            
            relations[incoming - 1] += 1
            relations[outgoing - 1] -= 1
            
        for r in range(0, len(relations)):
            if relations[r] == N - 1:
                return r + 1
    
        return -1
            
#timeComplexity: O(n)
#spaceComplexity: O(n)
