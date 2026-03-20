def gcd(a, b):
    if (a != 0) and (b != 0):
        if a > b:
            return gcd(a % b, b)
        else:
            return gcd(a, b % a)
    elif a == 0:
        return b
    else:
        return a

if __name__ == "__main__":
    input_text = input()
    input_list = input_text.split()
    a = int(input_list[0])
    b = int(input_list[1])
    result = gcd(a, b)
    print(result)