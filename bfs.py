from _collections import deque


def bfs(dic, cur, queue=deque(), visited=[]):
    visited.append(cur)
    for next in dic[cur] - set(visited):
        queue.append(next)

    while queue:
        next = queue.popleft()
        bfs(dic, next, queue, visited)

    return visited


dic = {
    1: set([2, 5]),
    2: set([3]),
    3: set([]),
    4: set([7]),
    5: set([2, 6]),
    6: set([7]),
    7: set([2])
}

if __name__ == '__main__':
    visited = bfs(dic, 1)
    print(visited)
