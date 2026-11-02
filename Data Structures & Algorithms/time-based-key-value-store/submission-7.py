class TimeMap:

    def __init__(self):
        self.dictt_for_value = {}    
        self.dictt_for_timestamp = collections.defaultdict(list)      

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictt_for_value[(key,timestamp)] = value
        self.dictt_for_timestamp[key].append(timestamp)

    

    def get(self, key: str, timestamp: int) -> str:
        lst = self.dictt_for_timestamp[key]
        if not lst:
            return ""

        l, r = 0, len(lst)-1
        prev_timestamp = -1

        while l<=r:
            m = (l + r) // 2
            if lst[m]<timestamp:
                prev_timestamp = lst[m]
                l = m + 1
            elif lst[m]>timestamp:
                r = m - 1
            else:
                prev_timestamp = lst[m]
                break

        if prev_timestamp == -1:
            return ""
            
        return self.dictt_for_value[(key,prev_timestamp)]




        
        
