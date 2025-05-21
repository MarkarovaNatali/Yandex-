"""Мы уже реализовывали функцию merge, которая способна "слить" два отсортированных списка в один.
Чаще всего её применяют в рекурсивном алгоритме сортировки слиянием.

Напишите рекурсивную функцию merge_sort, которая производит сортировку списка."""

def merge_sort(arr):
    if len(arr) <= 1:  # Базовый случай: если список из 0 или 1 элементов, он уже отсортирован
        return arr
    mid = len(arr) // 2  # Находим середину массива
    left_half = merge_sort(arr[:mid])  # Рекурсивно сортируем левую половину
    right_half = merge_sort(arr[mid:])  # Рекурсивно сортируем правую половину
    return merge(left_half, right_half)  # Сливаем две отсортированные части


def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):  # Сливаем два отсортированных списка
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])  # Добавляем оставшиеся элементы
    sorted_arr.extend(right[j:])  # Добавляем оставшиеся элементы
    return sorted_arr


print(merge_sort([3, 1, 5, 3]))
