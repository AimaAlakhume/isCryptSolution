def solution(crypt, solution):
    
    solutionDict = {soln[0]: soln[1] for soln in solution}
    
    str1, str2, str3 = '', '', ''
    
    word1 = crypt[0]
    for i in range(len(word1)):
        str1 += solutionDict[word1[i]]
        
    word2 = crypt[1]
    for i in range(len(word2)):
        str2 += solutionDict[word2[i]]
    
    word3 = crypt[2]
    for i in range(len(word3)):
        str3 += solutionDict[word3[i]]
    
    if (str1[0] == '0' and len(str1) != 1) or (str2[0] == '0' and len(str2) != 1) or (str3[0] == '0' and len(str3) != 1):
        return False
        
    if int(str1) + int(str2) == int(str3):
        return True
        
    return False
