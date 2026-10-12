class RandomizedSet:

    def __init__(self):
        self.List = []
        self.Dict = {}

    def insert(self, val: int) -> bool:
        if val in self.Dict:
            return False

        self.List.append(val)
        self.Dict[val] = len(self.List) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.Dict:
            return False

        index = self.Dict[val]
        self.List[index] = self.List[-1]
        value = self.List[index]
        self.List.pop()
        self.Dict.pop(val)

        if value != val:
            self.Dict[value] = index

        return True

    def getRandom(self) -> int:
        return random.choice(self.List)