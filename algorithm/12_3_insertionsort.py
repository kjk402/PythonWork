# 삽입 정렬 insertion sort

def insetionsort(A):
    for i in range(len(A)-1):
        for j in range(i +1, 0 ,-1):
            if A[j] < A[j-1] :
                A[j],A[j-1] = A[j-1],A[j]
            # else:
            #     break
    return A


num = list(map(int, input().split()))
insetionsort(num)
print(num)