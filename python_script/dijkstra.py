#! --*-- coding: utf-8 --*--


class Dijkstra(object):
    """
    Dijkstra算法 求地图上点的最短路径
    迪杰斯特拉(Dijkstra)算法是典型最短路径算法，用于计算一个节点到其他节点的最短路径。
    它的主要特点是以起始点为中心向外层层扩展(广度优先搜索思想)，直到扩展到终点为止

    基本思想
        1. 通过Dijkstra计算图G中的最短路径时，需要指定起点s(即从顶点s开始计算)。

        2. 此外，引进两个集合S和U。S的作用是记录已求出最短路径的顶点(以及相应的最短路径长度)，而U则是记录还未求出最短路径的顶点(以及该顶点到起点s的距离)。

        3. 初始时，S中只有起点s；U中是除s之外的顶点，并且U中顶点的路径是”起点s到该顶点的路径”。然后，从U中找出路径最短的顶点，并将其加入到S中；
           接着，更新U中的顶点和顶点对应的路径。 然后，再从U中找出路径最短的顶点，并将其加入到S中；接着，更新U中的顶点和顶点对应的路径。 … 重复该操作，直到遍历完所有顶点。

    操作步骤
        1. 初始时，S只包含起点s；U包含除s外的其他顶点，且U中顶点的距离为”起点s到该顶点的距离”[例如，U中顶点v的距离为(s,v)的长度，然后s和v不相邻，则v的距离为∞]。

        2. 从U中选出”距离最短的顶点k”，并将顶点k加入到S中；同时，从U中移除顶点k。

        3. 更新U中各个顶点到起点s的距离。之所以更新U中顶点的距离，是由于上一步中确定了k是求出最短路径的顶点，从而可以利用k来更新其它顶点的距离；例如，(s,v)的距离可能大于(s,k)+(k,v)的距离。

        4. 重复步骤(2)和(3)，直到遍历完所有顶点。
    """

    def __init__(self, graph, labels):
        """
        :param graph: 字典类型, 显示各个点之间距离
        :param labels: 列表类型, 所有的点的集合
        """
        self.graph = graph
        self.labels = labels

    def sort_dict(self, d):
        """
        根据距离从短到长排序
        :param d: 字典格式 {点: [到起始点距离, [起始点到该点中间路径]]}, 举例: {'A': (22, ['D', 'E', 'F']), 'B': (13, ['D', 'C'])}
        :return: 排序好的列表格式 举例: [('B', (13, ['D', 'C'])), ('A', (22, ['D', 'E', 'F']))]
        """
        return sorted(d.iteritems(), key=lambda x: x[1][0])

    def distance(self, s_node, e_node=None):
        """
        :param s_node: 初始节点
        :param e_node: 最终节点 可为空, 为空时返回起始点到所有初始节点的距离信息
        :return: 字典格式 最终节点不为空时: 返回起始节点到终结点的距离信息
                         最终节点为空时: 返回起始点到所有初始节点的距离信息
        """
        graph = self.graph
        labels = self.labels

        if e_node and e_node not in labels:
            raise Exception, "The end node: %s not in labels: % s" % (e_node, labels)

        U = {}
        S = {s_node: (0, )}  # float('inf'):  # 正无穷
        for node in labels:
            if node == s_node:
                U[node] = (0, [])
            elif node in graph.get(node, {}):
                U[node] = (graph[s_node][node], [])
            else:
                U[node] = (float('inf'), [])

        while len(S) < len(labels):

            if not U:
                break

            # 取最短路径信息, 放到S, 从U中剔除
            shortest = self.sort_dict(U)[0]
            current_node, (current_distance, current_path) = shortest
            if e_node and current_node == e_node:
                return {current_node: (current_distance, current_path + [current_node])}

            S[current_node] = (current_distance, current_path + [current_node])
            U.pop(current_node)

            # 更新 U 的距离数据
            shortest_info = graph.get(current_node, {})
            for node, distance in shortest_info.iteritems():
                if node in S:
                    continue
                if node not in U:
                    continue
                if U[node][0] > current_distance + distance:
                    U[node] = (current_distance + distance, current_path + [current_node])
        return S

if __name__ == '__main__':
    map_ = {
        "A": {"B": 12, "F": 16, "G": 14},
        "B": {"A": 12, "F": 7, "C": 10},
        "C": {"B": 10, "F": 6, "E": 5, "D": 3},
        "D": {"C": 3, "E": 4},
        "E": {"C": 5, "D": 4, "F": 2, "G": 8},
        "F": {"A": 16, "B": 7, "C": 6, "E": 2, "G": 9},
        "G": {"A": 14, "E": 8, "F": 9}
    }
    di = Dijkstra(map_, list('ABCDEFG'))

    # D 点到 A 的距离和中间路径
    print di.distance('D', 'A')
    print
    # D 点到其他店的距离路径
    print di.distance('D')