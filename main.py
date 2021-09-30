import time, sys, os
from merge_sort import merge_sort, Sort

arr = []
if __name__ == '__main__':

    terminal_input = sys.argv
    sort_type = terminal_input[1]
    if sort_type == "asc":
        sort_type = Sort.ASC
    else:
        sort_type = Sort.DESC

    arr = terminal_input[2].split(",")
    arr = [int(i) for i in arr]

    start_time = time.time()
    comparisons = merge_sort(arr, sort_type)
    end_time = time.time()
    general_time =  start_time - end_time

    print("MergeSort:")
    print("Execution time: ", general_time)
    print("Comparisons", comparisons)
    print(arr)

    command = "python -m unittest test_merge_sort.py"
    os.system(command)

