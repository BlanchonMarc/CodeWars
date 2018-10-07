def to_camel_case(text):
    #your code here
    if not text:
        return ""

    listAlpha = [x.isalpha() for x in text] #check for index of non-char
    newStr = '' #str to be returned
    check = 1 #checked and keep first char as original // Upper Case Cntrol
    for index in range(len(listAlpha)):
        if listAlpha[index]:
            if check == 0:
                newStr += text[index].upper()
                check = 1
            else:
                newStr += text[index]
        else:
            check = 0
    return newStr
