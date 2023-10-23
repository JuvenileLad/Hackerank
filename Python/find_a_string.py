def count_substring(string, sub_string):
    sub_stringLen = len(sub_string)
    counter = 0
    for i in string:
        strPos = string.find(i)
        str_ToCheck = string[strPos:strPos+sub_stringLen]
        if str_ToCheck == sub_string:
            counter += 1
        string = string[1:len(string)+1]
    return counter

if __name__ == '__main__':
    string = "ABCDCDC" #input().strip()
    sub_string = "CDC" #input().strip()
    
    count = count_substring(string, sub_string)
    print(count)