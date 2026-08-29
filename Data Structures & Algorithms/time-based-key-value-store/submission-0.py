class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        else:
            values_timestamps = self.time_map[key]

            low, high = 0, len(values_timestamps)-1

            while low<=high:
                mid = (low+high)//2
                if timestamp<values_timestamps[mid][1]:
                    high = mid-1
                elif timestamp>values_timestamps[mid][1]:
                    low = mid+1
                else:
                    return values_timestamps[mid][0] 

            if low == 0:
                return ""  
            else:
                return values_timestamps[low-1][0] 

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)