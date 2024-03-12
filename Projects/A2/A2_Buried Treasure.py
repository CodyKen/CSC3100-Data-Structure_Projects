class Stack:
    def __init__(self):
        self.__data = list()

    def __len__(self):
        return len(self.__data)

    def is_empty(self):
        return len(self.__data) == 0

    def push(self, e):
        self.__data.append(e)

    def top(self):
        if self.is_empty():
            print('The stack is empty.')
        else:
            return self.__data[self.__len__() - 1]

    def pop(self):
        if self.is_empty():
            print('The stack is empty.')
        else:
            return self.__data.pop()

    def printStack(self):
        return self.__data


def identify_square(p_wide, p_depthlist):
    area_square = 0
    left_bound = 0
    depth_stack = Stack()

    for i in range(p_wide):
        while (not depth_stack.is_empty()) and p_depthlist[depth_stack.top()] > p_depthlist[i]:
            cal_height = p_depthlist[depth_stack.pop()]
            if depth_stack.is_empty():
                left_bound = 0
            else:
                left_bound = depth_stack.top() + 1
            area_square = max(area_square, (i - left_bound) * cal_height)

        depth_stack.push(i)

    while not depth_stack.is_empty():
        cal_height = p_depthlist[depth_stack.pop()]
        if depth_stack.is_empty():
            left_bound = 0
        else:
            left_bound = depth_stack.top() + 1
        area_square = max(area_square, (p_wide - left_bound) * cal_height)

    return area_square


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        Widths = int(input())
        Depths = list(map(int, input().split()))
        area_treasure = identify_square(Widths, Depths)
        print(area_treasure)
