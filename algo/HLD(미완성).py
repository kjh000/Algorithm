# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 17:26:35 2020

@author: kjh1
"""
N = 10**5 + 5
adj = {}
chain = {}
for i in range(N):
    adj[i] = []
    chain[i] = []
sz = [0]*N
par = [0]*N

def dfs(i,p):
    par[i] = p
    sz[i] = 1
    
    for x in adj[i]:
        if x != p:
            sz[i] += dfs(x,i)
    
    return sz[i]

depth = [0]*N
chain_number = [0]*N
chain_index = [0]*N

def HLD(i,p,cur_chain,d):
    depth[i] = d
    chain_number[i] = cur_chain
    chain_index[i] = len(chain[cur_chain])
    chain[cur_chain].append(i)
    
    heavy = -1
    
    for x in adj[i]:
        if x != p and (heavy == -1 or sz[x] > sz[heavy]):
            heavy = x
    
    if heavy != -1:
        HLD(heavy,i,cur_chain,d)
        
    for x in adj[i]:
        if x !=p and x!= heavy:
            HLD(x,i,x,d+1)
            
            