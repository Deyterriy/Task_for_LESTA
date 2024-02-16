def merge_sort(arr):
    """Сортировка слиянием"""
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


arr = [1, 5, 2, 7, 8, 12, 1, 35, 67, 54, 3]
print(merge_sort(arr))

# Сложность алгоритма - nLog(n) - один из самых быстрых для большого объема данных
# сохраняет порядок одинаковых элементов в исходном массиве
# Сортировать можно любые типы данных, которые можно сравнить
# простая реализация.
