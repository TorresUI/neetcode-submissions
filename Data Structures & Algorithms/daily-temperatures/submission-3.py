class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperatureStack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            currentTemp = [i, t]

            while temperatureStack and currentTemp[1] > temperatureStack[-1][1]:
                index, temp = temperatureStack.pop()
                numOfDays = i - index
                res[index] = numOfDays
            
            temperatureStack.append(currentTemp)
        
        while temperatureStack:
            index, temp = temperatureStack.pop()
            res[index] = 0
        
        return res



