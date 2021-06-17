def merge_sort(array: list):
    size = len(array)
    if size == 1:
        return

    mid = size // 2

    left = array[:mid]
    merge_sort(left)

    right = array[mid:]
    merge_sort(right)

    index = 0

    while len(left) and len(right):
        if left[0] < right[0]:
            array[index] = left.pop(0)
            index += 1
        else:
            array[index] = right.pop(0)
            index += 1

    if len(left):
        array[index: index + len(left)] = left
        index += len(left)

    if len(right):
        array[index:] = right


if __name__ == '__main__':
    import random

    randomlist = [random.randint(1, 30) for x in range(0, 10)]

    print(randomlist)
    merge_sort(randomlist)
    print(randomlist)
