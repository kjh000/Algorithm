#N = 10
#tadd = [0]*(N+1)
#tmul = [0]*(N+1)

def inupadate(at,mul,add,tadd,tmul,N):
    if(at<1 or at>N): return
        
    while(at<=N):
        tmul[at] += mul
        tadd[at] += add
        
        at += at&-at
        
def range_update(l,r,by,tadd,tmul,N):
    inupadate(l,by,-by*(l-1),tadd,tmul,N)
    inupadate(r+1,-by,by*r,tadd,tmul,N)
    
def range_query(at,tadd,tmul,N):
    if(at==0): return 0
    if(at<1 or at>N): return 
    
    mul,add = 0,0
    
    i = at
    while i>0:
        mul +=tmul[i]
        add += tadd[i]
        i -= i&-i

    return at*mul + add


def solution(board, skill):
    
    l_cul =len(board)
    l_row = len(board[0])
    lq = len(skill)
    answer = 0
    
    Tree_add = [[0]*(l_row + 1)for _ in range(l_cul)]    
    Tree_mul = [[0]*(l_row + 1)for _ in range(l_cul)]
    
    for i in range(l_cul):
        for j in range(l_row):
            range_update(j+1,j+1,board[i][j],Tree_add[i],Tree_mul[i],l_row)
    
    
    for i in range(lq):
        c1,r1,c2,r2,deg = skill[i][1],skill[i][2],skill[i][3],skill[i][4],skill[i][5]
        if skill[i][0] == 1:
            for j in range(c1,c2+1):
                range_update(r1+1,r2+1,-deg,Tree_add[j],Tree_mul[j],l_row)
                
        else:
            for j in range(c1,c2+1):
                range_update(r1+1,r2+1,deg,Tree_add[j],Tree_mul[j],l_row)
            
    for i in range(l_cul):
        for j in range(l_row):
            qq = range_query(j+1,Tree_add[i],Tree_mul[i],l_row) - range_query(j,Tree_add[i],Tree_mul[i],l_row)
    
            if qq > 0:
                answer += 1
    
    return answer

solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])