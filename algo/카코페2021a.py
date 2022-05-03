def solution(id_list, report, k):
    
    n = len(id_list)
    rn = len(report)
    report_who = {}
    reported = {}
    
    for i in range(n):
        report_who[id_list[i]] = []
        reported[id_list[i]] = 0
    
    for i in range(rn):
        q = report[i].split()
        report_who[q[0]].append(q[1])

    for i in range(n):
        report_who[id_list[i]] = list(set(report_who[id_list[i]]))
        
        for j in range(len(report_who[id_list[i]])):
            reported[report_who[id_list[i]][j]] += 1
            
    
    
    answer = [0]*n
    
    for i in range(n):
        line = report_who[id_list[i]]
        feed = 0
        for j in range(len(line)):
            if reported[line[j]] >= k:
                feed += 1
        
        answer[i] = feed
        feed = 0            
    
    return answer



solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)