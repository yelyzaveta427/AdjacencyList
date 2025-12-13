import time
from typing import Dict, List, Callable
from graph_generation import generate_unweighted_undirected_graph
def estimate_algorithm_time(
        num_vertices: int,
        density: float,
        algorithm: Callable[[Dict[int, List[int]]], bool]) -> tuple[Dict[int, List[int]], bool, float]:

    print(f"Generation of graph with з V={num_vertices} and D={density}...")
    try:
        graph = generate_unweighted_undirected_graph(num_vertices, density)
    except ValueError as e:
        print(f"Mistake of generation: {e}")
        return {}, False, 0.0

    start_time = time.perf_counter()

    result = algorithm(graph)

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    return graph, result, execution_time