"""
Given a n*n adjacency array.
it will give you a maximum flow.
This version use BFS to search path.

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
import queue
import math

def maximum_flow_bfs(adjacency_matrix):
    branches = [0]*11

    #initial setting
    new_array = copy.deepcopy(adjacency_matrix)
    total = 0

    while(1):
        branches[0] = 1 #for measuring branch coverage
        #setting min to max_value
        min = math.inf
        #save visited nodes
        visited = [0]*len(new_array)
        #save parent nodes
        path = [0]*len(new_array)
        
        #initialize queue for BFS
        bfs = queue.Queue()

        #initial setting 
        visited[0] = 1
        bfs.put(0)

        #BFS to find path
        while(bfs.qsize() > 0):
            branches[1] = 1
            #pop from queue
            src = bfs.get()
            for k in range(len(new_array)):
                branches[2] = 1
                #checking capacity and visit
                if(new_array[src][k] > 0 and visited[k] == 0 ):
                    branches[3] = 1
                    #if not, put into queue and chage to visit and save path
                    visited[k] = 1
                    bfs.put(k)
                    path[k] = src
                else:
                    branches[4] = 1
            
        #if there is no path from src to sink
        if(visited[len(new_array) - 1] == 0):
            branches[5] = 1
            break
        else:
            branches[6] = 1
        
        #initial setting
        tmp = len(new_array) - 1

        #Get minimum flow
        while(tmp != 0):
            branches[7] = 1
            #find minimum flow
            if(min > new_array[path[tmp]][tmp]):
                branches[8] = 1
                min = new_array[path[tmp]][tmp]
            else:
                branches[9] = 1
            tmp = path[tmp]
            

        #initial setting
        tmp = len(new_array) - 1

        #reduce capacity
        while(tmp != 0):
            branches[10] = 1
            new_array[path[tmp]][tmp] = new_array[path[tmp]][tmp] - min
            tmp = path[tmp]

        total = total + min
    codeCoverage(branches)
    return total

def codeCoverage(branches):
    print("Check out this coverage:")
    print(branches)

