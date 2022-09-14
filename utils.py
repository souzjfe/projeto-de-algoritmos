from cmath import inf, sqrt
from time import process_time
from math import inf


def file_reader(path : str):
    with open(path, 'r') as file:
        file = file.read()
        file = file.split()
    return euclidian_graph(file, file.index('NODE_COORD_SECTION') + 1)
    

def euclidian_graph(file : list, graph_start : int):
    i = graph_start
    coords = list()
    try:
        while(file[i].isnumeric()):
            coords.append((int(file[i + 1]), int(file[i + 2])))
            i += 3
    except:
         while(file[i].isnumeric()):
            coords.append((float(file[i + 1]), float(file[i + 2])))
            i += 3

    graph = list()
    for x in range(len(coords)):
        node_distance = list()
        for y in range(len(coords)):
            if x == y:
                node_distance.append(inf)
            else:
                node_distance.append(pow(pow(coords[x][0] - coords[y][0], 2) + pow(coords[x][1] - coords[y][1], 2), 0.5))
        graph.append(tuple(node_distance))

    return tuple(graph)

def upperrow_graph(file : list, graph_start : int):
    graph = []
    begin = file.index('EDGE_WEIGHT_SECTION') + 1
    dimension = int(file[file.index('DIMENSION') + 1])

    for index in range(dimension - 1):
        line = []

        for line_index in range(dimension - 1):
            line.append(inf)
        graph.append(line)

    upperrow = []
    while(file[begin] != 'EOF'):
        upperrow.append(file[i])
        begin += 1
    
    index = 0
    for i in range(dimension - 1):
        for j in range(i + 1, dimension - 1):
            graph[i][j] = float(upperrow[index])
            graph[j][i] = float(upperrow[index])
            index += 1

    return tuple(graph)

def greedy_TSP(graph):
    traveled = [0]
    distance = 0
    current = 0
    begin = process_time()

    while(len(traveled) != len(graph)):
        min_distance = min_index = inf

        for index in range(len(graph)):
            if index in traveled:
                pass
            else:
                if graph[current][index] < min_distance:
                    min_distance = graph[current][index]
                    min_index = index
        current = min_index
        traveled.append(current)
        distance += min_distance
    distance += graph[current][0]
    
    return distance, process_time() - begin, traveled


if __name__ == '__main__':
    files = ['TSPLIB/a280.tsp', 'TSPLIB/ali535.tsp', 'TSPLIB/att532.tsp', 'TSPLIB/berlin52.tsp', 'TSPLIB/bier127.tsp', 'TSPLIB/brd14051.tsp', 'TSPLIB/burma14.tsp', 'TSPLIB/d198.tsp', 'TSPLIB/fl417.tsp', 'TSPLIB/rat575.tsp']
    
    for file in files:
        print(file_reader(file))