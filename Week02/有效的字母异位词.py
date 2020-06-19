#有效的字母异位词
#哈希
def isAnagram_1(s:str,t:str):
    if len(s)!=len(t):return False
    count=[0 for i in range(26)]
    for i in range(len(s)):
        count[ord(s[i])-ord('a')]+=1
        count[ord(t[i])-ord('a')]-=1
    for i in range(26):
        if count[i]!=0:
            return False
    return True

#有效的字母异位词
#排序
def isAnagram_2(s:str,t:str):
    if len(s)!=len(t):return False
    s=sorted(s)
    t=sorted(t)
    if s!=t:
        return False
    return True