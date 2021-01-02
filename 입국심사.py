def solution(n, times):
    arr = [0]*len(times)
    start = 0   
    end = max(times)*n
    while start <= end:
        check=0
        mid = (start + end)//2

        if sum([mid//i for i in times]) == n:
             end = mid-1
             #진행 인원이 맞아도 그중에서 최소 시간을 구하기 위해서
        elif sum([mid//i for i in times]) < n:
            start=mid+1
        elif sum([mid//i for i in times]) > n:
            end = mid-1   
    return start
#print(solution(6,[7,10]))
#print(solution(10,[1,5]))
#print(solution(1,[2,2]))
#print(solution(6,[3,7,10]))
#print(solution(10,[1,10,10]))
#solution(6, [7,10]) : 28
print(solution(6, [6,10]))# : 24
#solution(6, [8,10])# : 30
#solution(6, [4,10])# : 20
#solution(11, [3,4,10])# : 18