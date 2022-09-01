def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp
def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)
def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        while elements[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, elements)
    swap(pivot_index, end, elements)
    return end
if __name__ == '__main__':
    a = [4, 6, 3, 8, 3, 8, 9, 0]
    n = len(a) - 1
    quick_sort(a, 0, n)
    print(a)
