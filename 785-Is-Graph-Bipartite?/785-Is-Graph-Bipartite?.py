class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        colors = [0]*len(graph)

        stack = [node for node in range(len(graph))]
        stack.reverse()
        colors[0] = 1
        visited = set()
        visited.add(0)
        is_bipartite = True

        while stack:

            cur_node = stack.pop()

            if colors[cur_node] == 0:

                colors[cur_node] = 1

            cur_color = colors[cur_node]
            adjacent = graph[cur_node]

            for adj_node in adjacent:

                if colors[adj_node] == 0:

                    colors[adj_node] = - cur_color

                elif colors[adj_node] == cur_color:

                    is_bipartite = False
                    break

                if adj_node not in visited:

                    visited.add(adj_node)
                    stack.append(adj_node)

            if is_bipartite is False:

                break

        return is_bipartite
