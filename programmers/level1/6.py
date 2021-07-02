# 6번  K번째 수

def solution(arr, cmd):
   ans=[]
   for i,j,k in cmd:
       ans.append(sorted(arr[i-1:j])[k-1])
   return ans

arr = [1, 5, 2, 6, 3, 7, 4]
com = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(arr, com))