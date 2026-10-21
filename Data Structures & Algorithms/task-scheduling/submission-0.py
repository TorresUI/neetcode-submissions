class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = {}
        for t in tasks:
            freqMap[t] = -1 + freqMap.get(t, 0)
        
        frequencies = list(freqMap.values())
        heapq.heapify(frequencies)
        q = collections.deque()
        time = 0
        print(frequencies)

        while frequencies or q:
            #Check if at the current time we can introduce a value from the q
            if q and q[0][0] == time:
                time, freq = q.popleft()
                heapq.heappush(frequencies, freq)

            time += 1

            #We must process a task from the top of the heap
            if frequencies:
                task = heapq.heappop(frequencies)
                task += 1
                #Append [time, value] to q
                if task != 0:
                    q.append([time + n, task])
        return time


