import random
import timeit
import colorama


def merge_sort(arr):
    """
    Алгоритм сортування злиттям
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    """
    Функція для злиття двох відсортованих масивів
    """
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
    # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(lst):
    """
    Алгоритм сортування вставками
    """
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


_sorted_array = [i for i in range(10000)]


def sorted_array():
    """
    Повертає відсортований масив
    """
    return _sorted_array.copy()


_lightly_unsorted_array = [2, 1] + [(i + 2) for i in range(9998)]


def lightly_unsorted_array():
    """
    Повертає массив що потребує 1 операцію сортування в ідеальному випадку
    """
    return _lightly_unsorted_array.copy()


def get_random_array(size):
    """
    Повертає масив випадкових чисел
    """
    return [random.randint(0, 10000) for _ in range(size)]


_control_array = get_random_array(10000)


def control_array():
    """
    Повертає масив випадкових чисел для контрольного тесту алгоритмів (не відсортований)
    """
    return _control_array.copy()


def test_sorting_algorithm_time(sort_function, array):
    start_time = timeit.default_timer()
    sort_function(array)
    end_time = timeit.default_timer()
    return end_time - start_time


def test_algorythm(sort_function):
    return {
        "sorted_array": test_sorting_algorithm_time(sort_function, sorted_array()),
        "lightly_unsorted_array": test_sorting_algorithm_time(
            sort_function, lightly_unsorted_array()
        ),
        "control_array": test_sorting_algorithm_time(sort_function, control_array()),
        "random_array": [
            test_sorting_algorithm_time(sort_function, get_random_array(10000))
            for _ in range(10)
        ],
    }


def print_test_results(test_results, algorythm_name):
    print(f"{colorama.Fore.CYAN}{algorythm_name}{colorama.Fore.RESET}")
    for key, value in test_results.items():
        print(
            f"{key} {colorama.Fore.GREEN}: {(sum(value) / len(value)) if isinstance(value, list) else value} {colorama.Fore.RESET}"
        )


def calculate_averages(data_list):

    sums = {}
    counts = {}

    for item in data_list:
        for key, value in item.items():
            if key not in sums:
                sums[key] = 0
                counts[key] = 0
            sums[key] += sum(value) if isinstance(value, list) else value
            counts[key] += len(value) if isinstance(value, list) else 1

    result = {}
    for key in sums:
        result[key] = sums[key] / counts[key]

    return result


tests = {"insertion_sort": [], "merge_sort": [], "sorted": []}

for i in range(5):
    print(f"{i} {colorama.Fore.GREEN}: TEST{i+1} {colorama.Fore.RESET}")
    insertion_result = test_algorythm(insertion_sort)
    merge_result = test_algorythm(merge_sort)
    sorted_result = test_algorythm(sorted)

    tests["insertion_sort"].append(insertion_result)
    tests["merge_sort"].append(merge_result)
    tests["sorted"].append(sorted_result)

    print_test_results(insertion_result, "insertion_sort")
    print_test_results(merge_result, "merge_sort")
    print_test_results(sorted_result, "sorted")


print(f"{i} {colorama.Fore.GREEN}: AVERAGE Results  {colorama.Fore.RESET}")

print_test_results(calculate_averages(tests["insertion_sort"]), "insertion_sort")
print_test_results(calculate_averages(tests["merge_sort"]), "merge_sort")
print_test_results(calculate_averages(tests["sorted"]), "sorted")


# print_test_results(test_algorythm(insertion_sort), "insertion_sort")
"""
insertion_sort
sorted_array : 0.0007176250219345093 
lightly_unsorted_array : 0.0007210420444607735 
control_array : 1.0552957919426262 
random_array : 1.0638186459080317 
"""
# print_test_results(test_algorythm(merge_sort), "merge_sort")
"""
merge_sort
sorted_array : 0.011658957926556468 
lightly_unsorted_array : 0.011492667021229863 
control_array : 0.014473582967184484 
random_array : 0.014075087511446326 
"""
# print_test_results(test_algorythm(sorted), "sorted")
"""
sorted
sorted_array : 4.333304241299629e-05 
lightly_unsorted_array : 4.216702654957771e-05 
control_array : 0.0007953330641612411 
random_array : 0.0008173208101652562 
"""
