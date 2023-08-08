import random
def contains_numbers(lst):
    return any(isinstance(item, (int, float)) for item in lst)
def binary_search(arr, target): #(/)
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
def main():
    path = str(input('Path of file: '))
    with open(path, "r") as file:
        data = file.read().split()
        list = []
        for item in data:
            if item != ' ' or item != ',':
                if '.' in item:
                    list.append(float(item))
                else:
                    list.append(int(item))
        if contains_numbers(list):
            list.sort()
            print(list)
            target = float(input('What is your target number?: '))
            if target not in list:
                print('Denied, target number not in specified data.')
            else:
                result = binary_search(list, target)
                if result == - 1:
                     print('target value not found')
                else:
                    print(f'Target value found at index: {result}')

        

if __name__ == '__main__':
    main()