class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            temp = prices.copy()

            for a, b, price in flights:
                #Calculate the total price from a to b is the price of a and the price of the edge
                totalPrice = prices[a] + price

                if totalPrice < temp[b]:
                    #We found a short path to b node
                    temp[b] = totalPrice

            prices = temp
        
        return prices[dst] if prices[dst] != float("inf") else -1

