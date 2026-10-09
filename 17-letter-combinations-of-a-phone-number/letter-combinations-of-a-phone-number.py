class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        combo={
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"]
        }
        ans=[]
        path=[]
        pairs=[]
        chars=""
        for i in digits:
            i=int(i)
            pairs.append(combo[i])


        def backtrack(index):
            if( index == len(digits)):
                ans.append("".join(path))
                return
            for i in pairs[index]:
                path.append(i)
                backtrack(index+1)
                path.pop()

        backtrack(0)
        return ans
                
                
                

        