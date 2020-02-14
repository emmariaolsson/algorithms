"""
Given a n*n adjacency array.
it will give you a maximum flow.
This version use DFS to search path.

Assume the first is the source and the last is the sink.

Time complexity - O(Ef)

example

graph = [[0, 16, 13, 0, 0, 0], 
        [0, 0, 10, 12, 0, 0], 
        [0, 4, 0, 0, 14, 0], 
        [0, 0, 9, 0, 0, 20], 
        [0, 0, 0, 7, 0, 4], 
        [0, 0, 0, 0, 0, 0]] 

answer should be

23

"""
import copy
import math

def maximum_flow_dfs(adjacency_matrix):
    #initial setting
    checked = 0
    visited_Branches = [0] * 11
    print("\n")
    new_array = copy.deepcopy(adjacency_matrix)
    total = 0

    while(1):
        visited_Branches[0] = 1
        #setting min to max_value
        min = math.inf
        #save visited nodes
        visited = [0]*len(new_array)
        #save parent nodes
        path = [0]*len(new_array)
        
        #initialize stack for DFS
        stack = []

        #initial setting 
        visited[0] = 1
        stack.append(0)

        #DFS to find path
        while(len(stack) > 0):
            visited_Branches[1] = 1
            #pop from queue
            src = stack.pop()
            for k in range(len(new_array)):
                visited_Branches[2] = 1
                #checking capacity and visit
                if(new_array[src][k] > 0 and visited[k] == 0 ):
                    visited_Branches[3] = 1
                    #if not, put into queue and chage to visit and save path
                    visited[k] = 1
                    stack.append(k)
                    path[k] = src
                else:
                    visited_Branches[4] = 1
            
        #if there is no path from src to sink
        if(visited[len(new_array) - 1] == 0):
            visited_Branches[5] = 1
            break
        else:
            visited_Branches[6] = 1
        
        #initial setting
        tmp = len(new_array) - 1

        #Get minimum flow
        while(tmp != 0):
            visited_Branches[7] = 1
            #find minimum flow
            if(min > new_array[path[tmp]][tmp]):
                visited_Branches[8] = 1
                min = new_array[path[tmp]][tmp]
            else:
                visited_Branches[9] = 1
            tmp = path[tmp]

        #initial setting
        tmp = len(new_array) - 1

        #reduce capacity
        while(tmp != 0):
            visited_Branches[10] = 1
            new_array[path[tmp]][tmp] = new_array[path[tmp]][tmp] - min
            tmp = path[tmp]

        total = total + min

    for i in range(len(visited_Branches)):
        checked += (1 if visited_Branches[i] == 1 else 0)
    print(visited_Branches)
    print(str(checked/len(visited_Branches))+"%")
    
    return total
    