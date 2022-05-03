import math

def time_gap(t1,t2):
    t1 = t1.split(':')
    t2 = t2.split(':')
    
    minutes1 = int(t1[0])*60 + int(t1[1])
    minutes2 = int(t2[0])*60 + int(t2[1])
    
    return minutes2 - minutes1



def solution(fees, records):
    
    b_time = fees[0]
    b_fee = fees[1]
    p_time,p_fee = fees[2],fees[3]

    total = 0
    cars = []
    car = {}
    rn = len(records)
    
    answer = []
    
    for i in range(rn):
        line = records[i]
        c_num = int(line.split()[1])
        cars.append(c_num)
        
    cars = list(set(cars))
    cars.sort()
#    print(cars)
    for i in range(len(cars)):
        car[cars[i]] = [[],[]]

    for i in range(rn):
        line = records[i].split()
        if line[2] == 'IN':
            car[int(line[1])][0].append(line[0])
        else:
            car[int(line[1])][1].append(line[0])
            
            
    for i in range(len(cars)):
        IN,OUT = car[cars[i]][0],car[cars[i]][1]
        l_in = len(car[cars[i]][0])
        l_out = len(car[cars[i]][1])
        
        time = 0
        for j in range(l_out):
            tmp = time_gap(IN[j],OUT[j])
            time += tmp
        
        if l_in > l_out:
            time += time_gap(IN[-1],'23:59')
        
        if time <= b_time:
            total = b_fee
        else:
            total = b_fee
            
            time -= b_time
            pt = math.ceil(time/p_time)
            
            total += pt*p_fee
            
        
            
        answer.append(total)
        total = 0
    
    return answer



