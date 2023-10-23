if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    res = []
    x1 = [p for p in range(x+1)]
    y1 = [q for q in range(y+1)]
    z1 = [r for r in range(z+1)]
    res = [[i,j,k] for i in x1 for j in y1 for k in z1 if i+j+k!=n]
    print(res)