class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        combinedList = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        

        for i in pair:
            #Compute how much time it will take to get to target
            pos, speed = i
            t = (target - pos) / speed

            #check the top of the stack to see if this value is less than if it is then we dont add to the stack if it is greater than that time then add to the stack       
            if not stack or t > stack[-1]:
                stack.append(t)
            
        return len(stack)
