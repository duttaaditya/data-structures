def two_sums():
    input_text = input()
    input_list = input_text.split()
    a = int(input_list[0])
    b = int(input_list[1])
    sums = a + b
    return sums

if __name__ == "__main__":
    result = two_sums()
    print(result)