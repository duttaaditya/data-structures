def max_pair_product(arr, n):
    arr = [int(x) for x in arr]
    max1 = -1
    for i in range(n):
        if arr[i] > max1:
            id1 = i
            max1 = arr[id1]
    max2 = -1
    for i in range(n):
        if arr[i] > max2 and i != id1:
            max2 = arr[i]
    
    return max1 * max2

if __name__ == "__main__":
    n = int(input())
    input_text = input()
    input_list = input_text.split()
    result = max_pair_product(input_list, n)
    print(result)
