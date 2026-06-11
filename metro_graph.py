import heapq

class MetroGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # undirected

    def dijkstra(self, start, end):
        pq = [(0, start)]
        dist = {node: float('inf') for node in self.graph}
        parent = {node: None for node in self.graph}

        dist[start] = 0

        while pq:
            curr_dist, node = heapq.heappop(pq)

            if curr_dist > dist[node]:
                continue

            for neighbor, weight in self.graph[node]:
                new_dist = curr_dist + weight

                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    parent[neighbor] = node
                    heapq.heappush(pq, (new_dist, neighbor))

        return dist, parent

    def get_path(self, parent, start, end):
        path = []
        curr = end

        while curr is not None:
            path.append(curr)
            curr = parent[curr]

        path.reverse()

        return path if path and path[0] == start else []

    # 💰 FARE CALCULATION
    def calculate_fare(self, distance):
        rate_per_km = 2  # you can change this
        return distance * rate_per_km
