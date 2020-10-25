class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        map = {}
        temp = []
        for i in range(len(arr1)):
            if arr1[i] not in map:
                map[arr1[i]]=1
            else:
                map[arr1[i]]+=1
        for i in range(len(arr2)):
            for j in range(map[arr2[i]]):
                res.append(arr2[i])
        for i in range(len(arr1)):
            if arr1[i] not in res:
                temp.append(arr1[i])
        while(len(res)<len(arr1)):
            res.append(min(temp))
            temp.remove(min(temp))
        return res
                


        '''        
                temp.append(arr1[i])
        temp.sort()
        for i in temp:
            res.append(i)
        return res
        '''