def dfs(dic, cur, visited=[]):
    visited.append(cur)
    for next in dic[cur] - set(visited):
        if next not in visited:
            dfs(dic, next, visited)
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
    visited = dfs(dic, 1)
    print(visited)
