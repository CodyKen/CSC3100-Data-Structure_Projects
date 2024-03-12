import sys
sys.setrecursionlimit(2000000)
g_length = 0

class Edge:
    def __init__(self, root, length, next_node, next_edge):
        self.root = root
        self.length = length
        self.next_node = next_node
        self.next_edge = next_edge

    def add(self, node):
        self.next_edge = node

def build_tree(p_count_black, p_edges, p_ends, p_color, p_n, p_total_black):
    # 建造树的代码块
    global g_length
    
    for i in p_color:
        if i == 1:
            p_total_black += 1  # 记录总的黑节点数

    for j in range(p_n - 1):
        edge_data_lst = list(map(int, input().split()))
        edge = Edge(edge_data_lst[0], edge_data_lst[1], j + 2, None)
        index = edge.root - 1
        if p_edges[index] == None:
            p_edges[index] = edge
            p_ends[index] = edge

        else:
            # 同根
            if p_edges[index].root == edge.root:
                p_ends[index].add(edge)
                p_ends[index] = edge
            else:
                # 不同根
                # 首先保险先过一遍为空的情况
                if p_edges[index] == None:
                    p_edges[index] = edge
                    p_ends[index] = edge
                else:
                    if p_ends[index] == None: # 末端节点为空,直接将该处edge指向当前子树
                        p_edges[index].next_edge = edge
                    else:
                        # 末端节点不为空，直接将末端节点指向当前子树
                        p_ends[index].next_edge = edge
                    
                    p_ends[index] = edge

    dfs (0, p_edges[0], p_color, p_edges, p_count_black, p_total_black)


def dfs(p_node, p_edge, p_color, p_edges, p_count_black, p_total_black):
    global g_length
    sum_black = p_color[p_node]
    while p_edge != None:  # 开始遍历子树
        root = p_edge.next_node - 1
        next_node = root  # 向下定义一个新的根节点
        sum_black += dfs(next_node, p_edges[next_node], p_color, p_edges, p_count_black, p_total_black)  # 递归计算黑节点数
        g_length += (p_total_black - p_count_black[next_node]) * p_count_black[next_node] * p_edge.length  # 规律性公式
        p_edge = p_edge.next_edge

    p_count_black[p_node] = sum_black
    return sum_black


def main():
    n = eval(input())
    total_black = 0  # 记录总的黑色节点数
    # color = [0] * n  # 记录每个节点的颜色
    count_black = [0] * n  # 记录每个节点的子树中黑色节点的数量
    edges = [None] * n  # 存储树的结构
    ends = [None] * n
    color = list(map(int, input().split()))  # 记录每个节点的颜色

    build_tree(count_black, edges, ends, color, n, total_black)
    print(g_length)
    

main()
