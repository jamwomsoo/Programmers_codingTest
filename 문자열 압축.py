def solution(s):
    s=list(s)
    t = list()
    tmp =list()
    cnt = 1
    for leng in range(1,int(len(s)/2)+1 ):
        for i in range(0,len(s),leng):
            if s[i:i+leng] == s[i+leng:i+leng+leng]:
                cnt+=1
            else:
                if cnt>1:
                    if cnt>=10:
                        tmp.append(cnt/10)
                        tmp.append(cnt%10)
                    else:
                        tmp.append(cnt)
                    cnt=1
                    tmp.extend(s[i-leng:i])
                else :
                    tmp.extend(s[i:i+leng])
        t.append(len(tmp))
        del tmp[:]
        cnt=1
    if not t:
        t.append(len(s))
    return min(t)