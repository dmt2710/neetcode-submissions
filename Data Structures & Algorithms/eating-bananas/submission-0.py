class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r
        while l <= r:
            k = (l + r) // 2
            hour_spent = 0
            for p in piles:
                hour_spent += math.ceil(p/k)
            
            if hour_spent > h:
                l = k + 1
            elif hour_spent <= h:
                result = min(result, k)
                r = k - 1

        return result


        