if __name__ == '__main__':
    lst=[]
    scorelst=[]
    names=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scorelst.append(score)
        lst.append([name,score])
    scorelst.sort()
    for z in range(len(scorelst)):
        if(scorelst[z]>scorelst[0]):
            second=scorelst[z]
            break
    for j in range (len(scorelst)):
        if(second==lst[j][1]):
            names.append(lst[j][0])
    names.sort()
    for i in names:
        print(i)