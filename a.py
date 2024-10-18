import heapq
def a_star(graph,heuristics,start,goal):
    o_list=[]
    heapq.heappush(o_list,(heuristics.get(start),0,start,[]))
    came_from={}
    cost_so_far={start:0}

    while o_list:
        f,current_cost,current_node,path = heapq.heappop(o_list)

        if current_node==goal:
            return path+[current_node]
        
        for neighbour , cost in graph.get(current_node,{}).items():
            new_cost=current_cost+cost
            if neighbour not in cost_so_far or new_cost<cost_so_far[neighbour]:
                 cost_so_far[neighbour]=new_cost
                 priority=new_cost + heuristics.get(neighbour, float('inf'))
                 heapq.heappush(o_list,(priority,new_cost,neighbour,path+[current_node]))
                 came_from[neighbour]=current_node

    return None
    
graph={
    'Arad':{'Zerind':75,'Sibiu':140,'Timisora':118},
    'Zerind':{'Arad':75,'Oradia':71},
    'Oradia':{'Zerind':71,'Sibiu':151},
    'Sibiu':{'Oradia':151,'Arad':140,'Rimnica vilcia':80,'Fagarous':99},
    'Rimnicavilcia':{'Sibiu':80,'Pitesthi':97,'Cravoica':146},
    'Piteshti':{'Rimnica vilcia':97,'Cravoica':138,'Bucharest':101},
    'Cravoica':{'Rimnica vilcia':146,'Drobeta':120,'Piteshti':138},
    'Fagarous':{'Sibiu':99,'Bucharest':211},
    'Giurgiu':{'Bucharest':90},
    'Timisora':{'Arad':118,'Lugoj':111},
    'Lugoj':{'Timisora':111,'Mehadia':70},
    'Mehadia':{'Lugoj':70,'Drobeta':75},
    'Drobeta':{'Mehadia':75,'Cravoica':120},
    'Bucharest':{'Fagarous':211,'Pitesthi':101,'Giurgiu':90}
    }
heuristics={
    'Arad':366,'Zerind':374,'Oradia':380,'Sibiu':253,'Rimnica vilcia':193,
    'Piteshti':100,'Cravoica':160,'Fagarous':176,'Giurgiu':77,
    'Timisora':329,'Lugoj':244,'Mehadia':241,'Drobeta':242,'Bucharest':0
}
start_n='Arad'
goal_n='Bucharest'
path=a_star(graph,heuristics,start_n,goal_n)

if path:
    print("Path is",path)
else:
    print("Path not found")


