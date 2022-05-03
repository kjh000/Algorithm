# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:48:57 2019

@author: kjh1
"""
import copy
departure = 'home'
destination = 'school'

landscape = {
    'home':             {'hairShop':5, 'superMarket':10, 'EnglishAcademy':9},
    'hairShop' :        {'home':5 ,'superMarket':3, 'bank':11},
    'superMarket' :     {'hairShop':3, 'home':10, 'EnglishAcademy':7, 'restourant':3},
    'EnglishAcademy':   {'home':9, 'superMarket':7, 'school':12},
    'restourant' :      {'superMarket':3, 'bank':4},
    'bank' :            {'hairShop':11, 'restourant':4, 'EnglishAcademy':7, 'school':2},
    'school' :          {'bank':2, 'EnglishAcademy':12}
    }

routing = {}
for place in landscape.keys():
    routing[place]={'shortestDist':0, 'route':[], 'visited':0}

#④
def visitPlace(visit):
    routing[visit]['visited'] = 1
    for toGo, betweenDist in landscape[visit].items():
        toDist = routing[visit]['shortestDist'] + betweenDist
        if (routing[toGo]['shortestDist'] >= toDist) or  not routing[toGo]['route']:
            routing[toGo]['shortestDist'] = toDist
            routing[toGo]['route'] = copy.deepcopy(routing[visit]['route'])
            routing[toGo]['route'].append(visit)
            

visitPlace(departure)

while 1 :
    #③
    minDist = max(routing.values(), key=lambda x:x['shortestDist'])['shortestDist']
    toVisit = ''
    for name, search in routing.items():
        if 0 < search['shortestDist'] <= minDist and not search['visited']:
            minDist = search['shortestDist']
            toVisit = name
    #⑤
    if toVisit == '':
        break
    #④
    visitPlace(toVisit)

#    print ("["+toVisit+"]")
#    print ("Dist :", minDist)

print ("\n", "[", departure, "->", destination,"]")
print ("Route : ", routing[destination]['route'])
print ("ShortestDistance : ", routing[destination]['shortestDist'])

#print(routing)
print(type(landscape['home']['hairShop']))
