if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sumofmarks=0
    for i in range(len(student_marks[query_name])):
        sumofmarks+=student_marks[query_name][i]
    a=sumofmarks/len(student_marks[query_name])
    print ("%.2f"%a)