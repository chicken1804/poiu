
graph={
    'A':['B','C','D'],
    'B':['A','D'],
    'C':['A','E'],
    'D':['A','C','E'],
    'E':['C','D']
    
    
}
visited=[]
queue=[]
# def dfs(node,visited,graph):
#     if node not in visited:
#         print(node)
#         visited.append(node)
#         for i in graph[node]:
#             dfs(i,visited,graph)
            
# dfs('A',visited,graph)            

def bfs(node,visited,graph):
    visited.append(node)
    queue.append(node)
    while(queue):
        m=queue.pop(0)
        print(m ,'\n')
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    
            
bfs('A',visited,graph) 
# dfs('Devgad',visited,graph) 

