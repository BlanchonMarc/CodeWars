def longest_consec(strarr, k):
    # your code
    n = len(strarr)
    arr = []
    strconc = []
    if n == 0 or k > n or k <= 0:
        return ""
    else:
        arr = [len(x) for x in strarr]

    tempCounter = 0

    for i in range(len(strarr) - k + 1):
        for j in range(k):
            tempCounter += len(strarr[i + j])

        strconc.append(tempCounter)
        tempCounter = 0

    indexmax = strconc.index(max(strconc))

    tmpStr = []

    for i in range(indexmax, indexmax + k):
        tmpStr.append(strarr[i])

    return ''.join(tmpStr)


def longest_consec_optim(strarr, k):
    if k < 1 or len(strarr) < k or not strarr:
        return ""
    return max([''.join(strarr[a:a + k]) for a in range(len(strarr) - k + 1)],
               key=len)
