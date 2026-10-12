class TimeMap:

    def __init__(self):
        self.data={
        }
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.data):
            self.data[key]=[[timestamp],[value]]
        else:
            self.data[key][0].append(timestamp)  
            self.data[key][1].append(value)  
        
    def get(self, key: str, timestamp: int) -> str:

        if(key not in self.data):
            return ""
        
        timestamps=self.data[key][0]
        values=self.data[key][1]

        x=bisect_right(timestamps,timestamp) - 1

        if(x < 0):
            return ""
        
        return values[x]
        



        

