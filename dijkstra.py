import heapq
from math import inf


class Solution:
    def solution(self, N, M, k, A, B, C):
        A, B = [[i - 1 for i in x] for x in [A, B]]
        k -= 1

        def dijkstra(graph):
            city_paths = [set() for i in range(M)]
            for i, j in graph:
                city_paths[i].add(j)
            distances = [inf] * N
            distances[k] = 0
            queue = [i for i in range(N)]
            heapq.heapify(queue)
            while queue:
                city = heapq.heappop(queue)
                for next_city in city_paths[city]:
                    weight = distances[city] + graph[(city, next_city)]
                    if weight < distances[next_city]:
                        distances[next_city] = weight
                        heapq.heappush(queue, next_city)
            return distances

        go = dijkstra({(A[i], B[i]): C[i] for i in range(M)})
        back = dijkstra({(B[i], A[i]): C[i] for i in range(M)})
        return max(map(lambda x, y: x + y, go, back))


if __name__ == '__main__':
    N = 10
    M = 50
    k = 10
    A = [
        1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5,
        5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10,
        10, 10, 10
    ]
    B = [
        10, 4, 1, 7, 6, 2, 9, 4, 6, 1, 3, 1, 6, 10, 4, 5, 2, 6, 4, 8, 5, 1, 8,
        10, 4, 2, 10, 8, 3, 4, 10, 8, 9, 1, 3, 9, 6, 4, 1, 7, 9, 7, 10, 8, 6,
        5, 1, 2, 9, 4
    ]
    C = [
        97, 36, 45, 12, 71, 4, 98, 41, 22, 91, 47, 43, 16, 79, 85, 62, 70, 61,
        94, 69, 92, 83, 74, 75, 58, 15, 100, 40, 15, 75, 48, 12, 43, 19, 68,
        60, 88, 44, 68, 22, 18, 33, 53, 51, 83, 18, 41, 82, 37, 82
    ]

    S = Solution()
    result = S.solution(N, M, k, A, B, C)
    print(result)
