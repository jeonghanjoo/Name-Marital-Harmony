chardict = {'ㄱ':2, 'ㄲ':4, 'ㄴ':2, 'ㄷ':3, 'ㄸ':6, 'ㄹ':5, 'ㅁ':4, 'ㅂ':4, 'ㅃ':8, 'ㅅ':2, 'ㅆ':4, 'ㅇ':1, 'ㅈ':3, 'ㅉ':6, 'ㅊ':4, 'ㅋ':3, 'ㅌ':4, 'ㅍ':4, 'ㅎ':3, 'ㅏ':2, 'ㅐ':3, 'ㅑ':3, 'ㅒ':4, 'ㅓ':2, 'ㅔ':3, 'ㅕ':3, 'ㅖ':4, 'ㅗ':2, 'ㅛ':3, 'ㅜ':2, 'ㅠ':3, 'ㅡ':1, 'ㅣ':1, 'ㅢ':2}
CHO_DATA = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
JUNG_DATA = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
JONG_DATA = "ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"
KOR_KEY = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅛㅜㅠㅡㅣㅢ"

def index(s,ch):
    try:
        result = s.index(ch)
        return result
    except ValueError:
        return -1


def breakHangle(src):
    broken = ""
    if len(src) == 0:
        return broken
    for i in range(len(src)):
        ch = src[i]
        nCode = ord(ch)
        arrKeyIndex = [-1,-1,-1,-1,-1]

        if 0xac00 <= nCode and nCode <= 0xd7a3:
            nCode -= 0xac00
            arrKeyIndex[0] = int(nCode / (21 * 28))
            arrKeyIndex[1] = int(nCode / 28) % 21
            arrKeyIndex[3] = nCode % 28 - 1
        elif nCho != -1:
            arrKeyIndex[0] = nCho
        elif nJung != -1:
            arrKeyIndex[1] = nJung
        elif nJong != -1:
            arrKeyIndex[3] = nJong
        else:
            broken += ch

        if arrKeyIndex[1] != -1 :
            if arrKeyIndex[1] == 9 :					# ㅘ
                arrKeyIndex[1] = 27
                arrKeyIndex[2] = 19
            elif arrKeyIndex[1] == 10 :			# ㅙ
                arrKeyIndex[1] = 27
                arrKeyIndex[2] = 20
            elif arrKeyIndex[1] == 11 :			# ㅚ
                arrKeyIndex[1] = 27
                arrKeyIndex[2] = 32
            elif arrKeyIndex[1] == 14 :			# ㅝ
                arrKeyIndex[1] = 29
                arrKeyIndex[2] = 23
            elif arrKeyIndex[1] == 15 :			# ㅞ
                arrKeyIndex[1] = 29
                arrKeyIndex[2] = 24
            elif arrKeyIndex[1] == 16 :			# ㅟ
                arrKeyIndex[1] = 29
                arrKeyIndex[2] = 32
            elif arrKeyIndex[1] == 19 :			# ㅢ
                arrKeyIndex[1] = 31
                arrKeyIndex[2] = 32
            else :
                #print(str(arrKeyIndex[1]))
                arrKeyIndex[1] = index(KOR_KEY,JUNG_DATA[arrKeyIndex[1]])
                arrKeyIndex[2] = -1
        if arrKeyIndex[3] != -1 :
            if arrKeyIndex[3] == 2 :					# ㄳ
                arrKeyIndex[3] = 0
                arrKeyIndex[4] = 9
            elif arrKeyIndex[3] == 4 :			# ㄵ
                arrKeyIndex[3] = 2
                arrKeyIndex[4] = 12
            elif arrKeyIndex[3] == 5 :			# ㄶ
                arrKeyIndex[3] = 2
                arrKeyIndex[4] = 18
            elif arrKeyIndex[3] == 8 :			# ㄺ
                arrKeyIndex[3] = 5
                arrKeyIndex[4] = 0
            elif arrKeyIndex[3] == 9 :			# ㄻ
                arrKeyIndex[3] = 5
                arrKeyIndex[4] = 6
            elif arrKeyIndex[3] == 10 :			# ㄼ
                arrKeyIndex[3] = 5
                arrKeyIndex[4] = 7
            elif arrKeyIndex[3] == 11 :			# ㄽ
                arrKeyIndex[3] = 5
                arrKeyIndex[4] = 9
            elif arrKeyIndex[3] == 12 :			# ㄾ
                arrKeyIndex[3] = 5
                arrKeyIndex[4] = 16
            elif arrKeyIndex[3] == 13 :			# ㄿ
                arrKeyIndex[3] = 5
                arrKeyIndex[4] = 17
            elif arrKeyIndex[3] == 14 :			# ㅀ
                arrKeyIndex[3] = 5
                arrKeyIndex[4] = 18
            elif arrKeyIndex[3] == 17 :			# ㅄ
                arrKeyIndex[3] = 7
                arrKeyIndex[4] = 9
            else :
                #print(str(arrKeyIndex[3]))
                arrKeyIndex[3] = index(KOR_KEY,JONG_DATA[arrKeyIndex[3]])
                arrKeyIndex[4] = -1
        for j in range(5):
            if arrKeyIndex[j] != -1:
                broken += KOR_KEY[arrKeyIndex[j]]

    return broken


def charCount(ch):
    ss = breakHangle(ch)
    count = 0
    for t in ss:
        count += chardict[t]
    return count

def strToCountList(s):
    result = []
    for t in s:
        result.append(charCount(t))
    return result   


def sumCount(ls):
    result = []
    for i in range(len(ls)-1):
        result.append(((ls[i])+(ls[i+1]))%10)
    return result

def recursive(ls):
    #print(str(ls))
    if len(ls) == 2:
        return ls
    return recursive(sumCount(ls))

#len of s1 must be same as len of s2
def join(s1,s2):
    result = ""
    for i in range(len(s1)):
        result += s1[i]
        result += s2[i]
    return result

def goongHap(s1,s2):
    s = join(s1,s2)
    ls = strToCountList(s)
    result = (recursive(ls))
    return result[0]*10 + result[1]


people = ['김철수', '김미영', '오유진', '김진수', '박현진', '박지성', '김연아']



for i in range(len(people)):
    for j in range(len(people)):
        s1 = people[i]
        s2 = people[j]
        print(str(goongHap(s1,s2)),end='\t')
    print()


    





