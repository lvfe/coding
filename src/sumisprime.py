import math
class Solution:
    def sumisprime(self,A,k):
        result = []
        path = []
        start = 0
        A.sort()
        if len(A)==0:
            return []
        self.dfs(result,path,start,A,k)

        return len(result)

    def dfs(self,list, path, start, A, k):
        if len(path)==k:
            num=sum(path[:])
            if self.isPrime(num)==True:
                print(num)
                list.append(num)
            return
        for i in range(start,len(A)):
            path.append(A[i])
            self.dfs(list,path,i+1,A,k)
            path.pop()

    def isPrime(self, num):
        if num==1 or num==2:
            return True
        for i in range(2,math.floor(math.sqrt(num))+1,1):
            if num%i==0:
                return False
        return True

if __name__=='__main__':
    solution=Solution()
    print(solution.sumisprime([3,9,23,12,34,65,32,19,81],4))