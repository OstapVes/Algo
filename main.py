def valid(arr, val, angry_cows):
    counter = 1
    temp_element = arr[0]
    for i in range(len(arr)):
        if arr[i] - temp_element >= val:
            counter += 1
            temp_element = arr[i]
            if counter >= angry_cows:
                return True
    return False


def main():
    aggressive_cows_number = int(input("Кількість агресивних корів:"))
    arr = list(map(int, input("Стійла:").split()))
    arr.sort()
    right_index = arr[len(arr) - 1]
    left_index = 1
    ans = 0
    while left_index < right_index:
        mid_index = left_index + (right_index - left_index) // 2
        if valid(arr, mid_index, aggressive_cows_number):
            ans = mid_index
            left_index = mid_index + 1
        else:
            right_index = mid_index
    print("Мінімальне значення максимальної дистанції: " + str(ans))


if __name__ == "__main__":
    main()
