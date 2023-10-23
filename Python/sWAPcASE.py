def swap_case(s):
    swapped = ''''''
    for i in s:
        if i == i.lower():
            swapped = f"{swapped}{i.upper()}"
        elif i == i.upper():
            swapped = f"{swapped}{i.lower()}"
        else:
            swapped = f"{swapped}{i}"
    return swapped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)