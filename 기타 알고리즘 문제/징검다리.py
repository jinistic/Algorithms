from collections import deque

def solution(arr):
    N = len(arr)
    visited = [-1] * N
    queue = deque()
    queue.append(0)
    visited[0] = 0

    while queue:
        now = queue.popleft()
        next = now + arr[now]
        if next == N - 1:
            return visited[now] + 1
        elif next < N - 1 and visited[next] == -1:
            visited[next] = visited[now] + 1
            queue.append(next)

        next = now - arr[now]
        if next > 0 and visited[next] == -1:
            visited[next] = visited[now] + 1
            queue.append(next)

    return(visited[N - 1])

print(solution([4, 5, 1, 2, 1, 2, 3]), 4)
print(solution([4, 4, 1, 2, 1, 2, 3]), -1)
