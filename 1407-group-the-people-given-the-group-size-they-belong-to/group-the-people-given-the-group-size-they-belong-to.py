class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        d = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] in d:
                d[groupSizes[i]].append(i)
            else:
                d[groupSizes[i]] = [i]
        # print(d)
        arr = []
        for key,val in d.items():
            n = len(val) / key
            j = 0 
            for i in range(n):
                temp = []
                for k in range(key):
                    temp.append(val[j])
                    j+=1
                arr.append(temp)
        return(arr)