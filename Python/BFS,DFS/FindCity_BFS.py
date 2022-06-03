# 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리정보 K, 출발도시의 번호 X 가 주어진다.
# 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 주어지며 각 자연수는 공백으로 구분한다.
# 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미이다. 단, A와 B는 서로 다른 자연수이다.
# 출력 조건은 X로부터 출발하여 도달할 수 있는 도시 중에서 최단거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
# 이 때, 도달할 수 있는 도시중에서, 최단거리가 K인 도시가 하나도 존재하지 않는다면 -1을 출력한다.
from collections import deque
n, m, k, x = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]

node = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 출발도시 번호를 deque에 삽입

# 모든 도시에 대한 최단거리 초기화
distance = [-1] * (n+1)
#출발도시에 대한 거리는 0
distance[x] = 0


def bfs(n, m , k ,x):
    global distance
    queue = deque([x])
    
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[q] + 1
                if distance[i] == k:
                    node.append(i)
                    node.sort()
            else:
                continue

bfs(n ,m, k, x)
if len(node) == 0:
    print("-1")
else:
    for i in range(len(node)):
        print(node[i])