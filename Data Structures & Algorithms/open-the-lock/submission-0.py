class Solution:
    def getNextCombination(self, currentCombination):
        digits =  [int(currentCombination[0]), int(currentCombination[1]), int(currentCombination[2]), int(currentCombination[3])]
        res = []
        for i in range(4):
            digits[i] = (digits[i]+1)%10
            res.append("".join(str(dig) for dig in digits))
            digits[i] = (digits[i]-2)%10
            res.append("".join(str(dig) for dig in digits))
            digits[i] = (digits[i]+1)%10
        return res

    def openLock(self, deadends: List[str], target: str) -> int:
        combination = "0000"
        
        deadends_set = set(deadends)
        if combination in deadends_set:
            return -1
        visited_combinations = set()

        bfs_queue = deque()
        bfs_queue.append(combination)
        visited_combinations.add(combination)

        turn = -1

        while len(bfs_queue):
            bfs_queue_size = len(bfs_queue)
            turn += 1
            for i in range(bfs_queue_size):
                current_combination = bfs_queue.popleft()
                if current_combination == target:
                    return turn
                for next_combination in self.getNextCombination(current_combination):
                    if next_combination not in deadends_set and next_combination not in visited_combinations: 
                        visited_combinations.add(next_combination)
                        bfs_queue.append(next_combination)
        
        return -1



        