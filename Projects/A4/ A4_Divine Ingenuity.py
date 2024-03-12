import heapq

GRAPH = {}
FIELD = []
START_COOR = (0,0)
END_COOR = (0,0)


def main():
    global START_COOR, END_COOR
    m, n = map(int, input().split())  # m lines total, n columns total
    for i in range(m):
        line_info = list(input())
        FIELD.append(line_info)
    init_graph(m, n)


def init_graph(p_m, p_n):
    global START_COOR, END_COOR
    # Here use l to denote number of line, use c to denote number of column
    for l in range(p_m):
        for c in range(p_n):
            if FIELD[l][c] == 'i':
                START_COOR = (l, c)
            if FIELD[l][c] == 'j':
                END_COOR = (l, c)
            expand_neighbor(p_m, p_n, l, c)

    print(Dijkstra(p_m, p_n))


def expand_neighbor(p_m, p_n, p_l, p_c):
    adjacent = {}
    # initial state, to avoid x
    if p_l - 1 >= 0:
        adjacent[(p_l-1, p_c)] = 1
    if p_l <= p_m - 2:  # p_l + 1 <= p_m - 1
        adjacent[(p_l+1, p_c)] = 1
    if p_c - 1 >= 0:
        adjacent[(p_l, p_c-1)] = 1
    if p_c <= p_n - 2:  # p_c + 1 <= p_n - 1
        adjacent[(p_l, p_c+1)] = 1

    # check starting point
    if FIELD[p_l][p_c] == 'i' and (p_c - 1 >= 0):
        adjacent[(p_l, p_c - 1)] = 0
    if FIELD[p_l][p_c] == 'i' and (p_l <= p_m - 2):  # p_l + 1 <= p_m - 1
        adjacent[(p_l + 1, p_c)] = 0
    if FIELD[p_l][p_c] == 'i' and (p_c <= p_n - 2):  # p_c + 1 <= p_n - 1
        adjacent[(p_l, p_c + 1)] = 0
    if FIELD[p_l][p_c] == 'i' and (p_l - 1 >= 0):
        adjacent[(p_l - 1, p_c)] = 0

    # go along the wind will change the weight to 1
    if FIELD[p_l][p_c] == 'a' and (p_c - 1 >= 0):
        adjacent[(p_l, p_c - 1)] = 0
    if FIELD[p_l][p_c] == 's' and (p_l <= p_m - 2):  # p_l + 1 <= p_m - 1
        adjacent[(p_l + 1, p_c)] = 0
    if FIELD[p_l][p_c] == 'd' and (p_c <= p_n - 2):  # p_c + 1 <= p_n - 1
        adjacent[(p_l, p_c + 1)] = 0
    if FIELD[p_l][p_c] == 'w' and (p_l - 1 >= 0):
        adjacent[(p_l - 1, p_c)] = 0

    GRAPH[p_l, p_c] = adjacent  # update the whole graph

def Dijkstra(p_m, p_n):
    global START_COOR, END_COOR
    weight = []
    # initialize a two dim list
    for i in range(p_m):
        row = []
        for j in range(p_n):
            row.append(float('inf'))
        weight.append(row)

    # print(weight)
    # print(START_COOR[0])
    weight[START_COOR[0]][START_COOR[1]] = 0

    priority_que = [(0, START_COOR)]  # 0 denotes the current shortest distance from the start position to the node
    while len(priority_que) != 0:
        # Removes the node with the smallest current distance from the priority queue
        smallest = heapq.heappop(priority_que)
        # print(smallest,'smallest')

        # Unpack the information about the current node
        cur_weight, (cur_l, cur_c) = smallest

        # Traverse the neighbors of the current node and their weights
        for a, b in GRAPH[cur_l, cur_c].items():
            adj_coor = a
            adj_weight = b
            adj_l = adj_coor[0]
            adj_c = adj_coor[1]
            # Calculates the new distance from the starting position to the neighbor node
            temp_weight = cur_weight + adj_weight

            # If the new distance is smaller than the currently known shortest distance
            # print(adj_l,'adjl')
            # print(adj_c,'adjc')
            if temp_weight < weight[adj_l][adj_c]:
                # update the shortest distance
                weight[adj_l][adj_c] = temp_weight

                # The updated neighbor node is added back to the priority queue
                heapq.heappush(priority_que, (temp_weight, (adj_l, adj_c)))

    ans = weight[END_COOR[0]][END_COOR[1]]
    return ans

main()
