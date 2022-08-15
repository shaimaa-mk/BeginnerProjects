import math


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    # Find the midpoint and divide the list into two
    middle = math.floor(len(unsorted_list)/2)
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]
    left_sort = merge_sort(left_list)
    right_sort = merge_sort(right_list)
    return list(merge(left_sort, right_sort))


def merge(left, right):
    arr = []
    while len(left) != 0 and len(right) != 0:
        print(left, "Left")
        print(right, "Right")
        if left[0] < right[0]:
            arr.append((left[0]))
            left.remove(left[0])
            print(f"left {left}")
        elif right[0] < left[0]:
            arr.append(right[0])
            right.remove(right[0])
            print(f"right{right}")
    if len(left) == 0:
        arr = arr + right
        print(f" where left == 0 {arr}")

    if len(right) == 0:
        arr = arr + left
        print(f" where right == 0 {arr}")

    return arr


unsorted = [64, 34, 120, 12, 22, 70, 90]
print(merge_sort(unsorted))
