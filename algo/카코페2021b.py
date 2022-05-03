import string
import math

now = string.digits+string.ascii_lowercase

def change(num, base) :
    a, b = divmod(num, base)
    if a == 0 :
        return now[b] 
    else :
        return change(a, base) + now[b]
    

def is_Prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True


def solution(n, k):
#    if k != 10:    
#        changed = change(n,k)
#            
#        now = changed.split('0')
#    else:
#        t = str(n)
#        now = t.split('0')
#    answer = 0
    
    changed = change(n,k)
    answer = 0
    now = changed.split('0')
    for i in range(len(now)):
        if now[i] == '':
            continue
        tmp = int(now[i])
        
        
        if tmp > 2:
            
            if is_Prime(tmp):
                
                answer += 1
        elif tmp == 2:
            answer += 1
    print(answer)
    return answer

