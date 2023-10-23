if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    query_scoreList = student_marks[query_name]
    Score_sum = 0
    for i in query_scoreList:
        Score_sum += i
    avgScore = Score_sum/3
    print("{:.2f}".format(avgScore))
    