from math import inf


def prim(vertexs, edges):
    distances = {vertex: inf for vertex in vertexs}
    distances[vertexs[0]] = 0  # head, entry point

    for vertexs, cost in edges.items():
        vertex, next_vertex = vertexs
        weight = distances[vertex]
        if distances[next_vertex] > weight + cost:
            distances[next_vertex] = weight + cost

    return distances


if __name__ == '__main__':
    vertexs = ['a', 'b', 'c', 'd', 'e', 'f']
    edges = {
        ('a', 'b'): 7,
        ('a', 'c'): 9,
        ('a', 'f'): 14,
        ('b', 'c'): 10,
        ('b', 'd'): 15,
        ('c', 'd'): 11,
        ('c', 'f'): 2,
        ('d', 'e'): 6,
        ('e', 'f'): 9
    }

    distances = prim(vertexs, edges)
    print(distances)
