function bfsShortestPath(graph, start, target) {
  const queue = [start];
  const visited = new Set();
  visited.add(start);
  const parent = {};
  parent[start] = null;
  while (queue.length > 0) {
    const current = queue.shift();
    if (current === target) {
      const path = [];
      let node = target;
      while (node !== null) {
        path.push(node);
        node = parent[node];
      }
      return path.reverse();
    }
    for (const neighbor of graph[current]) {
      if (!visited.has(neighbor)) {
        visited.add(neighbor);
        parent[neighbor] = current;
        queue.push(neighbor);
      }
    }
  }
  return null;
}

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

console.log(bfsShortestPath(graph, 'A', 'F'));
