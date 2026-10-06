class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        queue=deque()
        queue.append(beginWord)
        visited=set()
        seq=0
        dif=0

        patterns={}

        for word in (wordList):
            for i in range(len(word)):
                pattern=word[:i] + "*" + word[i+1:]
                if( pattern not in patterns):
                    patterns[pattern]=[] 
                patterns[pattern].append(word)

        while queue:

            for i in range(len(queue)):
                removed=queue.popleft()
                visited.add(removed)
                if(removed == endWord):
                    seq+=1
                    return seq

                for i in range(len(removed)):
                    pattern=removed[:i] + "*" +removed[i+1:]
                    if(pattern in patterns):
                        for word in patterns[pattern]:
                            if(word not in visited):
                                visited.add(word)
                                queue.append(word)

            seq+=1

        return 0
            
            


        