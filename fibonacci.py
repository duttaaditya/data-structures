def fibonacci(n):
    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    # else:
    #     return fibonacci(n - 1) + fibonacci(n - 2)
    result = []
    if n <= 0:
        result.append(0)
    elif n == 1:
        result.append(1)
    else:
        result.append(0)
        result.append(1)
        for i in range(2,n+1):
            result = result[-3:]
            result.append(result[- 2] + result[- 1])
            # result.append(result[i-2] + result[i-1]) 
    return result[-1]


if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))
