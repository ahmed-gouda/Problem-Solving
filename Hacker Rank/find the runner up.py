if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a=list(arr)
    a.sort(reverse=True)
    for i in range(n):
        if(a[i]<a[0]):
            print(a[i])
            break