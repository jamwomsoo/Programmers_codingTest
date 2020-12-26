import copy
def solution(s):
    answer = []
    ls=[]
    cnt=0
    j=""
    tmp = list()
    for i in range(0,len(s)):
        if s[i]=='{':
            cnt+=1
        elif s[i]=='}': 
            cnt-=1
            if cnt%2==1:
                t = copy.deepcopy(tmp)
                ls.append(t)
                del tmp[:]
        elif s[i] != ',':
            j+=s[i]
            if (s[i+1]==',') | (s[i+1]=='}'):
                tmp.append(int(j))
                j=""
    cnt = 0
    while 1:
        if not ls:
            break
        cnt+=1
        for i in ls:
            if len(i) == cnt:
                tmp=list(filter(lambda x: x not in answer,i))
                answer.extend(tmp)
                ls.remove(i)
                break
    print(answer)
    return answer



solution("{{20,111},{111}}")