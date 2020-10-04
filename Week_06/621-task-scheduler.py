class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #桶方法
        from collections import Counter
        #统计每个字母出现的个数，以出现最多的次数为桶的个数
        size = len(tasks)
        task_ct =Counter(tasks)
        #得到出现最多的次数
        most = task_ct.most_common(1)#[(key,num)]
        nbucket = most[0][1]#得到桶的个数
        lastTaskSize = list(task_ct.values()).count(nbucket)#nbucket不是size // nbucket
        tim = (nbucket-1) * (n+1) + lastTaskSize
        return max(tim,size)