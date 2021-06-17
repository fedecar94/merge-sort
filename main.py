def merge_sort(array: list) -> list:
    if len(array) == 1:
        return array

    new_array = []

    mid = len(array) // 2

    left = merge_sort(array[:mid])

    right = merge_sort(array[mid:])

    while len(left) and len(right):
        if left[0] < right[0]:
            new_array.append(left.pop(0))
        else:
            new_array.append(right.pop(0))

    if len(left):
        new_array.extend(left)

    if len(right):
        new_array.extend(right)

    return new_array


if __name__ == '__main__':
    import random
    randomlist = []
    for i in range(0, 10):
        n = random.randint(1, 30)
        randomlist.append(n)
    print(merge_sort(randomlist))
