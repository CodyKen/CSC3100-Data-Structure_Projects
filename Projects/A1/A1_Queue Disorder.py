N = input()             # Number of people in the quene
height = input()    # Heights of people in the queue
list_height = height.split()   # Transfer the data into a list
list_height = [int(x) for x in list_height]
n = 0               # Define a counter

def Count_Disorder(lst):
    global n
    if len(lst) > 1:
        left_lst = lst[:len(lst)//2]
        right_lst = lst[len(lst)//2:]

        # recursion
        Count_Disorder(left_lst)
        Count_Disorder(right_lst)

        # merge
        i = 0  # left list index
        j = 0  # right list index
        k = 0  # merged list index
        mid = len(lst) // 2
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] <= right_lst[j]:
                lst[k] = left_lst[i]
                i += 1
            else:
                lst[k] = right_lst[j]
                j += 1
                n += mid - i
            k += 1

        while i < len(left_lst):
            lst[k] = left_lst[i]
            i += 1
            k += 1
        
        while j < len(right_lst):
            lst[k] = right_lst[j]
            j += 1
            k += 1
    
Count_Disorder(list_height)
print(n)