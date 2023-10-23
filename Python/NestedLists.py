if __name__ == '__main__':
    # main_list = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     main_list.append([name, score])
    main_list = [['Test1', 52], 
                ['Test2', 53], 
                ['Test3', 53]]
    scoresList = sorted([x[1] for x in main_list])
    lowest_score = min(scoresList)
    # the second lowest score placeholder will have 9s equal to
    # the number of digits in the max score
    # if 50 is the max score then 99; if 176 then 999 and so on.
    secondLowest_score = int(len(str(max(scoresList))) * '9')
    for i in range(len(main_list)):
        if scoresList[i] != lowest_score and scoresList[i] < secondLowest_score:
            secondLowest_score = scoresList[i]

    secondLowest_Scorer = sorted([i[0] for i in main_list if i[1]==secondLowest_score])
    for i in secondLowest_Scorer:
        print(i)
        

    