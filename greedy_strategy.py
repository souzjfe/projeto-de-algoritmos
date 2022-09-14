from utils import file_reader, greedy_TSP

if __name__ == '__main__':
    files = ['TSPLIB/a280.tsp', 'TSPLIB/ali535.tsp', 'TSPLIB/att532.tsp', 'TSPLIB/berlin52.tsp', 'TSPLIB/bier127.tsp', 'TSPLIB/burma14.tsp', 'TSPLIB/d198.tsp', 'TSPLIB/fl417.tsp', 'TSPLIB/rat575.tsp']
    string = 'NOME DO ARQUIVO  DISTANCIA  TEMPO  ROTA\n'
    for file in files:
        graph = file_reader(file)
        solution = greedy_TSP(graph)
        string += f'{file}  {solution[0]}  {solution[1]}\n'
    with open('output.txt', 'w') as file:
        file.write(string)



