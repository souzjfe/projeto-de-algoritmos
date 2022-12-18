from utils import file_reader, greedy_TSP, two_opt, write_table

if __name__ == '__main__':
    best_solutions = [2579, 27686, 7542, 118282, 15780, 11861, 6773]
    files = ['TSPLIB/a280.tsp',  'TSPLIB/att532.tsp', 'TSPLIB/berlin52.tsp', 'TSPLIB/bier127.tsp', 'TSPLIB/d198.tsp', 'TSPLIB/fl417.tsp', 'TSPLIB/rat575.tsp']
    two_opt_solutions = list()
    greedy_solutions = list()
    graph_time = list()
    for file in files:
        graph = file_reader(file)
        greedy_solution = greedy_TSP(graph)
        greedy_solutions.append(greedy_solution[0])
        two_opt_solutions.append(two_opt(graph, greedy_solution[2])[1])
    write_table(graph_name = files, best_solutions = best_solutions, greedy_solutions = greedy_solutions, tow_opt__solutions = two_opt_solutions, name = 'greedy_strategy.md', title='Greedy Strategy')



