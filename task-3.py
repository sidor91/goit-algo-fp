import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v, weight):
        # Додаємо ребро з вершини u до v з вагою weight
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []

        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))

    def dijkstra(self, start):
        # Ініціалізація відстаней як нескінченність
        distances = {vertex: float('inf') for vertex in self.adjacency_list}
        distances[start] = 0

        # Бінарна купа (пріоритетна черга)
        priority_queue = [(0, start)]  # (відстань, вершина)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Якщо знайдена коротша відстань, пропускаємо
            if current_distance > distances[current_vertex]:
                continue

            # Перевіряємо сусідів
            for neighbor, weight in self.adjacency_list[current_vertex]:
                distance = current_distance + weight

                # Якщо знайдено коротший шлях до сусіда
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

if __name__ == "__main__":
  g = Graph()
  g.add_edge('A', 'B', 1)
  g.add_edge('A', 'C', 4)
  g.add_edge('B', 'C', 2)
  g.add_edge('B', 'D', 5)
  g.add_edge('C', 'D', 1)

  start_vertex = 'A'
  shortest_paths = g.dijkstra(start_vertex)

  print(f"Найкоротші відстані від вершини '{start_vertex}':")
  for vertex in shortest_paths:
    print(f"{vertex}: {shortest_paths[vertex]}")