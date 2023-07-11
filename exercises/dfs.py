"""
Depth-First Search

By: Juan Muniain, Miguel Angel Bustamante, and Do Hyun Nam

Last modification date: 25/09/2022
"""

def dfs(graph, node):
  visited, stack = list(), [node]
  while stack:
    vertex = stack.pop()
    if vertex not in visited:
      visited.append(vertex)
      stack.extend([node for node in graph[vertex] if node not in visited])
      print(vertex)

  print(visited)

  return visited

def main():
  graph1 = {
    '1': ['2','3','4'],
    '2': ['1','3','5','6'],
    '3': ['1','2','7','8'],
    '4': ['1','8'],
    '5': ['2'],
    '6': ['2'],
    '7': ['3','9'],
    '8': ['3','4'],
    '9': ['7']
  }

  # DFS testing
  print("\n Running DFS in graph 1")
  dfs(graph1, "1")

if __name__ == '__main__':
  main()
  