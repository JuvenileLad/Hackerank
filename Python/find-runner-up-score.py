
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_arr = sorted(arr)
    print(sorted_arr)
    max_arr = max(sorted_arr)
    for i in sorted_arr[-1::-1]:
        print(i)
        if i != max_arr:
            runnersUp = i
            break
    print(runnersUp)