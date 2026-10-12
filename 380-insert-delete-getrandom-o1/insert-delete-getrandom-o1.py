class RandomizedSet:

    def __init__(self):
        self.List=[]
        self.Dict={}
        
    def insert(self, val: int) -> bool:
        if( val not in self.Dict):
            self.List.append(val)
            self.Dict[val]=len(self.List)-1
            return True
        else:
            return False
        
    def remove(self, val: int) -> bool:
        if(val in self.Dict):
            index=self.Dict[val]
            self.List[index]=self.List[-1]
            value= self.List[index]
            self.List.pop()
            self.Dict.pop(val)
            if( value != val):
                self.Dict[value]=index
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.List)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()