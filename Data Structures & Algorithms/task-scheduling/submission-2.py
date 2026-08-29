class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = len(tasks)
        
        task_count_dict = dict()
        for task in tasks: 
            task_count_dict[task] = task_count_dict.get(task, 0) + 1
        
        task_heap = []
        heapq.heapify(task_heap) 
        for task_name, task_count in task_count_dict.items():
            heapq.heappush(task_heap, [-1*task_count, 0, task_name])
        
        time = 0
        while len(task_heap):
            popped_tasks = []
            while len(task_heap) and task_heap[0][1]>time:
                popped_tasks.append(heapq.heappop(task_heap))
            if len(task_heap): 
                execute_task = task_heap[0]
                heapq.heappop(task_heap)
                execute_task[0] += 1
                execute_task[1] = time + n + 1
                if execute_task[0] != 0: 
                    heapq.heappush(task_heap, execute_task)
            for popped_task in popped_tasks: 
                heapq.heappush(task_heap, popped_task)
            time += 1

        return time
        # while task_count: 

        